# Pre-requisite
# Install "pip install FPDF"
import glob

from fpdf import FPDF
pdf = FPDF()
# Imagelist
path = "images/"
imagelist = glob.glob(path + '/**/*.png', recursive=True)

for image in imagelist:
    pdf.add_page()
    pdf.image(image)
    pdf.output("./Pdf/mypdf.pdf", "F")
