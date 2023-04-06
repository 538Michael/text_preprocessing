import codecs
import os
import re
from time import time

from lib import *

debug_mode = True

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

            first_step = check_hyphens(word)
            if first_step is None:
                continue

            second_step = remove_special_characters(first_step)
            if second_step is None:
                if second_step:
                    trash_words.append((word, "1"))
                continue

            third_step = check_if_short_word(second_step)
            if third_step is None:
                trash_words.append((word, "2"))
                continue

            fourth_step = remove_accents(second_step)
            if fourth_step is None:
                continue

            fifth_step = remove_stop_words(third_step)
            if fifth_step is None:
                trash_words.append((word, "4"))
                continue

            fifth_step_lower = fifth_step.lower()

            sixth_step = check_if_substantive(fifth_step_lower)
            if sixth_step is not None:
                final_words.append((word, sixth_step))
                continue

            seventh_step = check_if_verb(fifth_step_lower)
            if seventh_step is not None:
                final_words.append((word, seventh_step))
                continue

            eighth_step = check_if_archaic(fifth_step_lower)
            if eighth_step is not None:
                final_words.append((word, eighth_step))
                continue

            ninth_step = check_if_first_name(fifth_step)
            if ninth_step is not None:
                final_words.append((word, ninth_step))
                continue

            leftover_words.append((word, fifth_step))

        save_file(file_name, "final", final_words, debug=debug_mode)
        save_file(file_name, "leftover", leftover_words, debug=debug_mode)
        save_file(file_name, "trash", trash_words, debug=debug_mode)

        print(f"Elapsed time: {time() - start_time} seconds")
