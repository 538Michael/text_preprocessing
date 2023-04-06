with open("./txts/pequenas.txt", "r", encoding="utf-8-sig") as file:
    small_words = [word.strip() for word in file.readlines()]
    file.close()

with open("./txts/conectivos.txt", "r", encoding="utf-8-sig") as file:
    stop_words = [word.strip() for word in file.readlines()]
    file.close()

with open("./txts/plural_substantivos.txt", "r", encoding="utf-8-sig") as file:
    substantives = [word.strip().split(" ") for word in file.readlines()]
    file.close()

with open("./txts/verbos_conjugados.txt", "r", encoding="utf-8-sig") as file:
    verbs = [word.strip().split(" ") for word in file.readlines()]
    file.close()

with open("./txts/nomes_proprios.txt", "r", encoding="utf-8-sig") as file:
    first_names = [word.strip().split(" ") for word in file.readlines()]
    file.close()

with open("./txts/arcaismos.txt", "r", encoding="utf-8-sig") as file:
    archaisms = [word.strip().split(" ") for word in file.readlines()]
    file.close()
