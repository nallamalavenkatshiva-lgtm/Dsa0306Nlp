import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('punkt_tab')      # Add this line
nltk.download('wordnet')
nltk.download('omw-1.4')        # Optional but recommended

text = "The boys are playing football happily."

tokens = word_tokenize(text)

lemmatizer = WordNetLemmatizer()

print("Morphological Analysis:")
for word in tokens:
    print(word, "->", lemmatizer.lemmatize(word))