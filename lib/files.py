from unidecode import unidecode

from lib.util import *

gentiles = Trie()

with open("./txts/pequenas.txt", "r", encoding="utf-8-sig") as file:
    small_words = Trie()
    for word in file.readlines():
        word = word.strip()
        small_words.insert(word, word)
    file.close()

with open("./txts/conectivos.txt", "r", encoding="utf-8-sig") as file:
    stop_words = Trie()
    for word in file.readlines():
        word = word.strip()
        stop_words.insert(word, word)
    file.close()

with open("./txts/plural_substantivos.txt", "r", encoding="utf-8-sig") as file:
    substantives = Trie()
    for words in file.readlines():
        words = words.strip().split(" ")
        for word in words:
            substantives.insert(unidecode(word), words[0])
    file.close()

with open("./txts/verbos_conjugados.txt", "r", encoding="utf-8-sig") as file:
    verbs = Trie()
    for words in file.readlines():
        words = words.strip().split(" ")
        for word in words:
            verbs.insert(unidecode(word), words[0])
    file.close()

with open("./txts/nomes_proprios.txt", "r", encoding="utf-8-sig") as file:
    first_names = Trie()
    for words in file.readlines():
        words = words.strip().split(" ")
        for word in words:
            first_names.insert(word, words[0])
    file.close()

with open("./txts/arcaismos.txt", "r", encoding="utf-8-sig") as file:
    archaisms = Trie()
    for words in file.readlines():
        words = words.strip().split(" ")
        for word in words:
            archaisms.insert(unidecode(word), words[0])
    file.close()

with open("./txts/suffixes.txt", "r", encoding="utf-8-sig") as file:
    suffixes = [word.strip() for word in file.readlines()]
    file.close()

with open("./txts/gentilicos_brasileiros.txt", "r", encoding="utf-8-sig") as file:
    for words in file.readlines():
        words = words.strip().split(";")
        for word in words:
            gentiles.insert(unidecode(word), words[:3])
    file.close()

with open("./txts/gentilicos_mundiais.txt", "r", encoding="utf-8-sig") as file:
    for words in file.readlines():
        words = words.strip().split(";")
        for word in words:
            gentiles.insert(unidecode(word), words[:3])
    file.close()
