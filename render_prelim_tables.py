from PIL import Image, ImageDraw, ImageFont
import os

os.makedirs("assets/rendered_prelims", exist_ok=True)

# Image dimensions for Letter page at 300 DPI:
# 8.5 x 11 inches at 300 DPI = 2550 x 3300
IMG_W, IMG_H = 2550, 3300

try:
    font_title = ImageFont.truetype("timesbd.ttf", 68)
    font_chap = ImageFont.truetype("timesbd.ttf", 46)
    font_sec = ImageFont.truetype("times.ttf", 40)
    font_subsec = ImageFont.truetype("times.ttf", 36)
except Exception:
    font_title = font_chap = font_sec = font_subsec = ImageFont.load_default()

def render_list_of_figures():
    img = Image.new("RGB", (IMG_W, IMG_H), "white")
    draw = ImageDraw.Draw(img)
    
    # Title
    draw.text((220, 200), "List of Figures", fill="black", font=font_title)
    draw.line((220, 285, IMG_W - 220, 285), fill="black", width=3)
    
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
        ("7.4", "Packet Loss Tolerance Curve Under Simulated Network Drops (0-15%)", "27")
    ]
    
    y = 380
    for num, title, pg in figures:
        draw.text((220, y), f"Figure {num}:", fill="black", font=font_chap)
        draw.text((520, y), title, fill="black", font=font_sec)
        draw.text((IMG_W - 320, y), pg, fill="black", font=font_chap)
        draw.line((220, y + 65, IMG_W - 220, y + 65), fill="#E5E7EB", width=2)
        y += 135
        
    path = "assets/rendered_prelims/list_of_figures.png"
    img.save(path)
    print("Saved", path)
    return path

def render_list_of_tables():
    img = Image.new("RGB", (IMG_W, IMG_H), "white")
    draw = ImageDraw.Draw(img)
    
    # Title
    draw.text((220, 200), "List of Tables", fill="black", font=font_title)
    draw.line((220, 285, IMG_W - 220, 285), fill="black", width=3)
    
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
        ("10", "Project Objectives Achievement Status & Verification Matrix", "41")
    ]
    
    y = 380
    for num, title, pg in tables:
        draw.text((220, y), f"Table {num}:", fill="black", font=font_chap)
        draw.text((500, y), title, fill="black", font=font_sec)
        draw.text((IMG_W - 320, y), pg, fill="black", font=font_chap)
        draw.line((220, y + 65, IMG_W - 220, y + 65), fill="#E5E7EB", width=2)
        y += 145
        
    path = "assets/rendered_prelims/list_of_tables.png"
    img.save(path)
    print("Saved", path)
    return path

def render_toc_pages():
    toc_p1 = [
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
        ("2.1.3 Third-Generation P2P: Distributed Hash Tables (BitTorrent)", "6", 3)
    ]
    
    toc_p2 = [
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
        ("4.7 Component Interaction Automata & Session Recovery Mechanics", "15", 2)
    ]
    
    toc_p3 = [
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
        ("APPENDIX D: Markup Interface (index.html)", "48", 1)
    ]

    pages = [toc_p1, toc_p2, toc_p3]
    paths = []
    for idx, p_entries in enumerate(pages):
        img = Image.new("RGB", (IMG_W, IMG_H), "white")
        draw = ImageDraw.Draw(img)
        
        # Title on first page
        if idx == 0:
            draw.text((220, 180), "Contents", fill="black", font=font_title)
            draw.line((220, 265, IMG_W - 220, 265), fill="black", width=3)
            y = 330
        else:
            draw.text((220, 140), f"Contents (Continued - {idx+1})", fill="#374151", font=font_sec)
            draw.line((220, 200, IMG_W - 220, 200), fill="#9CA3AF", width=2)
            y = 260
            
        for title, pg, level in p_entries:
            if level == 0 or level == 1:
                f = font_chap
                indent = 220
            elif level == 2:
                f = font_sec
                indent = 270
            else:
                f = font_subsec
                indent = 330
                
            draw.text((indent, y), title, fill="black", font=f)
            draw.text((IMG_W - 320, y), pg, fill="black", font=f)
            y += 98
            
        path = f"assets/rendered_prelims/toc_page_{idx+1}.png"
        img.save(path)
        print("Saved", path)
        paths.append(path)
        
    return paths

if __name__ == "__main__":
    render_list_of_figures()
    render_list_of_tables()
    render_toc_pages()
    print("All preliminary graphics successfully generated!")
