# thesis_prelims.py
# Preliminary pages: Cover, Declaration, Certificate, Acknowledgments, Abstract, TOC, Lists, Nomenclature
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
from reportlab.lib import colors

def build_preliminaries(styles):
    flowables = []

    # ---------------------------------------------------------
    # 1. COVER PAGE / TITLE PAGE (Page 1)
    # ---------------------------------------------------------
    flowables.append(Spacer(1, 20))
    flowables.append(Paragraph("NATIONAL INSTITUTE OF TECHNOLOGY AGARTALA", styles['CoverInst']))
    flowables.append(Paragraph("DEPARTMENT OF COMPUTER SCIENCE &amp; ENGINEERING<br/>BARJALA, JIRANIA, TRIPURA (W) - 799046, INDIA", styles['CoverDept']))
    flowables.append(HRFlowable(width="100%", thickness=1.8, color=colors.HexColor("#991b1b"), spaceBefore=0, spaceAfter=25))

    flowables.append(Paragraph("PEERVAULT AI: BROWSER-NATIVE LAN PEER-TO-PEER END-TO-END ENCRYPTED FILE TRANSFER &amp; LOCAL INTELLIGENCE ARCHITECTURE", styles['CoverTitle']))
    flowables.append(Paragraph("A Capstone B.Tech Thesis Submitted in Partial Fulfillment of the Requirements<br/>for the Degree of <b>Bachelor of Technology</b> in <b>Computer Science and Engineering</b>", styles['CoverSub']))

    flowables.append(Spacer(1, 35))

    meta_data = [
        [Paragraph("<b>Submitted By:</b>", styles['CoverMetaHeader']), Paragraph("<b>Under the Guidance of:</b>", styles['CoverMetaHeader'])],
        [Paragraph("<b>RAM PEDAPATI</b><br/>Enrollment No: 23UCS191<br/>Registration No: 2317098<br/>B.Tech CSE (Class of 2027)<br/>Department of Computer Science &amp; Engg.<br/>National Institute of Technology Agartala<br/>Email: ramcode9841@gmail.com", styles['CoverMetaVal']),
         Paragraph("<b>Department Faculty Supervisor</b><br/>Department of Computer Science &amp; Engineering<br/>National Institute of Technology Agartala<br/>Barjala, Jirania, Tripura (W) - 799046", styles['CoverMetaVal'])],
    ]
    t_meta = Table(meta_data, colWidths=[250, 250])
    t_meta.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    flowables.append(t_meta)

    flowables.append(Spacer(1, 40))
    flowables.append(HRFlowable(width="100%", thickness=0.8, color=colors.HexColor("#cbd5e1"), spaceBefore=10, spaceAfter=15))
    flowables.append(Paragraph("Academic Session: 2026 - 2027<br/>Repository: github.com/ramcode-dev/peervault-ai | Production: peervault-ai.onrender.com", styles['CoverFoot']))
    flowables.append(PageBreak())

    # ---------------------------------------------------------
    # 2. CANDIDATE'S DECLARATION (Page 2)
    # ---------------------------------------------------------
    flowables.append(Paragraph("DECLARATION OF ORIGINALITY", styles['ChapTitle']))
    flowables.append(HRFlowable(width="100%", thickness=1.2, color=colors.HexColor("#991b1b"), spaceBefore=0, spaceAfter=16))

    flowables.append(Paragraph(
        "I hereby declare that the capstone project work entitled <b>\"PeerVault AI: Browser-Native LAN Peer-to-Peer End-to-End Encrypted File Transfer &amp; Local Intelligence Architecture\"</b> submitted to the Department of Computer Science &amp; Engineering, National Institute of Technology Agartala, is an authentic record of original engineering work carried out by me under academic supervision.",
        styles['Body']
    ))
    flowables.append(Paragraph(
        "The project formulates, designs, implements, and benchmarks a serverless peer-to-peer data transport pipeline using WebRTC SCTP DataChannels, Web Cryptography API (ECDH NIST P-256 and AES-GCM-256), adaptive backpressure queuing, and in-browser natural language processing. I confirm that no portion of this work has been submitted elsewhere for the award of any other degree, diploma, fellowship, or professional certification.",
        styles['Body']
    ))
    flowables.append(Paragraph(
        "Wherever third-party specifications, standard RFCs (RFC 8829, RFC 8831, RFC 8445, RFC 4960, RFC 5869, RFC 8446), cryptographic primitives, or open-source software libraries have been consulted or used, proper academic citations and standard acknowledgments are explicitly provided in the bibliography.",
        styles['Body']
    ))
    flowables.append(Spacer(1, 40))

    sig_data = [
        [Paragraph("<b>Date:</b> November 19, 2026<br/><b>Place:</b> NIT Agartala, Jirania", styles['CoverMetaVal']),
         Paragraph("<b>RAM PEDAPATI</b><br/>Roll Number: 23UCS191<br/>Registration Number: 2317098<br/>Department of Computer Science &amp; Engineering<br/>National Institute of Technology Agartala", styles['CoverMetaVal'])]
    ]
    t_sig = Table(sig_data, colWidths=[240, 260])
    t_sig.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    flowables.append(t_sig)
    flowables.append(PageBreak())

    # ---------------------------------------------------------
    # 3. CERTIFICATE OF APPROVAL (Page 3)
    # ---------------------------------------------------------
    flowables.append(Paragraph("CERTIFICATE OF APPROVAL", styles['ChapTitle']))
    flowables.append(HRFlowable(width="100%", thickness=1.2, color=colors.HexColor("#991b1b"), spaceBefore=0, spaceAfter=16))

    flowables.append(Paragraph(
        "This is to certify that the project entitled <b>\"PeerVault AI: Browser-Native LAN Peer-to-Peer End-to-End Encrypted File Transfer &amp; Local Intelligence Architecture\"</b> submitted by <b>RAM PEDAPATI (Roll No: 23UCS191, Reg No: 2317098)</b> to the Department of Computer Science &amp; Engineering, National Institute of Technology Agartala, is approved as a bona fide capstone project work.",
        styles['Body']
    ))
    flowables.append(Paragraph(
        "The project has been examined and evaluated by the internal and external examination committees on the basis of technical design, algorithmic rigor, cryptographic implementation, network benchmarking, and oral defense.",
        styles['Body']
    ))
    flowables.append(Spacer(1, 50))

    cert_signatures = [
        [Paragraph("____________________________<br/><b>Project Supervisor</b><br/>Department of CSE<br/>NIT Agartala", styles['CoverMetaVal']),
         Paragraph("____________________________<br/><b>Head of Department</b><br/>Department of CSE<br/>NIT Agartala", styles['CoverMetaVal'])],
        [Paragraph("<br/><br/>____________________________<br/><b>Internal Examiner</b><br/>Department of CSE<br/>NIT Agartala", styles['CoverMetaVal']),
         Paragraph("<br/><br/>____________________________<br/><b>External Examiner</b><br/>Board of Examiners<br/>NIT Agartala", styles['CoverMetaVal'])],
    ]
    t_cert = Table(cert_signatures, colWidths=[250, 250])
    t_cert.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 20),
    ]))
    flowables.append(t_cert)
    flowables.append(PageBreak())

    # ---------------------------------------------------------
    # 4. ACKNOWLEDGMENTS (Page 4)
    # ---------------------------------------------------------
    flowables.append(Paragraph("ACKNOWLEDGMENTS", styles['ChapTitle']))
    flowables.append(HRFlowable(width="100%", thickness=1.2, color=colors.HexColor("#991b1b"), spaceBefore=0, spaceAfter=16))

    flowables.append(Paragraph(
        "I express my deepest gratitude to my Project Supervisor and the faculty members of the Department of Computer Science &amp; Engineering at the National Institute of Technology Agartala for their intellectual guidance, technical critiques, and encouragement throughout the inception and development of PeerVault AI.",
        styles['Body']
    ))
    flowables.append(Paragraph(
        "I am profoundly grateful to the Head of the Department and the administration of NIT Agartala for providing access to the campus high-throughput computing facilities, experimental wireless LAN testbeds, and academic laboratory infrastructure essential for conducting multi-gigabit throughput and packet loss benchmarking.",
        styles['Body']
    ))
    flowables.append(Paragraph(
        "Special thanks are due to my peers, friends, and technical colleagues whose collaborative testing sessions across heterogeneous mobile and desktop operating systems enabled the discovery, debugging, and resolution of critical buffer backpressure bottlenecks, Web Crypto cross-browser quirks, and NAT candidate gathering edge cases.",
        styles['Body']
    ))
    flowables.append(Paragraph(
        "Finally, I extend my heartfelt gratitude to my family for their enduring support, patience, and motivation during long hours of research, code implementation, and mathematical modeling.",
        styles['Body']
    ))
    flowables.append(Spacer(1, 25))
    flowables.append(Paragraph("<b>Ram Pedapati</b><br/>Department of Computer Science &amp; Engineering<br/>National Institute of Technology Agartala", styles['CoverMetaVal']))
    flowables.append(PageBreak())

    # ---------------------------------------------------------
    # 5. ABSTRACT & EXECUTIVE SUMMARY (Pages 5-6)
    # ---------------------------------------------------------
    flowables.append(Paragraph("ABSTRACT", styles['ChapTitle']))
    flowables.append(HRFlowable(width="100%", thickness=1.2, color=colors.HexColor("#991b1b"), spaceBefore=0, spaceAfter=14))

    flowables.append(Paragraph(
        "Contemporary data transfer workflows in enterprise, academic, and domestic local area networks (LANs) predominantly route file payloads through centralized third-party cloud infrastructure (e.g., Google Drive, Dropbox, WeTransfer). This paradigm imposes substantial bandwidth inefficiencies, double transmission latency, storage quota limitations, and serious privacy risks arising from unauthorized intermediary access or subpoena exposure.",
        styles['Body']
    ))
    flowables.append(Paragraph(
        "This thesis presents <b>PeerVault AI</b>, a fully browser-native, zero-installation, peer-to-peer (P2P) data transport and intelligence platform engineered to eliminate intermediary storage servers entirely. PeerVault AI establishes direct, authenticated, full-duplex peer connections across local area networks and wide area networks using WebRTC SCTP DataChannels negotiated via an ephemeral Node.js signaling plane.",
        styles['Body']
    ))
    flowables.append(Paragraph(
        "Security is enforced through a zero-knowledge cryptographic pipeline implemented via the W3C Web Cryptography API. Peers execute an Elliptic Curve Diffie-Hellman (ECDH) key exchange over the NIST P-256 curve to derive a shared 256-bit master secret, which is fed into HKDF to generate symmetric keys. Payloads are partitioned into 64KB binary chunks and encrypted using AES-GCM-256 with cryptographically unique 96-bit initialization vectors (IVs) per chunk, guaranteeing confidentiality and forward secrecy without server-side key exposure.",
        styles['Body']
    ))
    flowables.append(Paragraph(
        "To prevent browser process crashes when handling multi-gigabyte files, an adaptive backpressure flow-control algorithm monitors the SCTP <code>bufferedAmount</code> buffer against a dynamic 4MB high-water threshold, pausing file reads until the hardware network interface card dispatches packets. an in-browser Term Frequency-Inverse Document Frequency (TF-IDF) natural language processing engine analyzes shared text documents locally to generate instant extractive summaries without cloud API roundtrips.",
        styles['Body']
    ))
    flowables.append(Paragraph(
        "Empirical benchmarks across Wi-Fi 6 (802.11ax) LAN testbeds demonstrate that PeerVault AI achieves sustained transfer throughput of <b>285 Mbps</b> (peaking at <b>420 Mbps</b>), reducing data transfer latency by <b>87.4% - 95.3%</b> compared to cloud storage uploads, while maintaining an uncompromised memory footprint below <b>45 MB RAM</b> on mobile devices. The complete architecture is deployed in production at <code>peervault-ai.onrender.com</code>.",
        styles['Body']
    ))
    flowables.append(Spacer(1, 10))
    flowables.append(Paragraph("<b>Keywords:</b> WebRTC, SCTP DataChannel, Peer-to-Peer, Zero-Knowledge Encryption, ECDH P-256, AES-GCM-256, Flow Control, Buffer Backpressure, Browser Security, TF-IDF NLP.", styles['BodyBold']))

    flowables.append(Spacer(1, 14))
    flowables.append(Paragraph("EXECUTIVE SUMMARY &amp; ENGINEERING HIGHLIGHTS", styles['SecTitle']))
    flowables.append(Paragraph(
        "A high-level synthesis of the system engineering deliverables and architectural innovations comprises:",
        styles['Body']
    ))
    flowables.append(Paragraph("• <b>Transport Decoupling:</b> Clean separation of lightweight signaling (Socket.io) from data streaming (WebRTC SCTP), ensuring the server processes &lt;5 KB of metadata per session.", styles['Bullet']))
    flowables.append(Paragraph("• <b>Hardware-Accelerated Cryptography:</b> In-browser Web Cryptography API leverages CPU AES-NI and ARMv8 cryptographic extensions for &gt;1.2 GB/s encryption throughput.", styles['Bullet']))
    flowables.append(Paragraph("• <b>Zero-Friction Link Onboarding:</b> Automated URL parameter extraction (<code>?room=room-XXXX</code>) eliminates code entry friction for non-technical users.", styles['Bullet']))
    flowables.append(Paragraph("• <b>Local Intelligence Layer:</b> Client-side extractive document summarization operates completely offline without external API dependencies or telemetry.", styles['Bullet']))
    flowables.append(Paragraph("• <b>Deterministic Memory Bounds:</b> Closed-loop flow control enforces a hard 4 MB heap ceiling, enabling gigabyte-scale transfers on low-spec mobile hardware.", styles['Bullet']))
    flowables.append(PageBreak())

    # ---------------------------------------------------------
    # 6. TABLE OF CONTENTS (Pages 7-8)
    # ---------------------------------------------------------
    flowables.append(Paragraph("TABLE OF CONTENTS", styles['ChapTitle']))
    flowables.append(HRFlowable(width="100%", thickness=1.2, color=colors.HexColor("#991b1b"), spaceBefore=0, spaceAfter=14))

    toc_entries = [
        ("Candidate's Declaration", "ii"),
        ("Certificate of Approval", "iii"),
        ("Acknowledgments", "iv"),
        ("Abstract & Executive Summary", "v"),
        ("List of Figures", "viii"),
        ("List of Tables", "ix"),
        ("Abbreviations & Nomenclature", "x"),
        ("Chapter 1: Introduction & Research Motivation", "11"),
        ("    1.1 The Centralized Cloud Dilemma in Local Area Networks", "11"),
        ("    1.2 Campus Network Dynamics: The NIT Agartala Context", "11"),
        ("    1.3 Threat Environment: Interception, ISP Throttling & Eavesdropping", "12"),
        ("    1.4 PeerVault AI: Core Vision & Architectural Philosophy", "12"),
        ("    1.5 Problem Statement and Formal Research Objectives", "13"),
        ("    1.6 Formal Research Hypotheses", "13"),
        ("    1.7 Comparative Survey of Related Academic & Open-Source Works", "14"),
        ("Chapter 2: Literature Survey & Theoretical Foundations", "14"),
        ("    2.1 Historical Evolution of P2P Architectures (Napster to BitTorrent)", "14"),
        ("    2.2 WebRTC Standards & Architecture (RFC 8829 & RFC 8831)", "14"),
        ("    2.3 JavaScript Session Establishment Protocol (JSEP, RFC 8829)", "15"),
        ("    2.4 SCTP 4-Way Handshake vs. TCP 3-Way Handshake Mechanics", "15"),
        ("    2.5 NAT Traversal Dynamics: STUN, TURN, and ICE (RFC 8445)", "15"),
        ("    2.6 Transport Layer Tradeoffs: TCP vs. UDP vs. SCTP", "16"),
        ("    2.7 Cryptographic Foundations: ECDH NIST P-256 & AES-GCM", "16"),
        ("    2.8 State-of-the-Art Comparative Analysis Matrix", "17"),
        ("Chapter 3: System Requirements & Mathematical Formulations", "18"),
        ("    3.1 Software Requirements Specification (Functional & Non-Functional)", "18"),
        ("    3.2 Network Information Theory: Shannon-Hartley Wi-Fi Capacity", "18"),
        ("    3.3 Bandwidth-Delay Product (BDP) and Flow Scaling Models", "19"),
        ("    3.4 Threat Modeling under the Dolev-Yao Adversarial Paradigm", "19"),
        ("    3.5 Queueing Theory: M/M/1/K Buffer Overflow Analysis", "20"),
        ("    3.6 Zero-Trust LAN Micro-Segmentation & Boundary Models", "21"),
        ("Chapter 4: System Architecture & Structural Design", "22"),
        ("    4.1 Dual-Tier Architectural Model (Control Plane vs Data Plane)", "22"),
        ("    4.2 Ephemeral WebSocket Signaling Server Design", "22"),
        ("    4.3 RTCPeerConnection Finite State Automaton", "22"),
        ("    4.4 Data Flow Diagrams (DFD Level 0, Level 1, Level 2)", "22"),
        ("    4.5 End-to-End Handshake & Transfer Sequence Flow", "23"),
        ("    4.6 UI/UX Design System: Cyber Neon Red & Metallic Gold Palette", "23"),
        ("    4.7 Cross-Platform Responsive Layout Mechanics", "23"),
        ("    4.8 Component Interaction Automata & Session Recovery Mechanics", "24"),
        ("Chapter 5: Step-by-Step Implementation of the 8 Editions", "25"),
        ("    5.1 Edition 1: WebSocket Signaling Hub & Dynamic Room Dispatch", "25"),
        ("    5.2 Edition 2: WebRTC DataChannel Integration & ICE Gathering", "26"),
        ("    5.3 Edition 3: 64KB Sliced Binary Streaming & Reassembly Buffer", "26"),
        ("    5.4 Edition 4: Adaptive Buffer Backpressure via bufferedAmountLow", "27"),
        ("    5.5 Edition 5: Real-Time Radar Telemetry & Audio Synthesizer Engine", "27"),
        ("    5.6 Edition 6: Ephemeral ECDH NIST P-256 Key Agreement", "28"),
        ("    5.7 Edition 7: Zero-Knowledge AES-GCM-256 Payload Encryption", "29"),
        ("    5.8 Edition 8: Client-Side TF-IDF NLP Document Summarizer", "29"),
        ("Chapter 6: Cryptographic Protocols & Security Verification", "31"),
        ("    6.1 ECDH NIST P-256 Key Agreement Formalism", "31"),
        ("    6.2 Elliptic Curve Group Law & Point Arithmetic Proofs", "31"),
        ("    6.3 AES-GCM-256 Cipher Block Mechanics & 96-Bit Nonce Uniqueness", "31"),
        ("    6.4 Galois Field Polynomial Multiplication Formalism (GHASH)", "32"),
        ("    6.5 Replay Attack Prevention and Tamper Detection Metrics", "32"),
        ("    6.6 V8 Memory Hygiene & Zero-Knowledge Security Audit", "32"),
        ("    6.7 Cryptographic Parameter & Cipher Suite Specifications", "33"),
        ("    6.8 Cryptographic Nonce Collision Bounds & Replay Window Analysis", "33"),
        ("Chapter 7: Experimental Benchmarks & Network Evaluation", "34"),
        ("    7.1 Experimental Testbed Configuration and Hardware Specs", "34"),
        ("    7.2 Throughput Performance: PeerVault AI vs. Cloud Relays", "34"),
        ("    7.3 Memory Footprint & RAM Stability under 4MB Backpressure", "34"),
        ("    7.4 Packet Loss Resilience & Network Jitter Tolerance", "35"),
        ("    7.5 Heterogeneous Cross-OS Goodput Matrix", "35"),
        ("    7.6 Chunk Size Sensitivity Analysis", "35"),
        ("Chapter 8: Comprehensive Faculty Viva Voce Defense (85 Questions)", "37"),
        ("Chapter 9: Conclusion, Limitations & Future Horizons", "50"),
        ("    9.1 Summary of Technical Contributions", "50"),
        ("    9.2 Engineering Limitations and Edge Case Constraints", "50"),
        ("    9.3 Future Research Roadmap", "50"),
        ("References & Standards Bibliography", "52"),
        ("Appendix A: Production Signaling Server Source Listing (server.js)", "55"),
        ("Appendix B: WebRTC Cryptographic Pipeline Listing (app.js)", "56"),
        ("Appendix C: Cybernetic UI Design Stylesheet (style.css)", "57"),
        ("Appendix D: HyperText Markup Interface (index.html)", "58"),
        ("Appendix E: Production Dockerfile & Render Cloud Manifests", "59"),
        ("Appendix F: Full Repository Directory Architecture", "59"),
    ]

    t_data = []
    for title, pg in toc_entries:
        if title.startswith("Chapter"):
            t_data.append([Paragraph(f"<b>{title}</b>", styles['TOCChap']), Paragraph(f"<b>{pg}</b>", styles['TOCPage'])])
        elif title.startswith("    "):
            t_data.append([Paragraph(f"&nbsp;&nbsp;&nbsp;&nbsp;{title.strip()}", styles['TOCItem']), Paragraph(pg, styles['TOCItem'])])
        else:
            t_data.append([Paragraph(title, styles['TOCItem']), Paragraph(pg, styles['TOCItem'])])

    t_toc = Table(t_data, colWidths=[440, 60])
    t_toc.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('TOPPADDING', (0,0), (-1,-1), 2),
    ]))
    flowables.append(t_toc)
    flowables.append(PageBreak())

    # ---------------------------------------------------------
    # 7. LIST OF FIGURES & TABLES (Page 9)
    # ---------------------------------------------------------
    flowables.append(Paragraph("LIST OF FIGURES &amp; TABLES", styles['ChapTitle']))
    flowables.append(HRFlowable(width="100%", thickness=1.2, color=colors.HexColor("#991b1b"), spaceBefore=0, spaceAfter=14))

    flowables.append(Paragraph("<b>List of Figures</b>", styles['SecTitle']))
    figs = [
        ("Figure 1.1: Centralized Cloud Storage vs Direct Peer-to-Peer Data Path", "2"),
        ("Figure 2.1: WebRTC Protocol Stack (DTLS, SCTP, SRTP over UDP)", "18"),
        ("Figure 2.2: Interactive Connectivity Establishment (ICE) Traversal Flow", "21"),
        ("Figure 2.3: Head-of-Line Blocking Comparison in TCP vs Multi-Stream SCTP", "25"),
        ("Figure 3.1: Shannon Capacity vs Signal-to-Noise Ratio in 802.11ax LAN", "39"),
        ("Figure 3.2: M/M/1/K Finite Queue State Transition Model", "47"),
        ("Figure 4.1: PeerVault AI Dual-Tier Architecture (Control vs Data Plane)", "51"),
        ("Figure 4.2: WebRTC PeerConnection State Transition Diagram", "55"),
        ("Figure 4.3: End-to-End Signaling, Key Agreement & Chunking Sequence", "60"),
        ("Figure 5.1: 64KB Slicing & BufferedAmount Backpressure Control Loop", "75"),
        ("Figure 5.2: UI Architecture: Concentric Radar & Telemetry Display", "78"),
        ("Figure 6.1: Zero-Knowledge ECDH P-256 & AES-GCM-256 Encryption Pipeline", "90"),
        ("Figure 7.1: Throughput Comparison: PeerVault AI LAN vs Google Drive", "102"),
        ("Figure 7.2: Memory Allocation Profile (RAM) with Backpressure Active", "106"),
    ]
    f_rows = [[Paragraph(f, styles['TOCItem']), Paragraph(p, styles['TOCItem'])] for f, p in figs]
    t_figs = Table(f_rows, colWidths=[440, 60])
    flowables.append(t_figs)

    flowables.append(Spacer(1, 14))
    flowables.append(Paragraph("<b>List of Tables</b>", styles['SecTitle']))
    tables_list = [
        ("Table 2.1: Comparative Matrix: PeerVault AI vs Centralized & P2P Tools", "34"),
        ("Table 3.1: Functional & Non-Functional Requirements Specification", "36"),
        ("Table 3.2: Dolev-Yao Threat Model & Corresponding Mitigations", "44"),
        ("Table 4.1: Pitch Black & Cyber Neon Red UI Design Tokens", "62"),
        ("Table 5.1: Architectural Evolution across the 8 Project Editions", "66"),
        ("Table 6.1: Cryptographic Parameter & Cipher Suite Specification", "92"),
        ("Table 7.1: Experimental Hardware & Network Testbed Parameters", "100"),
        ("Table 7.2: Transfer Latency (Seconds) across Varying Payload Sizes", "104"),
        ("Table 7.3: Network Jitter & Packet Loss Impact on Transfer Goodput", "108"),
    ]
    t_rows = [[Paragraph(t, styles['TOCItem']), Paragraph(p, styles['TOCItem'])] for t, p in tables_list]
    t_tbls = Table(t_rows, colWidths=[440, 60])
    flowables.append(t_tbls)
    flowables.append(PageBreak())

    # ---------------------------------------------------------
    # 8. ABBREVIATIONS & NOMENCLATURE (Pages 10-11)
    # ---------------------------------------------------------
    flowables.append(Paragraph("ABBREVIATIONS &amp; MATHEMATICAL NOMENCLATURE", styles['ChapTitle']))
    flowables.append(HRFlowable(width="100%", thickness=1.2, color=colors.HexColor("#991b1b"), spaceBefore=0, spaceAfter=14))

    abbr_data = [
        [Paragraph("<b>Symbol / Term</b>", styles['TableHead']), Paragraph("<b>Expansion &amp; Contextual Definition</b>", styles['TableHead'])],
        [Paragraph("AEAD", styles['TableCellBold']), Paragraph("Authenticated Encryption with Associated Data (NIST SP 800-38D)", styles['TableCell'])],
        [Paragraph("AES-GCM", styles['TableCellBold']), Paragraph("Advanced Encryption Standard in Galois/Counter Mode (256-bit key)", styles['TableCell'])],
        [Paragraph("AWGN", styles['TableCellBold']), Paragraph("Additive White Gaussian Noise (Stochastic channel impairment model)", styles['TableCell'])],
        [Paragraph("BDP", styles['TableCellBold']), Paragraph("Bandwidth-Delay Product (Link capacity multiplied by round-trip time: RTT &times; BW)", styles['TableCell'])],
        [Paragraph("B.Tech", styles['TableCellBold']), Paragraph("Bachelor of Technology (Computer Science &amp; Engineering)", styles['TableCell'])],
        [Paragraph("CSP", styles['TableCellBold']), Paragraph("Content Security Policy (W3C standard mitigating cross-site scripting)", styles['TableCell'])],
        [Paragraph("CSMA/CA", styles['TableCellBold']), Paragraph("Carrier-Sense Multiple Access with Collision Avoidance (IEEE 802.11 MAC)", styles['TableCell'])],
        [Paragraph("DFD", styles['TableCellBold']), Paragraph("Data Flow Diagram (Structural multi-level process architecture)", styles['TableCell'])],
        [Paragraph("DPI", styles['TableCellBold']), Paragraph("Deep Packet Inspection (Advanced packet payload analysis by ISPs)", styles['TableCell'])],
        [Paragraph("DTLS", styles['TableCellBold']), Paragraph("Datagram Transport Layer Security (RFC 6347 / RFC 9147)", styles['TableCell'])],
        [Paragraph("ECDH", styles['TableCellBold']), Paragraph("Elliptic Curve Diffie-Hellman Key Agreement (NIST P-256 / secp256r1)", styles['TableCell'])],
        [Paragraph("GHASH", styles['TableCellBold']), Paragraph("Galois Field 2^128 polynomial hash function used in GCM authentication", styles['TableCell'])],
        [Paragraph("HKDF", styles['TableCellBold']), Paragraph("HMAC-based Extract-and-Expand Key Derivation Function (RFC 5869)", styles['TableCell'])],
        [Paragraph("HOLB", styles['TableCellBold']), Paragraph("Head-of-Line Blocking (Queue latency induced by packet loss)", styles['TableCell'])],
        [Paragraph("HSTS", styles['TableCellBold']), Paragraph("HTTP Strict Transport Security (RFC 6797 web security header)", styles['TableCell'])],
        [Paragraph("ICE", styles['TableCellBold']), Paragraph("Interactive Connectivity Establishment (RFC 8445 traversal protocol)", styles['TableCell'])],
        [Paragraph("IND-CCA2", styles['TableCellBold']), Paragraph("Indistinguishability under Adaptive Chosen-Ciphertext Attack (Security standard)", styles['TableCell'])],
        [Paragraph("IV", styles['TableCellBold']), Paragraph("Initialization Vector (96-bit cryptographic nonce for GCM)", styles['TableCell'])],
        [Paragraph("JSEP", styles['TableCellBold']), Paragraph("JavaScript Session Establishment Protocol (RFC 8829 WebRTC model)", styles['TableCell'])],
        [Paragraph("LAN", styles['TableCellBold']), Paragraph("Local Area Network (IEEE 802.3 Ethernet / IEEE 802.11 Wi-Fi)", styles['TableCell'])],
        [Paragraph("MIMO", styles['TableCellBold']), Paragraph("Multiple-Input Multiple-Output (Spatial antenna multiplexing in Wi-Fi 6)", styles['TableCell'])],
        [Paragraph("MitM", styles['TableCellBold']), Paragraph("Man-in-the-Middle (Adversarial interception attack paradigm)", styles['TableCell'])],
        [Paragraph("MTU", styles['TableCellBold']), Paragraph("Maximum Transmission Unit (Network packet payload limit, typ. 1500 bytes)", styles['TableCell'])],
        [Paragraph("NAT", styles['TableCellBold']), Paragraph("Network Address Translation (RFC 3022 / RFC 4787 IP mapping)", styles['TableCell'])],
        [Paragraph("NIC", styles['TableCellBold']), Paragraph("Network Interface Card (Physical hardware network controller)", styles['TableCell'])],
        [Paragraph("NIST", styles['TableCellBold']), Paragraph("National Institute of Standards and Technology (USA)", styles['TableCell'])],
        [Paragraph("NLP", styles['TableCellBold']), Paragraph("Natural Language Processing (Text analysis and intelligence)", styles['TableCell'])],
        [Paragraph("OFDMA", styles['TableCellBold']), Paragraph("Orthogonal Frequency-Division Multiple Access (Wi-Fi 6 resource scheduling)", styles['TableCell'])],
        [Paragraph("P2P", styles['TableCellBold']), Paragraph("Peer-to-Peer Distributed Network Architecture", styles['TableCell'])],
        [Paragraph("RFC", styles['TableCellBold']), Paragraph("Request for Comments (Internet Engineering Task Force Standards)", styles['TableCell'])],
        [Paragraph("RTT", styles['TableCellBold']), Paragraph("Round-Trip Time (Signal propagation and processing duration)", styles['TableCell'])],
        [Paragraph("SACK", styles['TableCellBold']), Paragraph("Selective Acknowledgment (TCP/SCTP loss recovery mechanism)", styles['TableCell'])],
        [Paragraph("SCTP", styles['TableCellBold']), Paragraph("Stream Control Transmission Protocol (RFC 4960 / RFC 8831)", styles['TableCell'])],
        [Paragraph("SDP", styles['TableCellBold']), Paragraph("Session Description Protocol (RFC 4566 / RFC 8866)", styles['TableCell'])],
        [Paragraph("SNR", styles['TableCellBold']), Paragraph("Signal-to-Noise Ratio (Ratio of signal power to background noise power)", styles['TableCell'])],
        [Paragraph("SRTP", styles['TableCellBold']), Paragraph("Secure Real-time Transport Protocol (RFC 3711 audio/video transport)", styles['TableCell'])],
        [Paragraph("STUN", styles['TableCellBold']), Paragraph("Session Traversal Utilities for NAT (RFC 8489 discovery protocol)", styles['TableCell'])],
        [Paragraph("TF-IDF", styles['TableCellBold']), Paragraph("Term Frequency - Inverse Document Frequency (Statistical NLP Algorithm)", styles['TableCell'])],
        [Paragraph("TSN", styles['TableCellBold']), Paragraph("Transmission Sequence Number (SCTP packet sequencing identifier)", styles['TableCell'])],
        [Paragraph("TURN", styles['TableCellBold']), Paragraph("Traversal Using Relays around NAT (RFC 8656 relay protocol)", styles['TableCell'])],
        [Paragraph("WAN", styles['TableCellBold']), Paragraph("Wide Area Network (Public Internet routing infrastructure)", styles['TableCell'])],
        [Paragraph("WebRTC", styles['TableCellBold']), Paragraph("Web Real-Time Communications (W3C Recommendation / RFC 8829)", styles['TableCell'])],
    ]
    t_abbr = Table(abbr_data, colWidths=[90, 410])
    t_abbr.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#f1f5f9")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
    ]))
    flowables.append(t_abbr)
    flowables.append(PageBreak())

    return flowables
