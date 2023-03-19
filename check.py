with open("originais/Unitario_1903_04_0003_final.txt", "r") as f1:
    words1 = [word.strip() for word in f1.readlines()]

with open("txt_processados/Unitario_1903_04_0003_final.txt", "r") as f1:
    words2 = [word.strip().split()[1] for word in f1.readlines()]

for word in words1:
    if not word in words2:
        print(word)
