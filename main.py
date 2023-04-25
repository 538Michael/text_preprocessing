import codecs
import os
import re
from time import time

from lib import *

debug_mode = True

path = "./txt_to_be_processed"

for file_name in os.listdir(path):
    with codecs.open(
        f"{path}/{file_name}", "r", encoding="utf-8-sig", errors="ignore"
    ) as file:
        final_words = []
        trash_words = []
        leftover_words = []

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

            fourth_step = check_hyphens(third_step)
            if fourth_step is None:
                continue

            fifth_step = remove_stop_words(fourth_step)
            if fifth_step is None:
                trash_words.append((word, "5"))
                continue

            fifth_step_lower = fifth_step.lower()

            sixth_step = check_if_gentile(fifth_step_lower)
            if sixth_step is not None:
                for sixth_step_word in sixth_step:
                    final_words.append((word, sixth_step_word))
                continue

            seventh_step = check_if_substantive(fifth_step_lower)
            if seventh_step is not None:
                final_words.append((word, seventh_step))
                continue

            eighth_step = check_if_verb(fifth_step_lower)
            if eighth_step is not None:
                final_words.append((word, eighth_step))
                continue

            ninth_step = check_if_archaic(fifth_step_lower)
            if ninth_step is not None:
                final_words.append((word, ninth_step))
                continue

            tenth_step = check_if_first_name(fifth_step)
            if tenth_step is not None:
                final_words.append((word, tenth_step))
                continue

            leftover_words.append((word, fifth_step))

        save_file(file_name, "final", final_words, debug=debug_mode)
        save_file(file_name, "leftover", leftover_words, debug=debug_mode)
        save_file(file_name, "trash", trash_words, debug=debug_mode)

        print(f"Elapsed time: {time() - start_time} seconds")
