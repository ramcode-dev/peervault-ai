# PeerVault AI 🚀
### AI-Powered LAN Peer-to-Peer End-to-End Encrypted File Sharing Tool
**4th Year Computer Science & Engineering (CSE) Capstone Project**

---

## 📌 Edition 1: Node.js Signaling Server & LAN Discovery Protocol

Welcome to **Edition 1** of PeerVault AI! This milestone establishes the **Signaling Infrastructure** and **LAN Peer Discovery Protocol** required before WebRTC peer-to-peer data pipes can be created.

---

## 🏗️ Architecture Overview

```
+-------------------------------------------------------------------+
|                        LOCAL LAN NETWORK                          |
|                                                                   |
|   +------------------+                    +-------------------+   |
|   |  Browser Peer A  |                    |   Browser Peer B  |   |
|   +--------+---------+                    +---------+---------+   |
|            |                                        |             |
|            |  Socket.io WebSocket Connections       |             |
|            v                                        v             |
|   +-----------------------------------------------------------+   |
|   |             Node.js Express + Socket.io Server            |   |
|   |                  (Signaling Server)                       |   |
|   |   - Subnet/Room Discovery  - SDP Offer/Answer Relay       |   |
|   |   - ICE Candidate Relay    - Disconnect Handling          |   |
|   +-----------------------------------------------------------+   |
+-------------------------------------------------------------------+
```

> ⚠️ **Important Zero-Cloud Privacy Note:**
> In WebRTC architecture, browsers cannot connect directly to each other without knowing each other's IP address, port, and network NAT capabilities. The Node.js server acts **ONLY as a matchmaker (signaling server)**. File data NEVER passes through this server.

---

## 🚀 How to Run Edition 1 Locally

### 1. Install Dependencies
```bash
npm install
```

### 2. Start the Signaling Server
```bash
npm start
```
Or for development with auto-reload:
```bash
npm run dev
```

### 3. Open in Browser
- **Local machine**: `http://localhost:3000`
- **Other devices on the same Wi-Fi**: Open `http://<YOUR_LAN_IP>:3000` (printed in terminal log upon server start).

---

## 🎓 Faculty Viva & Explanation Guide for Edition 1

When presenting **Edition 1** to your project guide or faculty panel, use the following clear bullet points:

### 1. What was built in Edition 1?
> *"In Edition 1, we built the core **Signaling Server** using Node.js, Express, and Socket.io. Signaling is the first step in WebRTC peer-to-peer communication. It allows devices on the same Wi-Fi network to discover each other, create/join rooms, and exchange initial network metadata."*

### 2. Why do we need a Signaling Server if the app is P2P?
> *"WebRTC enables direct browser-to-browser data transfer. However, two browsers do not initially know each other's IP address, port number, or security parameters. The signaling server acts as an initial broker: Browser A sends an SDP Offer to the server, the server relays it to Browser B, Browser B returns an SDP Answer, and both exchange ICE network candidates. Once signaling is complete, browsers establish a direct P2P link and no longer rely on the server."*

### 3. Does the server store or see file data?
> *"No. The signaling server handles only lightweight JSON control messages (`join-room`, `signal-offer`, `signal-answer`, `ice-candidate`). In future editions, binary file chunks will travel directly over the WebRTC DataChannel."*

---

## 🔮 Next Step: Edition 2 Preview
In **Edition 2**, we will implement `RTCPeerConnection` and `RTCDataChannel` in `public/app.js` to convert these signaling connections into direct browser-to-browser P2P text chat pipes!
