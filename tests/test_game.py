import pytest
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


@pytest.mark.parametrize("the_word, guesses, expected_result",
                    [
                        ("sunny", [], "_____"),
                        ("sunny", ["l"], "_____"),
                        ("sunny", ["s"], "s____"),
                        ("sunny", ["l", "s"], "s____"),
                        ("sunny", ["s", "n"], "s_nn_"),
                    ])
def test_hangman_word(the_word: str, guesses: list, expected_result: str):
    assert hangman_word(the_word, guesses) == expected_result


