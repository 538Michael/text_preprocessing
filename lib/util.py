import os


def save_file(
    file_name: str, folder_name: str, words: list, debug: bool = False
) -> None:
    path = "./output/release"

    os.makedirs(f"{path}/{folder_name}", exist_ok=True)

    file_name = os.path.splitext(file_name)[0]

    with open(f"{path}/{folder_name}/{file_name}.txt", "w", encoding="utf-8") as file:
        for string in sorted(
            list(set(string[0 if folder_name == "trash" else 1] for string in words)),
            key=lambda x: x.lower(),
        ):
            file.write(f"{string}\n")

        file.close()

    if debug:
        debug_path = "./output/debug"

        os.makedirs(f"{debug_path}/{file_name}", exist_ok=True)

        with open(
            f"{debug_path}/{file_name}/{folder_name}.txt", "w", encoding="utf-8"
        ) as file:
            for string in sorted(
                list(set(tuple(string) for string in words)), key=lambda x: x[1].lower()
            ):
                file.write(f"{string[0]}\t{string[1]}\n")

            file.close()


class Trie:
    class TrieNode:
        def __init__(self):
            self.child = [0] * 256
            self.isleaf = 0
            self.value = None

    def __init__(self):
        self.trie = [self.TrieNode()]

    def insert(self, s, v):
        i = 0
        for x in s:
            c = ord(x) - ord("a")
            if self.trie[i].child[c] == 0:
                self.trie[i].child[c] = len(self.trie)
                self.trie.append(self.TrieNode())
            i = self.trie[i].child[c]
        self.trie[i].isleaf += 1
        self.trie[i].value = v

    def search(self, s):
        i = 0
        for x in s:
            c = ord(x) - ord("a")
            if self.trie[i].child[c] != 0:
                i = self.trie[i].child[c]
            else:
                return False
        if self.trie[i].isleaf == 0:
            return False
        return self.trie[i].value
