import codecs
import os
import re
from time import time

from lib import *

final_words = []
trash_words = []
leftover_words = []

path = "./txt_to_be_processed"

for file_name in os.listdir(path):
    with codecs.open(
        f"{path}/{file_name}", "r", encoding="utf-8-sig", errors="ignore"
    ) as file:
        text = file.read()
        # \(\)\[\]\{\}
        delimiters = r"[\s.?!,:;\'\"…]"
        words = re.split(delimiters, text)
        words = [word for word in words if word]

        print(file_name)

        start_time = time()

        for word in words:

            first_step = remove_special_characters(word)
            if first_step is None:
                if first_step:
                    trash_words.append((word, "1"))
                continue

            second_step = check_if_short_word(first_step)
            if second_step is None:
                trash_words.append((word, "2"))
                continue

            third_step = remove_accents(second_step)
            if third_step is None:
                continue

            fourth_step = remove_stop_words(third_step)
            if fourth_step is None:
                trash_words.append((word, "4"))
                continue

            if fourth_step[0].isupper():
                final_words.append((word, fourth_step))
                continue

            fifth_step = check_if_first_name(fourth_step)
            if fifth_step is not None:
                final_words.append((word, fifth_step))
                continue

            fourth_step = fourth_step.lower()

            sixth_step = check_if_substantive(fourth_step)
            if sixth_step is not None:
                final_words.append((word, sixth_step))
                continue

            seventh_step = check_if_verb(fourth_step)
            if seventh_step is not None:
                final_words.append((word, seventh_step))
                continue

            eighth_step = check_if_archaic(fourth_step)
            if eighth_step is not None:
                final_words.append((word, eighth_step))
                continue

            leftover_words.append((word, fourth_step))

        save_file(file_name, "final_words", final_words)
        save_file(file_name, "leftover_words", leftover_words)
        save_file(file_name, "trash_words", trash_words)

        print(f"Elapsed time: {time() - start_time} seconds")
