# render_threat_table.py
from PIL import Image, ImageDraw, ImageFont
import os

os.makedirs("assets/rendered_prelims", exist_ok=True)
IMG_W = 2550

try:
    font_bold = ImageFont.truetype("timesbd.ttf", 36)
    font_body = ImageFont.truetype("times.ttf", 34)
    font_head = ImageFont.truetype("timesbd.ttf", 38)
except Exception:
    font_bold = font_body = font_head = ImageFont.load_default()

def render_table_3_2():
    H = 1500
    img = Image.new("RGB", (IMG_W, H), "white")
    draw = ImageDraw.Draw(img)

    cols = [520, 980, 970]
    x_starts = [40]
    for w in cols[:-1]:
        x_starts.append(x_starts[-1] + w)

    headers = ["Adversarial Attack Vector", "Mechanics & Threat Objective", "PeerVault AI Countermeasure"]
    rows = [
        ["Signaling Eavesdropping", "Adversary monitors WebSocket signaling frames on public Wi-Fi to capture file contents.", "Zero-Knowledge Data Plane: Zero file chunks or symmetric keys sent via signaling. Only public ECDH keys exchanged."],
        ["Man-in-the-Middle (MitM)", "Active attacker replaces public ECDH keys during signaling handshake to intercept traffic.", "Cryptographic Fingerprinting: Derived session key hash displayed as visual fingerprint for out-of-band peer verification."],
        ["Packet Replay Attack", "Attacker captures encrypted 64KB chunks and injects them repeatedly into the stream.", "Strict Nonce Monotonicity: Every chunk contains incremental 32-bit chunk sequence number authenticated via AES-GCM."],
        ["Ciphertext Tampering", "Attacker flips bits in ciphertext chunks during wireless transit.", "AEAD Authentication Tag: AES-GCM calculates 128-bit GHASH tag. Tampered chunks fail verification and throw exception."],
        ["Memory Cold-Boot", "Adversary attempts to read encryption keys from browser memory after session termination.", "V8 Scoped Dereferencing: CryptoKey handles are scoped locally, non-exportable, and garbage-collected upon completion."],
        ["Timing Side-Channel", "Adversary measures cryptographic execution duration to deduce secret scalar bits.", "Constant-Time Web Crypto: Underlying BoringSSL/NSS cryptographic implementations execute constant-time multiplication."]
    ]

    y = 30
    row_h_head = 90
    draw.rectangle([x_starts[0], y, x_starts[0] + sum(cols), y + row_h_head], fill="#f1f5f9", outline="#cbd5e1", width=2)
    for i, h in enumerate(headers):
        draw.text((x_starts[i] + 20, y + 25), h, fill="black", font=font_head)

    y += row_h_head
    row_h = 220
    for r_idx, row in enumerate(rows):
        draw.rectangle([x_starts[0], y, x_starts[0] + sum(cols), y + row_h], fill="white", outline="#cbd5e1", width=2)
        for c_idx, cell in enumerate(row):
            f = font_bold if c_idx == 0 else font_body
            words = cell.split(" ")
            line1, line2, line3 = "", "", ""
            max_len = 24 if c_idx == 0 else 46
            for w in words:
                if len(line1 + " " + w) < max_len:
                    line1 = (line1 + " " + w).strip()
                elif len(line2 + " " + w) < max_len:
                    line2 = (line2 + " " + w).strip()
                else:
                    line3 = (line3 + " " + w).strip()
            
            draw.text((x_starts[c_idx] + 20, y + 30), line1, fill="black", font=f)
            if line2:
                draw.text((x_starts[c_idx] + 20, y + 80), line2, fill="black", font=font_body)
            if line3:
                draw.text((x_starts[c_idx] + 20, y + 130), line3, fill="black", font=font_body)

        y += row_h

    for x in x_starts:
        draw.line([x, 30, x, y], fill="#cbd5e1", width=2)
    draw.line([x_starts[0] + sum(cols), 30, x_starts[0] + sum(cols), y], fill="#cbd5e1", width=2)

    path = "assets/rendered_prelims/table_3_2_threat.png"
    img.save(path)
    print("Saved", path)
    return path

if __name__ == "__main__":
    render_table_3_2()
