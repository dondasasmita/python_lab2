import sys
from fpdf import FPDF


pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

title = sys.argv[1]
text = sys.argv[2]

pdf.cell(200, 10, txt=title, ln=1, align="C")
pdf.cell(200, 10, txt=text, ln=2, align="L")

pdf.output("demo.pdf")
