import os
import random


def load_word_list(filename: str) -> list:
    with open(filename, "r") as f:
        word_list_2 = []
        while True:
            this_word = f.readline()

            if len(this_word) == 0:
                # end of file - stop here
                break
            else:

                this_word_cleaned = this_word.strip()

                if this_word_cleaned:
                    word_list_2.append(this_word_cleaned)

    return word_list_2

def get_filename(filename:str) -> str:
    return os.path.join(os.path.dirname(__file__), filename)

def pick_word() -> str:
    file_path = get_filename("word_list_hangman")
    word_list = load_word_list(file_path)
    the_word = random.choice(word_list)
    return the_word
