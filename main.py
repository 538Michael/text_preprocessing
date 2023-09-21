import codecs
import os
import re
from time import time
from config import config


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
            step = word
            if config["cleanup"]["special_characters"]:
                step = remove_special_characters(step)
                if step is None:
                    trash_words.append((word, "1"))
                    continue

            if config["cleanup"]["short_words"]:
                step = remove_short_words(step)
                if step is None:
                    trash_words.append((word, "2"))
                    continue

            if config["cleanup"]["accents"]:
                step = remove_accents(step)
                if step is None:
                    continue

            if config["cleanup"]["hyphens"]:
                step = remove_hyphens(step)
                if step is None:
                    continue

            if config["cleanup"]["stop_words"]:
                step = remove_stop_words(step)
                if step is None:
                    trash_words.append((word, "5"))
                    continue

            step_lower = step.lower()

            if config["verify"]["gentile"]:
                sixth_step = check_if_gentile(step_lower)
                if sixth_step is not None:
                    for sixth_step_word in sixth_step:
                        final_words.append((word, sixth_step_word))
                    continue

            if config["verify"]["substantive"]:
                seventh_step = check_if_substantive(step_lower)
                if seventh_step is not None:
                    final_words.append((word, seventh_step))
                    continue

            if config["verify"]["verb"]:
                eighth_step = check_if_verb(step_lower)
                if eighth_step is not None:
                    final_words.append((word, eighth_step))
                    continue

            if config["verify"]["archaic"]:
                ninth_step = check_if_archaic(step_lower)
                if ninth_step is not None:
                    final_words.append((word, ninth_step))
                    continue

            if config["verify"]["first_name"]:
                tenth_step = check_if_first_name(step)
                if tenth_step is not None:
                    final_words.append((word, tenth_step))
                    continue

            leftover_words.append((word, step_lower))

        save_file(file_name, "final", final_words, debug=debug_mode)
        save_file(file_name, "leftover", leftover_words, debug=debug_mode)
        save_file(file_name, "trash", trash_words, debug=debug_mode)

        print(f"Elapsed time: {time() - start_time} seconds")
