with open("./TXTs/PEQUENAS.txt", "r", encoding="utf-8") as file:
    small_words = [word.strip() for word in file.readlines()]
    file.close()

with open("./TXTs/conectivos.txt", "r", encoding="utf-8") as file1, open(
    "./TXTs/aurelio_conectivos.txt", "r", encoding="utf-8"
) as file2:
    stop_words1 = [word.strip() for word in file1.readlines()]
    stop_words2 = [word.strip() for word in file2.readlines()]
    stop_words = stop_words1 + stop_words2
    file1.close()
    file2.close()

with open("./TXTs/plural_substantivos.txt", "r", encoding="utf-8") as file:
    substantives = [word.strip().split(" ") for word in file.readlines()]
    file.close()

with open("./TXTs/Verbos_conjugados.txt", "r", encoding="utf-8") as file:
    verbs = [word.strip().split(" ") for word in file.readlines()]
    file.close()

with open("./TXTs/nomes_proprios.txt", "r", encoding="utf-8") as file:
    first_names = [word.strip().split(" ") for word in file.readlines()]
    file.close()

with open("./TXTs/arcaismos.txt", "r", encoding="utf-8") as file:
    archaisms = [word.strip().split(" ") for word in file.readlines()]
    file.close()
