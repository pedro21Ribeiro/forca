import random
from words import words
import string

def ValidWords():
    word = random.choice(words).upper()
    while '-' in word or ' ' in word:
        word = random.choice(words).upper()

    return word

def hangman():
    word = ValidWords()
    wordLetters = set(word)
    alphabet = set(string.ascii_uppercase)
    usedletters = set()
    lives = 6

    while len(wordLetters) > 0 and lives > 0:
        print('estas letras já foram ultilizadas: ', ' '.join(usedletters) + '\n')
        # i is a letter
        print('ainda restam', lives,'tentativas')
        lista = [i if i in usedletters else '-' for i in word]
        print('palavra: ', ' '.join(lista))
        
        userGuess = input('Escolha uma letra:   ')
        userGuess = userGuess.upper()
        if userGuess in alphabet - usedletters:
            usedletters.add(userGuess)
            if userGuess in wordLetters:
                wordLetters.remove(userGuess)
            else:
                lives = lives -1
                print('letra errada')

        elif userGuess in usedletters:
            print('essa letra já foi usada\n')
        else:
            print('charactere invalido, favor usar somente letras \n')
    if lives == 0:
        print('voce perdeu')
    else:
        print('parabéns voce acerteou a palavra', word)
hangman()
