from game import pick_word, play_hangman

if __name__ == '__main__':
    the_word = pick_word()
    print(the_word)
    play_hangman(the_word) #Sender variabelen hentet i linje 4 som the word

