def pluralize(noun):
    if noun.endswith(("s", "x", "z", "ch", "sh")):
        return noun + "es"

    elif noun.endswith("y") and noun[-2] not in "aeiou":
        return noun[:-1] + "ies"

    else:
        return noun + "s"

# Test words
words = ["cat", "bus", "box", "baby", "church", "boy"]

for word in words:
    print(f"{word} -> {pluralize(word)}")