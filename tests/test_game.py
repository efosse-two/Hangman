from game import load_word_list, hangman_word
import os

def get_filename(filename:str) -> str:
    return os.path.join(os.path.dirname(__file__), filename)

def test_load_word_list():
    file_path = get_filename("test_word_list_1")
    assert load_word_list(file_path) == ["cat", "dog", "fish"]


def test_word_list_2():
    file_path = get_filename("test_word_list_2")


    assert load_word_list(file_path) == ["mouse", "monkey"]



def test_hangman_word():
    assert hangman_word("sunny", []) == "_____"
    assert hangman_word("sunny", ["l"]) == "_____"
    assert hangman_word("sunny", ["s"]) == "s____"
    assert hangman_word("sunny", ["l", "s"]) == "s____"
    assert hangman_word("sunny", ["s", "n"]) == "s_nn_"
