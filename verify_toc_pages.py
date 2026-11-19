# verify_toc_pages.py
from reportlab.platypus import Flowable, Paragraph, SimpleDocTemplate
from thesis_styles import get_thesis_styles, LaTeXNumberedCanvas
from thesis_prelims import build_preliminaries
from thesis_ch1_ch2 import build_chapters_1_and_2
from thesis_ch3_ch4 import build_chapters_3_and_4
from thesis_ch5_ch6 import build_chapters_5_and_6
from thesis_ch7_ch8 import build_chapters_7_and_8
from thesis_ch9_refs import build_chapter_9_and_refs

class PageTracker(Flowable):
    def __init__(self, key, registry):
        super().__init__()
        self.key = key
        self.registry = registry
    def draw(self):
        self.registry[self.key] = self.canv._pageNumber

def verify():
    reg = {}
    styles = get_thesis_styles()
    story = []
    
    def wrap(flist):
        out = []
        for f in flist:
            if isinstance(f, Paragraph):
                t = f.text.replace('<b>', '').replace('</b>', '').strip()
                if 'CHAPTER ' in t or 'REFERENCES' in t or 'APPENDIX ' in t:
                    out.append(PageTracker(t[:32], reg))
            out.append(f)
        return out

    story.extend(build_preliminaries(styles))
    story.extend(wrap(build_chapters_1_and_2(styles)))
    story.extend(wrap(build_chapters_3_and_4(styles)))
    story.extend(wrap(build_chapters_5_and_6(styles)))
    story.extend(wrap(build_chapters_7_and_8(styles)))
    story.extend(wrap(build_chapter_9_and_refs(styles)))

    doc = SimpleDocTemplate('verify_temp.pdf', leftMargin=54, rightMargin=54, topMargin=54, bottomMargin=54)
    doc.build(story, canvasmaker=LaTeXNumberedCanvas)
    
    for k, v in sorted(reg.items(), key=lambda x: x[1]):
        print(f'{k:35} -> Page {v}')

if __name__ == '__main__':
    verify()
