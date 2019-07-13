# simple_demo.py

from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

title = "My PDF DEMO!"
text = "This is my attempt to create pdf using python library."
text2 = "Next line to try."

pdf.cell(200, 10, txt=title, ln=1, align="C")
pdf.cell(200, 10, txt=text, ln=2, align="L")
pdf.cell(200, 10, txt=text2, ln=3, align="L")

pdf.output("demo.pdf")
