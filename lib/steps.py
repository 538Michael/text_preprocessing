import re

from unidecode import unidecode

from .files import *

# from spacy.lang.pt.stop_words import STOP_WORDS


# First step
def remove_special_characters(word: str) -> str:

    if word is None:
        return None

    word = word.replace("ç", "c").replace("Ç", "c")
    word = re.sub(r"[^a-zA-Z-\u00C0-\u017F]", "", word)

    return word


# Second step
def check_if_short_word(word: str) -> bool:

    if word is None:
        return None

    if len(word) <= 3 and not (word.lower() in small_words):
        return None

    return word


# Third step
def remove_accents(word: str) -> str:

    if word is None:
        return None

    return unidecode(word)


# Fourth step
def remove_stop_words(word: str) -> str:

    if word is None:
        return None

    if word.lower() not in stop_words:
        if word[0].isupper():
            return word.title()
        else:
            return word

    return None


# Fifth step
def check_if_first_name(word: str) -> str:

    if word is None:
        return None

    if word[0].isupper() or word.lower() in first_names:
        return word.title()

    return None


# Sixth step
def check_if_substantive(word: str) -> str:

    if word is None:
        return None

    for substantive in substantives:
        if word in substantive:
            return substantive[0]

    return None


# Seventh step
def check_if_verb(word: str) -> str:

    if word is None:
        return None

    for verb in verbs:
        if word in verb:
            return verb[0]

    return None


# Eighth step
def check_if_archaic(word: str) -> str:

    if word is None:
        return None

    for archaism in archaisms:
        if word in archaism:
            return archaism[1]

    return None
