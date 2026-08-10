// PeerVault AI - Edition 1 Client Signaling Logic

document.addEventListener('DOMContentLoaded', () => {
  // DOM Elements
  const statusBox = document.getElementById('statusBox');
  const statusGlow = document.getElementById('statusGlow');
  const socketStatusText = document.getElementById('socketStatusText');
  const yourSocketIdEl = document.getElementById('yourSocketId');
  const activeRoomNameEl = document.getElementById('activeRoomName');
  const peerNameInput = document.getElementById('peerNameInput');
  const roomIdInput = document.getElementById('roomIdInput');
  const btnJoinRoom = document.getElementById('btnJoinRoom');
  const btnGenerateRoom = document.getElementById('btnGenerateRoom');
  const peersListEl = document.getElementById('peersList');
  const peerCountBadge = document.getElementById('peerCountBadge');
  const consoleLog = document.getElementById('consoleLog');
  const btnClearLog = document.getElementById('btnClearLog');

  // Random Codename Generator
  const codeAdjectives = ['Cyber', 'Quantum', 'Shadow', 'Solar', 'Hyper', 'Nova', 'Cryptic', 'Vortex'];
  const codeAnimals = ['Falcon', 'Otter', 'Phoenix', 'Panther', 'Raven', 'Lynx', 'Viper', 'Titan'];
  
  function generateRandomName() {
    const adj = codeAdjectives[Math.floor(Math.random() * codeAdjectives.length)];
    const animal = codeAnimals[Math.floor(Math.random() * codeAnimals.length)];
    const num = Math.floor(10 + Math.random() * 90);
    return `${adj}-${animal}-${num}`;
  }

  peerNameInput.value = generateRandomName();

  // Logging Utility
  function logEvent(message, type = 'info') {
    const time = new Date().toLocaleTimeString();
    const div = document.createElement('div');
    div.className = `log-entry ${type}`;
    div.textContent = `[${time}] ${message}`;
    consoleLog.appendChild(div);
    consoleLog.scrollTop = consoleLog.scrollHeight;
  }

  btnClearLog.addEventListener('click', () => {
    consoleLog.innerHTML = '';
    logEvent('Console cleared by user.', 'system');
  });

  // Socket.io Connection Setup
  logEvent('Initializing Socket.io connection to signaling server...', 'info');
  const socket = io();

  let activeRoom = null;
  let currentPeers = {}; // { socketId: { socketId, peerName } }

  // Socket Lifecycle Events
  socket.on('connect', () => {
    logEvent(`Connected to signaling server with Socket ID: ${socket.id}`, 'success');
    statusGlow.classList.add('online');
    socketStatusText.textContent = 'Online & Connected';
    yourSocketIdEl.textContent = socket.id;
  });

  socket.on('disconnect', (reason) => {
    logEvent(`Disconnected from signaling server. Reason: ${reason}`, 'error');
    statusGlow.classList.remove('online');
    socketStatusText.textContent = 'Disconnected';
    yourSocketIdEl.textContent = 'Disconnected';
    activeRoomNameEl.textContent = 'None';
    currentPeers = {};
    renderPeersList();
  });

  socket.on('connect_error', (err) => {
    logEvent(`Connection Error: ${err.message}`, 'error');
    socketStatusText.textContent = 'Connection Error';
  });

  // Room Join Action
  function joinRoom() {
    const roomId = roomIdInput.value.trim();
    const name = peerNameInput.value.trim() || generateRandomName();

    if (!roomId) {
      logEvent('Please enter or generate a room code first!', 'warn');
      return;
    }

    logEvent(`Sending room join request: Room = "${roomId}", Name = "${name}"...`, 'info');
    socket.emit('join-room', { roomId, name });
  }

  btnJoinRoom.addEventListener('click', joinRoom);

  btnGenerateRoom.addEventListener('click', () => {
    const randomRoom = 'room-' + Math.random().toString(36).substring(2, 8);
    roomIdInput.value = randomRoom;
    logEvent(`Generated random room code: ${randomRoom}`, 'info');
  });

  // Room Events from Signaling Server
  socket.on('room-joined', (data) => {
    const { roomId, peers } = data;
    activeRoom = roomId;
    activeRoomNameEl.textContent = roomId;
    logEvent(`Successfully joined room "${roomId}". Existing peer count: ${peers.length}`, 'success');

    currentPeers = {};
    peers.forEach(p => {
      currentPeers[p.socketId] = p;
    });

    renderPeersList();
  });

  socket.on('user-joined', (peer) => {
    logEvent(`New peer discovered in room: ${peer.peerName} (${peer.socketId})`, 'success');
    currentPeers[peer.socketId] = peer;
    renderPeersList();
  });

  socket.on('user-disconnected', (peer) => {
    logEvent(`Peer left the room: ${peer.peerName} (${peer.socketId})`, 'warn');
    delete currentPeers[peer.socketId];
    renderPeersList();
  });

  // WebRTC Signaling Relay Listeners (Prepared for Edition 2)
  socket.on('signal-offer', (data) => {
    logEvent(`[WebRTC Signaling] Received SDP Offer from peer: ${data.senderSocketId}`, 'info');
  });

  socket.on('signal-answer', (data) => {
    logEvent(`[WebRTC Signaling] Received SDP Answer from peer: ${data.senderSocketId}`, 'info');
  });

  socket.on('ice-candidate', (data) => {
    logEvent(`[WebRTC Signaling] Received ICE Candidate from peer: ${data.senderSocketId}`, 'info');
  });

  // Render Discovered Peers Radar Grid
  function renderPeersList() {
    const peerIds = Object.keys(currentPeers);
    peerCountBadge.textContent = `${peerIds.length} Peer${peerIds.length === 1 ? '' : 's'}`;

    if (peerIds.length === 0) {
      peersListEl.innerHTML = `
        <div class="empty-peers">
          <div class="empty-icon">📡</div>
          <p>Joined room "${activeRoom || 'N/A'}". Waiting for other devices on the LAN to join this room code.</p>
        </div>
      `;
      return;
    }

    peersListEl.innerHTML = '';
    peerIds.forEach(id => {
      const peer = currentPeers[id];
      const firstLetter = (peer.peerName || 'P').charAt(0).toUpperCase();

      const item = document.createElement('div');
      item.className = 'peer-item';
      item.innerHTML = `
        <div class="peer-avatar-name">
          <div class="peer-avatar">${firstLetter}</div>
          <div class="peer-details">
            <span class="peer-name">${peer.peerName}</span>
            <span class="peer-id-sub">ID: ${peer.socketId.substring(0, 10)}...</span>
          </div>
        </div>
        <span class="peer-ready-tag">Signaling Connected</span>
      `;
      peersListEl.appendChild(item);
    });
  }
});
