const express = require('express');
const http = require('http');
const { Server } = require('socket.io');
const os = require('os');
const path = require('path');
const cors = require('cors');
const helmet = require('helmet');

// ─── Timestamp helper ───────────────────────────────────────────────────────
function ts() {
  return `[${new Date().toISOString()}]`;
}

// ─── TF-IDF-style extractive summariser (pure Node.js, no API key) ──────────
function extractiveSummarise(text, topN = 3) {
  if (!text || typeof text !== 'string') return { summary: '', sentences: [] };

  // Split into sentences
  const sentences = text
    .replace(/([.?!])\s+/g, '$1\n')
    .split('\n')
    .map((s) => s.trim())
    .filter((s) => s.length > 10);

  if (sentences.length === 0) return { summary: text, sentences: [] };
  if (sentences.length <= topN) return { summary: text, sentences };

  // Build word frequency map (stop-words excluded)
  const STOP_WORDS = new Set([
    'a','an','the','is','it','in','on','at','to','for','of','and','or','but',
    'with','this','that','are','was','were','be','been','has','have','had',
    'do','does','did','from','by','as','i','we','you','he','she','they',
    'my','our','your','his','her','their','its','not','no','so','if','than',
    'then','just','about','which','what','who','when','where','how',
  ]);

  const wordFreq = {};
  const wordRegex = /\b[a-zA-Z]{3,}\b/g;

  sentences.forEach((sentence) => {
    const words = (sentence.toLowerCase().match(wordRegex) || []).filter(
      (w) => !STOP_WORDS.has(w)
    );
    words.forEach((w) => {
      wordFreq[w] = (wordFreq[w] || 0) + 1;
    });
  });

  // Score each sentence by sum of word frequencies
  const scored = sentences.map((sentence, idx) => {
    const words = (sentence.toLowerCase().match(wordRegex) || []).filter(
      (w) => !STOP_WORDS.has(w)
    );
    const score =
      words.reduce((sum, w) => sum + (wordFreq[w] || 0), 0) /
      Math.max(words.length, 1);
    return { sentence, score, idx };
  });

  // Pick top-N by score, preserve original order
  const top = scored
    .slice()
    .sort((a, b) => b.score - a.score)
    .slice(0, topN)
    .sort((a, b) => a.idx - b.idx);

  return {
    summary: top.map((s) => s.sentence).join(' '),
    sentences: top.map((s) => s.sentence),
  };
}

// ─── App setup ──────────────────────────────────────────────────────────────
const app = express();

// Security headers (helmet) — allow inline scripts/styles for the UI
app.use(
  helmet({
    contentSecurityPolicy: false, // disabled so the glassmorphism UI loads fine
  })
);

app.use(cors());
app.use(express.json());

// Anti-caching headers so client updates reflect immediately on all browsers/devices
app.use((req, res, next) => {
  res.set('Cache-Control', 'no-store, no-cache, must-revalidate, proxy-revalidate');
  res.set('Pragma', 'no-cache');
  res.set('Expires', '0');
  next();
});

app.use(
  express.static(path.join(__dirname, 'public'), {
    etag: false,
    maxAge: 0,
    lastModified: false,
  })
);

// ─── REST Endpoints ─────────────────────────────────────────────────────────

// GET /api/health
app.get('/api/health', (req, res) => {
  console.log(`${ts()} [HEALTH] Health check requested`);
  res.json({
    status: 'ok',
    edition: 'Complete',
    project: 'PeerVault AI',
    uptime: process.uptime(),
    timestamp: new Date().toISOString(),
  });
});

// GET /api/room-stats
app.get('/api/room-stats', (req, res) => {
  console.log(`${ts()} [STATS] Room stats requested`);
  const stats = Object.entries(rooms).map(([roomId, peers]) => ({
    roomId,
    peerCount: Object.keys(peers).length,
    peers: Object.values(peers).map((p) => ({
      socketId: p.socketId,
      peerName: p.peerName,
      joinedAt: p.joinedAt,
    })),
  }));
  res.json({
    totalRooms: stats.length,
    totalPeers: stats.reduce((sum, r) => sum + r.peerCount, 0),
    rooms: stats,
    timestamp: new Date().toISOString(),
  });
});

// POST /api/ai-summarize  (Edition 8)
app.post('/api/ai-summarize', (req, res) => {
  const { text } = req.body || {};
  console.log(
    `${ts()} [AI] Summarise request — input length: ${text ? text.length : 0} chars`
  );

  if (!text || typeof text !== 'string' || text.trim().length === 0) {
    return res.status(400).json({ error: 'Request body must include a non-empty "text" field.' });
  }

  if (text.length > 100_000) {
    return res.status(413).json({ error: 'Text too long — maximum 100,000 characters.' });
  }

  const result = extractiveSummarise(text, 3);
  console.log(`${ts()} [AI] Summary produced — ${result.sentences.length} sentences`);

  res.json({
    summary: result.summary,
    sentences: result.sentences,
    algorithm: 'TF-IDF Extractive (top-3 sentences)',
    inputLength: text.length,
    timestamp: new Date().toISOString(),
  });
});

// ─── HTTP + Socket.io server ─────────────────────────────────────────────────
const server = http.createServer(app);
const io = new Server(server, {
  cors: {
    origin: '*',
    methods: ['GET', 'POST'],
  },
});

// ─── In-memory room tracking ─────────────────────────────────────────────────
// Structure: { roomId: { socketId: { socketId, peerName, joinedAt } } }
const rooms = {};

// Helper — local IPv4 addresses
function getLocalIpAddresses() {
  const interfaces = os.networkInterfaces();
  const addresses = [];
  for (const name of Object.keys(interfaces)) {
    for (const iface of interfaces[name]) {
      if (iface.family === 'IPv4' && !iface.internal) {
        addresses.push(iface.address);
      }
    }
  }
  return addresses.length > 0 ? addresses : ['127.0.0.1'];
}

// ─── Socket.io Signaling ─────────────────────────────────────────────────────
io.on('connection', (socket) => {
  console.log(`${ts()} [CONNECT] Peer connected: ${socket.id}`);

  let currentRoom = null;
  let peerName = `Peer-${socket.id.substring(0, 5)}`;

  // ── Edition 1 — Room join/leave ──────────────────────────────────────────
  socket.on('join-room', (data) => {
    const { roomId, name } = data || {};
    if (!roomId) return;

    currentRoom = roomId;
    if (name) peerName = name;

    socket.join(roomId);

    if (!rooms[roomId]) rooms[roomId] = {};

    rooms[roomId][socket.id] = {
      socketId: socket.id,
      peerName,
      joinedAt: new Date().toISOString(),
    };

    console.log(`${ts()} [ROOM JOIN] ${peerName} (${socket.id}) joined room: ${roomId}`);

    // Send current room state to the newly joined peer
    const peersInRoom = Object.values(rooms[roomId]).filter(
      (p) => p.socketId !== socket.id
    );
    socket.emit('room-joined', {
      roomId,
      yourSocketId: socket.id,
      peers: peersInRoom,
    });

    // Notify existing peers
    socket.to(roomId).emit('user-joined', {
      socketId: socket.id,
      peerName,
    });
  });

  // ── Leave room ──────────────────────────────────────────────────────────
  socket.on('leave-room', (data) => {
    const { roomId } = data || {};
    if (!roomId) return;
    socket.leave(roomId);
    if (rooms[roomId]) {
      delete rooms[roomId][socket.id];
      if (Object.keys(rooms[roomId]).length === 0) {
        delete rooms[roomId];
        console.log(`${ts()} [ROOM] Room "${roomId}" removed (empty after leave)`);
      } else {
        io.to(roomId).emit('user-disconnected', { socketId: socket.id, peerName });
      }
    }
    currentRoom = null;
    console.log(`${ts()} [ROOM LEAVE] ${peerName} (${socket.id}) left room: ${roomId}`);
  });

  // ── Edition 2 — WebRTC Signaling relay ──────────────────────────────────
  socket.on('signal-offer', (data) => {
    const { targetSocketId, offer, sdp } = data;
    const payload = offer || sdp; // accept both keys for compatibility
    console.log(`${ts()} [SIGNAL] Offer: ${socket.id} → ${targetSocketId}`);
    io.to(targetSocketId).emit('signal-offer', {
      senderSocketId: socket.id,
      sdp: payload,
      offer: payload,
    });
  });

  socket.on('signal-answer', (data) => {
    const { targetSocketId, answer, sdp } = data;
    const payload = answer || sdp; // accept both keys for compatibility
    console.log(`${ts()} [SIGNAL] Answer: ${socket.id} → ${targetSocketId}`);
    io.to(targetSocketId).emit('signal-answer', {
      senderSocketId: socket.id,
      sdp: payload,
      answer: payload,
    });
  });

  socket.on('ice-candidate', (data) => {
    const { targetSocketId, candidate } = data;
    console.log(`${ts()} [SIGNAL] ICE Candidate: ${socket.id} → ${targetSocketId}`);
    io.to(targetSocketId).emit('ice-candidate', {
      senderSocketId: socket.id,
      candidate,
    });
  });

  // ── Editions 3-7 — Server stays as pure signaling broker ────────────────
  //    File transfer, E2EE, chunking all happen client-side via RTCDataChannel.
  //    No server-side changes needed.

  // ── Disconnection ────────────────────────────────────────────────────────
  socket.on('disconnect', () => {
    console.log(`${ts()} [DISCONNECT] Peer disconnected: ${socket.id}`);
    if (currentRoom && rooms[currentRoom]) {
      delete rooms[currentRoom][socket.id];
      if (Object.keys(rooms[currentRoom]).length === 0) {
        delete rooms[currentRoom];
        console.log(`${ts()} [ROOM] Room "${currentRoom}" is now empty — removed`);
      } else {
        io.to(currentRoom).emit('user-disconnected', {
          socketId: socket.id,
          peerName,
        });
      }
    }
  });
});

// ─── Start server ─────────────────────────────────────────────────────────────
const PORT = process.env.PORT || 3000;
server.listen(PORT, () => {
  const lanIps = getLocalIpAddresses();
  console.log('================================================================');
  console.log('  PeerVault AI — All 8 Editions — Signaling Server Active');
  console.log('================================================================');
  console.log(` ${ts()} Server started`);
  console.log(` Local Access  : http://localhost:${PORT}`);
  lanIps.forEach((ip) => {
    console.log(` LAN Access    : http://${ip}:${PORT}`);
  });
  console.log(' REST Endpoints:');
  console.log(`   GET  /api/health`);
  console.log(`   GET  /api/room-stats`);
  console.log(`   POST /api/ai-summarize`);
  console.log('================================================================');
});
