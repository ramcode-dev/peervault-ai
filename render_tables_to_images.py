# render_tables_to_images.py
# Renders Table 2.1 and Table 3.1 as crisp 300-DPI images
from PIL import Image, ImageDraw, ImageFont
import os

os.makedirs("assets/rendered_prelims", exist_ok=True)
IMG_W = 2550

try:
    font_bold = ImageFont.truetype("timesbd.ttf", 36)
    font_body = ImageFont.truetype("times.ttf", 34)
    font_small = ImageFont.truetype("times.ttf", 30)
    font_head = ImageFont.truetype("timesbd.ttf", 38)
except Exception:
    font_bold = font_body = font_small = font_head = ImageFont.load_default()

def render_table_2_1():
    # Table 2.1 Comparative Analysis Matrix
    # Height approx 1400 px
    H = 1450
    img = Image.new("RGB", (IMG_W, H), "white")
    draw = ImageDraw.Draw(img)

    # Column widths
    cols = [550, 480, 480, 480, 520]
    x_starts = [40]
    for w in cols[:-1]:
        x_starts.append(x_starts[-1] + w)

    headers = ["Feature / Dimension", "Cloud Storage\n(Drive / Dropbox)", "BitTorrent\nP2P Clients", "Local Airdrop /\nNearby Share", "PeerVault AI\n(Our Architecture)"]
    rows = [
        ["Client Software Installation", "Not required (Web) / Apps", "Mandatory native client", "OS-locked (Apple/Android)", "Zero Installation (WebRTC)"],
        ["Data Transmission Path", "Double WAN Relay", "Distributed Swarm", "Proprietary Ad-Hoc Wi-Fi", "Direct Subnet P2P LAN"],
        ["Server Storage Footprint", "Persistent cloud disk", "None (Swarm cache)", "None", "Zero Server Storage"],
        ["Cryptographic Guarantee", "Server-side decryption", "Plaintext (SHA-1 hash)", "Proprietary TLS handshake", "Zero-Knowledge ECDH+GCM"],
        ["File Size Quotas / Limits", "Strict (2GB - 15GB)", "Unlimited (Disk bound)", "OS buffer bound", "Unlimited (4MB Flow Ctrled)"],
        ["Local Document Intelligence", "Cloud AI (Telemetry)", "None", "None", "Client-Side TF-IDF NLP"],
        ["Cross-Platform Interoperability", "Universal (Web)", "Desktop / Mobile apps", "Incompatible ecosystems", "Universal Browser Native"]
    ]

    y = 30
    row_h_head = 140
    # Draw header bg
    draw.rectangle([x_starts[0], y, x_starts[0] + sum(cols), y + row_h_head], fill="#f1f5f9", outline="#cbd5e1", width=2)
    for i, h in enumerate(headers):
        lines = h.split("\n")
        curr_y = y + 25 if len(lines) > 1 else y + 45
        for line in lines:
            draw.text((x_starts[i] + 20, curr_y), line, fill="black", font=font_head)
            curr_y += 45

    y += row_h_head
    row_h = 160
    for r_idx, row in enumerate(rows):
        bg = "#fef2f2" # highlight PeerVault col
        draw.rectangle([x_starts[0], y, x_starts[0] + sum(cols), y + row_h], fill="white", outline="#cbd5e1", width=2)
        # Highlight last col
        draw.rectangle([x_starts[4], y, x_starts[4] + cols[4], y + row_h], fill="#fef2f2", outline="#cbd5e1", width=2)

        for c_idx, cell in enumerate(row):
            f = font_bold if (c_idx == 0 or c_idx == 4) else font_body
            # word wrap inside cell
            words = cell.split(" ")
            line1, line2 = "", ""
            for w in words:
                if len(line1 + " " + w) < 24:
                    line1 = (line1 + " " + w).strip()
                else:
                    line2 = (line2 + " " + w).strip()
            
            if line2:
                draw.text((x_starts[c_idx] + 20, y + 35), line1, fill="black", font=f)
                draw.text((x_starts[c_idx] + 20, y + 85), line2, fill="black", font=f)
            else:
                draw.text((x_starts[c_idx] + 20, y + 55), line1, fill="black", font=f)

        y += row_h

    # Vertical grid lines
    for x in x_starts:
        draw.line([x, 30, x, y], fill="#cbd5e1", width=2)
    draw.line([x_starts[0] + sum(cols), 30, x_starts[0] + sum(cols), y], fill="#cbd5e1", width=2)

    path = "assets/rendered_prelims/table_2_1.png"
    img.save(path)
    print("Saved", path)
    return path

def render_table_3_1():
    # Table 3.1 SRS Table
    H = 2600
    img = Image.new("RGB", (IMG_W, H), "white")
    draw = ImageDraw.Draw(img)

    cols = [420, 1420, 670]
    x_starts = [40]
    for w in cols[:-1]:
        x_starts.append(x_starts[-1] + w)

    headers = ["Category", "Requirement ID & Specification", "Verification Metric"]
    rows = [
        ["Functional", "FR-1 (Dynamic Room Dispatch): The signaling hub generates pseudo-random room IDs and supports auto-joining via query parameter.", "100% automated connection without manual entry."],
        ["Functional", "FR-2 (ICE Handshake): Exchange SDP Offer/Answer and STUN ICE candidates over WebSocket without transferring file payloads.", "PeerConnection state resolves to 'connected' in <1.2s."],
        ["Functional", "FR-3 (Binary Chunking): File payloads of arbitrary size are sliced into uniform 64KB ArrayBuffer slices over SCTP DataChannel.", "Bit-level file integrity validated via SHA-256 match."],
        ["Functional", "FR-4 (Zero-Knowledge Cryptography): Performs ECDH NIST P-256 key agreement and encrypts chunks via AES-GCM-256 with distinct 96-bit IVs.", "Signaling server capture confirms zero plaintext leakage."],
        ["Functional", "FR-5 (Local AI Intelligence): In-browser TF-IDF engine parses received text/code files and extracts key representative sentences.", "Summarization execution time <350ms for 100KB document."],
        ["Functional", "FR-6 (Visual Telemetry): Canvas radar sweep and real-time throughput / ETA telemetry update at 4 Hz (every 250ms).", "Smooth 60 FPS animation with zero frame drops during transfer."],
        ["Functional", "FR-7 (Audio Synthesizer): Web Audio API synthesizes sine frequency audio cues on connection, transfer, and completion.", "Audible feedback with <15ms latency and zero HTTP fetching."],
        ["Functional", "FR-8 (Graceful Abort): Either peer can cancel an active transfer mid-stream, freeing allocated buffers cleanly.", "DataChannel abort signal clears memory arrays in <50ms."],
        ["Functional", "FR-9 (Multi-File Queuing): Transmission engine supports sequential batch transfer of queued files over one peer connection.", "Automatic transition to next queued item without renegotiation."],
        ["Non-Functional", "NFR-1 (Memory Ceiling): Total browser heap consumption during active file transmission must not exceed 45 MB.", "Chrome DevTools Memory Heap profiler snapshot <45 MB."],
        ["Non-Functional", "NFR-2 (Throughput Performance): Sustained local transfer throughput over Wi-Fi 6 LAN must exceed 200 Mbps (25 MB/s).", "Average transfer throughput measured at >280 Mbps."],
        ["Non-Functional", "NFR-3 (Zero Installation): Platform executes entirely within evergreen web browsers without native plugins or extensions.", "100% functional across Chrome, Edge, Firefox, and Safari."],
        ["Non-Functional", "NFR-4 (High Availability): Signaling service achieves 99.9% uptime with automated health checks.", "Continuous HTTP 200 OK via /api/health endpoint monitoring."],
        ["Non-Functional", "NFR-5 (Accessible Contrast): User interface elements comply with WCAG 2.1 AAA high-contrast standards (>=7:1 ratio).", "Axe Accessibility DevTools automated score: 100/100."]
    ]

    y = 30
    row_h_head = 90
    draw.rectangle([x_starts[0], y, x_starts[0] + sum(cols), y + row_h_head], fill="#f1f5f9", outline="#cbd5e1", width=2)
    for i, h in enumerate(headers):
        draw.text((x_starts[i] + 20, y + 25), h, fill="black", font=font_head)

    y += row_h_head
    row_h = 165
    for r_idx, row in enumerate(rows):
        draw.rectangle([x_starts[0], y, x_starts[0] + sum(cols), y + row_h], fill="white", outline="#cbd5e1", width=2)
        for c_idx, cell in enumerate(row):
            f = font_bold if c_idx == 0 else font_body
            # wrap cell
            words = cell.split(" ")
            line1, line2 = "", ""
            max_len = 18 if c_idx == 0 else (68 if c_idx == 1 else 32)
            for w in words:
                if len(line1 + " " + w) < max_len:
                    line1 = (line1 + " " + w).strip()
                else:
                    line2 = (line2 + " " + w).strip()
            draw.text((x_starts[c_idx] + 20, y + 35), line1, fill="black", font=f)
            if line2:
                draw.text((x_starts[c_idx] + 20, y + 85), line2, fill="black", font=font_body)

        y += row_h

    for x in x_starts:
        draw.line([x, 30, x, y], fill="#cbd5e1", width=2)
    draw.line([x_starts[0] + sum(cols), 30, x_starts[0] + sum(cols), y], fill="#cbd5e1", width=2)

    path = "assets/rendered_prelims/table_3_1.png"
    img.save(path)
    print("Saved", path)
    return path

if __name__ == "__main__":
    render_table_2_1()
    render_table_3_1()
    print("Rendered tables successfully.")
