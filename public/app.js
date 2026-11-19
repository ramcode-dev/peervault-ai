// PeerVault AI — All 8 Editions Complete
// WebRTC P2P + E2EE (ECDH+AES-GCM-256) + File Transfer + AI Summarizer

(async function () {
  'use strict';

  /* =============================================
     CONSTANTS & CONFIG
     ============================================= */
  const CHUNK_SIZE = 64 * 1024; // 64 KB
  const ICE_SERVERS = {
    iceServers: [
      { urls: 'stun:stun.l.google.com:19302' },
      { urls: 'stun:stun1.l.google.com:19302' },
      { urls: 'stun:stun2.l.google.com:19302' },
      { urls: 'stun:stun3.l.google.com:19302' },
      { urls: 'stun:stun4.l.google.com:19302' },
      { urls: 'stun:stun.services.mozilla.com' },
      { urls: 'stun:global.stun.twilio.com:3478' },
    ],
  };

  /* =============================================
     DOM REFERENCES
     ============================================= */
  const $ = (id) => document.getElementById(id);

  // Navbar badges & audio toggle
  const p2pBadge = $('p2pBadge');
  const p2pBadgeText = $('p2pBadgeText');
  const e2eeBadge = $('e2eeBadge');
  const e2eeBadgeIcon = $('e2eeBadgeIcon');
  const e2eeBadgeText = $('e2eeBadgeText');
  const btnSoundToggle = $('btnSoundToggle');
  const soundToggleIcon = $('soundToggleIcon');
  const soundToggleText = $('soundToggleText');

  // Connection tab
  const statusGlow = $('statusGlow');
  const socketStatusText = $('socketStatusText');
  const yourSocketIdEl = $('yourSocketId');
  const activeRoomNameEl = $('activeRoomName');
  const peerNameInput = $('peerNameInput');
  const roomIdInput = $('roomIdInput');
  const btnJoinRoom = $('btnJoinRoom');
  const btnLeaveRoom = $('btnLeaveRoom');
  const btnShareRoom = $('btnShareRoom');
  const btnGenerateRoom = $('btnGenerateRoom');
  const peersListEl = $('peersList');
  const peerCountBadge = $('peerCountBadge');
  const chatSection = $('chatSection');
  const chatMessages = $('chatMessages');
  const chatInput = $('chatInput');
  const btnSendChat = $('btnSendChat');

  // File transfer tab
  const p2pRequiredNotice = $('p2pRequiredNotice');
  const dropZone = $('dropZone');
  const fileInput = $('fileInput');
  const selectedFileInfo = $('selectedFileInfo');
  const selectedFileName = $('selectedFileName');
  const selectedFileSize = $('selectedFileSize');
  const btnSendFile = $('btnSendFile');
  const transferProgressSection = $('transferProgressSection');
  const progressFilename = $('progressFilename');
  const progressPct = $('progressPct');
  const progressBarFill = $('progressBarFill');
  const transferSpeed = $('transferSpeed');
  const transferETA = $('transferETA');
  const transferBytes = $('transferBytes');
  const xferStatusBadge = $('xferStatusBadge');
  const receivedFilesSection = $('receivedFilesSection');
  const receivedFilesList = $('receivedFilesList');

  // Security tab
  const e2eeStatusBlock = $('e2eeStatusBlock');
  const e2eeIconBig = $('e2eeIconBig');
  const e2eeTitleText = $('e2eeTitleText');
  const e2eeDescText = $('e2eeDescText');
  const ecdhFingerprint = $('ecdhFingerprint');
  const btnCopyFingerprint = $('btnCopyFingerprint');
  const peerKeySection = $('peerKeySection');
  const peerFingerprint = $('peerFingerprint');

  // AI tab
  const aiTextInput = $('aiTextInput');
  const aiCharCount = $('aiCharCount');
  const btnSummarize = $('btnSummarize');
  const btnLoadSample = $('btnLoadSample');
  const btnClearAI = $('btnClearAI');
  const aiResultSection = $('aiResultSection');
  const aiResultBox = $('aiResultBox');
  const aiMeta = $('aiMeta');
  const btnCopySummary = $('btnCopySummary');
  const aiLoading = $('aiLoading');
  const aiError = $('aiError');

  // Console tab & toasts
  const consoleLog = $('consoleLog');
  const btnClearLog = $('btnClearLog');
  const consoleEntryCount = $('consoleEntryCount');
  const toastContainer = $('toastContainer');

  /* =============================================
     WEB AUDIO SYNTHESIZER & SOUND FX
     ============================================= */
  let soundEnabled = localStorage.getItem('peervault_sound') !== 'false';
  let audioCtx = null;

  function updateSoundUI() {
    if (soundEnabled) {
      btnSoundToggle.classList.remove('muted');
      soundToggleIcon.textContent = '🔊';
      soundToggleText.textContent = 'Audio';
    } else {
      btnSoundToggle.classList.add('muted');
      soundToggleIcon.textContent = '🔇';
      soundToggleText.textContent = 'Muted';
    }
  }

  btnSoundToggle.addEventListener('click', () => {
    soundEnabled = !soundEnabled;
    localStorage.setItem('peervault_sound', soundEnabled ? 'true' : 'false');
    updateSoundUI();
    showToast(`Audio cues ${soundEnabled ? 'enabled' : 'muted'}.`, 'info');
    if (soundEnabled) playTone('click');
  });

  updateSoundUI();

  function playTone(type = 'click') {
    if (!soundEnabled) return;
    try {
      if (!audioCtx) {
        audioCtx = new (window.AudioContext || window.webkitAudioContext)();
      }
      if (audioCtx.state === 'suspended') {
        audioCtx.resume();
      }

      const osc = audioCtx.createOscillator();
      const gain = audioCtx.createGain();
      osc.connect(gain);
      gain.connect(audioCtx.destination);

      const now = audioCtx.currentTime;

      if (type === 'peer') {
        // High-tech two-tone chime (440Hz -> 880Hz)
        osc.type = 'sine';
        osc.frequency.setValueAtTime(440, now);
        osc.frequency.exponentialRampToValueAtTime(880, now + 0.14);
        gain.gain.setValueAtTime(0.08, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.35);
        osc.start(now);
        osc.stop(now + 0.36);
      } else if (type === 'transfer') {
        // High-tech success chord
        osc.type = 'triangle';
        osc.frequency.setValueAtTime(523.25, now);
        osc.frequency.setValueAtTime(659.25, now + 0.08);
        osc.frequency.setValueAtTime(783.99, now + 0.16);
        gain.gain.setValueAtTime(0.12, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.45);
        osc.start(now);
        osc.stop(now + 0.46);
      } else {
        // Crisp subtle click
        osc.type = 'sine';
        osc.frequency.setValueAtTime(800, now);
        gain.gain.setValueAtTime(0.04, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.05);
        osc.start(now);
        osc.stop(now + 0.06);
      }
    } catch (_) {}
  }

  /* =============================================
     TOAST NOTIFICATIONS
     ============================================= */
  function showToast(message, type = 'gold') {
    if (!toastContainer) return;
    const toast = document.createElement('div');
    toast.className = `toast-item ${type}`;

    let icon = '⚡';
    if (type === 'success') icon = '✅';
    if (type === 'red') icon = '⚠️';
    if (type === 'crypto') icon = '🛡️';

    toast.innerHTML = `<span style="font-size:1.1rem;">${icon}</span><span>${message}</span>`;
    toastContainer.appendChild(toast);

    setTimeout(() => {
      if (toast.parentNode) toast.parentNode.removeChild(toast);
    }, 3800);
  }

  /* =============================================
     LOGGING UTILITY
     ============================================= */
  let logCount = 0;

  function logEvent(message, type = 'info') {
    const time = new Date().toLocaleTimeString();
    const div = document.createElement('div');
    div.className = `log-entry ${type}`;
    div.textContent = `[${time}] ${message}`;
    consoleLog.appendChild(div);
    consoleLog.scrollTop = consoleLog.scrollHeight;
    logCount++;
    consoleEntryCount.textContent = `${logCount} event${logCount !== 1 ? 's' : ''}`;
  }

  btnClearLog.addEventListener('click', () => {
    consoleLog.innerHTML = '';
    logCount = 0;
    consoleEntryCount.textContent = '0 events';
    logEvent('Console cleared.', 'system');
  });

  /* =============================================
     TAB SWITCHING
     ============================================= */
  document.querySelectorAll('.tab-btn').forEach((btn) => {
    btn.addEventListener('click', () => {
      const tabId = btn.dataset.tab;
      document.querySelectorAll('.tab-btn').forEach((b) => b.classList.remove('active'));
      document.querySelectorAll('.tab-panel').forEach((p) => p.classList.remove('active'));
      btn.classList.add('active');
      $(`tab-${tabId}`).classList.add('active');
    });
  });

  /* =============================================
     RANDOM CODENAME GENERATOR
     ============================================= */
  const codeAdjectives = ['Cyber', 'Quantum', 'Shadow', 'Solar', 'Hyper', 'Nova', 'Cryptic', 'Vortex'];
  const codeAnimals = ['Falcon', 'Otter', 'Phoenix', 'Panther', 'Raven', 'Lynx', 'Viper', 'Titan'];

  function generateRandomName() {
    const adj = codeAdjectives[Math.floor(Math.random() * codeAdjectives.length)];
    const an = codeAnimals[Math.floor(Math.random() * codeAnimals.length)];
    const num = Math.floor(10 + Math.random() * 90);
    return `${adj}-${an}-${num}`;
  }

  peerNameInput.value = generateRandomName();

  /* =============================================
     HELPERS
     ============================================= */
  function formatBytes(bytes) {
    if (bytes < 1024) return `${bytes} B`;
    if (bytes < 1048576) return `${(bytes / 1024).toFixed(1)} KB`;
    if (bytes < 1073741824) return `${(bytes / 1048576).toFixed(2)} MB`;
    return `${(bytes / 1073741824).toFixed(2)} GB`;
  }

  function formatETA(seconds) {
    if (!isFinite(seconds) || seconds < 0) return '—';
    if (seconds < 60) return `${Math.round(seconds)}s`;
    if (seconds < 3600) return `${Math.floor(seconds / 60)}m ${Math.round(seconds % 60)}s`;
    return `${Math.floor(seconds / 3600)}h ${Math.floor((seconds % 3600) / 60)}m`;
  }

  /* =============================================
     CRYPTO ENGINE (Ed 6+7)
     Ed 6: ECDH P-256 key pair generation + fingerprint
     Ed 7: Derive AES-GCM-256 shared key, encrypt/decrypt chunks
     ============================================= */
  let myECDHKeyPair = null;
  let sharedAESKey = null;
  let myPublicKeyJWK = null;
  let myPrivateKey = null;

  async function generateECDHKeyPair() {
    myECDHKeyPair = await window.crypto.subtle.generateKey(
      { name: 'ECDH', namedCurve: 'P-256' },
      true,
      ['deriveKey']
    );
    myPublicKeyJWK = await window.crypto.subtle.exportKey('jwk', myECDHKeyPair.publicKey);
    myPrivateKey = myECDHKeyPair.privateKey;

    // Compute fingerprint: SHA-256 of the raw SPKI public key
    const spkiBytes = await window.crypto.subtle.exportKey('spki', myECDHKeyPair.publicKey);
    const hashBuffer = await window.crypto.subtle.digest('SHA-256', spkiBytes);
    const hashArray = Array.from(new Uint8Array(hashBuffer));
    const fingerprint = hashArray
      .map((b) => b.toString(16).padStart(2, '0'))
      .join(':')
      .toUpperCase()
      .match(/.{1,5}/g)
      .join(' ');

    ecdhFingerprint.textContent = fingerprint;
    logEvent('ECDH P-256 key pair generated. Fingerprint computed.', 'crypto');
    return fingerprint;
  }

  async function deriveSharedKey(peerPublicKeyJWK) {
    const peerPublicKey = await window.crypto.subtle.importKey(
      'jwk',
      peerPublicKeyJWK,
      { name: 'ECDH', namedCurve: 'P-256' },
      false,
      []
    );
    sharedAESKey = await window.crypto.subtle.deriveKey(
      { name: 'ECDH', public: peerPublicKey },
      myPrivateKey,
      { name: 'AES-GCM', length: 256 },
      false,
      ['encrypt', 'decrypt']
    );
    logEvent('AES-GCM-256 shared key derived via ECDH. E2EE is now active.', 'crypto');
    setE2EEActive(true);

    // Show peer fingerprint
    const peerSPKI = await window.crypto.subtle.exportKey(
      'spki',
      await window.crypto.subtle.importKey(
        'jwk',
        peerPublicKeyJWK,
        { name: 'ECDH', namedCurve: 'P-256' },
        true,
        []
      )
    );
    const peerHash = await window.crypto.subtle.digest('SHA-256', peerSPKI);
    const peerHashArr = Array.from(new Uint8Array(peerHash));
    const peerFP = peerHashArr
      .map((b) => b.toString(16).padStart(2, '0'))
      .join(':')
      .toUpperCase()
      .match(/.{1,5}/g)
      .join(' ');
    peerFingerprint.textContent = peerFP;
    peerKeySection.style.display = 'flex';
  }

  async function encryptChunk(arrayBuffer) {
    const iv = window.crypto.getRandomValues(new Uint8Array(12));
    const encrypted = await window.crypto.subtle.encrypt(
      { name: 'AES-GCM', iv },
      sharedAESKey,
      arrayBuffer
    );
    // Prepend IV (12 bytes) to ciphertext
    const result = new Uint8Array(12 + encrypted.byteLength);
    result.set(iv, 0);
    result.set(new Uint8Array(encrypted), 12);
    return result.buffer;
  }

  async function decryptChunk(arrayBuffer) {
    const data = new Uint8Array(arrayBuffer);
    const iv = data.slice(0, 12);
    const ciphertext = data.slice(12);
    const decrypted = await window.crypto.subtle.decrypt(
      { name: 'AES-GCM', iv },
      sharedAESKey,
      ciphertext
    );
    return decrypted;
  }

  function setE2EEActive(active) {
    const cryptoVerifiedBadge = $('cryptoVerifiedBadge');
    if (active) {
      e2eeBadge.classList.add('active');
      e2eeBadgeIcon.textContent = '🔒';
      e2eeBadgeText.textContent = 'E2EE Active';
      e2eeStatusBlock.classList.add('active');
      e2eeIconBig.textContent = '🔒';
      e2eeTitleText.textContent = '🔒 E2EE Active';
      e2eeDescText.textContent = 'AES-GCM-256 encryption is active. All file chunks are encrypted end-to-end.';
      if (cryptoVerifiedBadge) cryptoVerifiedBadge.style.display = 'flex';
      showToast('E2EE Active: AES-GCM-256 session established', 'crypto');
    } else {
      e2eeBadge.classList.remove('active');
      e2eeBadgeIcon.textContent = '🔓';
      e2eeBadgeText.textContent = 'Not Encrypted';
      e2eeStatusBlock.classList.remove('active');
      e2eeIconBig.textContent = '🔓';
      e2eeTitleText.textContent = 'E2EE Not Active';
      e2eeDescText.textContent = 'Establish a P2P connection to enable AES-GCM-256 encryption.';
      if (cryptoVerifiedBadge) cryptoVerifiedBadge.style.display = 'none';
    }
  }

  // Generate ECDH keys on load
  generateECDHKeyPair().catch((err) => {
    logEvent(`Crypto key generation failed: ${err.message}`, 'error');
    ecdhFingerprint.textContent = 'Key generation failed — WebCrypto not available.';
  });

  btnCopyFingerprint.addEventListener('click', () => {
    navigator.clipboard.writeText(ecdhFingerprint.textContent).then(() => {
      btnCopyFingerprint.textContent = '✅ Copied!';
      setTimeout(() => (btnCopyFingerprint.textContent = '📋 Copy'), 2000);
    });
  });

  /* =============================================
     STATE
     ============================================= */
  let activeRoom = null;
  let currentPeers = {}; // { socketId: { socketId, peerName } }
  let peerConnection = null;
  let dataChannel = null; // main signaling/key exchange channel
  let fileChannel = null; // dedicated file transfer channel
  let remotePeerId = null;
  let myName = '';

  // Key exchange state
  let keyExchangeDone = false;

  // ICE candidate queue — holds candidates that arrive before remote description is set
  let pendingIceCandidates = [];

  // File transfer state
  let selectedFile = null;
  let sendingFile = false;
  let receivingFile = false;
  let recvMeta = null; // { name, size, totalChunks, encrypted }
  let recvChunks = []; // array of ArrayBuffers
  let recvChunkCount = 0;
  let recvBytesReceived = 0;
  let recvStartTime = null;
  let sendAborted = false; // flag to cancel in-flight send

  /* =============================================
     SOCKET.IO SETUP
     ============================================= */
  logEvent('Initializing Socket.io connection to signaling server...', 'info');
  const socket = io();

  socket.on('connect', () => {
    logEvent(`Connected to signaling server. Socket ID: ${socket.id}`, 'success');
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
    activeRoom = null;
    currentPeers = {};
    renderPeersList();
    closePeerConnection();
    btnLeaveRoom.style.display = 'none';
    btnJoinRoom.style.display = '';
  });

  socket.on('connect_error', (err) => {
    logEvent(`Connection Error: ${err.message}`, 'error');
    socketStatusText.textContent = 'Connection Error';
  });

  /* =============================================
     ROOM MANAGEMENT
     ============================================= */
  function joinRoom() {
    const roomId = roomIdInput.value.trim();
    myName = peerNameInput.value.trim() || generateRandomName();
    peerNameInput.value = myName;

    if (!roomId) {
      logEvent('Please enter or generate a room code first!', 'warn');
      return;
    }

    logEvent(`Joining room "${roomId}" as "${myName}"...`, 'info');
    socket.emit('join-room', { roomId, name: myName });
  }

  btnJoinRoom.addEventListener('click', joinRoom);

  btnLeaveRoom.addEventListener('click', () => {
    if (activeRoom) {
      socket.emit('leave-room', { roomId: activeRoom });
      logEvent(`Left room "${activeRoom}".`, 'warn');
      showToast(`Left room "${activeRoom}"`, 'info');
    }
    activeRoom = null;
    activeRoomNameEl.textContent = 'None';
    currentPeers = {};
    renderPeersList();
    closePeerConnection();
    btnLeaveRoom.style.display = 'none';
    btnShareRoom.style.display = 'none';
    btnJoinRoom.style.display = '';
    roomIdInput.value = '';
  });

  btnShareRoom.addEventListener('click', () => {
    if (!activeRoom) return;
    const shareUrl = `${window.location.origin}${window.location.pathname}?room=${encodeURIComponent(activeRoom)}`;
    navigator.clipboard.writeText(shareUrl).then(() => {
      showToast('📋 Room link copied to clipboard!', 'success');
      playTone('click');
      btnShareRoom.textContent = '✅ Copied!';
      setTimeout(() => {
        btnShareRoom.innerHTML = `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><line x1="8.59" y1="13.51" x2="15.42" y2="17.49"/><line x1="15.41" y1="6.51" x2="8.59" y2="10.49"/></svg> Copy Invite Link`;
      }, 2000);
    }).catch(() => {
      prompt('Copy this room URL:', shareUrl);
    });
  });

  btnGenerateRoom.addEventListener('click', () => {
    const r = 'pvault-' + Math.random().toString(36).substring(2, 8);
    roomIdInput.value = r;
    logEvent(`Generated room code: ${r}`, 'info');
    showToast(`Generated code: ${r}`, 'info');
    playTone('click');
  });

  socket.on('room-joined', (data) => {
    const { roomId, peers } = data;
    activeRoom = roomId;
    activeRoomNameEl.textContent = roomId;
    logEvent(`Joined room "${roomId}". Peers already here: ${peers.length}`, 'success');
    showToast(`Connected to room: ${roomId}`, 'gold');

    currentPeers = {};
    peers.forEach((p) => { currentPeers[p.socketId] = p; });
    renderPeersList();

    btnJoinRoom.style.display = 'none';
    btnLeaveRoom.style.display = '';
    btnShareRoom.style.display = '';

    // If there's already a peer in room, initiate WebRTC as offerer
    if (peers.length > 0) {
      remotePeerId = peers[0].socketId;
      logEvent(`Auto-initiating WebRTC connection to peer: ${peers[0].peerName}`, 'info');
      initiatePeerConnection(true);
    }
  });

  socket.on('user-joined', (peer) => {
    logEvent(`Peer joined: ${peer.peerName} (${peer.socketId})`, 'success');
    showToast(`Peer discovered: ${peer.peerName}`, 'success');
    playTone('peer');
    currentPeers[peer.socketId] = peer;
    renderPeersList();

    // If not already connected, this peer is the answerer
    if (!peerConnection && !remotePeerId) {
      remotePeerId = peer.socketId;
      logEvent(`New peer detected, waiting for WebRTC offer from ${peer.peerName}...`, 'info');
    }
  });

  socket.on('user-disconnected', (peer) => {
    logEvent(`Peer left: ${peer.peerName} (${peer.socketId})`, 'warn');
    showToast(`Peer disconnected: ${peer.peerName}`, 'red');
    delete currentPeers[peer.socketId];
    renderPeersList();
    // Only close P2P if the disconnected peer was our active connected peer
    if (peer.socketId === remotePeerId) {
      logEvent('Active P2P peer disconnected. Closing connection.', 'warn');
      closePeerConnection();
    }
  });

  /* =============================================
     WEBRTC SIGNALING (Ed 2)
     ============================================= */
  async function initiatePeerConnection(isOfferer) {
    if (peerConnection) {
      logEvent('WebRTC connection already exists. Skipping.', 'warn');
      return;
    }

    logEvent(`Creating RTCPeerConnection. Role: ${isOfferer ? 'Offerer' : 'Answerer'}`, 'webrtc');
    peerConnection = new RTCPeerConnection(ICE_SERVERS);

    // ICE candidate handling
    peerConnection.onicecandidate = (event) => {
      if (event.candidate) {
        socket.emit('ice-candidate', {
          targetSocketId: remotePeerId,
          candidate: event.candidate,
        });
        logEvent('Sent ICE candidate to peer.', 'webrtc');
      }
    };

    peerConnection.onconnectionstatechange = () => {
      const state = peerConnection.connectionState;
      logEvent(`RTCPeerConnection state: ${state}`, 'webrtc');
      if (state === 'connected') {
        setP2PConnected(true);
      } else if (state === 'failed' || state === 'disconnected' || state === 'closed') {
        setP2PConnected(false);
        if (state === 'failed') {
          logEvent('WebRTC connection failed. Try rejoining the room.', 'error');
          closePeerConnection();
        }
      }
    };

    // Data channels
    if (isOfferer) {
      // Chat / key exchange channel
      dataChannel = peerConnection.createDataChannel('control', { ordered: true });
      setupControlChannel(dataChannel);

      // File transfer channel
      fileChannel = peerConnection.createDataChannel('filetransfer', {
        ordered: true,
        maxRetransmits: 10,
      });
      setupFileChannel(fileChannel);

      // Create offer
      const offer = await peerConnection.createOffer();
      await peerConnection.setLocalDescription(offer);
      socket.emit('signal-offer', { targetSocketId: remotePeerId, sdp: offer });
      logEvent('Sent SDP Offer to peer.', 'webrtc');
    } else {
      // Answerer: wait for data channels from offerer
      peerConnection.ondatachannel = (event) => {
        const ch = event.channel;
        if (ch.label === 'control') {
          dataChannel = ch;
          setupControlChannel(dataChannel);
        } else if (ch.label === 'filetransfer') {
          fileChannel = ch;
          setupFileChannel(fileChannel);
        }
      };
    }
  }

  // Helper: flush queued ICE candidates after setRemoteDescription
  async function flushPendingIceCandidates() {
    if (!peerConnection || pendingIceCandidates.length === 0) return;
    logEvent(`Flushing ${pendingIceCandidates.length} queued ICE candidates...`, 'webrtc');
    for (const candidate of pendingIceCandidates) {
      try {
        await peerConnection.addIceCandidate(new RTCIceCandidate(candidate));
      } catch (e) {
        logEvent(`Queued ICE candidate error: ${e.message}`, 'error');
      }
    }
    pendingIceCandidates = [];
  }

  socket.on('signal-offer', async (data) => {
    logEvent(`Received SDP Offer from: ${data.senderSocketId}`, 'webrtc');
    // Set remotePeerId BEFORE creating peer connection so ICE candidates go to right peer
    remotePeerId = data.senderSocketId;

    if (peerConnection) {
      logEvent('Already have a peer connection. Closing old one before answering new offer.', 'warn');
      closePeerConnection();
      remotePeerId = data.senderSocketId; // re-set after close resets it
    }

    await initiatePeerConnection(false);
    // Accept both 'sdp' and 'offer' keys from server for compatibility
    const remoteSDP = data.sdp || data.offer;
    await peerConnection.setRemoteDescription(new RTCSessionDescription(remoteSDP));
    const answer = await peerConnection.createAnswer();
    await peerConnection.setLocalDescription(answer);
    socket.emit('signal-answer', { targetSocketId: data.senderSocketId, sdp: answer });
    logEvent('Sent SDP Answer to peer.', 'webrtc');
    await flushPendingIceCandidates();
  });

  socket.on('signal-answer', async (data) => {
    logEvent(`Received SDP Answer from: ${data.senderSocketId}`, 'webrtc');
    if (peerConnection) {
      // Accept both 'sdp' and 'answer' keys from server for compatibility
      const remoteSDP = data.sdp || data.answer;
      await peerConnection.setRemoteDescription(new RTCSessionDescription(remoteSDP));
      await flushPendingIceCandidates();
    }
  });

  socket.on('ice-candidate', async (data) => {
    logEvent(`Received ICE candidate from: ${data.senderSocketId}`, 'webrtc');
    if (peerConnection) {
      // Queue candidate if remote description not yet set
      if (!peerConnection.remoteDescription || !peerConnection.remoteDescription.type) {
        logEvent('Remote description not set yet — queuing ICE candidate.', 'warn');
        pendingIceCandidates.push(data.candidate);
        return;
      }
      try {
        await peerConnection.addIceCandidate(new RTCIceCandidate(data.candidate));
      } catch (e) {
        logEvent(`ICE candidate error: ${e.message}`, 'error');
      }
    }
  });

  function closePeerConnection() {
    if (dataChannel) { try { dataChannel.close(); } catch (_) {} dataChannel = null; }
    if (fileChannel) { try { fileChannel.close(); } catch (_) {} fileChannel = null; }
    if (peerConnection) { try { peerConnection.close(); } catch (_) {} peerConnection = null; }
    remotePeerId = null;
    keyExchangeDone = false;
    sharedAESKey = null;
    pendingIceCandidates = [];
    sendAborted = true; // cancel any in-flight send
    setP2PConnected(false);
    setE2EEActive(false);
    peerKeySection.style.display = 'none';
    chatSection.style.display = 'none';
    sendingFile = false;
    receivingFile = false;
    logEvent('P2P connection closed and reset.', 'warn');
  }

  function setP2PConnected(connected) {
    if (connected) {
      p2pBadge.classList.add('connected');
      const badgeDot = p2pBadge.querySelector('.badge-dot');
      if (badgeDot) { badgeDot.classList.remove('disconnected'); badgeDot.classList.add('connected'); }
      p2pBadgeText.textContent = 'P2P Connected';
      chatSection.style.display = '';
      p2pRequiredNotice.style.display = 'none';
      updatePeerListP2PStatus(true);
    } else {
      p2pBadge.classList.remove('connected');
      const badgeDot = p2pBadge.querySelector('.badge-dot');
      if (badgeDot) { badgeDot.classList.add('disconnected'); badgeDot.classList.remove('connected'); }
      p2pBadgeText.textContent = 'P2P Disconnected';
      chatSection.style.display = 'none';
      p2pRequiredNotice.style.display = '';
      updatePeerListP2PStatus(false);
    }
  }

  /* =============================================
     CONTROL CHANNEL — Chat + Key Exchange (Ed 2, 6, 7)
     ============================================= */
  function setupControlChannel(channel) {
    channel.onopen = () => {
      logEvent('Control DataChannel opened. Initiating ECDH key exchange...', 'crypto');
      // Send our public key to peer
      channel.send(JSON.stringify({
        type: 'ecdh-key',
        publicKey: myPublicKeyJWK,
        name: myName || peerNameInput.value.trim(),
      }));
    };

    channel.onmessage = async (event) => {
      let msg;
      try { msg = JSON.parse(event.data); } catch (_) { return; }

      if (msg.type === 'ecdh-key') {
        // Received peer's public key — derive shared secret
        logEvent(`Received peer's ECDH public key. Deriving shared AES-GCM-256 key...`, 'crypto');
        try {
          await deriveSharedKey(msg.publicKey);
          keyExchangeDone = true;
          // Send our public key back as ack so BOTH sides can derive
          channel.send(JSON.stringify({
            type: 'ecdh-ack',
            publicKey: myPublicKeyJWK,
            name: myName || peerNameInput.value.trim(),
          }));
          logEvent('E2EE key exchange complete. AES-GCM-256 session active.', 'crypto');
        } catch (e) {
          logEvent(`Key derivation failed: ${e.message}`, 'error');
        }
      } else if (msg.type === 'ecdh-ack') {
        // Peer confirmed with their public key — derive shared secret if not already done
        if (!keyExchangeDone && msg.publicKey) {
          logEvent('Received ecdh-ack with peer public key. Deriving shared key...', 'crypto');
          try {
            await deriveSharedKey(msg.publicKey);
            keyExchangeDone = true;
            logEvent('E2EE key exchange complete (ack path). AES-GCM-256 session active.', 'crypto');
          } catch (e) {
            logEvent(`Key derivation failed (ack): ${e.message}`, 'error');
          }
        } else {
          logEvent('Peer confirmed key exchange.', 'crypto');
        }
      } else if (msg.type === 'chat') {
        appendChatMessage(msg.text, msg.senderName || 'Peer', false);
      }
    };

    channel.onerror = (e) => {
      logEvent(`Control channel error: ${e.message || 'unknown'}`, 'error');
    };

    channel.onclose = () => {
      logEvent('Control DataChannel closed.', 'warn');
    };
  }

  /* =============================================
     FILE CHANNEL (Ed 3+4+7)
     ============================================= */
  function setupFileChannel(channel) {
    channel.binaryType = 'arraybuffer';

    channel.onopen = () => {
      logEvent('File transfer DataChannel opened.', 'info');
    };

    channel.onmessage = async (event) => {
      // Could be JSON control message or binary chunk
      if (typeof event.data === 'string') {
        let msg;
        try { msg = JSON.parse(event.data); } catch (_) { return; }

        if (msg.type === 'file-meta') {
          receivingFile = true;
          recvMeta = { name: msg.name, size: msg.size, totalChunks: msg.totalChunks, encrypted: msg.encrypted };
          recvChunks = new Array(msg.totalChunks);
          recvChunkCount = 0;
          recvBytesReceived = 0;
          recvStartTime = Date.now();

          logEvent(`Receiving file: ${msg.name} (${formatBytes(msg.size)}, ${msg.totalChunks} chunks)`, 'info');
          xferStatusBadge.textContent = 'Receiving...';
          xferStatusBadge.className = 'xfer-status-badge receiving';

          progressFilename.textContent = msg.name;
          progressPct.textContent = '0%';
          progressBarFill.style.width = '0%';
          transferProgressSection.style.display = '';

          // Switch to File Transfer tab
          document.querySelector('[data-tab="filetransfer"]').click();

        } else if (msg.type === 'file-done') {
          await reassembleFile();
        }
      } else {
        // Binary chunk — encrypted payload with 12-byte IV prefix
        if (!receivingFile || !recvMeta) return;

        try {
          let chunkData;
          if (sharedAESKey && keyExchangeDone && recvMeta.encrypted) {
            chunkData = await decryptChunk(event.data);
          } else {
            chunkData = event.data;
          }

          // We receive in order (ordered channel), so push sequentially
          recvChunks[recvChunkCount] = chunkData;
          recvChunkCount++;
          recvBytesReceived += chunkData.byteLength;

          // Update progress
          const pct = Math.round((recvChunkCount / recvMeta.totalChunks) * 100);
          progressPct.textContent = `${pct}%`;
          progressBarFill.style.width = `${pct}%`;

          const elapsed = (Date.now() - recvStartTime) / 1000;
          const speedBps = recvBytesReceived / elapsed;
          const remaining = (recvMeta.size - recvBytesReceived) / speedBps;
          transferSpeed.textContent = `${(speedBps / 1048576).toFixed(2)} MB/s`;
          transferETA.textContent = `ETA: ${formatETA(remaining)}`;
          transferBytes.textContent = `${formatBytes(recvBytesReceived)} / ${formatBytes(recvMeta.size)}`;
        } catch (e) {
          logEvent(`Chunk decrypt error: ${e.message}`, 'error');
        }
      }
    };

    channel.onerror = (e) => {
      logEvent(`File channel error: ${e.message || 'unknown'}`, 'error');
    };

    channel.onclose = () => {
      logEvent('File transfer DataChannel closed.', 'warn');
    };
  }

  async function reassembleFile() {
    // Capture meta before resetting state
    const fileName = recvMeta.name;
    const fileSize = recvMeta.size;
    const totalChunks = recvMeta.totalChunks;
    const wasEncrypted = recvMeta.encrypted;

    logEvent(`All ${totalChunks} chunks received. Reassembling "${fileName}"...`, 'success');

    const validChunks = recvChunks.slice(0, recvChunkCount).filter(Boolean);
    const blob = new Blob(validChunks);
    const url = URL.createObjectURL(blob);

    // Auto-trigger download
    const a = document.createElement('a');
    a.href = url;
    a.download = fileName;
    a.style.display = 'none';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);

    // Show in received files list
    receivedFilesSection.style.display = '';
    const item = document.createElement('div');
    item.className = 'received-file-item';
    item.innerHTML = `
      <span>✅</span>
      <a href="${url}" download="${fileName}">${fileName}</a>
      <span style="font-size:0.78rem;color:var(--text-muted);font-family:var(--font-mono);">${formatBytes(fileSize)} ${wasEncrypted ? '🔒' : ''}</span>
    `;
    receivedFilesList.appendChild(item);

    xferStatusBadge.textContent = 'Received ✓';
    xferStatusBadge.className = 'xfer-status-badge done';
    showToast(`File received: ${fileName} (${formatBytes(fileSize)})`, 'success');
    playTone('transfer');
    progressPct.textContent = '100%';
    progressBarFill.style.width = '100%';

    // Now reset state
    receivingFile = false;
    recvMeta = null;
    recvChunks = [];
    recvChunkCount = 0;
    recvBytesReceived = 0;

    logEvent(`File "${fileName}" (${formatBytes(fileSize)}) saved. Auto-download triggered.`, 'success');
  }

  /* =============================================
     CHAT (Ed 2)
     ============================================= */
  function appendChatMessage(text, senderName, isSelf) {
    const div = document.createElement('div');
    div.className = `chat-msg ${isSelf ? 'sent' : 'received'}`;
    div.innerHTML = `<div class="chat-msg-name">${isSelf ? 'You' : senderName}</div>${escapeHTML(text)}`;
    chatMessages.appendChild(div);
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }

  function appendChatSystem(text) {
    const div = document.createElement('div');
    div.className = 'chat-msg system-msg';
    div.textContent = text;
    chatMessages.appendChild(div);
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }

  function escapeHTML(str) {
    return str.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  }

  function sendChat() {
    const text = chatInput.value.trim();
    if (!text || !dataChannel || dataChannel.readyState !== 'open') return;
    const name = myName || peerNameInput.value.trim();
    dataChannel.send(JSON.stringify({ type: 'chat', text, senderName: name }));
    appendChatMessage(text, name, true);
    chatInput.value = '';
    logEvent(`Chat sent: "${text}"`, 'info');
  }

  btnSendChat.addEventListener('click', sendChat);
  chatInput.addEventListener('keydown', (e) => { if (e.key === 'Enter') sendChat(); });

  /* =============================================
     FILE TRANSFER — SENDING (Ed 3+4+7)
     ============================================= */
  // Drop zone — click and touch support
  dropZone.addEventListener('click', () => fileInput.click());
  dropZone.addEventListener('touchend', (e) => {
    e.preventDefault(); // prevent ghost click double-trigger
    fileInput.click();
  });

  dropZone.addEventListener('dragover', (e) => {
    e.preventDefault();
    dropZone.classList.add('drag-over');
  });

  dropZone.addEventListener('dragleave', () => dropZone.classList.remove('drag-over'));

  dropZone.addEventListener('drop', (e) => {
    e.preventDefault();
    dropZone.classList.remove('drag-over');
    if (e.dataTransfer.files.length) {
      handleFileSelected(e.dataTransfer.files[0]);
    }
  });

  fileInput.addEventListener('change', () => {
    if (fileInput.files.length) handleFileSelected(fileInput.files[0]);
  });

  function handleFileSelected(file) {
    selectedFile = file;
    selectedFileName.textContent = file.name;
    selectedFileSize.textContent = formatBytes(file.size);
    selectedFileInfo.style.display = '';
    logEvent(`File selected: ${file.name} (${formatBytes(file.size)})`, 'info');
  }

  btnSendFile.addEventListener('click', async () => {
    if (!selectedFile) { logEvent('No file selected.', 'warn'); return; }
    if (!fileChannel || fileChannel.readyState !== 'open') {
      logEvent('File transfer channel not ready. Ensure P2P is connected.', 'warn'); return;
    }
    if (sendingFile) { logEvent('Transfer already in progress.', 'warn'); return; }

    // If key exchange not done yet, send without encryption (plain binary)
    if (!keyExchangeDone) {
      logEvent('⚠️ E2EE key exchange not complete — sending without encryption. Connect P2P first for encrypted transfer.', 'warn');
    }
    sendFile(selectedFile);
  });

  // Helper: read a specific slice of a File as ArrayBuffer without loading it all
  function readFileSlice(file, start, end) {
    return new Promise((resolve, reject) => {
      const reader = new FileReader();
      reader.onload = (e) => resolve(e.target.result);
      reader.onerror = () => reject(reader.error);
      reader.readAsArrayBuffer(file.slice(start, end));
    });
  }

  async function sendFile(file) {
    sendingFile = true;
    sendAborted = false;
    const totalChunks = Math.ceil(file.size / CHUNK_SIZE);
    const isEncrypted = keyExchangeDone && sharedAESKey;

    logEvent(`Starting file send: "${file.name}" (${formatBytes(file.size)}, ${totalChunks} chunks, ${isEncrypted ? 'E2EE ON' : 'No Encryption'})`, 'info');

    xferStatusBadge.textContent = 'Sending...';
    xferStatusBadge.className = 'xfer-status-badge sending';

    // Send metadata header — also tell receiver if encrypted
    fileChannel.send(JSON.stringify({
      type: 'file-meta',
      name: file.name,
      size: file.size,
      totalChunks,
      encrypted: isEncrypted,
    }));

    progressFilename.textContent = file.name;
    transferProgressSection.style.display = '';
    progressPct.textContent = '0%';
    progressBarFill.style.width = '0%';

    const startTime = Date.now();
    let bytesSent = 0;

    // Read and send chunks one at a time (memory-safe, works on mobile)
    for (let i = 0; i < totalChunks; i++) {
      if (sendAborted) {
        logEvent('File send aborted.', 'warn');
        sendingFile = false;
        return;
      }

      const start = i * CHUNK_SIZE;
      const end = Math.min(start + CHUNK_SIZE, file.size);

      let chunk;
      try {
        chunk = await readFileSlice(file, start, end);
      } catch (e) {
        logEvent(`File read error on chunk ${i}: ${e.message}`, 'error');
        sendingFile = false;
        return;
      }

      // Encrypt chunk only if key is ready
      let payload;
      try {
        payload = isEncrypted ? await encryptChunk(chunk) : chunk;
      } catch (e) {
        logEvent(`Encryption failed on chunk ${i}: ${e.message}`, 'error');
        sendingFile = false;
        return;
      }

      // Throttle if buffer is filling up (backpressure) — 4MB limit for mobile safety
      while (fileChannel.bufferedAmount > 4 * 1024 * 1024) {
        await new Promise((r) => setTimeout(r, 50));
      }

      fileChannel.send(payload);
      bytesSent += (end - start);

      // Update progress
      const pct = Math.round(((i + 1) / totalChunks) * 100);
      progressPct.textContent = `${pct}%`;
      progressBarFill.style.width = `${pct}%`;

      const elapsed = (Date.now() - startTime) / 1000 || 0.001;
      const speedBps = bytesSent / elapsed;
      const remaining = (file.size - bytesSent) / speedBps;
      transferSpeed.textContent = `${(speedBps / 1048576).toFixed(2)} MB/s`;
      transferETA.textContent = `ETA: ${formatETA(remaining)}`;
      transferBytes.textContent = `${formatBytes(bytesSent)} / ${formatBytes(file.size)}`;

      // Yield every 8 chunks to keep UI responsive
      if (i % 8 === 0) await new Promise((r) => setTimeout(r, 0));
    }

    // Send done signal
    fileChannel.send(JSON.stringify({ type: 'file-done' }));

    xferStatusBadge.textContent = 'Sent ✓';
    xferStatusBadge.className = 'xfer-status-badge done';
    sendingFile = false;

    const totalTime = ((Date.now() - startTime) / 1000).toFixed(1);
    logEvent(`File "${file.name}" sent in ${totalTime}s. All ${totalChunks} chunks ${isEncrypted ? 'encrypted &' : ''} transferred.`, 'success');
    showToast(`File "${file.name}" sent successfully (${totalTime}s)!`, 'success');
    playTone('transfer');
  }

  /* =============================================
     PEERS LIST RENDERING
     ============================================= */
  function renderPeersList() {
    const peerIds = Object.keys(currentPeers);
    peerCountBadge.textContent = `${peerIds.length} Peer${peerIds.length !== 1 ? 's' : ''}`;

    if (peerIds.length === 0) {
      peersListEl.innerHTML = `
        <div class="empty-peers">
          <div class="empty-icon">📡</div>
          <p>${activeRoom ? `Joined room "${activeRoom}". Waiting for peers to join...` : 'Join or create a room to discover peers.'}</p>
        </div>
      `;
      return;
    }

    peersListEl.innerHTML = '';
    peerIds.forEach((id) => {
      const peer = currentPeers[id];
      const letter = (peer.peerName || 'P').charAt(0).toUpperCase();
      const isConnected = id === remotePeerId && !!peerConnection && peerConnection.connectionState === 'connected';

      const item = document.createElement('div');
      item.className = 'peer-item';
      item.innerHTML = `
        <div class="peer-avatar-name">
          <div class="peer-avatar">${letter}</div>
          <div class="peer-details">
            <span class="peer-name">${peer.peerName}</span>
            <span class="peer-id-sub">ID: ${peer.socketId.substring(0, 10)}...</span>
          </div>
        </div>
        <span class="peer-ready-tag" style="${isConnected ? 'background:rgba(0,255,136,0.12);color:var(--accent-green);border-color:rgba(0,255,136,0.3)' : ''}">
          ${isConnected ? '🔗 P2P Connected' : 'Signaling Connected'}
        </span>
      `;
      peersListEl.appendChild(item);
    });
  }

  function updatePeerListP2PStatus(connected) {
    renderPeersList();
  }

  /* =============================================
     AI SUMMARIZER (Ed 8)
     ============================================= */
  aiTextInput.addEventListener('input', () => {
    aiCharCount.textContent = `${aiTextInput.value.length} characters`;
  });

  btnClearAI.addEventListener('click', () => {
    aiTextInput.value = '';
    aiCharCount.textContent = '0 characters';
    aiResultSection.style.display = 'none';
    aiError.style.display = 'none';
  });

  btnSummarize.addEventListener('click', async () => {
    const text = aiTextInput.value.trim();
    if (!text) { logEvent('AI: No text provided.', 'warn'); return; }
    if (text.length < 50) { logEvent('AI: Text too short for summarization.', 'warn'); return; }

    aiLoading.style.display = 'flex';
    aiResultSection.style.display = 'none';
    aiError.style.display = 'none';
    btnSummarize.disabled = true;

    logEvent('Sending text to AI summarizer endpoint...', 'info');

    try {
      const res = await fetch('/api/ai-summarize', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text }),
      });

      if (!res.ok) {
        const err = await res.json().catch(() => ({ error: 'Server error' }));
        throw new Error(err.error || `HTTP ${res.status}`);
      }

      const data = await res.json();

      aiLoading.style.display = 'none';
      aiResultSection.style.display = '';

      aiResultBox.innerHTML = '';
      // server returns { summary: string, sentences: string[] }
      const sentences = data.sentences && data.sentences.length > 0
        ? data.sentences
        : [data.summary].filter(Boolean);

      sentences.forEach((sentence) => {
        const span = document.createElement('span');
        span.className = 'summary-sentence';
        span.textContent = sentence;
        aiResultBox.appendChild(span);
      });

      aiMeta.textContent = `${data.inputLength || '?'} chars → ${sentences.length} key sentence${sentences.length !== 1 ? 's' : ''} extracted · ${data.algorithm || 'TF-IDF Extractive'}`;
      logEvent(`AI summarization complete. ${sentences.length} sentence${sentences.length !== 1 ? 's' : ''} extracted.`, 'success');
    } catch (err) {
      aiLoading.style.display = 'none';
      aiError.style.display = '';
      aiError.textContent = `Error: ${err.message}`;
      logEvent(`AI summarization error: ${err.message}`, 'error');
    } finally {
      btnSummarize.disabled = false;
    }
  });

  btnCopySummary.addEventListener('click', () => {
    const text = Array.from(aiResultBox.querySelectorAll('.summary-sentence'))
      .map((el) => el.textContent)
      .join(' ');
    navigator.clipboard.writeText(text).then(() => {
      btnCopySummary.textContent = '✅ Copied!';
      setTimeout(() => (btnCopySummary.textContent = '📋 Copy'), 2000);
    });
  });

  if (btnLoadSample) {
    btnLoadSample.addEventListener('click', () => {
      const sampleText = `Decentralized peer-to-peer file transmission systems eliminate single points of failure and surveillance risks associated with centralized cloud storage. By leveraging WebRTC RTCDataChannel protocols over SCTP and UDP, direct browser-to-browser pipes achieve maximum local network throughput without routing data through third-party intermediate relays. To ensure absolute data confidentiality, cryptographic key exchange is conducted via Elliptic Curve Diffie-Hellman (ECDH) on the NIST P-256 curve, deriving an ephemeral 256-bit AES-GCM session key independently on both client terminals. Binary files are fragmented into 64-kilobyte chunks, where each chunk is authenticated and encrypted using a cryptographically random 12-byte initialization vector to prevent replay attacks and side-channel leakage. Furthermore, adaptive backpressure flow control dynamically throttles transmission according to client buffer capacity, preventing browser memory exhaustion during gigabyte-scale transfers. In conclusion, the PeerVault AI architecture successfully guarantees zero-knowledge end-to-end encryption, high-throughput local network synchronization, and resilient NAT traversal.`;
      aiTextInput.value = sampleText;
      aiCharCount.textContent = `${sampleText.length} characters`;
      showToast('Sample technical abstract loaded!', 'info');
      playTone('click');
    });
  }

  /* =============================================
     INITIAL RENDER & URL INVITE DETECTION
     ============================================= */
  renderPeersList();
  logEvent('PeerVault AI — All 8 Editions ready. Generating ECDH keys...', 'system');

  // Auto-fill and auto-join if invite link was clicked (?room=...)
  const urlParams = new URLSearchParams(window.location.search);
  const queryRoom = urlParams.get('room');
  if (queryRoom) {
    roomIdInput.value = queryRoom;
    logEvent(`URL invite detected for room: "${queryRoom}". Joining automatically...`, 'info');
    showToast(`Invite detected for room: ${queryRoom}`, 'gold');
    setTimeout(() => {
      joinRoom();
    }, 700);
  }

})();
