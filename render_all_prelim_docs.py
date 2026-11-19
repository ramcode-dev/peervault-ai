# render_all_prelim_docs.py
# Renders crisp 300-DPI images for official NIT Agartala thesis prelim pages:
# Cover 1, Cover 2, Approval, Declaration, Certificate.
from PIL import Image, ImageDraw, ImageFont
import os

os.makedirs("assets/rendered_prelims", exist_ok=True)
IMG_W, IMG_H = 2550, 3300 # 8.5 x 11 inches at 300 DPI

try:
    font_title = ImageFont.truetype("timesbd.ttf", 62)
    font_head = ImageFont.truetype("timesbd.ttf", 52)
    font_bold = ImageFont.truetype("timesbd.ttf", 42)
    font_italic = ImageFont.truetype("timesi.ttf", 38)
    font_body = ImageFont.truetype("times.ttf", 38)
    font_small = ImageFont.truetype("times.ttf", 32)
except Exception:
    font_title = font_head = font_bold = font_italic = font_body = font_small = ImageFont.load_default()

def draw_centered_text(draw, y, text, font, fill="black"):
    bbox = draw.textbbox((0, 0), text, font=font)
    w = bbox[2] - bbox[0]
    x = (IMG_W - w) // 2
    draw.text((x, y), text, fill=fill, font=font)
    return y + (bbox[3] - bbox[1])

def render_cover_1():
    img = Image.new("RGB", (IMG_W, IMG_H), "white")
    draw = ImageDraw.Draw(img)

    y = 200
    y = draw_centered_text(draw, y, "PeerVault AI: Browser-Native End-to-End Encrypted", font_title) + 15
    y = draw_centered_text(draw, y, "P2P LAN File Transfer & Local Intelligence", font_title) + 15
    y = draw_centered_text(draw, y, "Architecture", font_title) + 50

    # Draw emblem
    try:
        logo = Image.open("assets/nita_logo.png")
        # Resize maintaining aspect
        lw, lh = 600, int(600 * (logo.height / logo.width))
        logo = logo.resize((lw, lh), Image.Resampling.LANCZOS)
        img.paste(logo, ((IMG_W - lw) // 2, y), mask=logo if logo.mode == 'RGBA' else None)
        y += lh + 60
    except Exception as e:
        print("Emblem error:", e)
        y += 400

    y = draw_centered_text(draw, y, "Submitted By:", font_head) + 30
    y = draw_centered_text(draw, y, "RAM PEDAPATI (23UCS191)", font_bold) + 15
    y = draw_centered_text(draw, y, "TERLI JOGISWARA PRABHAS (23UCS180)", font_bold) + 15
    y = draw_centered_text(draw, y, "UNNAVADA NIKHILESH KUMAR (23UCS177)", font_bold) + 15
    y = draw_centered_text(draw, y, "SITHALAM HARI KRISHNA SAI DURGA PRASAD (23UCS178)", font_bold) + 120

    y = draw_centered_text(draw, y, "COMPUTER SCIENCE & ENGINEERING DEPARTMENT", font_bold) + 15
    y = draw_centered_text(draw, y, "NATIONAL INSTITUTE OF TECHNOLOGY, AGARTALA", font_bold) + 15
    y = draw_centered_text(draw, y, "INDIA-799046", font_bold) + 15
    y = draw_centered_text(draw, y, "APRIL, 2026", font_bold)

    path = "assets/rendered_prelims/cover_page_1.png"
    img.save(path)
    print("Saved", path)
    return path

def render_cover_2():
    img = Image.new("RGB", (IMG_W, IMG_H), "white")
    draw = ImageDraw.Draw(img)

    y = 180
    y = draw_centered_text(draw, y, "PeerVault AI: Browser-Native End-to-End Encrypted", font_title) + 15
    y = draw_centered_text(draw, y, "P2P LAN File Transfer & Local Intelligence", font_title) + 15
    y = draw_centered_text(draw, y, "Architecture", font_title) + 40

    y = draw_centered_text(draw, y, "Report submitted to", font_italic) + 10
    y = draw_centered_text(draw, y, "National Institute of Technology, Agartala", font_bold) + 10
    y = draw_centered_text(draw, y, "for the award of the degree of", font_italic) + 10
    y = draw_centered_text(draw, y, "Bachelor of Technology", font_head) + 10
    y = draw_centered_text(draw, y, "in", font_italic) + 10
    y = draw_centered_text(draw, y, "Computer Science & Engineering", font_head) + 30

    y = draw_centered_text(draw, y, "by", font_italic) + 15
    y = draw_centered_text(draw, y, "RAM PEDAPATI (23UCS191)", font_bold) + 10
    y = draw_centered_text(draw, y, "TERLI JOGISWARA PRABHAS (23UCS180)", font_bold) + 10
    y = draw_centered_text(draw, y, "UNNAVADA NIKHILESH KUMAR (23UCS177)", font_bold) + 10
    y = draw_centered_text(draw, y, "SITHALAM HARI KRISHNA SAI DURGA PRASAD (23UCS178)", font_bold) + 35

    y = draw_centered_text(draw, y, "Under the Guidance of", font_italic) + 20

    # Two supervisors side by side
    col1_x = 450
    col2_x = 1450
    draw.text((col1_x, y), "Dr. Awnish Kumar", fill="black", font=font_bold)
    draw.text((col1_x, y + 50), "Assistant Professor", fill="black", font=font_body)
    draw.text((col1_x, y + 100), "(Supervisor)", fill="black", font=font_italic)

    draw.text((col2_x, y), "Dr. Prashant Bharadwaj", fill="black", font=font_bold)
    draw.text((col2_x, y + 50), "Assistant Professor", fill="black", font=font_body)
    draw.text((col2_x, y + 100), "(Co-Supervisor)", fill="black", font=font_italic)

    y += 200

    # Small emblem
    try:
        logo = Image.open("assets/nita_logo_small.png")
        lw, lh = 240, int(240 * (logo.height / logo.width))
        logo = logo.resize((lw, lh), Image.Resampling.LANCZOS)
        img.paste(logo, ((IMG_W - lw) // 2, y), mask=logo if logo.mode == 'RGBA' else None)
        y += lh + 40
    except Exception as e:
        y += 180

    y = draw_centered_text(draw, y, "COMPUTER SCIENCE & ENGINEERING DEPARTMENT", font_bold) + 15
    y = draw_centered_text(draw, y, "NATIONAL INSTITUTE OF TECHNOLOGY AGARTALA", font_bold) + 15
    y = draw_centered_text(draw, y, "APRIL, 2026", font_bold)

    path = "assets/rendered_prelims/cover_page_2.png"
    img.save(path)
    print("Saved", path)
    return path

def render_approval():
    img = Image.new("RGB", (IMG_W, IMG_H), "white")
    draw = ImageDraw.Draw(img)

    y = 250
    y = draw_centered_text(draw, y, "REPORT APPROVAL FOR B.TECH", font_head) + 40
    draw.line((250, y, IMG_W - 250, y), fill="black", width=3)
    y += 100

    text_lines = [
        "This report entitled “PeerVault AI: Browser-Native End-to-End Encrypted P2P LAN File",
        "Transfer & Local Intelligence Architecture”, by Ram Pedapati (23UCS191), Terli Jogiswara",
        "Prabhas (23UCS180), Unnavada Nikhilesh Kumar (23UCS177), and Sithalam Hari Krishna Sai",
        "Durga Prasad (23UCS178) is approved in partial fulfilment of the requirements for the award",
        "of Bachelor of Technology in Computer Science & Engineering."
    ]
    for line in text_lines:
        draw.text((250, y), line, fill="black", font=font_body)
        y += 65

    y += 350
    # 2 Supervisor Signatures
    col1_x = 350
    col2_x = 1450

    draw.line((col1_x, y, col1_x + 600, y), fill="black", width=2)
    draw.text((col1_x, y + 20), "Dr. Awnish Kumar", fill="black", font=font_bold)
    draw.text((col1_x, y + 75), "(Project Supervisor)", fill="black", font=font_italic)
    draw.text((col1_x, y + 130), "Assistant Professor", fill="black", font=font_body)
    draw.text((col1_x, y + 185), "Computer Science & Engg. Dept.", fill="black", font=font_body)
    draw.text((col1_x, y + 240), "NIT, Agartala", fill="black", font=font_body)

    draw.line((col2_x, y, col2_x + 600, y), fill="black", width=2)
    draw.text((col2_x, y + 20), "Dr. Prashant Bharadwaj", fill="black", font=font_bold)
    draw.text((col2_x, y + 75), "(Co-Supervisor)", fill="black", font=font_italic)
    draw.text((col2_x, y + 130), "Assistant Professor", fill="black", font=font_body)
    draw.text((col2_x, y + 185), "Computer Science & Engg. Dept.", fill="black", font=font_body)
    draw.text((col2_x, y + 240), "NIT Agartala", fill="black", font=font_body)

    y += 450
    draw.text((250, y), "Date: ..............................", fill="black", font=font_body)
    draw.text((250, y + 70), "Place: NIT, Agartala", fill="black", font=font_body)

    path = "assets/rendered_prelims/approval_page.png"
    img.save(path)
    print("Saved", path)
    return path

def render_declaration():
    img = Image.new("RGB", (IMG_W, IMG_H), "white")
    draw = ImageDraw.Draw(img)

    y = 220
    y = draw_centered_text(draw, y, "DECLARATION", font_head) + 40
    draw.line((250, y, IMG_W - 250, y), fill="black", width=3)
    y += 90

    text_lines = [
        "We declare that the work presented in this report titled “PeerVault AI: Browser-Native End-to-End",
        "Encrypted P2P LAN File Transfer & Local Intelligence Architecture”, submitted to the Computer",
        "Science and Engineering Department, National Institute of Technology, Agartala, for the award of",
        "the Bachelor of Technology degree in Computer Science & Engineering, represents our ideas",
        "in our own words and where others' ideas or words have been included, we have adequately cited",
        "and referenced the original sources.",
        "",
        "We also declare that we have adhered to all principles of academic honesty and integrity and have",
        "not misrepresented or fabricated or falsified any idea, data, fact, or source in our submission.",
        "We understand that any violation of the above will be a cause for disciplinary action by the Institute",
        "and can also evoke penal action from the sources which have thus not been properly cited or from",
        "whom proper permission has not been taken when needed."
    ]
    for line in text_lines:
        if line:
            draw.text((250, y), line, fill="black", font=font_body)
        y += 62

    y += 120
    draw.text((250, y), "APRIL, 2026", fill="black", font=font_bold)
    draw.text((250, y + 60), "NIT Agartala", fill="black", font=font_bold)

    # Student Signature lines
    sig_x = 1350
    members = [
        "Ram Pedapati (23UCS191)",
        "Terli Jogiswara Prabhas (23UCS180)",
        "Unnavada Nikhilesh Kumar (23UCS177)",
        "Sithalam Hari Krishna Sai Durga Prasad (23UCS178)"
    ]
    for m in members:
        draw.line((sig_x, y, sig_x + 850, y), fill="black", width=2)
        draw.text((sig_x, y + 18), m, fill="black", font=font_bold)
        y += 135

    path = "assets/rendered_prelims/declaration_page.png"
    img.save(path)
    print("Saved", path)
    return path

def render_certificate():
    img = Image.new("RGB", (IMG_W, IMG_H), "white")
    draw = ImageDraw.Draw(img)

    y = 250
    y = draw_centered_text(draw, y, "CERTIFICATE", font_head) + 40
    draw.line((250, y, IMG_W - 250, y), fill="black", width=3)
    y += 100

    text_lines = [
        "It is certified that the work contained in the report titled “PeerVault AI: Browser-Native End-to-End",
        "Encrypted P2P LAN File Transfer & Local Intelligence Architecture”, by Ram Pedapati (23UCS191),",
        "Terli Jogiswara Prabhas (23UCS180), Unnavada Nikhilesh Kumar (23UCS177), and Sithalam Hari",
        "Krishna Sai Durga Prasad (23UCS178) has been carried out under our supervision.",
        "",
        "This work has not been submitted elsewhere for a degree."
    ]
    for line in text_lines:
        if line:
            draw.text((250, y), line, fill="black", font=font_body)
        y += 65

    y += 350
    col1_x = 350
    col2_x = 1450

    draw.line((col1_x, y, col1_x + 600, y), fill="black", width=2)
    draw.text((col1_x, y + 20), "Dr. Awnish Kumar", fill="black", font=font_bold)
    draw.text((col1_x, y + 75), "Assistant Professor", fill="black", font=font_body)
    draw.text((col1_x, y + 130), "Computer Science & Engg. Dept.", fill="black", font=font_body)
    draw.text((col1_x, y + 185), "NIT Agartala", fill="black", font=font_body)

    draw.line((col2_x, y, col2_x + 600, y), fill="black", width=2)
    draw.text((col2_x, y + 20), "Dr. Prashant Bharadwaj", fill="black", font=font_bold)
    draw.text((col2_x, y + 75), "Assistant Professor", fill="black", font=font_body)
    draw.text((col2_x, y + 130), "Computer Science & Engg. Dept.", fill="black", font=font_body)
    draw.text((col2_x, y + 185), "NIT Agartala", fill="black", font=font_body)

    path = "assets/rendered_prelims/certificate_page.png"
    img.save(path)
    print("Saved", path)
    return path

if __name__ == "__main__":
    render_cover_1()
    render_cover_2()
    render_approval()
    render_declaration()
    render_certificate()
    print("Rendered all preliminary images successfully.")
