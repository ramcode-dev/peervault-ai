# build_full_thesis.py
# Compiles the comprehensive 60-70 page B.Tech Capstone Thesis for PeerVault AI
import os
import sys
import shutil
import re
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate

from thesis_styles import LaTeXNumberedCanvas, get_thesis_styles
from thesis_prelims import build_preliminaries
from thesis_ch1_ch2 import build_chapters_1_and_2
from thesis_ch3_ch4 import build_chapters_3_and_4
from thesis_ch5_ch6 import build_chapters_5_and_6
from thesis_ch7_ch8 import build_chapters_7_and_8
from thesis_ch9_refs import build_chapter_9_and_refs

def compile_pdf(output_pdf_path):
    styles = get_thesis_styles()

    doc = SimpleDocTemplate(
        output_pdf_path,
        pagesize=letter,
        leftMargin=54,   # 0.75 in
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )

    story = []
    print("Building Preliminaries...")
    story.extend(build_preliminaries(styles))

    print("Building Chapters 1 & 2...")
    story.extend(build_chapters_1_and_2(styles))

    print("Building Chapters 3 & 4...")
    story.extend(build_chapters_3_and_4(styles))

    print("Building Chapters 5 & 6...")
    story.extend(build_chapters_5_and_6(styles))

    print("Building Chapters 7 & 8...")
    story.extend(build_chapters_7_and_8(styles))

    print("Building Chapter 9 & References...")
    story.extend(build_chapter_9_and_refs(styles))

    print("Compiling PDF with LaTeXNumberedCanvas...")
    doc.build(story, canvasmaker=LaTeXNumberedCanvas)
    print(f"Compilation complete: {output_pdf_path}")

def count_pdf_pages(pdf_path):
    with open(pdf_path, 'rb') as f:
        data = f.read()
    # Find /Count in Pages or count /Type /Page
    matches = re.findall(rb'/Type\s*/Page\b', data)
    return len(matches)

if __name__ == "__main__":
    out_pdf = "PeerVault_AI_Project_Report.pdf"
    compile_pdf(out_pdf)
    pages = count_pdf_pages(out_pdf)
    print(f"\n==========================================")
    print(f"Generated PDF Page Count: {pages} pages")
    print(f"==========================================\n")
