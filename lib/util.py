import os


def save_file(folder_name: str, file_name: str, words: list) -> None:

    if not os.path.exists("./output"):
        os.makedirs("./output")

    folder_name = os.path.splitext(folder_name)[0]

    if not os.path.exists(f"./output/{folder_name}"):
        os.makedirs(f"./output/{folder_name}")

    with open(f"./output/{folder_name}/{file_name}.txt", "w", encoding="utf-8") as file:
        for string in sorted(
            list(set(tuple(string) for string in words)), key=lambda x: x[1].lower()
        ):
            file.write(f"{string[0]}\t{string[1]}\n")
