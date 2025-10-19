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
            result += letter
        else:
            result += "_"
    return result

def get_user_guess(): #function to get input from the user, due to "input"
    guess = input("Guess a letter: ") #Input skrives inn manuelt i console

    if len(guess) > 1:
        return None
    return guess

def play_hangman(the_word):
    guessed_letters = []
    life = 3

    while life > 0:
        guess = get_user_guess()
        if guess is None:
            life -= 1
            print(f"Nice try you cheater! you lost one life, you have {life} lives left  - Guess only 1 letter!")
            continue


        if guess not in guessed_letters:
            guessed_letters.append(guess) #puts guessed letters into a guessed list

            current_state = hangman_word(the_word, guessed_letters)
            print(current_state)  # shows the current status for the user guesses

            if guess not in the_word:
                life -= 1 #number of lives - 1

                if life == 1:
                    print(f"wrong letter, only {life} life left")
                else: # if life is more or less than 1
                    print(f"wrong letter, {life} lives left")

                if life == 0:
                    print(f"You lost!")
                    break



            if "_" not in current_state:
                print("Congrats!") #when the word is complete
                break
        else:
            print("Are you stupid? This letter was already guessed")

