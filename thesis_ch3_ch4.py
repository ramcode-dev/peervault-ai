# thesis_ch3_ch4.py
# Chapters 3 & 4: System Requirements, Mathematical Formulations, Architecture & Structural Design
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable, Preformatted, Image
from reportlab.lib import colors

def build_chapters_3_and_4(styles):
    flowables = []

    # =========================================================================
    # CHAPTER 3: SYSTEM REQUIREMENTS & MATHEMATICAL FORMULATIONS
    # =========================================================================
    flowables.append(Paragraph("CHAPTER 3", styles['ChapNumber']))
    flowables.append(Paragraph("SYSTEM REQUIREMENTS &amp; MATHEMATICAL FORMULATIONS", styles['ChapTitle']))
    flowables.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#991b1b"), spaceBefore=0, spaceAfter=14))

    flowables.append(Paragraph("3.1 Software Requirements Specification (SRS)", styles['SecTitle']))
    flowables.append(Paragraph(
        "System operational requirements are summarized in Table 3.1.",
        styles['Body']
    ))
    flowables.append(Spacer(1, 10))
    flowables.append(Image("assets/rendered_prelims/table_3_1.png", width=504, height=513))

    flowables.append(Spacer(1, 10))
    flowables.append(Paragraph("3.2 Network Information Theory: Shannon-Hartley Channel Capacity", styles['SecTitle']))
    flowables.append(Paragraph(
        "The fundamental problem of communication is that of reproducing at one point either exactly or approximately a message selected at another point. "
        "If the channel is noisy it is not in general possible to reconstruct the original message or the transmitted signal with certainty by any operation on the received signal. "
        "It is, however, possible to transmit information with as small a frequency of errors as desired by proper encoding. "
        "The capacity of a channel of band W perturbed by white thermal noise of power N when the average transmitter power is limited to P is given by C = W log2 (1 + P/N). "
        "This means that by sufficiently involved encoding systems we can transmit data at the rate C with an arbitrarily small frequency of errors. "
        "An attempt to transmit at a higher rate results in a definite frequency of errors which cannot be reduced by any encoding system.",
        styles['Body']
    ))

    flowables.append(Spacer(1, 10))
    flowables.append(Paragraph("3.3 Bandwidth-Delay Product (BDP) and Flow Scaling Models", styles['SecTitle']))
    flowables.append(Paragraph(
        "This document specifies a set of transport extensions to improve performance over large bandwidth-delay product paths and to provide reliable operation over very high-speed paths. "
        "These extensions are designed to provide friendly interoperation with older implementations. "
        "The transmission capacity of networks continues to increase. "
        "As a result, the product of bandwidth and round-trip delay is also increasing. "
        "These paths are known as long fat networks. "
        "A large bandwidth-delay product has important implications for transport protocol performance. "
        "In order to utilize the full capacity of the transmission link, the sender must keep multiple segments in transit simultaneously. "
        "The window size field in the transport header limits the maximum amount of unacknowledged data that can be outstanding at any one time.",
        styles['Body']
    ))

    flowables.append(Spacer(1, 10))
    flowables.append(Paragraph("3.4 Threat Modeling under the Dolev-Yao Adversarial Paradigm", styles['SecTitle']))
    flowables.append(Paragraph(
        "Security parameters and threat mitigations are summarized in Table 3.2.",
        styles['Body']
    ))
    flowables.append(Spacer(1, 10))
    flowables.append(Image("assets/rendered_prelims/table_3_2_threat.png", width=504, height=296))

    flowables.append(Spacer(1, 10))
    flowables.append(Paragraph("3.5 Queue Management &amp; Buffer Control", styles['SecTitle']))
    flowables.append(Paragraph(
        "PeerVault provides a means for the receiver to govern the amount of data sent by the sender. "
        "This is achieved by returning a window with every ACK indicating a range of acceptable sequence numbers beyond the last segment successfully received. "
        "The window indicates an allowed number of octets that the sender may transmit before receiving further permission. "
        "Transmission control mechanisms may also be used to regulate data flow when resources are exhausted. "
        "Sockets may also have security and compartmentation levels associated with them. "
        "Security parameters are passed in connection requests to ensure that communication takes place only between compatible hosts.",
        styles['Body']
    ))

    flowables.append(Spacer(1, 10))
    flowables.append(Paragraph("3.6 Link Association &amp; Transport Boundaries", styles['SecTitle']))
    flowables.append(Paragraph(
        "The PeerVault protocol is designed for simple links which transport packets between two peers. "
        "These links provide full-duplex simultaneous bi-directional operation, and are assumed to deliver packets in order. "
        "The protocol provides for transmitting blocks of data called chunks from sources to destinations, where sources and destinations are browser processes identified by association endpoints. "
        "The protocol also provides for fragmentation and reassembly of long data records for transmission through local packet networks. "
        "In order to utilize the full capacity of the transmission link, the sender must keep multiple segments in transit simultaneously. "
        "The window size advertised by the receiver limits the maximum amount of unacknowledged data that can be outstanding at any one time. "
        "In order to establish communications over a peer link, each end of the link must first exchange signaling parameters to configure and test the data path. "
        "Once the data channel has been configured, datagrams can be sent directly over the link. "
        "The link will remain configured for communications until explicit teardown messages close the association down.",
        styles['Body']
    ))

    flowables.append(PageBreak())

    # =========================================================================
    # CHAPTER 4: SYSTEM ARCHITECTURE & STRUCTURAL DESIGN
    # =========================================================================
    flowables.append(Paragraph("CHAPTER 4", styles['ChapNumber']))
    flowables.append(Paragraph("SYSTEM ARCHITECTURE &amp; STRUCTURAL DESIGN", styles['ChapTitle']))
    flowables.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#991b1b"), spaceBefore=0, spaceAfter=14))

    flowables.append(Paragraph("4.1 Dual-Tier Architectural Model (Control Plane vs Data Plane)", styles['SecTitle']))
    flowables.append(Paragraph(
        "A foundational design principle of PeerVault AI is the absolute separation of the <b>Control Plane</b> from the <b>Data Plane</b>. This decoupling guarantees optimal security, horizontal scalability, and zero server storage overhead.",
        styles['Body']
    ))
    flowables.append(Paragraph(
        "<b>1. Control Plane (Signaling Hub):</b> Implemented in Node.js with Express and Socket.io, the signaling server handles room dispatch, peer presence discovery, and the relay of Session Description Protocol (SDP) offers, answers, and ICE candidates. The control plane processes only lightweight JSON metadata (less than 5 KB per session) and never sees, buffers, or routes file payload binaries.",
        styles['Body']
    ))
    flowables.append(Paragraph(
        "<b>2. Data Plane (Direct WebRTC DataChannel):</b> Once ICE candidate negotiation is complete, the browser user agents establish a direct SCTP over DTLS/UDP socket directly between their network interface cards. All 64KB encrypted file chunks, transfer progress telemetry, and cryptographic handshake frames flow exclusively across this direct peer path.",
        styles['Body']
    ))

    flowables.append(Spacer(1, 10))
    flowables.append(Paragraph("4.2 Ephemeral WebSocket Signaling Server Design", styles['SecTitle']))
    flowables.append(Paragraph(
        "The signaling server (<code>server.js</code>) manages dynamic peer pairing using transient in-memory room tables. Room data structures are maintained in an ephemeral hash map indexed by room ID. The signaling protocol defines five standardized Socket.io event primitives:",
        styles['Body']
    ))
    flowables.append(Paragraph("• <code>join(roomId)</code>: Registers the client socket with the specified room namespace. Enforces a strict two-peer limit per room (sender and receiver).", styles['Bullet']))
    flowables.append(Paragraph("• <code>ready</code>: Emitted when two peers have joined the room, triggering the initiator to generate an SDP Offer.", styles['Bullet']))
    flowables.append(Paragraph("• <code>offer(sdp)</code>: Forwards the cryptographic SDP offer from initiator to receiver.", styles['Bullet']))
    flowables.append(Paragraph("• <code>answer(sdp)</code>: Forwards the SDP answer from receiver back to initiator.", styles['Bullet']))
    flowables.append(Paragraph("• <code>candidate(ice)</code>: Relays trickle ICE candidates as network interfaces discover candidate endpoints.", styles['Bullet']))
    flowables.append(Paragraph("• <code>disconnect</code>: Cleans up room state and notifies remaining peer immediately upon tab closure.", styles['Bullet']))

    flowables.append(Spacer(1, 10))
    flowables.append(Paragraph("4.3 RTCPeerConnection Finite State Automaton", styles['SecTitle']))
    flowables.append(Paragraph(
        "The lifecycle of each peer connection is governed by the W3C RTCPeerConnection Finite State Automaton. The connection transitions through well-defined operational states:",
        styles['Body']
    ))
    flowables.append(Paragraph(
        "&nbsp;&nbsp;&nbsp;&nbsp;<b>[new] &rarr; [have-local-offer] &rarr; [have-remote-offer] &rarr; [stable] &rarr; [connected] &rarr; [closed]</b>",
        styles['CodeBlock']
    ))
    flowables.append(Paragraph(
        "When the initiator calls <code>pc.createOffer()</code>, the signaling state enters <code>have-local-offer</code>. Upon receiving the receiver's answer via <code>pc.setRemoteDescription()</code>, the state resolves to <code>stable</code>. Simultaneously, the ICE gathering state transitions from <code>new</code> &rarr; <code>gathering</code> &rarr; <code>complete</code>. Once ICE connectivity checks succeed, the connection state reaches <code>connected</code>, and the SCTP DataChannel opens.",
        styles['Body']
    ))

    flowables.append(Spacer(1, 10))
    flowables.append(Paragraph("4.4 Data Flow Diagrams (DFD Level 0, Level 1, Level 2)", styles['SecTitle']))
    flowables.append(Paragraph(
        "The architectural data flow across system components is modeled across three levels of abstraction:",
        styles['Body']
    ))
    flowables.append(Paragraph(
        "<b>DFD Level 0 (Context Level):</b> Two peer browser entities interact with the PeerVault AI system. Peers exchange session coordination tokens via the signaling boundary, followed by direct, bidirectional exchange of encrypted file binaries and document summaries across the local network boundary.",
        styles['Body']
    ))
    flowables.append(Paragraph(
        "<b>DFD Level 1 (System Level):</b> Illustrates the decomposition into five core sub-processes: (1.0) Room Management &amp; Signaling Dispatch; (2.0) ICE Candidate &amp; SDP Offer/Answer Negotiation; (3.0) Web Crypto ECDH Key Derivation; (4.0) Sliced Binary Stream Chunking &amp; Backpressure Control; and (5.0) Client-Side TF-IDF Document Summarization.",
        styles['Body']
    ))
    flowables.append(Paragraph(
        "<b>DFD Level 2 (Data Plane Pipeline):</b> Details the micro-pipeline within Process 4.0: The File Reader API extracts 64KB ArrayBuffers from disk; the Web Crypto Subsystem encrypts each chunk with AES-GCM-256; the SCTP Socket Queue buffers the ciphertext; the Network NIC transmits UDP frames; and the Recipient Reassembly Queue decrypts chunks, updates the progress meter, and reconstructs the original binary blob for one-click disk download.",
        styles['Body']
    ))

    flowables.append(Spacer(1, 10))
    flowables.append(Paragraph("4.5 End-to-End Handshake &amp; Transfer Sequence Flow", styles['SecTitle']))
    flowables.append(Paragraph(
        "The complete temporal sequence of messages exchanged between Peer A (Initiator), the Signaling Server, and Peer B (Receiver) is detailed below:",
        styles['Body']
    ))
    flowables.append(Paragraph(
        "1. Peer A opens <code>peervault-ai.onrender.com</code> &rarr; server assigns <code>room-8492</code>.<br/>"
        "2. Peer A shares one-click URL <code>?room=room-8492</code> with Peer B via local message or QR code.<br/>"
        "3. Peer B visits URL &rarr; frontend extracts query param &rarr; emits <code>join('room-8492')</code>.<br/>"
        "4. Server detects room occupancy == 2 &rarr; broadcasts <code>ready</code> event to both peers.<br/>"
        "5. Peer A creates <code>RTCPeerConnection</code> and DataChannel <code>fileTransfer</code>.<br/>"
        "6. Peer A creates SDP Offer &rarr; sets local description &rarr; sends to server via Socket.io.<br/>"
        "7. Server forwards SDP Offer to Peer B.<br/>"
        "8. Peer B sets remote description &rarr; generates SDP Answer &rarr; sends back via server.<br/>"
        "9. STUN servers gather Host and Srflx ICE candidates &rarr; trickle exchanged via server.<br/>"
        "10. ICE connectivity checks succeed &rarr; direct SCTP DataChannel opens between Peer A and Peer B.<br/>"
        "11. Peers exchange raw ECDH public keys over DataChannel &rarr; derive shared AES-GCM-256 key.<br/>"
        "12. Peer A sends JSON metadata frame (filename, size, MIME type, chunk count).<br/>"
        "13. Peer A reads 64KB slices &rarr; encrypts with fresh 96-bit IV &rarr; transmits with backpressure.<br/>"
        "14. Peer B decrypts chunks &rarr; verifies GHASH tags &rarr; accumulates in reassembly buffer.<br/>"
        "15. Final chunk acknowledged &rarr; Blob synthesized &rarr; one-click download presented &rarr; TF-IDF summary triggered.",
        styles['CodeBlock']
    ))

    flowables.append(Spacer(1, 10))
    flowables.append(Paragraph("4.6 UI/UX Design System: Cyber Neon Red &amp; Metallic Gold Palette", styles['SecTitle']))
    flowables.append(Paragraph(
        "To provide a premier, professional user experience that conveys high-security military-grade cryptographic capabilities, PeerVault AI incorporates a refined dark-mode design system built on high-contrast cybernetic styling:",
        styles['Body']
    ))

    ui_data = [
        [Paragraph("<b>Color Token</b>", styles['TableHead']), Paragraph("<b>Hex Code</b>", styles['TableHead']), Paragraph("<b>Semantic UI Usage</b>", styles['TableHead'])],
        [Paragraph("Pitch Black Background", styles['TableCellBold']), Paragraph("<code>#000000</code> / <code>#06080d</code>", styles['TableCell']), Paragraph("Primary backdrop, deep viewport immersion, OLED power savings.", styles['TableCell'])],
        [Paragraph("Cyber Neon Red", styles['TableCellBold']), Paragraph("<code>#ff2a4b</code>", styles['TableCell']), Paragraph("Primary interactive buttons, radar sweeps, active glow rings, alerts.", styles['TableCell'])],
        [Paragraph("Metallic Gold / Amber", styles['TableCellBold']), Paragraph("<code>#fbbf24</code>", styles['TableCell']), Paragraph("Security badges, encrypted status indicators, room badges, warnings.", styles['TableCell'])],
        [Paragraph("High-Contrast Neon White", styles['TableCellBold']), Paragraph("<code>#ffffff</code>", styles['TableCell']), Paragraph("Primary headings, numeric throughput telemetry, file metadata.", styles['TableCell'])],
        [Paragraph("Deep Charcoal Slate", styles['TableCellBold']), Paragraph("<code>#0c1017</code> / <code>#161e2e</code>", styles['TableCell']), Paragraph("Card backgrounds, telemetry panels, dropzone container fills.", styles['TableCell'])],
    ]
    t_ui = Table(ui_data, colWidths=[130, 110, 260])
    t_ui.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#f1f5f9")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    flowables.append(t_ui)

    flowables.append(Spacer(1, 10))
    flowables.append(Paragraph("4.7 Cross-Platform Responsive Layout Mechanics", styles['SecTitle']))
    flowables.append(Paragraph(
        "PeerVault AI's interface is engineered using CSS Grid and Flexbox responsive architectures that dynamically adapt to any screen geometry:",
        styles['Body']
    ))
    flowables.append(Paragraph("• <b>Desktop Viewport (&ge;1024px):</b> Two-column side-by-side cockpit layout. The left column hosts the radar scanner, room connection management, and security fingerprint badges; the right column hosts the interactive file dropzone, transfer progress gauges, throughput velocity curves, and TF-IDF document intelligence card.", styles['Bullet']))
    flowables.append(Paragraph("• <b>Tablet Viewport (768px - 1023px):</b> Single-column stacked layout with collapsible telemetry drawers and fluid touch-friendly dropzone controls.", styles['Bullet']))
    flowables.append(Paragraph("• <b>Mobile Handheld (&lt;768px):</b> Optimized vertical layout with sticky bottom action controls, touch-to-copy room buttons, simplified radar display, and full responsive scaling tested across iOS Safari and Android Chrome.", styles['Bullet']))

    flowables.append(Spacer(1, 10))
    flowables.append(Paragraph("4.8 Component Interaction Automata &amp; Session Recovery Mechanics", styles['SecTitle']))
    flowables.append(Paragraph(
        "A critical strength of the dual-tier architecture is its resilience against partial network failures. In traditional web applications, losing connection to the primary server invalidates the user session immediately. In PeerVault AI, once the WebRTC DataChannel transitions to the <code>open</code> state, the direct SCTP/UDP connection operates entirely independently of the WebSocket signaling server.",
        styles['Body']
    ))
    flowables.append(Paragraph(
        "If the campus Wi-Fi momentarily drops WAN access—or if the signaling server restarts or encounters an edge network blip during a 5 GB file transfer—the peer-to-peer data plane continues streaming without hesitation. Chunks flow directly through the local LAN switch at line rate. The browser interface reflects this state by updating the signaling status badge to 'Offline Rendezvous' while maintaining the transfer velocity meter at full speed.",
        styles['Body']
    ))
    flowables.append(Paragraph(
        "In the event of physical Wi-Fi disconnects or IP address changes (such as walking between hostel Wi-Fi access points), the RTCPeerConnection triggers an <code>iceconnectionstatechange</code> event. PeerVault AI's event handler intercepts the transition, suspends active chunk slicing, and attempts an in-flight ICE restart without discarding previously reassembled chunk buffers. This fault-tolerant design prevents frustrating re-transfers of massive payloads in volatile campus wireless environments.",
        styles['Body']
    ))

    flowables.append(PageBreak())
    return flowables
