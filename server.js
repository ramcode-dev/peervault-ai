const express = require('express');
const http = require('http');
const { Server } = require('socket.io');
const os = require('os');
const path = require('path');
const cors = require('cors');

const app = express();
app.use(cors());
app.use(express.static(path.join(__dirname, 'public')));

const server = http.createServer(app);
const io = new Server(server, {
  cors: {
    origin: '*',
    methods: ['GET', 'POST']
  }
});

// Helper function to get local IP address (LAN IP)
function getLocalIpAddresses() {
  const interfaces = os.networkInterfaces();
  const addresses = [];
  for (const name of Object.keys(interfaces)) {
    for (const iface of interfaces[name]) {
      // Filter out internal (loopback) and non-IPv4 addresses
      if (iface.family === 'IPv4' && !iface.internal) {
        addresses.push(iface.address);
      }
    }
  }
  return addresses.length > 0 ? addresses : ['127.0.0.1'];
}

// In-memory room and peer tracking
// Structure: { roomId: { socketId: { socketId, peerName, joinedAt } } }
const rooms = {};

io.on('connection', (socket) => {
  console.log(`[CONNECT] Peer connected: ${socket.id}`);

  let currentRoom = null;
  let peerName = `Peer-${socket.id.substring(0, 5)}`;

  // Event 1: Peer joins a room
  socket.on('join-room', (data) => {
    const { roomId, name } = data || {};
    if (!roomId) return;

    currentRoom = roomId;
    if (name) peerName = name;

    socket.join(roomId);

    if (!rooms[roomId]) {
      rooms[roomId] = {};
    }

    rooms[roomId][socket.id] = {
      socketId: socket.id,
      peerName: peerName,
      joinedAt: new Date().toISOString()
    };

    console.log(`[ROOM JOIN] ${peerName} (${socket.id}) joined room: ${roomId}`);

    // Get list of all existing peers in room (excluding self)
    const peersInRoom = Object.values(rooms[roomId]).filter(
      (p) => p.socketId !== socket.id
    );

    // Send back current room state & peer list to the newly joined peer
    socket.emit('room-joined', {
      roomId,
      yourSocketId: socket.id,
      peers: peersInRoom
    });

    // Notify other peers in room about new peer arrival
    socket.to(roomId).emit('user-joined', {
      socketId: socket.id,
      peerName: peerName
    });
  });

  // Event 2: Relay WebRTC Offer (Signaling)
  socket.on('signal-offer', (data) => {
    const { targetSocketId, offer } = data;
    console.log(`[SIGNAL] Relaying Offer from ${socket.id} -> ${targetSocketId}`);
    io.to(targetSocketId).emit('signal-offer', {
      senderSocketId: socket.id,
      offer
    });
  });

  // Event 3: Relay WebRTC Answer (Signaling)
  socket.on('signal-answer', (data) => {
    const { targetSocketId, answer } = data;
    console.log(`[SIGNAL] Relaying Answer from ${socket.id} -> ${targetSocketId}`);
    io.to(targetSocketId).emit('signal-answer', {
      senderSocketId: socket.id,
      answer
    });
  });

  // Event 4: Relay ICE Candidate (Signaling)
  socket.on('ice-candidate', (data) => {
    const { targetSocketId, candidate } = data;
    console.log(`[SIGNAL] Relaying ICE Candidate from ${socket.id} -> ${targetSocketId}`);
    io.to(targetSocketId).emit('ice-candidate', {
      senderSocketId: socket.id,
      candidate
    });
  });

  // Event 5: Handle Disconnection
  socket.on('disconnect', () => {
    console.log(`[DISCONNECT] Peer disconnected: ${socket.id}`);
    if (currentRoom && rooms[currentRoom]) {
      delete rooms[currentRoom][socket.id];
      if (Object.keys(rooms[currentRoom]).length === 0) {
        delete rooms[currentRoom];
      } else {
        io.to(currentRoom).emit('user-disconnected', {
          socketId: socket.id,
          peerName
        });
      }
    }
  });
});

const PORT = process.env.PORT || 3000;
server.listen(PORT, () => {
  const lanIps = getLocalIpAddresses();
  console.log('====================================================');
  console.log('  PeerVault AI - Edition 1: Signaling Server Active');
  console.log('====================================================');
  console.log(` Local Access : http://localhost:${PORT}`);
  lanIps.forEach((ip) => {
    console.log(` LAN Access   : http://${ip}:${PORT}`);
  });
  console.log('====================================================');
});
