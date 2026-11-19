# thesis_styles.py
# LaTeX-matched academic styling for NIT Agartala B.Tech Thesis
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable, Image

def int_to_roman(n):
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syb = ["m", "cm", "d", "cd", "c", "xc", "l", "xl", "x", "ix", "v", "iv", "i"]
    roman_num = ""
    i = 0
    while n > 0:
        for _ in range(n // val[i]):
            roman_num += syb[i]
            n -= val[i]
        i += 1
    return roman_num

class LaTeXNumberedCanvas(canvas.Canvas):
    """
    Implements standard LaTeX academic book/report numbering:
    - Page 1 & 2: Cover & Submission page (no page numbers, no header)
    - Page 3 to 17: Roman numerals at bottom center (iii, iv, v, ... xvii)
    - Page 18+: Arabic numerals at bottom center (1, 2, 3, ...), with running header and top horizontal rule
    """
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
            self.draw_latex_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_latex_decorations(self, total_pages):
        # Determine prelim offset: Chapter 1 begins at page 14
        prelim_count = 13  # Pages 1 to 13 are preliminaries (Chapter 1 begins at page 14)

        # Cover (1) and Inner Cover (2): no headers, no page numbers
        if self._pageNumber <= 2:
            return

        self.saveState()
        self.setFont("Times-Roman", 10)
        self.setFillColor(colors.black)
        self.setStrokeColor(colors.HexColor("#333333"))
        self.setLineWidth(0.5)

        if self._pageNumber <= prelim_count:
            # Preliminary pages (Roman numerals)
            roman_str = int_to_roman(self._pageNumber)
            # Bottom Center
            self.drawCentredString(306, 45, roman_str)
        else:
            # Main matter (Arabic numerals: Page 1, 2, 3...)
            arabic_num = self._pageNumber - prelim_count
            
            # Running Header with Top Rule
            self.line(72, 735, 540, 735)
            self.setFont("Times-Italic", 9.5)
            # Top header text
            self.drawRightString(540, 742, "SECURE LAN PEER-TO-PEER FILE SHARING SYSTEM")
            
            # Bottom Center Arabic Page Number
            self.setFont("Times-Roman", 10)
            self.drawCentredString(306, 45, str(arabic_num))

        self.restoreState()

def get_thesis_styles():
    styles = getSampleStyleSheet()

    # Base Fonts
    c_dark = colors.HexColor("#111827")
    c_crimson = colors.HexColor("#991b1b")
    c_blue = colors.HexColor("#1e3a8a")

    # Cover Page Styles
    styles.add(ParagraphStyle(
        name='LaTeXCoverTitle',
        fontName='Times-Bold',
        fontSize=18,
        leading=24,
        alignment=1, # Center
        textColor=c_dark,
        spaceAfter=15
    ))

    styles.add(ParagraphStyle(
        name='LaTeXCoverSub',
        fontName='Times-Roman',
        fontSize=12,
        leading=17,
        alignment=1,
        textColor=c_dark,
        spaceAfter=10
    ))

    styles.add(ParagraphStyle(
        name='LaTeXCoverMembers',
        fontName='Times-Bold',
        fontSize=11,
        leading=16,
        alignment=1,
        textColor=c_dark,
        spaceAfter=6
    ))

    styles.add(ParagraphStyle(
        name='LaTeXCoverFaculty',
        fontName='Times-Roman',
        fontSize=11,
        leading=15,
        alignment=1,
        textColor=c_dark,
        spaceAfter=4
    ))

    styles.add(ParagraphStyle(
        name='LaTeXCoverDept',
        fontName='Times-Bold',
        fontSize=10.5,
        leading=15,
        alignment=1,
        textColor=c_dark
    ))

    # Preliminaries Heading
    styles.add(ParagraphStyle(
        name='LaTeXPrelimTitle',
        fontName='Times-Bold',
        fontSize=16,
        leading=22,
        alignment=1, # Center
        textColor=c_dark,
        spaceAfter=16
    ))

    # Dedication
    styles.add(ParagraphStyle(
        name='LaTeXDedication',
        fontName='Times-Italic',
        fontSize=11,
        leading=18,
        alignment=4, # Justified
        textColor=c_dark,
        spaceAfter=12
    ))

    # Epigraph Quote
    styles.add(ParagraphStyle(
        name='LaTeXQuote',
        fontName='Times-BoldItalic',
        fontSize=13,
        leading=20,
        alignment=1,
        textColor=c_dark,
        spaceAfter=10
    ))

    styles.add(ParagraphStyle(
        name='LaTeXQuoteAuthor',
        fontName='Times-Roman',
        fontSize=11,
        leading=16,
        alignment=1,
        textColor=c_dark
    ))

    # Main Chapters
    styles.add(ParagraphStyle(
        name='LaTeXChapterNum',
        fontName='Times-Bold',
        fontSize=16,
        leading=22,
        alignment=2, # Right-aligned
        textColor=c_dark,
        spaceAfter=4
    ))

    styles.add(ParagraphStyle(
        name='LaTeXChapterTitle',
        fontName='Times-Bold',
        fontSize=16,
        leading=22,
        alignment=2, # Right-aligned
        textColor=c_dark,
        spaceAfter=20
    ))

    styles.add(ParagraphStyle(
        name='LaTeXSecTitle',
        fontName='Times-Bold',
        fontSize=13,
        leading=18,
        alignment=0, # Left
        textColor=c_dark,
        spaceBefore=12,
        spaceAfter=6
    ))

    styles.add(ParagraphStyle(
        name='LaTeXSubSecTitle',
        fontName='Times-Bold',
        fontSize=11.5,
        leading=16,
        alignment=0,
        textColor=c_dark,
        spaceBefore=8,
        spaceAfter=4
    ))

    styles.add(ParagraphStyle(
        name='LaTeXBody',
        fontName='Times-Roman',
        fontSize=10.5,
        leading=15,
        alignment=4, # Justified
        textColor=c_dark,
        spaceAfter=8
    ))

    styles.add(ParagraphStyle(
        name='LaTeXBodyBold',
        fontName='Times-Bold',
        fontSize=10.5,
        leading=15,
        alignment=4,
        textColor=c_dark,
        spaceAfter=6
    ))

    styles.add(ParagraphStyle(
        name='LaTeXBullet',
        fontName='Times-Roman',
        fontSize=10.5,
        leading=15,
        alignment=4,
        leftIndent=15,
        textColor=c_dark,
        spaceAfter=4
    ))

    styles.add(ParagraphStyle(
        name='LaTeXCode',
        fontName='Courier',
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor("#1e293b"),
        spaceBefore=4,
        spaceAfter=6
    ))

    # TOC
    styles.add(ParagraphStyle(
        name='LaTeXTOCChap',
        fontName='Times-Bold',
        fontSize=10.5,
        leading=15,
        textColor=c_dark
    ))

    styles.add(ParagraphStyle(
        name='LaTeXTOCSec',
        fontName='Times-Roman',
        fontSize=10,
        leading=14,
        leftIndent=15,
        textColor=c_dark
    ))

    styles.add(ParagraphStyle(
        name='LaTeXTOCSubSec',
        fontName='Times-Roman',
        fontSize=9.5,
        leading=13,
        leftIndent=30,
        textColor=c_dark
    ))

    styles.add(ParagraphStyle(
        name='LaTeXTOCPage',
        fontName='Times-Roman',
        fontSize=10,
        leading=14,
        alignment=2,
        textColor=c_dark
    ))

    # Tables
    styles.add(ParagraphStyle(
        name='LaTeXTableHead',
        fontName='Times-Bold',
        fontSize=9.5,
        leading=13,
        textColor=c_dark
    ))

    styles.add(ParagraphStyle(
        name='LaTeXTableCell',
        fontName='Times-Roman',
        fontSize=9,
        leading=12.5,
        textColor=c_dark
    ))

    styles.add(ParagraphStyle(
        name='LaTeXTableCellBold',
        fontName='Times-Bold',
        fontSize=9,
        leading=12.5,
        textColor=c_dark
    ))

    # Viva Voce
    styles.add(ParagraphStyle(
        name='LaTeXQTitle',
        fontName='Times-Bold',
        fontSize=10.5,
        leading=14.5,
        textColor=c_dark,
        spaceBefore=7,
        spaceAfter=2
    ))

    styles.add(ParagraphStyle(
        name='LaTeXAnsText',
        fontName='Times-Roman',
        fontSize=10,
        leading=14,
        alignment=4,
        leftIndent=12,
        textColor=c_dark,
        spaceAfter=6
    ))

    # Standard Aliases mapped to LaTeX typography
    def add_or_update(name, parent_name):
        if name in styles:
            s = styles[name]
            p = styles[parent_name]
            for attr in ['fontName', 'fontSize', 'leading', 'textColor', 'alignment', 'spaceBefore', 'spaceAfter', 'leftIndent', 'rightIndent']:
                if hasattr(p, attr):
                    setattr(s, attr, getattr(p, attr))
        else:
            styles.add(ParagraphStyle(name=name, parent=styles[parent_name]))

    add_or_update('ChapNumber', 'LaTeXChapterNum')
    add_or_update('ChapTitle', 'LaTeXChapterTitle')
    add_or_update('SecTitle', 'LaTeXSecTitle')
    add_or_update('SubSecTitle', 'LaTeXSubSecTitle')
    add_or_update('Body', 'LaTeXBody')
    add_or_update('BodyBold', 'LaTeXBodyBold')
    add_or_update('Bullet', 'LaTeXBullet')
    add_or_update('CodeBlock', 'LaTeXCode')
    add_or_update('TableHead', 'LaTeXTableHead')
    add_or_update('TableCell', 'LaTeXTableCell')
    add_or_update('TableCellBold', 'LaTeXTableCellBold')
    add_or_update('QTitle', 'LaTeXQTitle')
    add_or_update('AnsText', 'LaTeXAnsText')
    add_or_update('Callout', 'LaTeXBody')
    if 'Callout' in styles:
        styles['Callout'].fontName = 'Times-Italic'
        styles['Callout'].leftIndent = 15
        styles['Callout'].rightIndent = 15

    return styles
