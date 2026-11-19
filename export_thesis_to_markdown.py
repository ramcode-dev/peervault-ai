# export_thesis_to_markdown.py
import re
import html
import os
from reportlab.platypus import Paragraph, Table, Preformatted, PageBreak, Spacer, HRFlowable
from thesis_styles import get_thesis_styles
from thesis_prelims import build_preliminaries
from thesis_ch1_ch2 import build_chapters_1_and_2
from thesis_ch3_ch4 import build_chapters_3_and_4
from thesis_ch5_ch6 import build_chapters_5_and_6
from thesis_ch7_ch8 import build_chapters_7_and_8
from thesis_ch9_refs import build_chapter_9_and_refs

def clean_html(text):
    if not text:
        return ""
    # Replace common formatting
    text = re.sub(r'<b>(.*?)</b>', r'**\1**', text, flags=re.DOTALL)
    text = re.sub(r'<i>(.*?)</i>', r'*\1*', text, flags=re.DOTALL)
    text = text.replace('<br/>', '\n').replace('<br>', '\n')
    text = text.replace('&nbsp;', ' ')
    text = text.replace('&ge;', '>=')
    text = text.replace('&le;', '<=')
    text = text.replace('&asymp;', '~=')
    text = text.replace('&times;', 'x')
    text = text.replace('&plusmn;', '+/-')
    text = text.replace('&isin;', 'in')
    text = text.replace('&forall;', 'for all')
    text = text.replace('&rarr;', '->')
    text = text.replace('&larr;', '<-')
    text = text.replace('&bull;', '*')
    text = text.replace('&alpha;', 'alpha')
    text = text.replace('&beta;', 'beta')
    text = text.replace('&lambda;', 'lambda')
    text = text.replace('&mu;', 'mu')
    text = text.replace('&rho;', 'rho')
    text = text.replace('&pi;', 'pi')
    text = text.replace('&sum;', 'sum')
    text = html.unescape(text)
    # Remove any stray XML/HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    return text.strip()

def table_to_markdown(table):
    lines = []
    # table._cellvalues contains the data (strings or Paragraphs)
    raw_data = table._cellvalues
    if not raw_data:
        return ""
    
    # Process cells
    grid = []
    for row in raw_data:
        grid_row = []
        for cell in row:
            if isinstance(cell, Paragraph):
                txt = clean_html(cell.text)
            elif isinstance(cell, str):
                txt = clean_html(cell)
            else:
                txt = str(cell)
            txt = txt.replace('\n', ' ').replace('|', '\\|')
            grid_row.append(txt)
        grid.append(grid_row)
    
    if not grid:
        return ""
    
    # Header
    header = "| " + " | ".join(grid[0]) + " |"
    sep = "| " + " | ".join(["---"] * len(grid[0])) + " |"
    lines.append(header)
    lines.append(sep)
    
    for row in grid[1:]:
        # Pad row if shorter
        while len(row) < len(grid[0]):
            row.append("")
        lines.append("| " + " | ".join(row[:len(grid[0])]) + " |")
    
    return "\n".join(lines) + "\n"

def convert_thesis():
    styles = get_thesis_styles()
    flowables = []
    flowables.extend(build_preliminaries(styles))
    flowables.extend(build_chapters_1_and_2(styles))
    flowables.extend(build_chapters_3_and_4(styles))
    flowables.extend(build_chapters_5_and_6(styles))
    flowables.extend(build_chapters_7_and_8(styles))
    flowables.extend(build_chapter_9_and_refs(styles))

    md_lines = []
    
    # Metadata Frontmatter
    md_lines.append("# B.TECH CAPSTONE THESIS: PEERVAULT AI")
    md_lines.append("**Browser-Native End-to-End Encrypted P2P LAN File Transfer & Local Intelligence Architecture**\n")
    md_lines.append("> **Institution:** National Institute of Technology (NIT), Agartala  ")
    md_lines.append("> **Department:** Department of Computer Science & Engineering  ")
    md_lines.append("> **Degree:** Bachelor of Technology (B.Tech) in Computer Science & Engineering (Class of 2027)  ")
    md_lines.append("> **Academic Session:** 2026-2027  ")
    md_lines.append("> **Project Group Members:**  ")
    md_lines.append("> 1. **Ram Pedapati** (Enrollment: 23UCS191)  ")
    md_lines.append("> 2. **Terli Jogiswara Prabhas** (Enrollment: 23UCS180)  ")
    md_lines.append("> 3. **Unnavada Nikhilesh Kumar** (Enrollment: 23UCS177)  ")
    md_lines.append("> 4. **Sithalam Hari Krishna Sai Durga Prasad** (Enrollment: 23UCS178)  ")
    md_lines.append("> **Supervisor:** Dr. Awnish Kumar (Assistant Professor, CSE Dept., NIT Agartala)  ")
    md_lines.append("> **Co-Supervisor:** Dr. Prashant Bharadwaj (Assistant Professor, CSE Dept., NIT Agartala)  ")
    md_lines.append("> **Repository:** [https://github.com/ramcode-dev/peervault-ai](https://github.com/ramcode-dev/peervault-ai)  ")
    md_lines.append("> **Live Deployment:** [https://peervault-ai.onrender.com](https://peervault-ai.onrender.com)\n")
    md_lines.append("---\n")

    current_chap_num = ""

    for f in flowables:
        if isinstance(f, Paragraph):
            style_name = f.style.name
            raw_text = f.text
            clean_txt = clean_html(raw_text)

            if style_name == 'ChapNumber':
                current_chap_num = clean_txt
                continue

            if style_name == 'ChapTitle':
                if current_chap_num:
                    md_lines.append(f"\n# {current_chap_num}: {clean_txt}\n")
                    current_chap_num = ""
                else:
                    md_lines.append(f"\n# {clean_txt}\n")
                continue

            if style_name == 'SecTitle':
                md_lines.append(f"\n## {clean_txt}\n")
                continue

            if style_name == 'SubSecTitle':
                md_lines.append(f"\n### {clean_txt}\n")
                continue

            if style_name == 'QTitle':
                md_lines.append(f"\n### {clean_txt}\n")
                continue

            if style_name == 'AnsText':
                md_lines.append(f"**Answer:** {clean_txt}\n")
                continue

            if style_name == 'Bullet':
                md_lines.append(f"* {clean_txt}")
                continue

            if style_name == 'Callout':
                md_lines.append(f"> [!NOTE]\n> {clean_txt}\n")
                continue

            if style_name == 'CodeBlock':
                md_lines.append(f"```javascript\n{clean_txt}\n```\n")
                continue

            if style_name in ['CoverTitle', 'CoverInst', 'CoverDept', 'CoverSub', 'CoverFoot']:
                # Already captured in frontmatter
                continue

            if style_name == 'CoverMetaVal':
                continue

            if style_name in ['Body', 'BodyBold', 'TOCChap', 'TOCSec', 'TOCPage', 'TableHead', 'TableCell', 'TableCellBold']:
                md_lines.append(f"{clean_txt}\n")
                continue

            md_lines.append(f"{clean_txt}\n")

        elif isinstance(f, Table):
            md_table = table_to_markdown(f)
            md_lines.append(md_table)

        elif isinstance(f, HRFlowable):
            md_lines.append("\n---\n")

        elif isinstance(f, PageBreak):
            # Page breaks don't need markdown tags
            pass

        elif isinstance(f, Spacer):
            pass

    full_md = "\n".join(md_lines)
    # Deduplicate excessive newlines
    full_md = re.sub(r'\n{3,}', '\n\n', full_md)

    with open('THESIS.md', 'w', encoding='utf-8') as f:
        f.write(full_md)
    with open('PROJECT_REPORT.md', 'w', encoding='utf-8') as f:
        f.write(full_md)

    print(f"Export Complete!")
    print(f"THESIS.md size: {len(full_md)} characters, {len(full_md.split())} words")
    print(f"Lines count: {len(full_md.splitlines())}")

if __name__ == '__main__':
    convert_thesis()
