from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = [
    "playing",
    "played",
    "plays",
    "running",
    "runner",
    "studies",
    "studying",
    "easily",
    "fairly"
]

print("Word\t\tStem")

for word in words:
    print(f"{word}\t\t{ps.stem(word)}")