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


def hangman_word (the_word: str, guessed_letters: list) -> str:
    result = ""
    for letter in the_word:
        if letter in guessed_letters:
            result = result + letter
        else:
            result = result + "_"
    return result

def get_user_guess(): #function to get input from the user
    guess = input("Guess the letter: ") #Input skrives inn manuelt
    return guess

def play_hangman(the_word):
    guessed_letters = []

    while True:
        print(hangman_word(the_word, guessed_letters)) #shows the current status for the user guesses

        guess = get_user_guess()

        if guess not in guessed_letters:
            guessed_letters.append(guess) #puts guessed letters into a guessed list

            if "_" not in hangman_word(the_word, guessed_letters):
                print(hangman_word(the_word, guessed_letters)) #prints the current state of the guesses
                print("Congrats!") #when the word is complete
                break




