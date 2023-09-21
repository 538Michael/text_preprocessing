import re

from unidecode import unidecode

from .files import *

translation_table = str.maketrans(
    "", "", "\u0300-\u0305\u0307-\u036F\u1AB0-\u1AFF\u1DC0-\u1DFF"
)

# from spacy.lang.pt.stop_words import STOP_WORDS


def remove_special_characters(word: str) -> str:
    if word is None:
        return None

    # word = word.replace("ç", "c").replace("Ç", "c")
    word = re.sub(r"[^a-zA-Z-\u00C0-\u017F]", "", word)

    if len(word) == 0:
        return None

    return word


def check_if_short_word(word: str) -> bool:
    if word is None or len(word) == 0:
        return None

    if word == "pai":
        print(small_words.search(word.lower()))

    if len(word) <= 3 and not small_words.search(word.lower()):
        return None

    return word


def remove_accents(word: str) -> str:
    if word is None or len(word) == 0:
        return None

    return unidecode(word)


def check_hyphens(word: str) -> list:
    if word is None or len(word) == 0:
        return None

    try:
        index = word.index("-")
        rindex = word.rindex("-")
    except ValueError:
        return word

    first_check = index in [0, 1]
    second_check = rindex in [len(word) - 1, len(word) - 2]

    if first_check and second_check:
        word = word[(index + 1) : rindex]
    elif first_check:
        word = word[(index + 1) :]
    elif second_check:
        word = word[:rindex]

    word_lower = word.lower()

    for suffix in ["-" + suffix for suffix in suffixes]:
        if word_lower.endswith(suffix):
            word = word[: -len(suffix)]

    pattern = "|".join(map(re.escape, ["-" + suffix + "-" for suffix in suffixes]))
    match = re.search(pattern, word_lower)
    if match:
        word = word[: match.start()]

    if len(word) == 0:
        return None

    return word


def remove_stop_words(word: str) -> str:
    if word is None or len(word) == 0:
        return None

    word_lower = word.lower()

    if not stop_words.search(word_lower):
        if word[0].isupper():
            return word_lower.capitalize()
        else:
            return word

    if len(word) == 0:
        return None

    return None


def check_if_substantive(word: str) -> str:
    if word is None or len(word) == 0:
        return None

    result = substantives.search(word)

    if result != False:
        return result

    return None


def check_if_verb(word: str) -> str:
    if word is None or len(word) == 0:
        return None

    result = verbs.search(word)

    if result != False:
        return result

    return None


def check_if_archaic(word: str) -> str:
    if word is None:
        return None

    result = archaisms.search(word)

    if result != False:
        return result

    return None


def check_if_first_name(word: str) -> str:
    if word is None or len(word) == 0:
        return None

    if word[0].isupper() or first_names.search(word.lower()) != False:
        return word.title()

    return None


def check_if_gentile(word: str) -> str:
    if word is None:
        return None

    result = gentiles.search(word)

    if result != False:
        return result

    return None
