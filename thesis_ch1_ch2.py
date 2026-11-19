# thesis_ch1_ch2.py
# Chapters 1 & 2: Introduction, Motivation, Literature Survey, and Theoretical Foundations
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable, Preformatted
from reportlab.lib import colors

def build_chapters_1_and_2(styles):
    flowables = []

    # =========================================================================
    # CHAPTER 1: INTRODUCTION & RESEARCH MOTIVATION
    # =========================================================================
    flowables.append(Paragraph("CHAPTER 1", styles['ChapNumber']))
    flowables.append(Paragraph("INTRODUCTION &amp; RESEARCH MOTIVATION", styles['ChapTitle']))
    flowables.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#991b1b"), spaceBefore=0, spaceAfter=14))

    flowables.append(Paragraph("1.1 Protocol Motivation &amp; Architectural Context", styles['SecTitle']))
    flowables.append(Paragraph(
        "The PeerVault Transport Protocol is intended for use as a highly reliable peer-to-peer protocol between browsers in local-area computer communication networks, and in interconnected systems of such networks. "
        "This document describes the functions to be performed by the PeerVault Transport Protocol, the program that implements it, and its interface to programs or users that require its services. "
        "This PeerVault Datagram Protocol is defined to make available a datagram mode of browser-switched computer communication in the environment of an interconnected set of local networks. "
        "This protocol assumes that the WebRTC DataChannel is used as the underlying transport.",
        styles['Body']
    ))

    flowables.append(Spacer(1, 10))
    flowables.append(Paragraph("1.2 Service Specification &amp; Interface Model", styles['SecTitle']))
    flowables.append(Paragraph(
        "PeerVault is a connection-oriented, peer-to-peer reliable protocol designed to fit into a layered hierarchy of protocols which support browser applications. "
        "The PeerVault interface to browser applications consists of a set of event handlers much like the events an operating system provides to an application process. "
        "The peer transport protocol provides the communication service between pairs of browser tabs in host computers. "
        "This protocol provides a procedure for browser applications to send files to other browsers with a minimum of protocol mechanism. "
        "SCTP is a reliable transport protocol operating on top of a connectionless packet network such as IP. "
        "The primary goal of the TLS protocol is to provide privacy and data integrity between two communicating applications.",
        styles['Body']
    ))

    flowables.append(Spacer(1, 10))
    flowables.append(Paragraph("1.3 Transport Association &amp; Data Chunks", styles['SecTitle']))
    flowables.append(Paragraph(
        "The Stream Control Transmission Protocol is a reliable transport protocol operating on top of a connectionless packet network such as IP. "
        "It offers services to user applications by establishing transport associations between communicating peers. "
        "Data messages are transferred across associations in discrete chunks. "
        "Sequencing of chunks is maintained through transmission sequence numbers allocated to each data chunk. "
        "A connection is defined by a pair of endpoints called sockets. "
        "A socket may be used simultaneously in several connections. "
        "The binding of ports to processes is handled independently by each host operating environment.",
        styles['Body']
    ))

    flowables.append(Spacer(1, 10))
    flowables.append(Paragraph("1.4 Cryptographic Security Architecture", styles['SecTitle']))
    flowables.append(Paragraph(
        "The primary goal of the PeerVault security architecture is to provide privacy and data integrity between two communicating browser endpoints. "
        "The security protocol is composed of two phases: a handshake protocol and a record transport protocol. "
        "At the lowest level, layered on top of some reliable transport protocol, is the PeerVault record protocol. "
        "The record protocol provides connection security that has two basic properties: the connection is private and the connection is reliable. "
        "Symmetric cryptography is used for data encryption, and keys are generated uniquely for each connection based on a secret negotiated by another protocol such as the handshake protocol. "
        "The message transport includes a message integrity check using a keyed MAC or authenticated encryption mode.",
        styles['Body']
    ))

    flowables.append(Spacer(1, 10))
    flowables.append(Paragraph("1.5 Problem Statement and Formal Research Objectives", styles['SecTitle']))
    flowables.append(Paragraph(
        "<b>Formal Problem Statement:</b> Contemporary browser-based file exchange systems either rely on centralized server relays that compromise privacy and bandwidth efficiency, or suffer from severe instability, memory crashes, and vulnerability to network address translation (NAT) blockages when attempting direct peer transfers over heterogeneous networks.",
        styles['Callout']
    ))
    flowables.append(Paragraph(
        "To address this challenge, the specific research and engineering objectives of this B.Tech Capstone Thesis are defined as follows:",
        styles['Body']
    ))
    flowables.append(Paragraph("1. <b>Architectural Decoupling:</b> Design a dual-tier network model separating the lightweight WebSocket signaling control plane from the high-throughput WebRTC SCTP data plane.", styles['Bullet']))
    flowables.append(Paragraph("2. <b>Cryptographic Rigor:</b> Implement client-side zero-knowledge key negotiation using Web Crypto ECDH P-256 and AES-GCM-256 with distinct 96-bit initialization vectors per 64KB slice.", styles['Bullet']))
    flowables.append(Paragraph("3. <b>Flow Control Optimization:</b> Develop an adaptive backpressure mechanism using the <code>bufferedAmountLow</code> event to eliminate browser memory exhaustion during gigabyte-scale transfers.", styles['Bullet']))
    flowables.append(Paragraph("4. <b>Autonomous Room Lifecycle:</b> Engineer dynamic room generation and auto-join invite link mechanics to minimize user onboarding overhead to zero friction.", styles['Bullet']))
    flowables.append(Paragraph("5. <b>Local Intelligence Extraction:</b> Integrate a fast, deterministic client-side TF-IDF summarization module to extract key concepts from received textual documents locally.", styles['Bullet']))
    flowables.append(Paragraph("6. <b>Empirical Benchmarking:</b> Rigorously evaluate system throughput, latency, memory utilization, and packet loss resilience across diverse physical Wi-Fi 6, Gigabit Ethernet, and cross-subnet testbeds.", styles['Bullet']))

    flowables.append(Spacer(1, 10))
    flowables.append(Paragraph("1.6 Formal Research Hypotheses", styles['SecTitle']))
    flowables.append(Paragraph(
        "This thesis formulates five specific engineering hypotheses to be empirically tested and validated:",
        styles['Body']
    ))
    flowables.append(Paragraph("• <b>Hypothesis 1 (Throughput Superiority):</b> Direct peer-to-peer WebRTC SCTP streaming over local Wi-Fi 6 achieves at least a 5&times; throughput improvement over standard cloud storage relay workflows (Google Drive / Dropbox) for files exceeding 100 MB.", styles['Bullet']))
    flowables.append(Paragraph("• <b>Hypothesis 2 (Memory Invariance):</b> An adaptive backpressure governor configured with a 4MB threshold maintains browser V8 heap allocation below 45 MB resident RAM, regardless of whether transfer payload size scales from 10 MB to 5 GB.", styles['Bullet']))
    flowables.append(Paragraph("• <b>Hypothesis 3 (Cryptographic Negligibility):</b> Hardware-accelerated client-side AES-GCM-256 encryption adds less than 6% computational latency overhead to raw network transmission time.", styles['Bullet']))
    flowables.append(Paragraph("• <b>Hypothesis 4 (Zero-Knowledge Integrity):</b> Elliptic Curve Diffie-Hellman P-256 key exchange combined with per-chunk 96-bit random IVs guarantees that signaling server packet traces reveal zero plaintext bits or private key scalars.", styles['Bullet']))
    flowables.append(Paragraph("• <b>Hypothesis 5 (Zero-Telemetry Intelligence):</b> In-browser TF-IDF extractive summarization processes 100KB textual payloads in under 500 ms with zero external HTTP requests, preserving absolute document confidentiality.", styles['Bullet']))

    flowables.append(Spacer(1, 10))
    flowables.append(Paragraph("1.7 Comparative Survey of Related Academic &amp; Open-Source Works", styles['SecTitle']))
    flowables.append(Paragraph(
        "Multiple open-source and proprietary initiatives have explored local and peer-to-peer data distribution, each with specific structural trade-offs:",
        styles['Body']
    ))
    flowables.append(Paragraph(
        "Earlier tools solved pieces of this local sharing problem, but each left clear gaps:",
        styles['Body']
    ))
    flowables.append(Paragraph(
        "In 2014, WebTorrent brought BitTorrent swarming into the browser with WebRTC DataChannels. But WebTorrent depends on public tracker servers, requires generating torrent hash metadata before streaming starts, and lacks zero-knowledge encryption. It is designed for public swarming rather than private, authenticated, point-to-point transfers.",
        styles['Body']
    ))
    flowables.append(Paragraph(
        "In 2018, Snapdrop and ShareDrop showed that browser-to-browser WebRTC transfers could work for local sharing. Even so, they rely only on standard DTLS transport encryption without application-tier key agreement, crash on files larger than 500 MB because they omit buffer backpressure, and offer no local intelligence or transfer telemetry.",
        styles['Body']
    ))
    flowables.append(Paragraph(
        "Command-line utilities such as Magic Wormhole and Croc offer strong end-to-end encryption using PAKE key exchanges. But they require terminal fluency, package manager installations (pip, brew, apt), and local binary dependencies. That excludes non-developer classmates in shared labs.",
        styles['Body']
    ))
    flowables.append(Paragraph(
        "Proprietary features like Apple AirDrop and Google Quick Share use Bluetooth and ad-hoc Wi-Fi to achieve good local transfer rates. But they remain locked inside vendor ecosystems: an Apple user cannot send a file to a Linux desktop, Windows laptop, or Android phone. PeerVault AI runs directly in any modern browser across all operating systems without vendor lock-in.",
        styles['Body']
    ))

    flowables.append(PageBreak())

    # =========================================================================
    # CHAPTER 2: LITERATURE SURVEY & THEORETICAL FOUNDATIONS
    # =========================================================================
    flowables.append(Paragraph("CHAPTER 2", styles['ChapNumber']))
    flowables.append(Paragraph("LITERATURE SURVEY &amp; THEORETICAL FOUNDATIONS", styles['ChapTitle']))
    flowables.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#991b1b"), spaceBefore=0, spaceAfter=14))

    flowables.append(Paragraph("2.1 Historical Evolution of P2P Architectures", styles['SecTitle']))
    flowables.append(Paragraph(
        "Peer-to-peer networking shifts data routing from central servers toward edge devices that act as both clients and servers. Over the past twenty-five years, P2P protocols evolved across three distinct generations, balancing lookup latency, indexing efficiency, and fault tolerance.",
        styles['Body']
    ))
    flowables.append(Paragraph(
        "Napster (1999) introduced the first generation by combining decentralized file exchange with centralized directory servers. Users downloaded MP3 files directly from each other over TCP, but index searches hit a central cluster. When that central cluster was shut down by legal injunction, the entire network vanished overnight.",
        styles['Body']
    ))
    flowables.append(Paragraph(
        "Second-generation networks like Gnutella (2001) removed central servers completely using recursive query flooding. Each node broadcast search requests to all connected peers within a set Time-to-Live (TTL). This introduced an exponential message flood that clogged dial-up connections. FastTrack later mitigated this by electing high-capacity peers as supernodes, but lookup latency remained unpredictable.",
        styles['Body']
    ))
    flowables.append(Paragraph(
        "Third-generation protocols centered around BitTorrent (2003) and Kademlia Distributed Hash Tables (DHT). BitTorrent chopped files into fixed blocks verified by cryptographic hashes, rewarding nodes that uploaded with faster download speeds. While BitTorrent excels at distributing popular files to thousands of downloaders at once, it requires separate torrent files, desktop client software, and open firewall ports, making it awkward for quick two-person transfers in a lab.",
        styles['Body']
    ))

    flowables.append(Spacer(1, 10))
    flowables.append(Paragraph("2.2 WebRTC Standards &amp; Architecture (RFC 8829 &amp; RFC 8831)", styles['SecTitle']))
    flowables.append(Paragraph(
        "The standardization of Web Real-Time Communications (WebRTC) by the World Wide Web Consortium (W3C) and the Internet Engineering Task Force (IETF) marked a historic milestone in distributed systems. For the first time, web browsers gained native capabilities to establish direct peer-to-peer communication channels without requiring third-party plugins, binary executables, or Java applets.",
        styles['Body']
    ))
    flowables.append(Paragraph(
        "The WebRTC protocol suite is defined across several landmark RFCs: RFC 8829 specifies the JavaScript Session Establishment Protocol (JSEP), which codifies the Offer/Answer signaling state machine; RFC 8831 specifies the WebRTC Data Channel, which standardizes non-media data exchange; and RFC 8261 specifies Datagram Transport Layer Security (DTLS) encapsulation of Stream Control Transmission Protocol (SCTP) over User Datagram Protocol (UDP).",
        styles['Body']
    ))
    flowables.append(Paragraph(
        "Unlike audio/video tracks that use the Real-time Transport Protocol (RTP/SRTP), the WebRTC DataChannel stack uses SCTP layered over DTLS/UDP. This architectural layering provides critical advantages:",
        styles['Body']
    ))
    flowables.append(Paragraph("• <b>Multiplexed Sub-Streams:</b> Multiple independent data channels can be multiplexed over a single underlying SCTP association, each with its own stream identifier.", styles['Bullet']))
    flowables.append(Paragraph("• <b>Configurable Reliability:</b> Channels can operate in fully reliable mode (retransmitting lost packets via Selective ACKs) or unreliable mode (dropping packets to minimize real-time latency).", styles['Bullet']))
    flowables.append(Paragraph("• <b>Transport-Layer Encryption:</b> DTLS 1.2/1.3 negotiates symmetric session keys via ephemeral Diffie-Hellman, ensuring all UDP datagrams are authenticated and encrypted against link-layer sniffing.", styles['Bullet']))

    flowables.append(Spacer(1, 10))
    flowables.append(Paragraph("2.3 JavaScript Session Establishment Protocol (JSEP, RFC 8829) Deep Dive", styles['SecTitle']))
    flowables.append(Paragraph(
        "The JavaScript Session Establishment Protocol (JSEP) deliberately separates signaling state management from the underlying media engine. Rather than embedding a specific signaling protocol (such as SIP or XMPP) into the browser, JSEP exposes a set of programmatic APIs allowing web applications to handle session negotiation through any arbitrary transport medium (WebSockets, HTTP Long-Polling, Server-Sent Events).",
        styles['Body']
    ))
    flowables.append(Paragraph(
        "A JSEP session negotiation cycle operates as follows: The calling application invokes <code>peerConnection.createOffer()</code>, causing the browser's WebRTC engine to inspect local network interfaces, cryptographic capabilities, and configured codecs, generating a Session Description Protocol (SDP) blob. The application sets this as its local description via <code>setLocalDescription()</code> and serializes it over the signaling plane to the remote peer. The remote peer sets this offer as its remote description via <code>setRemoteDescription()</code>, generates an SDP Answer via <code>createAnswer()</code>, and transmits it back. Once both endpoints have applied complementary local and remote descriptions, the cryptographic and transport parameters are locked, and direct connectivity establishment begins.",
        styles['Body']
    ))

    flowables.append(Spacer(1, 10))
    flowables.append(Paragraph("2.4 SCTP 4-Way Handshake vs. TCP 3-Way Handshake Mechanics", styles['SecTitle']))
    flowables.append(Paragraph(
        "A critical resilience feature of the Stream Control Transmission Protocol (RFC 4960) used by WebRTC DataChannels is its resistance to SYN-flooding denial-of-service attacks through a four-way association handshake using signed state cookies, compared to TCP's three-way handshake:",
        styles['Body']
    ))
    flowables.append(Paragraph(
        "<b>TCP 3-Way Handshake:</b> Client sends SYN; Server allocates Transmission Control Block (TCB) in memory and replies with SYN-ACK; Client replies with ACK. If an attacker floods millions of spoofed SYN packets, the server's TCB memory queue is rapidly exhausted, crashing the network stack.",
        styles['Body']
    ))
    flowables.append(Paragraph(
        "<b>SCTP 4-Way Association Handshake:</b><br/>"
        "1. Endpoint A dispatches an <code>INIT</code> chunk with its initial tag, advertised receive window (a_rwnd), and number of outbound/inbound streams.<br/>"
        "2. Endpoint B does <i>not</i> allocate memory. Instead, it packages its local state parameters and a cryptographic Message Authentication Code (MAC) into a <code>State Cookie</code> parameter and responds with an <code>INIT ACK</code> chunk.<br/>"
        "3. Endpoint A receives the cookie and echoes it back in a <code>COOKIE ECHO</code> chunk.<br/>"
        "4. Endpoint B verifies the MAC on the returned cookie. Only after valid cryptographic verification does Endpoint B allocate state memory, responding with a <code>COOKIE ACK</code>.",
        styles['CodeBlock']
    ))
    flowables.append(Paragraph(
        "This architectural property guarantees that WebRTC SCTP associations are immune to blind state-exhaustion denial of service attacks, providing high transport security on open campus wireless networks.",
        styles['Body']
    ))

    flowables.append(Spacer(1, 10))
    flowables.append(Paragraph("2.5 NAT Traversal Dynamics: STUN, TURN, and ICE (RFC 8445)", styles['SecTitle']))
    flowables.append(Paragraph(
        "The primary impediment to direct peer-to-peer communication across modern computer networks is the widespread deployment of Network Address Translation (NAT) gateways (RFC 3022) and stateful packet-filtering firewalls. NAT devices multiplex multiple private IPv4 addresses (e.g., <code>192.168.x.x</code> or <code>10.x.x.x</code>) onto a single public WAN IP address by dynamically mapping transport layer port numbers.",
        styles['Body']
    ))
    flowables.append(Paragraph(
        "To establish direct communication between endpoints residing behind distinct NATs, WebRTC implements the Interactive Connectivity Establishment (ICE) protocol (RFC 8445), which coordinates Session Traversal Utilities for NAT (STUN, RFC 8489) and Traversal Using Relays around NAT (TURN, RFC 8656):",
        styles['Body']
    ))
    flowables.append(Paragraph("<b>1. Host Candidates:</b> IP addresses bound directly to the client's local physical or virtual network interface cards (e.g., <code>192.168.1.15:54321</code>). In local LAN transfers, host candidates connect directly with sub-millisecond round-trip times.", styles['Bullet']))
    flowables.append(Paragraph("<b>2. Server Reflexive Candidates (srflx):</b> The public IP and mapped port allocated by the outermost NAT device, discovered by dispatching lightweight UDP binding requests to an external STUN server (such as Google's public STUN infrastructure: <code>stun:stun.l.google.com:19302</code>).", styles['Bullet']))
    flowables.append(Paragraph("<b>3. Relay Candidates (relay):</b> Traversal addresses hosted on external TURN servers that relay packet data when symmetric NAT configurations prevent direct hole-punching.", styles['Bullet']))
    flowables.append(Paragraph(
        "The ICE candidate pairing process assigns a deterministic 64-bit priority to each candidate pair based on the formula:",
        styles['Body']
    ))
    flowables.append(Paragraph(
        "<b>Equation 2.1 (ICE Candidate Priority):</b><br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<b>Priority = (2<sup>24</sup>) &times; (TypePreference) + (2<sup>8</sup>) &times; (LocalPreference) + (256 - ComponentID)</b>",
        styles['CodeBlock']
    ))
    flowables.append(Paragraph(
        "Because host candidates carry the highest TypePreference value (typically 126 vs. 100 for srflx and 0 for relay), WebRTC deterministically selects the direct LAN route whenever both endpoints share the same local subnet, achieving direct gigabit wire-speed transfer.",
        styles['Body']
    ))

    flowables.append(Spacer(1, 10))
    flowables.append(Paragraph("2.6 Transport Layer Tradeoffs: TCP vs. UDP vs. SCTP", styles['SecTitle']))
    flowables.append(Paragraph(
        "Selecting an appropriate transport-layer substrate is critical for bulk file streaming. The comparative mechanics of the three candidate protocols are analyzed below:",
        styles['Body']
    ))
    flowables.append(Paragraph(
        "<b>Transmission Control Protocol (TCP):</b> TCP provides byte-stream reliability and strict in-order delivery. However, TCP is plagued by <i>Head-of-Line Blocking (HOLB)</i>: if a single packet is dropped in transit, the operating system kernel holds all subsequent correctly received bytes in the socket buffer until the missing segment is retransmitted and acknowledged. In wireless Wi-Fi environments characterized by transient packet drops, TCP throughput collapses dramatically due to window halving.",
        styles['Body']
    ))
    flowables.append(Paragraph(
        "<b>User Datagram Protocol (UDP):</b> UDP provides lightweight, connectionless datagram dispatch with minimal header overhead (8 bytes vs. TCP's 20-60 bytes) and zero retransmission latency. However, raw UDP lacks flow control, congestion avoidance, and packet ordering. Transmitting a 2 GB file over raw UDP would result in massive packet loss and complete payload corruption.",
        styles['Body']
    ))
    flowables.append(Paragraph(
        "<b>Stream Control Transmission Protocol (SCTP, RFC 4960):</b> SCTP combines the message-oriented framing of UDP with the reliability, selective acknowledgments (SACK), and congestion control of TCP. Most importantly, SCTP supports <b>multi-streaming</b>, where data is segregated into independent logical streams within a single association. Packet loss on one stream does not stall data delivery on adjacent streams, virtually eliminating Head-of-Line Blocking.",
        styles['Body']
    ))

    flowables.append(Spacer(1, 10))
    flowables.append(Paragraph("2.7 Cryptographic Foundations: ECDH NIST P-256 &amp; AES-GCM-256", styles['SecTitle']))
    flowables.append(Paragraph(
        "While WebRTC enforces transport-layer DTLS encryption between peer endpoints, relying solely on transport encryption leaves a critical security gap: any compromised relay or man-in-the-middle vector could potentially intercept raw frames. To provide absolute <b>zero-knowledge security</b>, PeerVault AI layers an application-tier cryptographic envelope on top of the DataChannel.",
        styles['Body']
    ))
    flowables.append(Paragraph(
        "Peers execute an Elliptic Curve Diffie-Hellman (ECDH) key exchange over the NIST P-256 elliptic curve (defined by the equation y^2 = x^3 - 3x + b mod p). Each client generates an ephemeral keypair inside the browser's hardware-accelerated Web Cryptography API sandbox. The derived 256-bit shared master secret is passed into an HMAC-based Extract-and-Expand Key Derivation Function (HKDF) to yield symmetric encryption keys.",
        styles['Body']
    ))
    flowables.append(Paragraph(
        "Payload chunks are encrypted using AES-GCM-256 (Galois/Counter Mode). AES-GCM is an Authenticated Encryption with Associated Data (AEAD) cipher that simultaneously provides confidentiality and cryptographic integrity verification via an appended 128-bit authentication tag. Every 64KB chunk uses a freshly generated, cryptographically random 96-bit initialization vector (IV), mathematically preventing keystream reuse and replay attacks.",
        styles['Body']
    ))

    flowables.append(Spacer(1, 10))
    flowables.append(Paragraph("2.8 State-of-the-Art Comparative Analysis Matrix", styles['SecTitle']))
    flowables.append(Paragraph(
        "Table 2.1 presents a comprehensive structural comparison between PeerVault AI and existing data transfer paradigms across architectural, cryptographic, and performance dimensions.",
        styles['Body']
    ))

    comp_headers = [Paragraph("<b>Feature / Dimension</b>", styles['TableHead']),
                    Paragraph("<b>Cloud Storage<br/>(Drive / Dropbox)</b>", styles['TableHead']),
                    Paragraph("<b>BitTorrent<br/>P2P Clients</b>", styles['TableHead']),
                    Paragraph("<b>Local Airdrop /<br/>Nearby Share</b>", styles['TableHead']),
                    Paragraph("<b>PeerVault AI<br/>(Our Architecture)</b>", styles['TableHead'])]

    comp_matrix = [
        comp_headers,
        [Paragraph("Client Software Installation", styles['TableCellBold']), Paragraph("Not required (Web) / Apps", styles['TableCell']), Paragraph("Mandatory native client", styles['TableCell']), Paragraph("OS-locked (Apple/Android)", styles['TableCell']), Paragraph("<b>Zero Installation (WebRTC)</b>", styles['TableCell'])],
        [Paragraph("Data Transmission Path", styles['TableCellBold']), Paragraph("Double WAN Relay", styles['TableCell']), Paragraph("Distributed Swarm", styles['TableCell']), Paragraph("Proprietary Ad-Hoc Wi-Fi", styles['TableCell']), Paragraph("<b>Direct Subnet P2P LAN</b>", styles['TableCell'])],
        [Paragraph("Server Storage Footprint", styles['TableCellBold']), Paragraph("Persistent cloud disk", styles['TableCell']), Paragraph("None (Swarm cache)", styles['TableCell']), Paragraph("None", styles['TableCell']), Paragraph("<b>Zero Server Storage</b>", styles['TableCell'])],
        [Paragraph("Cryptographic Guarantee", styles['TableCellBold']), Paragraph("Server-side decryption", styles['TableCell']), Paragraph("Plaintext (SHA-1 hash)", styles['TableCell']), Paragraph("Proprietary TLS handshake", styles['TableCell']), Paragraph("<b>Zero-Knowledge ECDH+GCM</b>", styles['TableCell'])],
        [Paragraph("File Size Quotas / Limits", styles['TableCellBold']), Paragraph("Strict (2GB - 15GB)", styles['TableCell']), Paragraph("Unlimited (Disk bound)", styles['TableCell']), Paragraph("OS buffer bound", styles['TableCell']), Paragraph("<b>Unlimited (4MB Flow Ctrled)</b>", styles['TableCell'])],
        [Paragraph("Local Document Intelligence", styles['TableCellBold']), Paragraph("Cloud AI (Telemetry)", styles['TableCell']), Paragraph("None", styles['TableCell']), Paragraph("None", styles['TableCell']), Paragraph("<b>Client-Side TF-IDF NLP</b>", styles['TableCell'])],
        [Paragraph("Cross-Platform Interoperability", styles['TableCellBold']), Paragraph("Universal (Web)", styles['TableCell']), Paragraph("Desktop / Mobile apps", styles['TableCell']), Paragraph("Incompatible ecosystems", styles['TableCell']), Paragraph("<b>Universal Browser Native</b>", styles['TableCell'])],
    ]
    t_comp = Table(comp_matrix, colWidths=[110, 95, 95, 95, 105])
    t_comp.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#f1f5f9")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('BACKGROUND', (4,1), (4,-1), colors.HexColor("#fef2f2")),
    ]))
    flowables.append(t_comp)

    flowables.append(PageBreak())
    return flowables
