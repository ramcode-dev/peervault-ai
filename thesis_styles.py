# thesis_styles.py
# ReportLab style definitions and custom canvas for PeerVault AI Capstone Thesis
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable, Preformatted

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, total_pages):
        # Preliminary pages (1 to 4: Title, Declaration, Certificate, Acknowledgments) don't have header/footer
        if self._pageNumber <= 4:
            return

        self.saveState()
        self.setFont("Helvetica-Bold", 7.5)
        self.setFillColor(colors.HexColor("#475569"))

        # Running Header
        self.drawString(54, 755, "NIT AGARTALA  |  DEPARTMENT OF COMPUTER SCIENCE & ENGINEERING  |  B.TECH THESIS")
        self.setStrokeColor(colors.HexColor("#cbd5e1"))
        self.setLineWidth(0.6)
        self.line(54, 747, 558, 747)

        # Running Footer
        self.line(54, 45, 558, 45)
        self.setFont("Helvetica", 7.5)
        self.drawString(54, 32, "PeerVault AI: End-to-End Encrypted WebRTC LAN File Transfer & Intelligence Architecture")
        page_str = f"Page {self._pageNumber} of {total_pages}"
        self.drawRightString(558, 32, page_str)
        self.restoreState()

def get_thesis_styles():
    styles = getSampleStyleSheet()

    c_primary = colors.HexColor("#0f172a")  # Deep Navy / Slate
    c_accent = colors.HexColor("#991b1b")   # Academic Crimson
    c_gold = colors.HexColor("#b45309")     # Amber / Gold
    c_dark = colors.HexColor("#1e293b")     # Body Charcoal
    c_muted = colors.HexColor("#64748b")    # Slate Muted
    c_code_bg = colors.HexColor("#f8fafc")  # Subtle code background
    c_border = colors.HexColor("#e2e8f0")

    custom = {
        'CoverInst': ParagraphStyle('CoverInst', fontName='Helvetica-Bold', fontSize=14, leading=18, alignment=1, textColor=c_primary, spaceAfter=4),
        'CoverDept': ParagraphStyle('CoverDept', fontName='Helvetica', fontSize=10.5, leading=15, alignment=1, textColor=c_muted, spaceAfter=24),
        'CoverTitle': ParagraphStyle('CoverTitle', fontName='Helvetica-Bold', fontSize=20, leading=25, alignment=1, textColor=c_accent, spaceAfter=10),
        'CoverSub': ParagraphStyle('CoverSub', fontName='Helvetica', fontSize=11, leading=16, alignment=1, textColor=c_dark, spaceAfter=24),
        'CoverMetaHeader': ParagraphStyle('CoverMetaHeader', fontName='Helvetica-Bold', fontSize=9.5, leading=13, textColor=c_primary),
        'CoverMetaVal': ParagraphStyle('CoverMetaVal', fontName='Helvetica', fontSize=9, leading=13, textColor=c_dark),
        'CoverFoot': ParagraphStyle('CoverFoot', fontName='Helvetica', fontSize=8.5, leading=12, alignment=1, textColor=c_muted),

        'ChapNumber': ParagraphStyle('ChapNumber', fontName='Helvetica-Bold', fontSize=12, leading=16, textColor=c_accent, spaceBefore=10, spaceAfter=2, keepWithNext=True),
        'ChapTitle': ParagraphStyle('ChapTitle', fontName='Helvetica-Bold', fontSize=17, leading=22, textColor=c_primary, spaceBefore=2, spaceAfter=14, keepWithNext=True),
        'SecTitle': ParagraphStyle('SecTitle', fontName='Helvetica-Bold', fontSize=12, leading=16, textColor=c_accent, spaceBefore=14, spaceAfter=6, keepWithNext=True),
        'SubSecTitle': ParagraphStyle('SubSecTitle', fontName='Helvetica-Bold', fontSize=10, leading=14, textColor=c_gold, spaceBefore=10, spaceAfter=4, keepWithNext=True),

        'Body': ParagraphStyle('Body', fontName='Helvetica', fontSize=9.5, leading=14.5, textColor=c_dark, spaceAfter=7, alignment=4),
        'BodyBold': ParagraphStyle('BodyBold', fontName='Helvetica-Bold', fontSize=9.5, leading=14.5, textColor=c_dark, spaceAfter=7),
        'Bullet': ParagraphStyle('Bullet', fontName='Helvetica', fontSize=9, leading=13.5, textColor=c_dark, leftIndent=14, spaceAfter=3),
        'Callout': ParagraphStyle('Callout', fontName='Helvetica-Oblique', fontSize=9, leading=13.5, textColor=colors.HexColor("#334155"), leftIndent=16, rightIndent=16, spaceBefore=6, spaceAfter=8),

        'CodeBlock': ParagraphStyle('CodeBlock', fontName='Courier', fontSize=7.5, leading=10.5, textColor=c_primary, backColor=c_code_bg, borderPadding=5, spaceBefore=4, spaceAfter=7),
        'TableHead': ParagraphStyle('TableHead', fontName='Helvetica-Bold', fontSize=8.5, leading=11, alignment=1, textColor=c_primary),
        'TableCell': ParagraphStyle('TableCell', fontName='Helvetica', fontSize=8, leading=11, textColor=c_dark),
        'TableCellBold': ParagraphStyle('TableCellBold', fontName='Helvetica-Bold', fontSize=8, leading=11, textColor=c_dark),

        'QTitle': ParagraphStyle('QTitle', fontName='Helvetica-Bold', fontSize=9.5, leading=14, textColor=c_primary, spaceBefore=10, spaceAfter=3, keepWithNext=True),
        'AnsText': ParagraphStyle('AnsText', fontName='Helvetica', fontSize=9, leading=13.5, textColor=c_dark, leftIndent=10, spaceAfter=7),

        'TOCItem': ParagraphStyle('TOCItem', fontName='Helvetica', fontSize=9, leading=14, textColor=c_dark),
        'TOCPage': ParagraphStyle('TOCPage', fontName='Helvetica-Bold', fontSize=9, leading=14, alignment=2, textColor=c_accent),
        'TOCChap': ParagraphStyle('TOCChap', fontName='Helvetica-Bold', fontSize=9.5, leading=15, textColor=c_primary),
    }
    return custom
