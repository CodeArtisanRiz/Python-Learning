# Pre-requisite
# Install "pip install langdetect"

from langdetect import detect
text = input("Enter text in any language: ")
print(detect(text))