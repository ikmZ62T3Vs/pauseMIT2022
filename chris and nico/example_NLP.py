from rake_nltk import Rake
import nltk

rake_nltk_var = Rake()
text = """Structures store values of different types, in fields. Fields are given names; they are referred to as structurename.fieldname using the dot operator"""
r = Rake()

# Extraction given the text.
print(r.extract_keywords_from_text(text))



# To get keyword phrases ranked highest to lowest.
print(r.get_ranked_phrases())
