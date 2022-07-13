# Pre-requisite
# Install "pip install pyqrcode" library
# Install "pip install pypng" library
import pyqrcode
import png

# String which represents the QR Code
s = "www.google.in"

# Generate QR Code
url = pyqrcode.create(s)
# Geerate Images in images folder
url.svg("./images/myqr.svg", scale=8)
url.png("./images/myqr.png", scale=6)

print("Done")
