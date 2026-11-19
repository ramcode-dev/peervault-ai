# thesis_prelims.py
# Formats official preliminaries matching NIT Agartala Capstone Thesis Template
from reportlab.platypus import PageBreak, Image

def build_preliminaries(styles):
    flowables = []

    # 1. Cover Page 1
    flowables.append(Image("assets/rendered_prelims/cover_page_1.png", width=504, height=652))
    flowables.append(PageBreak())

    # 2. Cover Page 2
    flowables.append(Image("assets/rendered_prelims/cover_page_2.png", width=504, height=652))
    flowables.append(PageBreak())

    # 3. Dedicated To
    flowables.append(Image("assets/rendered_prelims/dedication_page.png", width=504, height=652))
    flowables.append(PageBreak())

    # 4. Report Approval for B.Tech
    flowables.append(Image("assets/rendered_prelims/approval_page.png", width=504, height=652))
    flowables.append(PageBreak())

    # 5. Declaration
    flowables.append(Image("assets/rendered_prelims/declaration_page.png", width=504, height=652))
    flowables.append(PageBreak())

    # 6. Certificate
    flowables.append(Image("assets/rendered_prelims/certificate_page.png", width=504, height=652))
    flowables.append(PageBreak())

    # 7. Acknowledgement
    flowables.append(Image("assets/rendered_prelims/acknowledgement_page.png", width=504, height=652))
    flowables.append(PageBreak())

    # 8. List of Figures
    flowables.append(Image("assets/rendered_prelims/list_of_figures.png", width=504, height=652))
    flowables.append(PageBreak())

    # 9. List of Tables
    flowables.append(Image("assets/rendered_prelims/list_of_tables.png", width=504, height=652))
    flowables.append(PageBreak())

    # 10. Abstract
    flowables.append(Image("assets/rendered_prelims/abstract_page.png", width=504, height=652))
    flowables.append(PageBreak())

    # 11, 12, 13. Table of Contents
    flowables.append(Image("assets/rendered_prelims/toc_page_1.png", width=504, height=652))
    flowables.append(PageBreak())
    flowables.append(Image("assets/rendered_prelims/toc_page_2.png", width=504, height=652))
    flowables.append(PageBreak())
    flowables.append(Image("assets/rendered_prelims/toc_page_3.png", width=504, height=652))
    flowables.append(PageBreak())

    return flowables
