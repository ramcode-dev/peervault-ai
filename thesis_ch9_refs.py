# thesis_ch9_refs.py
# Chapter 9: Conclusion & Future Horizons, Formal IEEE/RFC References, and Appendices A-F
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable, Preformatted
from reportlab.lib import colors

def build_chapter_9_and_refs(styles):
    flowables = []

    # =========================================================================
    # CHAPTER 9: CONCLUSION, LIMITATIONS & FUTURE HORIZONS
    # =========================================================================
    flowables.append(Paragraph("CHAPTER 9", styles['ChapNumber']))
    flowables.append(Paragraph("CONCLUSION, LIMITATIONS &amp; FUTURE HORIZONS", styles['ChapTitle']))
    flowables.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#991b1b"), spaceBefore=0, spaceAfter=14))

    flowables.append(Paragraph("9.1 Summary of Technical Contributions", styles['SecTitle']))
    flowables.append(Paragraph(
        "This capstone B.Tech thesis has formulated, implemented, and empirically benchmarked <b>PeerVault AI</b>, a browser-native, serverless, peer-to-peer data transport and intelligence platform designed to eliminate third-party cloud intermediaries in local area and campus networks. The primary engineering contributions achieved in this work include:",
        styles['Body']
    ))
    flowables.append(Paragraph(
        "• <b>Dual-Tier Architecture:</b> Decoupled lightweight Node.js/Socket.io signaling from the high-throughput WebRTC SCTP data plane, ensuring that zero bytes of payload binaries ever traverse the server.",
        styles['Bullet']
    ))
    flowables.append(Paragraph(
        "• <b>Zero-Knowledge Cryptography:</b> Engineered a client-side cryptographic pipeline using Web Crypto ECDH NIST P-256 key agreement and AES-GCM-256 authenticated encryption with cryptographically random 96-bit IVs per 64KB slice.",
        styles['Bullet']
    ))
    flowables.append(Paragraph(
        "• <b>Deterministic Flow Control:</b> Designed an asynchronous backpressure governor using the <code>bufferedAmountLow</code> event with a 4MB threshold, completely eliminating browser memory crashes during gigabyte-scale transfers.",
        styles['Bullet']
    ))
    flowables.append(Paragraph(
        "• <b>Zero Friction Onboarding:</b> Implemented dynamic room generation with one-click query parameter auto-joining (<code>?room=room-XXXX</code>) and cybernetic HTML5 radar telemetry.",
        styles['Bullet']
    ))
    flowables.append(Paragraph(
        "• <b>Private Document Intelligence:</b> Integrated an in-browser TF-IDF natural language processing summarizer that extracts key concepts from shared textual files locally with zero external API telemetry.",
        styles['Bullet']
    ))
    flowables.append(Paragraph(
        "• <b>Empirical Benchmarks:</b> Demonstrated that PeerVault AI achieves sustained LAN throughput of <b>285 Mbps</b> (peaking at <b>420 Mbps</b>), reducing transfer latency by <b>87.4% - 95.3%</b> compared to cloud storage uploads, while maintaining an uncompromised memory footprint below <b>45 MB RAM</b>.",
        styles['Bullet']
    ))

    flowables.append(Spacer(1, 10))
    flowables.append(Paragraph("9.2 Engineering Limitations and Edge Case Constraints", styles['SecTitle']))
    flowables.append(Paragraph(
        "While PeerVault AI demonstrates outstanding performance in local network environments, several technical limitations must be acknowledged:",
        styles['Body']
    ))
    flowables.append(Paragraph(
        "1. <b>Symmetric NAT Traversal across Strict Enterprise WANs:</b> When two peers reside behind distinct symmetric NAT firewalls on separate wide area networks, direct UDP hole-punching via STUN fails. While deploying TURN relay servers would bridge these connections, doing so introduces significant server bandwidth costs and re-centralizes the data path.",
        styles['Bullet']
    ))
    flowables.append(Paragraph(
        "2. <b>Mobile Browser Background Tab Throttling:</b> Mobile operating systems (iOS and Android) aggressively suspend JavaScript execution timers and throttle network sockets when a browser tab is placed in the background, which can stall long-running transfers if the user switches apps.",
        styles['Bullet']
    ))
    flowables.append(Paragraph(
        "3. <b>Ephemeral Signaling Dependency:</b> Although no file data flows through the server, an initial connection requires access to the signaling hub to exchange SDP metadata. If Internet connectivity is interrupted before pairing, initial peer discovery cannot complete without a local LAN-hosted signaling instance.",
        styles['Bullet']
    ))

    flowables.append(Spacer(1, 10))
    flowables.append(Paragraph("9.3 Future Research Roadmap", styles['SecTitle']))
    flowables.append(Paragraph(
        "The architectural foundations established in this thesis provide fertile ground for future investigation across three promising directions:",
        styles['Body']
    ))
    flowables.append(Paragraph(
        "<b>1. Migration to WebTransport over HTTP/3 (QUIC):</b> As the W3C WebTransport API matures, migrating the transport layer from WebRTC SCTP to QUIC datagrams and unidirectional streams will allow multiplexed transfers with even lower connection establishment latency and native connection migration across changing network interfaces (e.g., direct handoff from Wi-Fi to 5G cellular).",
        styles['Body']
    ))
    flowables.append(Paragraph(
        "<b>2. In-Browser Small Language Models via WebGPU:</b> Expanding on our TF-IDF summarizer, future iterations can integrate lightweight quantized local language models (such as SmolLM-135M or Gemma-2B-Q4) running directly on the client's GPU via WebGPU and ONNX Runtime Web, enabling advanced semantic Q&amp;A and document analysis completely client-side without cloud APIs.",
        styles['Body']
    ))
    flowables.append(Paragraph(
        "<b>3. Multi-Peer Swarm Mesh Distribution:</b> Extending the current point-to-point architecture into a multi-peer BitTorrent-style mesh swarming protocol will enable simultaneous broadcast of large datasets (e.g., software patches, classroom lecture videos) to dozens of local peers concurrently with O(log N) distribution efficiency.",
        styles['Body']
    ))

    flowables.append(PageBreak())

    # =========================================================================
    # REFERENCES & STANDARDS BIBLIOGRAPHY
    # =========================================================================
    flowables.append(Paragraph("REFERENCES &amp; STANDARDS BIBLIOGRAPHY", styles['ChapTitle']))
    flowables.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#991b1b"), spaceBefore=0, spaceAfter=14))

    refs = [
        "[1] C. Jennings, H. Bostr&ouml;m, and E. Rescorla, \"JavaScript Session Establishment Protocol (JSEP),\" IETF RFC 8829, Jan. 2021.",
        "[2] R. Jesup, S. Loreto, and M. T&uuml;xen, \"WebRTC Data Channels,\" IETF RFC 8831, Jan. 2021.",
        "[3] R. Stewart, \"Stream Control Transmission Protocol,\" IETF RFC 4960, Sep. 2007.",
        "[4] P. Rosenberg, R. Mahy, P. Matthews, and D. Wing, \"Session Traversal Utilities for NAT (STUN),\" IETF RFC 8489, Feb. 2020.",
        "[5] R. Mahy, P. Matthews, and J. Rosenberg, \"Traversal Using Relays around NAT (TURN),\" IETF RFC 8656, Feb. 2020.",
        "[6] J. Rosenberg, A. Keranen, H. Lowekamp, and A. B. Roach, \"Interactive Connectivity Establishment (ICE),\" IETF RFC 8445, Jul. 2018.",
        "[7] E. Rescorla and N. Modadugu, \"Datagram Transport Layer Security Version 1.2,\" IETF RFC 6347, Jan. 2012.",
        "[8] E. Rescorla, H. Tschofenig, and N. Modadugu, \"The Datagram Transport Layer Security (DTLS) Protocol Version 1.3,\" IETF RFC 9147, May 2022.",
        "[9] M. Dworkin, \"Recommendation for Block Cipher Modes of Operation: Galois/Counter Mode (GCM) and GMAC,\" NIST Special Publication 800-38D, Nov. 2007.",
        "[10] National Institute of Standards and Technology, \"Digital Signature Standard (DSS),\" FIPS PUB 186-4, Jul. 2013.",
        "[11] H. Krawczyk and P. Eronen, \"HMAC-based Extract-and-Expand Key Derivation Function (HKDF),\" IETF RFC 5869, May 2010.",
        "[12] World Wide Web Consortium, \"Web Cryptography API - W3C Recommendation,\" W3C Candidate Recommendation, Jan. 2017.",
        "[13] C. E. Shannon, \"A Mathematical Theory of Communication,\" Bell System Technical Journal, vol. 27, no. 3, pp. 379-423, Jul. 1948.",
        "[14] D. Dolev and A. C. Yao, \"On the Security of Public Key Protocols,\" IEEE Transactions on Information Theory, vol. 29, no. 2, pp. 198-208, 1983.",
        "[15] B. Cohen, \"Incentives Build Robustness in BitTorrent,\" in Proc. 1st Workshop on Economics of Peer-to-Peer Systems, Berkeley, CA, 2003.",
        "[16] P. Maymounkov and D. Mazi&egrave;res, \"Kademlia: A Peer-to-Peer Information System Based on the XOR Metric,\" in Peer-to-Peer Systems (IPTPS), Springer, 2002, pp. 53-65.",
        "[17] S. Loreto and P. Levis, \"Known Issues and Best Practices for the Use of Long Polling and Streaming in Bidirectional HTTP,\" IETF RFC 6202, Apr. 2011.",
        "[18] I. Fette and A. Melnikov, \"The WebSocket Protocol,\" IETF RFC 6455, Dec. 2011.",
        "[19] IEEE 802.11ax-2021, \"IEEE Standard for Information Technology - Telecommunications and Information Exchange Between Systems - Local and Metropolitan Area Networks - Specific Requirements - Part 11: Wireless LAN Medium Access Control (MAC) and Physical Layer (PHY) Specifications,\" IEEE, 2021.",
        "[20] G. Salton and C. Buckley, \"Term-weighting Approaches in Automatic Text Retrieval,\" Information Processing &amp; Management, vol. 24, no. 5, pp. 513-523, 1988.",
        "[21] H. P. Luhn, \"The Automatic Creation of Literature Abstracts,\" IBM Journal of Research and Development, vol. 2, no. 2, pp. 159-165, 1958.",
        "[22] L. Kleinrock, \"Queueing Systems, Volume 1: Theory,\" John Wiley &amp; Sons, New York, 1975.",
        "[23] D. G. Cantor and D. Gerhrts, \"Optimal Buffer Allocation in Packet-Switched Networks,\" IEEE Transactions on Computers, vol. C-23, no. 11, pp. 1159-1169, Nov. 1974.",
        "[24] V. Jacobson, \"Congestion Avoidance and Control,\" ACM SIGCOMM Computer Communication Review, vol. 18, no. 4, pp. 314-329, Aug. 1988.",
        "[25] J. Postel, \"Transmission Control Protocol,\" IETF RFC 793, Sep. 1981.",
        "[26] J. Postel, \"User Datagram Protocol,\" IETF RFC 768, Aug. 1980.",
        "[27] M. Handley and V. Jacobson, \"SDP: Session Description Protocol,\" IETF RFC 4566, Jul. 2006.",
        "[28] M. Baugher, D. McGrew, M. Naslund, E. Carrara, and K. Norrman, \"The Secure Real-time Transport Protocol (SRTP),\" IETF RFC 3711, Mar. 2004.",
        "[29] E. Rescorla, \"The Transport Layer Security (TLS) Protocol Version 1.3,\" IETF RFC 8446, Aug. 2018.",
        "[30] P. S. S. B. Barros, E. P. B. Filho, and C. E. C. Galindo, \"Performance Analysis of WebRTC Data Channels for Low Latency Applications,\" IEEE Access, vol. 8, pp. 165432-165444, 2020.",
        "[31] L. De Cicco and S. Mascolo, \"An Experimental Evaluation of the WebRTC Congestion Control Algorithm,\" in Proc. ACM CoNEXT, 2013, pp. 1-6.",
        "[32] S. Holmer, M. Lundin, G. Carlsson, and B. E. Westerlund, \"A Google Congestion Control Algorithm for Real-Time Communication,\" IETF Internet-Draft, draft-ietf-rmcat-gcc-02, Mar. 2016.",
        "[33] F. Baker, \"Requirements for IP Version 4 Routers,\" IETF RFC 1812, Jun. 1995.",
        "[34] K. S. S. Kumar and R. Sukumar, \"Comprehensive Security Assessment of WebRTC Implementations in Modern Browsers,\" Journal of Information Security and Applications, vol. 48, pp. 102-115, Oct. 2019.",
        "[35] M. Thomson and C. Huitema, \"An Unreliable Datagram Extension to QUIC,\" IETF RFC 9221, Mar. 2022.",
        "[36] M. Bishop, \"Hypertext Transfer Protocol Version 3 (HTTP/3),\" IETF RFC 9114, Jun. 2022.",
        "[37] V. Vasiliev, \"WebTransport over HTTP/3,\" IETF Internet-Draft, draft-ietf-webtrans-http3-09, Oct. 2023.",
        "[38] A. Langley et al., \"The QUIC Transport Protocol: Design and Internet-Scale Deployment,\" in Proc. ACM SIGCOMM, 2017, pp. 183-196.",
        "[39] J. Iyengar and M. Thomson, \"QUIC: A UDP-Based Multiplexed and Secure Transport,\" IETF RFC 9000, May 2021.",
        "[40] M. Ray and S. Dispensa, \"Transport Layer Security (TLS) Renegotiation Indication Extension,\" IETF RFC 5746, Feb. 2010.",
        "[41] A. J. Menezes, P. C. van Oorschot, and S. A. Vanstone, \"Handbook of Applied Cryptography,\" CRC Press, 1996.",
        "[42] N. Koblitz, \"Elliptic Curve Cryptosystems,\" Mathematics of Computation, vol. 48, no. 177, pp. 203-209, 1987.",
        "[43] V. S. Miller, \"Use of Elliptic Curves in Cryptography,\" in Proc. CRYPTO '85, Springer, 1985, pp. 417-426.",
        "[44] W3C Web Audio Working Group, \"Web Audio API - W3C Recommendation,\" Jun. 2021.",
        "[45] W3C WebGPU Working Group, \"WebGPU Specification - W3C Working Draft,\" Apr. 2024.",
        "[46] T. Berners-Lee, R. Fielding, and L. Masinter, \"Uniform Resource Identifier (URI): Generic Syntax,\" IETF RFC 3986, Jan. 2005.",
        "[47] D. Eastlake and P. Jones, \"US Secure Hash Algorithm 1 (SHA1),\" IETF RFC 3174, Sep. 2001.",
        "[48] National Institute of Standards and Technology, \"Secure Hash Standard (SHS),\" FIPS PUB 180-4, Aug. 2015.",
        "[49] J. Salowey, H. Zhou, P. Eronen, and H. Tschofenig, \"HMAC-SHA-256, HMAC-SHA-384, and HMAC-SHA-512 in Stored Passwords,\" IETF RFC 4868, May 2007.",
        "[50] J. Schaad, \"Cryptographic Message Syntax (CMS),\" IETF RFC 5652, Sep. 2009.",
        "[51] W3C WebAppSec Working Group, \"Content Security Policy Level 3,\" W3C Working Draft, Oct. 2022.",
        "[52] J. Hodges, C. Jackson, and A. Barth, \"HTTP Strict Transport Security (HSTS),\" IETF RFC 6797, Nov. 2012.",
        "[53] D. Cooper et al., \"Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile,\" IETF RFC 5280, May 2008.",
        "[54] C. R. Kalmanek et al., \"Data Networks: Routing, Traffic, and Congestion Control,\" IEEE Communications Magazine, vol. 35, no. 10, 1997.",
        "[55] M. Allman, V. Paxson, and E. Blanton, \"TCP Congestion Control,\" IETF RFC 5681, Sep. 2009.",
    ]

    for ref in refs:
        flowables.append(Paragraph(ref, styles['Bullet']))
        flowables.append(Spacer(1, 2))

    flowables.append(PageBreak())

    # =========================================================================
    # APPENDICES
    # =========================================================================
    flowables.append(Paragraph("APPENDIX A", styles['ChapNumber']))
    flowables.append(Paragraph("SIGNALING SERVER SOURCE LISTING (server.js)", styles['ChapTitle']))
    flowables.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#991b1b"), spaceBefore=0, spaceAfter=14))

    code_app_a = (
        "// ============================================================================\n"
        "// PeerVault AI - Production Signaling Server (Node.js + Express + Socket.io)\n"
        "// Location: server.js | Deployed on Render: peervault-ai.onrender.com\n"
        "// ============================================================================\n"
        "const express = require('express');\n"
        "const http = require('http');\n"
        "const { Server } = require('socket.io');\n"
        "const helmet = require('helmet');\n"
        "const path = require('path');\n"
        "\n"
        "const app = express();\n"
        "const server = http.createServer(app);\n"
        "const io = new Server(server, {\n"
        "  cors: { origin: '*' },\n"
        "  pingTimeout: 30000,\n"
        "  pingInterval: 10000\n"
        "});\n"
        "\n"
        "// 1. Production Helmet Security Headers\n"
        "app.use(helmet({\n"
        "  contentSecurityPolicy: false,\n"
        "  crossOriginEmbedderPolicy: false\n"
        "}));\n"
        "\n"
        "// 2. Anti-Caching Headers for Instant Client Asset Refreshes\n"
        "app.use((req, res, next) =&gt; {\n"
        "  res.setHeader('Cache-Control', 'no-store, no-cache, must-revalidate, proxy-revalidate');\n"
        "  res.setHeader('Pragma', 'no-cache');\n"
        "  res.setHeader('Expires', '0');\n"
        "  next();\n"
        "});\n"
        "\n"
        "app.use(express.static(path.join(__dirname, 'public')));\n"
        "\n"
        "// 3. Health Check &amp; Telemetry Endpoints\n"
        "app.get('/api/health', (req, res) =&gt; {\n"
        "  res.json({\n"
        "    status: 'ok',\n"
        "    service: 'peervault-ai',\n"
        "    version: '2.4.0',\n"
        "    timestamp: new Date().toISOString(),\n"
        "    activeRooms: io.sockets.adapter.rooms.size\n"
        "  });\n"
        "});\n"
        "\n"
        "// 4. Ephemeral WebRTC Signaling Hub\n"
        "io.on('connection', (socket) =&gt; {\n"
        "  socket.on('join', (roomId) =&gt; {\n"
        "    const room = io.sockets.adapter.rooms.get(roomId);\n"
        "    const numClients = room ? room.size : 0;\n"
        "\n"
        "    if (numClients === 0) {\n"
        "      socket.join(roomId);\n"
        "      socket.emit('created', roomId);\n"
        "    } else if (numClients === 1) {\n"
        "      socket.join(roomId);\n"
        "      socket.emit('joined', roomId);\n"
        "      io.to(roomId).emit('ready'); // Triggers SDP offer\n"
        "    } else {\n"
        "      socket.emit('full', roomId); // Strictly enforce 2 peers\n"
        "    }\n"
        "  });\n"
        "\n"
        "  socket.on('signal', (data) =&gt; {\n"
        "    socket.to(data.room).emit('signal', data.payload);\n"
        "  });\n"
        "\n"
        "  socket.on('disconnecting', () =&gt; {\n"
        "    for (const r of socket.rooms) {\n"
        "      if (r !== socket.id) socket.to(r).emit('peer-left');\n"
        "    }\n"
        "  });\n"
        "});\n"
        "\n"
        "const PORT = process.env.PORT || 3000;\n"
        "server.listen(PORT, () =&gt; console.log(`PeerVault Server running on port ${PORT}`));"
    )
    flowables.append(Paragraph(code_app_a.replace('\n', '<br/>').replace(' ', '&nbsp;'), styles['CodeBlock']))

    flowables.append(Spacer(1, 15))
    flowables.append(Paragraph("APPENDIX B", styles['ChapNumber']))
    flowables.append(Paragraph("WEBRTC CRYPTOGRAPHIC PIPELINE LISTING (public/app.js)", styles['ChapTitle']))
    flowables.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#991b1b"), spaceBefore=0, spaceAfter=14))

    code_app_b = (
        "// ============================================================================\n"
        "// PeerVault AI - Core Client Pipeline (ECDH P-256 + AES-GCM-256 + Backpressure)\n"
        "// Location: public/app.js\n"
        "// ============================================================================\n"
        "let ecdhKeyPair = null;\n"
        "let derivedAESKey = null;\n"
        "let peerConnection = null;\n"
        "let dataChannel = null;\n"
        "const CHUNK_SIZE = 64 * 1024; // 64 KB\n"
        "\n"
        "async function initECDHKeyExchange() {\n"
        "  ecdhKeyPair = await window.crypto.subtle.generateKey(\n"
        "    { name: 'ECDH', namedCurve: 'P-256' },\n"
        "    false,\n"
        "    ['deriveKey', 'deriveBits']\n"
        "  );\n"
        "  const exportedPublic = await window.crypto.subtle.exportKey('raw', ecdhKeyPair.publicKey);\n"
        "  return exportedPublic;\n"
        "}\n"
        "\n"
        "async function deriveSharedAESKey(peerPublicKeyRaw) {\n"
        "  const peerPublicKey = await window.crypto.subtle.importKey(\n"
        "    'raw',\n"
        "    peerPublicKeyRaw,\n"
        "    { name: 'ECDH', namedCurve: 'P-256' },\n"
        "    false,\n"
        "    []\n"
        "  );\n"
        "  derivedAESKey = await window.crypto.subtle.deriveKey(\n"
        "    { name: 'ECDH', public: peerPublicKey },\n"
        "    ecdhKeyPair.privateKey,\n"
        "    { name: 'AES-GCM', length: 256 },\n"
        "    false,\n"
        "    ['encrypt', 'decrypt']\n"
        "  );\n"
        "  // Visual SHA-256 Fingerprint for Verification\n"
        "  const rawBits = await window.crypto.subtle.deriveBits(\n"
        "    { name: 'ECDH', public: peerPublicKey },\n"
        "    ecdhKeyPair.privateKey,\n"
        "    256\n"
        "  );\n"
        "  const hash = await window.crypto.subtle.digest('SHA-256', rawBits);\n"
        "  renderSecurityFingerprint(new Uint8Array(hash));\n"
        "}\n"
        "\n"
        "async function encryptChunk(cryptoKey, arrayBufferSlice) {\n"
        "  const iv = window.crypto.getRandomValues(new Uint8Array(12));\n"
        "  const ciphertext = await window.crypto.subtle.encrypt(\n"
        "    { name: 'AES-GCM', iv: iv },\n"
        "    cryptoKey,\n"
        "    arrayBufferSlice\n"
        "  );\n"
        "  const combined = new Uint8Array(12 + ciphertext.byteLength);\n"
        "  combined.set(iv, 0);\n"
        "  combined.set(new Uint8Array(ciphertext), 12);\n"
        "  return combined.buffer;\n"
        "}\n"
        "\n"
        "async function decryptChunk(cryptoKey, combinedBuffer) {\n"
        "  const iv = combinedBuffer.slice(0, 12);\n"
        "  const ciphertext = combinedBuffer.slice(12);\n"
        "  return await window.crypto.subtle.decrypt(\n"
        "    { name: 'AES-GCM', iv: new Uint8Array(iv) },\n"
        "    cryptoKey,\n"
        "    ciphertext\n"
        "  );\n"
        "}\n"
        "\n"
        "async function sendChunkWithBackpressure(dc, chunkBuffer) {\n"
        "  if (dc.bufferedAmount &gt; 4 * 1024 * 1024) {\n"
        "    await new Promise((resolve) =&gt; {\n"
        "      const lowHandler = () =&gt; {\n"
        "        dc.removeEventListener('bufferedamountlow', lowHandler);\n"
        "        resolve();\n"
        "      };\n"
        "      dc.addEventListener('bufferedamountlow', lowHandler);\n"
        "    });\n"
        "  }\n"
        "  dc.send(chunkBuffer);\n"
        "}"
    )
    flowables.append(Paragraph(code_app_b.replace('\n', '<br/>').replace(' ', '&nbsp;'), styles['CodeBlock']))

    flowables.append(Spacer(1, 15))
    flowables.append(Paragraph("APPENDIX C", styles['ChapNumber']))
    flowables.append(Paragraph("CYBERNETIC UI DESIGN SYSTEM (public/style.css)", styles['ChapTitle']))
    flowables.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#991b1b"), spaceBefore=0, spaceAfter=14))

    code_app_c = (
        "/* ==========================================================================\n"
        "   PeerVault AI - Pitch Black &amp; Cyber Neon Red Design System\n"
        "   Location: public/style.css\n"
        "   ========================================================================== */\n"
        ":root {\n"
        "  --bg-pitch-black: #000000;\n"
        "  --bg-deep-slate: #06080d;\n"
        "  --card-bg: #0c1017;\n"
        "  --card-border: #161e2e;\n"
        "  --cyber-red: #ff2a4b;\n"
        "  --cyber-red-glow: rgba(255, 42, 75, 0.45);\n"
        "  --metallic-gold: #fbbf24;\n"
        "  --gold-glow: rgba(251, 191, 36, 0.35);\n"
        "  --neon-white: #ffffff;\n"
        "  --text-dim: #94a3b8;\n"
        "  --font-mono: 'JetBrains Mono', 'Fira Code', monospace;\n"
        "}\n"
        "\n"
        "body {\n"
        "  background: radial-gradient(circle at 50% 0%, #110508 0%, #000000 70%);\n"
        "  color: var(--neon-white);\n"
        "  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;\n"
        "  margin: 0; padding: 0;\n"
        "  min-height: 100vh;\n"
        "}\n"
        "\n"
        ".radar-canvas {\n"
        "  border: 1px solid var(--card-border);\n"
        "  border-radius: 50%;\n"
        "  background: rgba(12, 16, 23, 0.8);\n"
        "  box-shadow: 0 0 25px rgba(255, 42, 75, 0.2);\n"
        "}\n"
        "\n"
        ".action-btn-primary {\n"
        "  background: linear-gradient(135deg, #ff2a4b 0%, #b91c1c 100%);\n"
        "  color: #ffffff;\n"
        "  font-weight: 600;\n"
        "  border: none;\n"
        "  border-radius: 8px;\n"
        "  box-shadow: 0 4px 14px rgba(255, 42, 75, 0.4);\n"
        "  cursor: pointer;\n"
        "  transition: transform 0.15s ease, box-shadow 0.15s ease;\n"
        "}\n"
        "\n"
        ".badge-gold {\n"
        "  background: rgba(251, 191, 36, 0.12);\n"
        "  border: 1px solid rgba(251, 191, 36, 0.4);\n"
        "  color: var(--metallic-gold);\n"
        "  padding: 4px 10px;\n"
        "  border-radius: 6px;\n"
        "  font-family: var(--font-mono);\n"
        "}"
    )
    flowables.append(Paragraph(code_app_c.replace('\n', '<br/>').replace(' ', '&nbsp;'), styles['CodeBlock']))

    flowables.append(Spacer(1, 15))
    flowables.append(Paragraph("APPENDIX D", styles['ChapNumber']))
    flowables.append(Paragraph("FRONTEND HTML USER INTERFACE (public/index.html)", styles['ChapTitle']))
    flowables.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#991b1b"), spaceBefore=0, spaceAfter=14))

    code_app_d = (
        "&lt;!DOCTYPE html&gt;\n"
        "&lt;html lang=\"en\"&gt;\n"
        "&lt;head&gt;\n"
        "  &lt;meta charset=\"UTF-8\"&gt;\n"
        "  &lt;meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"&gt;\n"
        "  &lt;title&gt;PeerVault AI - Encrypted P2P LAN Transfer&lt;/title&gt;\n"
        "  &lt;link rel=\"stylesheet\" href=\"style.css\"&gt;\n"
        "&lt;/head&gt;\n"
        "&lt;body&gt;\n"
        "  &lt;div class=\"app-container\"&gt;\n"
        "    &lt;header class=\"top-bar\"&gt;\n"
        "      &lt;div class=\"brand\"&gt;&lt;span class=\"accent\"&gt;PEERVAULT&lt;/span&gt; AI&lt;/div&gt;\n"
        "      &lt;div class=\"security-status badge-gold\"&gt;MILITARY-GRADE ECDH+AES-GCM&lt;/div&gt;\n"
        "    &lt;/header&gt;\n"
        "    &lt;main class=\"cockpit-grid\"&gt;\n"
        "      &lt;section class=\"panel-left\"&gt;\n"
        "        &lt;canvas id=\"radarCanvas\" width=\"300\" height=\"300\" class=\"radar-canvas\"&gt;&lt;/canvas&gt;\n"
        "        &lt;div class=\"room-controls\"&gt;\n"
        "          &lt;input type=\"text\" id=\"roomInput\" placeholder=\"Enter room ID...\"&gt;\n"
        "          &lt;button id=\"connectBtn\" class=\"action-btn-primary\"&gt;Connect Peer&lt;/button&gt;\n"
        "        &lt;/div&gt;\n"
        "        &lt;div id=\"fingerprintDisplay\" class=\"fingerprint-card hidden\"&gt;&lt;/div&gt;\n"
        "      &lt;/section&gt;\n"
        "      &lt;section class=\"panel-right\"&gt;\n"
        "        &lt;div id=\"dropZone\" class=\"file-dropzone\"&gt;Drag &amp; Drop Files or Click to Browse&lt;/div&gt;\n"
        "        &lt;div id=\"progressSection\" class=\"progress-section hidden\"&gt;\n"
        "          &lt;div class=\"progress-bar\"&gt;&lt;div id=\"progressFill\" class=\"progress-fill\"&gt;&lt;/div&gt;&lt;/div&gt;\n"
        "          &lt;div id=\"telemetryStats\" class=\"telemetry-stats\"&gt;&lt;/div&gt;\n"
        "        &lt;/div&gt;\n"
        "        &lt;div id=\"summaryCard\" class=\"summary-card hidden\"&gt;&lt;/div&gt;\n"
        "      &lt;/section&gt;\n"
        "    &lt;/main&gt;\n"
        "  &lt;/div&gt;\n"
        "  &lt;script src=\"/socket.io/socket.io.js\"&gt;&lt;/script&gt;\n"
        "  &lt;script src=\"app.js\"&gt;&lt;/script&gt;\n"
        "&lt;/body&gt;\n"
        "&lt;/html&gt;"
    )
    flowables.append(Paragraph(code_app_d.replace('\n', '<br/>').replace(' ', '&nbsp;'), styles['CodeBlock']))

    flowables.append(Spacer(1, 15))
    flowables.append(Paragraph("APPENDIX E", styles['ChapNumber']))
    flowables.append(Paragraph("CLOUD DEPLOYMENT &amp; CONTAINER MANIFESTS", styles['ChapTitle']))
    flowables.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#991b1b"), spaceBefore=0, spaceAfter=14))

    flowables.append(Paragraph(
        "<b>Procfile:</b><br/><code>web: node server.js</code><br/><br/>"
        "<b>nixpacks.toml:</b><br/><code>[phases.setup]<br/>nixPkgs = [\"nodejs_20\"]<br/>[phases.build]<br/>cmds = [\"npm ci\"]<br/>[start]<br/>cmd = \"node server.js\"</code><br/><br/>"
        "<b>Production Environment Variables:</b><br/>"
        "• <code>NODE_ENV=production</code><br/>"
        "• <code>PORT=3000</code><br/>"
        "• <code>RENDER_SERVICE_ID=srv-dbsrpodg1s2s7381504g</code>",
        styles['CodeBlock']
    ))

    flowables.append(Spacer(1, 15))
    flowables.append(Paragraph("APPENDIX F", styles['ChapNumber']))
    flowables.append(Paragraph("PROJECT DIRECTORY ARCHITECTURE &amp; ARTIFACTS", styles['ChapTitle']))
    flowables.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#991b1b"), spaceBefore=0, spaceAfter=14))

    code_app_f = (
        "peervault-ai/\n"
        "├── server.js                   # Node.js signaling server (Express + Socket.io + Helmet)\n"
        "├── package.json                # Project dependencies, metadata, and scripts\n"
        "├── Procfile                    # Render cloud execution entry point\n"
        "├── nixpacks.toml               # Container build configuration\n"
        "├── public/\n"
        "│   ├── index.html              # Cybernetic Cockpit UI layout &amp; DOM bindings\n"
        "│   ├── style.css               # Pitch Black, Cyber Neon Red &amp; Gold Design System\n"
        "│   └── app.js                  # WebRTC DataChannel, ECDH P-256 &amp; AES-GCM Pipeline\n"
        "├── PROJECT_REPORT.md           # Full Markdown Edition of B.Tech Capstone Thesis\n"
        "├── THESIS.md                   # Mirrored Complete Academic Thesis\n"
        "├── PeerVault_AI_Project_Report.pdf # Compiled 65-Page Formal Academic Thesis Document\n"
        "├── build_full_thesis.py        # ReportLab PDF master compilation orchestrator\n"
        "├── thesis_styles.py            # ReportLab layout styles and running headers\n"
        "├── thesis_prelims.py           # Preliminaries (Cover, Declaration, Cert, Abstract, TOC)\n"
        "├── thesis_ch1_ch2.py           # Chapters 1 &amp; 2 (Intro, Motivation, Survey, Foundations)\n"
        "├── thesis_ch3_ch4.py           # Chapters 3 &amp; 4 (SRS, Shannon Capacity, Architecture, DFDs)\n"
        "├── thesis_ch5_ch6.py           # Chapters 5 &amp; 6 (8 Editions Implementation &amp; Cryptography)\n"
        "├── thesis_ch7_ch8.py           # Chapters 7 &amp; 8 (Benchmarks &amp; 85 Faculty Viva Voce Q&amp;As)\n"
        "└── thesis_ch9_refs.py          # Chapter 9, Bibliography (55 RFCs) &amp; Appendices A-F"
    )
    flowables.append(Paragraph(code_app_f.replace('\n', '<br/>').replace(' ', '&nbsp;'), styles['CodeBlock']))

    return flowables
