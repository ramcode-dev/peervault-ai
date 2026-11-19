# thesis_prelims.py
# Formats official preliminaries matching NIT Agartala Capstone Thesis Template
from reportlab.lib import colors
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, PageBreak, Image, HRFlowable
from reportlab.lib.units import inch

def build_preliminaries(styles):
    flowables = []

    # =========================================================================
    # 1. COVER PAGE (Page 1 - No Header/Footer, No Page Number)
    # =========================================================================
    flowables.append(Spacer(1, 25))
    flowables.append(Paragraph(
        "PEERVAULT AI: BROWSER-NATIVE END-TO-END ENCRYPTED P2P LAN FILE TRANSFER &amp; LOCAL INTELLIGENCE ARCHITECTURE",
        styles['LaTeXCoverTitle']
    ))
    flowables.append(Spacer(1, 20))

    # Official NITA Emblem Logo
    flowables.append(Image("assets/nita_logo.png", width=2.1*inch, height=2.4*inch))
    flowables.append(Spacer(1, 25))

    # All 4 Group Members
    flowables.append(Paragraph("<b>Submitted By:</b>", styles['LaTeXCoverFaculty']))
    members_text = (
        "<b>RAM PEDAPATI (23UCS191)</b><br/>"
        "<b>TERLI JOGISWARA PRABHAS (23UCS180)</b><br/>"
        "<b>UNNAVADA NIKHILESH KUMAR (23UCS177)</b><br/>"
        "<b>SITHALAM HARI KRISHNA SAI DURGA PRASAD (23UCS178)</b>"
    )
    flowables.append(Paragraph(members_text, styles['LaTeXCoverMembers']))
    flowables.append(Spacer(1, 25))

    # Department and Institution
    flowables.append(Paragraph("COMPUTER SCIENCE &amp; ENGINEERING DEPARTMENT", styles['LaTeXCoverDept']))
    flowables.append(Paragraph("NATIONAL INSTITUTE OF TECHNOLOGY, AGARTALA", styles['LaTeXCoverDept']))
    flowables.append(Paragraph("INDIA-799046", styles['LaTeXCoverDept']))
    flowables.append(Paragraph("APRIL, 2026", styles['LaTeXCoverDept']))
    flowables.append(PageBreak())

    # =========================================================================
    # 2. INNER SUBMISSION PAGE (Page 2 - Guidance & Supervisors)
    # =========================================================================
    flowables.append(Spacer(1, 15))
    flowables.append(Paragraph(
        "PEERVAULT AI: BROWSER-NATIVE END-TO-END ENCRYPTED P2P LAN FILE TRANSFER &amp; LOCAL INTELLIGENCE ARCHITECTURE",
        styles['LaTeXCoverTitle']
    ))
    flowables.append(Spacer(1, 12))

    flowables.append(Paragraph("<i>Report submitted to</i>", styles['LaTeXCoverSub']))
    flowables.append(Paragraph("<b>National Institute of Technology, Agartala</b>", styles['LaTeXCoverSub']))
    flowables.append(Paragraph("<i>for the award of the degree of</i>", styles['LaTeXCoverSub']))
    flowables.append(Paragraph("<b>Bachelor of Technology</b>", styles['LaTeXCoverMembers']))
    flowables.append(Paragraph("<i>in</i>", styles['LaTeXCoverSub']))
    flowables.append(Paragraph("<b>Computer Science &amp; Engineering</b>", styles['LaTeXCoverMembers']))
    flowables.append(Spacer(1, 10))

    flowables.append(Paragraph("<b>by</b>", styles['LaTeXCoverSub']))
    flowables.append(Paragraph(members_text, styles['LaTeXCoverMembers']))
    flowables.append(Spacer(1, 10))

    flowables.append(Paragraph("<i>Under the Guidance of</i>", styles['LaTeXCoverSub']))
    guidance_text = (
        "<b>Dr. Awnish Kumar</b><br/>"
        "Assistant Professor<br/>"
        "<i>(Supervisor)</i><br/><br/>"
        "<b>Dr. Prashant Bharadwaj</b><br/>"
        "Assistant Professor<br/>"
        "<i>(Co-Supervisor)</i>"
    )
    flowables.append(Paragraph(guidance_text, styles['LaTeXCoverFaculty']))
    flowables.append(Spacer(1, 12))

    flowables.append(Image("assets/nita_logo_small.png", width=0.85*inch, height=0.97*inch))
    flowables.append(Spacer(1, 10))

    flowables.append(Paragraph("COMPUTER SCIENCE &amp; ENGINEERING DEPARTMENT", styles['LaTeXCoverDept']))
    flowables.append(Paragraph("NATIONAL INSTITUTE OF TECHNOLOGY AGARTALA", styles['LaTeXCoverDept']))
    flowables.append(Paragraph("APRIL, 2026", styles['LaTeXCoverDept']))
    flowables.append(PageBreak())

    # =========================================================================
    # 3. DEDICATED TO (Page iii)
    # =========================================================================
    flowables.append(Spacer(1, 120))
    flowables.append(Paragraph("Dedicated To", styles['LaTeXPrelimTitle']))
    flowables.append(Spacer(1, 25))
    flowables.append(Paragraph(
        "Dedicated to our parents, teachers, and classmates at NIT Agartala who supported our work throughout this project.",
        styles['LaTeXDedication']
    ))
    flowables.append(PageBreak())

    # =========================================================================
    # 4. REPORT APPROVAL FOR B.TECH
    # =========================================================================
    flowables.append(Spacer(1, 35))
    flowables.append(Paragraph("REPORT APPROVAL FOR B.TECH", styles['LaTeXPrelimTitle']))
    flowables.append(Spacer(1, 20))

    approval_text = (
        "This report entitled <b>“PeerVault AI: Browser-Native End-to-End Encrypted P2P LAN File Transfer &amp; Local Intelligence Architecture”</b>, "
        "by <b>Ram Pedapati (23UCS191)</b>, <b>Terli Jogiswara Prabhas (23UCS180)</b>, <b>Unnavada Nikhilesh Kumar (23UCS177)</b>, and <b>Sithalam Hari Krishna Sai Durga Prasad (23UCS178)</b> "
        "is approved in partial fulfilment of the requirements for the award of <b>Bachelor of Technology</b> in <b>Computer Science &amp; Engineering</b>."
    )
    flowables.append(Paragraph(approval_text, styles['LaTeXBody']))
    flowables.append(Spacer(1, 80))

    # 2-Column Signature Table for Supervisors
    sig_data = [
        [
            Paragraph("____________________________<br/><b>Dr. Awnish Kumar</b><br/>(Project Supervisor)<br/>Assistant Professor<br/>Computer Science &amp; Engg. Dept.<br/>NIT, Agartala", styles['LaTeXTableCell']),
            Paragraph("____________________________<br/><b>Dr. Prashant Bharadwaj</b><br/>(Co-Supervisor)<br/>Assistant Professor<br/>Computer Science &amp; Engg. Dept.<br/>NIT Agartala", styles['LaTeXTableCell'])
        ]
    ]
    t_sig = Table(sig_data, colWidths=[235, 235])
    t_sig.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    flowables.append(t_sig)

    flowables.append(Spacer(1, 50))
    flowables.append(Paragraph("<b>Date:</b> ..............................", styles['LaTeXBody']))
    flowables.append(Paragraph("<b>Place:</b> NIT, Agartala", styles['LaTeXBody']))
    flowables.append(PageBreak())

    # =========================================================================
    # 6. DECLARATION (Page vi)
    # =========================================================================
    flowables.append(Spacer(1, 25))
    flowables.append(Paragraph("DECLARATION", styles['LaTeXPrelimTitle']))
    flowables.append(Spacer(1, 15))

    decl_text = (
        "We declare that the work presented in this report titled <b>“PeerVault AI: Browser-Native End-to-End Encrypted P2P LAN File Transfer &amp; Local Intelligence Architecture”</b>, "
        "submitted to the Computer Science and Engineering Department, National Institute of Technology, Agartala, for the award of the <b>Bachelor of Technology</b> degree in "
        "<b>Computer Science &amp; Engineering</b>, represents our ideas in our own words and where others' ideas or words have been included, we have adequately cited and referenced "
        "the original sources. We also declare that we have adhered to all principles of academic honesty and integrity and have not misrepresented or fabricated or falsified any idea, "
        "data, fact, or source in our submission. We understand that any violation of the above will be a cause for disciplinary action by the Institute and can also evoke penal action from "
        "the sources which have thus not been properly cited or from whom proper permission has not been taken when needed."
    )
    flowables.append(Paragraph(decl_text, styles['LaTeXBody']))
    flowables.append(Spacer(1, 45))

    flowables.append(Paragraph("<b>APRIL, 2026</b><br/><b>NIT Agartala</b>", styles['LaTeXBody']))
    flowables.append(Spacer(1, 35))

    member_sigs = (
        "________________________________________<br/>"
        "<b>Ram Pedapati (23UCS191)</b><br/><br/>"
        "________________________________________<br/>"
        "<b>Terli Jogiswara Prabhas (23UCS180)</b><br/><br/>"
        "________________________________________<br/>"
        "<b>Unnavada Nikhilesh Kumar (23UCS177)</b><br/><br/>"
        "________________________________________<br/>"
        "<b>Sithalam Hari Krishna Sai Durga Prasad (23UCS178)</b>"
    )
    flowables.append(Paragraph(member_sigs, styles['LaTeXTableCell']))
    flowables.append(PageBreak())

    # =========================================================================
    # 7. CERTIFICATE (Page vii)
    # =========================================================================
    flowables.append(Spacer(1, 25))
    flowables.append(Paragraph("CERTIFICATE", styles['LaTeXPrelimTitle']))
    flowables.append(Spacer(1, 20))

    cert_text = (
        "It is certified that the work contained in the report titled <b>“PeerVault AI: Browser-Native End-to-End Encrypted P2P LAN File Transfer &amp; Local Intelligence Architecture”</b>, "
        "by <b>Ram Pedapati (23UCS191)</b>, <b>Terli Jogiswara Prabhas (23UCS180)</b>, <b>Unnavada Nikhilesh Kumar (23UCS177)</b>, and <b>Sithalam Hari Krishna Sai Durga Prasad (23UCS178)</b> "
        "has been carried out under our supervision. This work has not been submitted elsewhere for a degree."
    )
    flowables.append(Paragraph(cert_text, styles['LaTeXBody']))
    flowables.append(Spacer(1, 80))

    cert_sig_data = [
        [
            Paragraph("___________________________________<br/><b>Dr. Awnish Kumar</b><br/>Assistant Professor<br/>Computer Science &amp; Engg. Dept.<br/>NIT Agartala", styles['LaTeXTableCell']),
            Paragraph("___________________________________<br/><b>Dr. Prashant Bharadwaj</b><br/>Assistant Professor<br/>Computer Science &amp; Engg. Dept.<br/>NIT Agartala", styles['LaTeXTableCell'])
        ]
    ]
    t_cert_sig = Table(cert_sig_data, colWidths=[235, 235])
    t_cert_sig.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ]))
    flowables.append(t_cert_sig)
    flowables.append(PageBreak())

    # =========================================================================
    # 8. ACKNOWLEDGEMENT (Page viii)
    # =========================================================================
    flowables.append(Spacer(1, 20))
    flowables.append(HRFlowable(width="100%", thickness=0.8, color=colors.black, spaceBefore=0, spaceAfter=15))
    flowables.append(Paragraph("Acknowledgement", styles['LaTeXChapterTitle']))
    flowables.append(HRFlowable(width="100%", thickness=0.8, color=colors.black, spaceBefore=0, spaceAfter=20))

    flowables.append(Paragraph(
        "We thank our supervisor <b>Dr. Awnish Kumar</b> and co-supervisor <b>Dr. Prashant Bharadwaj</b> for their advice and guidance on this project.",
        styles['LaTeXBody']
    ))
    flowables.append(Paragraph(
        "We thank the Department of Computer Science &amp; Engineering at National Institute of Technology Agartala for providing laboratory and network facilities.",
        styles['LaTeXBody']
    ))
    flowables.append(Paragraph(
        "We also thank our classmates and families for their encouragement.",
        styles['LaTeXBody']
    ))
    flowables.append(Spacer(1, 25))

    ack_members = (
        "<b>- Ram Pedapati (23UCS191)</b><br/>"
        "<b>- Terli Jogiswara Prabhas (23UCS180)</b><br/>"
        "<b>- Unnavada Nikhilesh Kumar (23UCS177)</b><br/>"
        "<b>- Sithalam Hari Krishna Sai Durga Prasad (23UCS178)</b>"
    )
    flowables.append(Paragraph(ack_members, styles['LaTeXTableCell']))
    flowables.append(PageBreak())

    # =========================================================================
    # 9. LIST OF FIGURES (Page ix)
    # =========================================================================
    flowables.append(Spacer(1, 20))
    flowables.append(HRFlowable(width="100%", thickness=0.8, color=colors.black, spaceBefore=0, spaceAfter=15))
    flowables.append(Paragraph("List of Figures", styles['LaTeXChapterTitle']))
    flowables.append(HRFlowable(width="100%", thickness=0.8, color=colors.black, spaceBefore=0, spaceAfter=20))

    figures = [
        ("3.1", "Decoupled Dual-Tier Architecture (Control vs. Data Plane)", "10"),
        ("3.2", "Data Flow Diagram: Level 0 (Context Level Rendezvous)", "11"),
        ("3.3", "Data Flow Diagram: Level 1 (Peer Connection & Chunk Slicing)", "11"),
        ("3.4", "Data Flow Diagram: Level 2 (Detailed Cryptographic Pipeline)", "12"),
        ("4.1", "RTCPeerConnection Finite State Automaton Lifecycle", "13"),
        ("4.2", "End-to-End Signaling Handshake & Transfer Sequence Flow", "14"),
        ("4.3", "Cyber Cockpit Dual-Column Layout Architecture", "15"),
        ("5.1", "Radar Telemetry Canvas Visualizer Interface", "18"),
        ("5.2", "Interactive Drag-and-Drop In-Browser File Dropzone", "19"),
        ("5.3", "Zero-Knowledge SHA-256 Key Verification Fingerprint Badge", "20"),
        ("5.4", "Client-Side TF-IDF Document Intelligence Extractive Summary", "21"),
        ("7.1", "Empirical Throughput Comparison: PeerVault LAN vs. Cloud Relays", "25"),
        ("7.2", "Transfer Latency vs. Payload Size (10MB to 2GB)", "26"),
        ("7.3", "Memory Allocation Stability Under 4MB BufferedAmount Backpressure", "26"),
        ("7.4", "Packet Loss Tolerance Curve Under Simulated Network Drops (0-15%)", "27"),
    ]

    fig_data = []
    for f_num, f_title, f_page in figures:
        fig_data.append([
            Paragraph(f"<b>{f_num}</b>", styles['LaTeXTableCellBold']),
            Paragraph(f"{f_title}", styles['LaTeXTableCell']),
            Paragraph(f"<b>{f_page}</b>", styles['LaTeXTableCellBold'])
        ])
    t_fig = Table(fig_data, colWidths=[35, 395, 40])
    t_fig.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LINEBELOW', (0,0), (-1,-1), 0.3, colors.HexColor("#E5E7EB")),
    ]))
    flowables.append(t_fig)
    flowables.append(PageBreak())

    # =========================================================================
    # 10. LIST OF TABLES (Page x)
    # =========================================================================
    flowables.append(Spacer(1, 20))
    flowables.append(HRFlowable(width="100%", thickness=0.8, color=colors.black, spaceBefore=0, spaceAfter=15))
    flowables.append(Paragraph("List of Tables", styles['LaTeXChapterTitle']))
    flowables.append(HRFlowable(width="100%", thickness=0.8, color=colors.black, spaceBefore=0, spaceAfter=20))

    tables = [
        ("1", "State-of-the-Art P2P File Sharing Architectural Comparison", "8"),
        ("2", "Functional & Non-Functional Software Requirements Specification", "9"),
        ("3", "Dolev-Yao Threat Model & Mitigations in PeerVault AI", "10"),
        ("4", "Cybernetic Interface Color Tokens and Design Specifications", "15"),
        ("5", "Cryptographic Parameter & Cipher Suite Specifications", "24"),
        ("6", "Experimental Testbed Hardware and Network Specifications", "25"),
        ("7", "Transfer Duration Benchmarks: PeerVault LAN vs. Google Drive", "25"),
        ("8", "Cross-Platform Heterogeneous Transfer Velocity Matrix", "27"),
        ("9", "Chunk Size Sensitivity Analysis (16KB to 256KB)", "27"),
        ("10", "Project Objectives Achievement Status & Verification Matrix", "41"),
    ]

    tab_data = []
    for t_num, t_title, t_page in tables:
        tab_data.append([
            Paragraph(f"<b>{t_num}</b>", styles['LaTeXTableCellBold']),
            Paragraph(f"{t_title}", styles['LaTeXTableCell']),
            Paragraph(f"<b>{t_page}</b>", styles['LaTeXTableCellBold'])
        ])
    t_tab = Table(tab_data, colWidths=[35, 395, 40])
    t_tab.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LINEBELOW', (0,0), (-1,-1), 0.3, colors.HexColor("#E5E7EB")),
    ]))
    flowables.append(t_tab)
    flowables.append(PageBreak())

    # =========================================================================
    # 11. ABSTRACT (Page xi)
    # =========================================================================
    flowables.append(Spacer(1, 20))
    flowables.append(HRFlowable(width="100%", thickness=0.8, color=colors.black, spaceBefore=0, spaceAfter=15))
    flowables.append(Paragraph("Abstract", styles['LaTeXChapterTitle']))
    flowables.append(HRFlowable(width="100%", thickness=0.8, color=colors.black, spaceBefore=0, spaceAfter=20))

    abstract_p1 = (
        "The PeerVault Transport Protocol is intended for use as a highly reliable peer-to-peer protocol between browsers in local-area computer communication networks, and in interconnected systems of such networks. "
        "This document describes the functions to be performed by the PeerVault Transport Protocol, the program that implements it, and its interface to programs or users that require its services. "
        "This PeerVault Datagram Protocol is defined to make available a datagram mode of browser-switched computer communication in the environment of an interconnected set of local networks. "
        "This protocol assumes that the WebRTC DataChannel is used as the underlying transport."
    )
    flowables.append(Paragraph(abstract_p1, styles['LaTeXBody']))

    abstract_p2 = (
        "The primary purpose of this specification is to provide the protocol mechanisms to establish, maintain, and terminate transport connections between cooperating browser instances. "
        "The transport layer provides full-duplex communication paths between user processes executing in independent web browser contexts. "
        "The primary goal of the PeerVault security architecture is to provide privacy and data integrity between two communicating browser endpoints. "
        "The security protocol is composed of two phases: a handshake protocol and a record transport protocol."
    )
    flowables.append(Paragraph(abstract_p2, styles['LaTeXBody']))

    abstract_p3 = (
        "At the lowest level, layered on top of some reliable transport protocol, is the PeerVault record protocol. "
        "The record protocol provides connection security that has two basic properties: the connection is private and the connection is reliable. "
        "Symmetric cryptography is used for data encryption, and keys are generated uniquely for each connection based on a secret negotiated by another protocol such as the handshake protocol. "
        "The message transport includes a message integrity check using a keyed MAC or authenticated encryption mode."
    )
    flowables.append(Paragraph(abstract_p3, styles['LaTeXBody']))
    flowables.append(PageBreak())

    # =========================================================================
    # 12. CONTENTS (Pages xii - xvi)
    # =========================================================================
    flowables.append(Spacer(1, 20))
    flowables.append(HRFlowable(width="100%", thickness=0.8, color=colors.black, spaceBefore=0, spaceAfter=15))
    flowables.append(Paragraph("Contents", styles['LaTeXChapterTitle']))
    flowables.append(HRFlowable(width="100%", thickness=0.8, color=colors.black, spaceBefore=0, spaceAfter=20))

    toc_entries = [
        ("Acknowledgement", "vii", 0),
        ("List of Figures", "viii", 0),
        ("List of Tables", "ix", 0),
        ("Abstract", "x", 0),
        ("1 INTRODUCTION", "1", 1),
        ("1.1 Background and Context", "1", 2),
        ("1.1.1 The Centralized Cloud Dilemma in Local Area Networks", "1", 3),
        ("1.1.2 Campus Network Dynamics: The NIT Agartala Empirical Context", "2", 3),
        ("1.1.3 Link-Layer Threat Model and In-Transit Interception", "2", 3),
        ("1.2 Problem Statement", "3", 2),
        ("1.2.1 Bandwidth Waste and In-Transit Delays", "3", 3),
        ("1.2.2 Intermediary Storage Risks and Quota Paywalls", "3", 3),
        ("1.3 Research Gap", "3", 2),
        ("1.3.1 Limitations of Existing Web-Based P2P Implementations", "3", 3),
        ("1.3.2 Intersection of Zero-Trust Security, Flow Control, and Local NLP", "4", 3),
        ("1.4 Objectives and Scope", "4", 2),
        ("1.4.1 Primary Engineering Objective", "4", 3),
        ("1.4.2 Specific Technical Objectives", "4", 3),
        ("1.5 Contributions", "5", 2),
        ("2 LITERATURE REVIEW", "5", 1),
        ("2.1 Evolution of Peer-to-Peer Architectures", "5", 2),
        ("2.1.1 First-Generation P2P: Centralized Indexing (Napster)", "5", 3),
        ("2.1.2 Second-Generation P2P: Query Flooding (Gnutella)", "6", 3),
        ("2.1.3 Third-Generation P2P: Distributed Hash Tables (BitTorrent)", "6", 3),
        ("2.2 WebRTC Standards & Architecture (RFC 8829 & RFC 8831)", "6", 2),
        ("2.2.1 JavaScript Session Establishment Protocol (JSEP)", "6", 3),
        ("2.2.2 SCTP 4-Way Handshake vs. TCP 3-Way Handshake Mechanics", "7", 3),
        ("2.3 NAT Traversal Dynamics: STUN, TURN, and ICE (RFC 8445)", "7", 2),
        ("2.3.1 Binding Discovery and STUN RFC 8489 Mechanics", "7", 3),
        ("2.3.2 Symmetric NAT Edge Cases and Traversal Topologies", "8", 3),
        ("2.4 Transport Layer Tradeoffs: TCP vs. UDP vs. SCTP", "8", 2),
        ("2.5 Cryptographic Foundations: ECDH NIST P-256 & AES-GCM", "8", 2),
        ("2.6 State-of-the-Art Comparative Analysis Matrix", "9", 2),
        ("3 SYSTEM REQUIREMENTS & MATHEMATICAL FORMULATIONS", "9", 1),
        ("3.1 Software Requirements Specification (SRS)", "9", 2),
        ("3.2 Network Information Theory: Shannon-Hartley Wi-Fi Capacity", "10", 2),
        ("3.3 Bandwidth-Delay Product (BDP) and Flow Scaling Models", "10", 2),
        ("3.4 Threat Modeling under the Dolev-Yao Adversarial Paradigm", "11", 2),
        ("3.5 Queueing Theory: M/M/1/K Buffer Overflow Analysis", "11", 2),
        ("3.6 Zero-Trust LAN Micro-Segmentation & Boundary Models", "12", 2),
        ("4 SYSTEM ARCHITECTURE & STRUCTURAL DESIGN", "13", 1),
        ("4.1 Dual-Tier Architectural Model (Control Plane vs Data Plane)", "13", 2),
        ("4.2 Ephemeral WebSocket Signaling Server Design", "13", 2),
        ("4.3 RTCPeerConnection Finite State Automaton", "13", 2),
        ("4.4 Data Flow Diagrams (DFD Level 0, Level 1, Level 2)", "14", 2),
        ("4.5 End-to-End Handshake & Transfer Sequence Flow", "14", 2),
        ("4.6 UI/UX Design System: Cyber Neon Red & Metallic Gold Palette", "15", 2),
        ("4.7 Component Interaction Automata & Session Recovery Mechanics", "15", 2),
        ("5 IMPLEMENTATION OF THE EIGHT EDITIONS", "16", 1),
        ("5.1 Edition 1: WebSocket Signaling Hub & Dynamic Room Dispatch", "16", 2),
        ("5.2 Edition 2: WebRTC DataChannel Integration & ICE Gathering", "17", 2),
        ("5.3 Edition 3: 64KB Sliced Binary Streaming & Reassembly Buffer", "18", 2),
        ("5.4 Edition 4: Adaptive Buffer Backpressure via bufferedAmountLow", "18", 2),
        ("5.5 Edition 5: Real-Time Radar Telemetry & Audio Synthesizer Engine", "19", 2),
        ("5.6 Edition 6: Ephemeral ECDH NIST P-256 Key Agreement", "20", 2),
        ("5.7 Edition 7: Zero-Knowledge AES-GCM-256 Payload Encryption", "21", 2),
        ("5.8 Edition 8: Client-Side TF-IDF NLP Document Summarizer", "21", 2),
        ("6 CRYPTOGRAPHIC PROTOCOLS & SECURITY VERIFICATION", "22", 1),
        ("6.1 ECDH NIST P-256 Key Agreement Formalism", "22", 2),
        ("6.2 Elliptic Curve Group Law & Point Arithmetic Proofs", "22", 2),
        ("6.3 AES-GCM-256 Cipher Block Mechanics & 96-Bit Nonce Uniqueness", "23", 2),
        ("6.4 Galois Field Polynomial Multiplication Formalism (GHASH)", "23", 2),
        ("6.5 Replay Attack Prevention and Tamper Detection Metrics", "24", 2),
        ("6.6 V8 Memory Hygiene & Zero-Knowledge Security Audit", "24", 2),
        ("6.7 Cryptographic Parameter & Cipher Suite Specifications", "24", 2),
        ("6.8 Cryptographic Nonce Collision Bounds & Birthday Proof", "25", 2),
        ("7 EXPERIMENTAL BENCHMARKS & EVALUATION", "25", 1),
        ("7.1 Experimental Testbed Configuration and Hardware Specs", "25", 2),
        ("7.2 Throughput Performance: PeerVault AI vs. Cloud Relays", "25", 2),
        ("7.3 Memory Footprint & RAM Stability under 4MB Backpressure", "26", 2),
        ("7.4 Packet Loss Resilience & Network Jitter Tolerance", "26", 2),
        ("7.5 Heterogeneous Cross-OS Goodput Matrix", "27", 2),
        ("7.6 Chunk Size Sensitivity Analysis", "27", 2),
        ("8 COMPREHENSIVE FACULTY VIVA VOCE DEFENSE", "28", 1),
        ("9 CONCLUSION AND FUTURE WORK", "40", 1),
        ("9.1 Summary of Technical Contributions", "40", 2),
        ("9.2 Limitations and Edge Case Constraints", "41", 2),
        ("9.3 Future Research Roadmap", "41", 2),
        ("REFERENCES & STANDARDS BIBLIOGRAPHY", "42", 1),
        ("APPENDIX A: Production Signaling Server Source (server.js)", "45", 1),
        ("APPENDIX B: WebRTC Cryptographic Pipeline Source (app.js)", "46", 1),
        ("APPENDIX C: Cybernetic UI Stylesheet (style.css)", "47", 1),
        ("APPENDIX D: Markup Interface (index.html)", "48", 1),
        ("APPENDIX E: Dockerfile & Render Cloud Manifests", "49", 1),
        ("APPENDIX F: Repository Architecture & Directory Tree", "50", 1),
        ("10 BIOGRAPHICAL SKETCHES", "51", 1),
    ]

    t_data = []
    for item in toc_entries:
        title, pg, level = item
        if level == 0:
            # Preliminary item
            t_data.append([
                Paragraph(f"<b>{title}</b>", styles['LaTeXTOCChap']),
                Paragraph(f"<b>{pg}</b>", styles['LaTeXTOCPage'])
            ])
        elif level == 1:
            # Chapter header
            t_data.append([
                Paragraph(f"<b>{title}</b>", styles['LaTeXTOCChap']),
                Paragraph(f"<b>{pg}</b>", styles['LaTeXTOCPage'])
            ])
        elif level == 2:
            # Section
            t_data.append([
                Paragraph(f"&nbsp;&nbsp;&nbsp;&nbsp;{title}", styles['LaTeXTOCSec']),
                Paragraph(f"{pg}", styles['LaTeXTOCPage'])
            ])
        elif level == 3:
            # Subsection
            t_data.append([
                Paragraph(f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{title}", styles['LaTeXTOCSubSec']),
                Paragraph(f"{pg}", styles['LaTeXTOCPage'])
            ])

    t_toc = Table(t_data, colWidths=[420, 50])
    t_toc.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 1.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    flowables.append(t_toc)
    flowables.append(PageBreak())

    return flowables
