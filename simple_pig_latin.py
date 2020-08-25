import string


def pig_word(w):
    return f"{w[1:]}{w[0]}ay" if w not in string.punctuation else w


def pig_it(text):
    return " ".join([pig_word(w) for w in text.split(" ")])