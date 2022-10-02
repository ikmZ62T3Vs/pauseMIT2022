
from PIL import Image
from pytesseract import pytesseract
from rake_nltk import Rake
import nltk
import pandas as pd

#Define path to tessaract.exe
path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#Define path to image
path_to_image = "C://Users//chris//Downloads//Educational Slides.jpg"

#Point tessaract_cmd to tessaract.exe
pytesseract.tesseract_cmd = path_to_tesseract

#Open image with PIL
img = Image.open(path_to_image)

#Extract text from image
text = pytesseract.image_to_string(img)
text = pd.read_csv('extract.csv', index_col=0)
cast_list = list(text.index[0:])
cast_list.sort()

print(text)



rake_nltk_var = Rake()

r = Rake()

# Extraction given the text.
print(r.extract_keywords_from_text(text))




# To get keyword phrases ranked highest to lowest.
print(r.get_ranked_phrases())
