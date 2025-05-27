from weasyprint import HTML

html = HTML(string='<h1 style="color:red">WeasyPrint is working!</h1>')
html.write_pdf("test_output.pdf")