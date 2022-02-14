# Hangman Game (Jogo da Forca)
# Object Oriented Programming (Programação Orientada a Objetos)

# Import
import random

# Board (Tabuleiro)
board = ['''
>>>>>>>>>>HANGMAN<<<<<<<<<<
+---+
|   |
    |
    |
    |
    |
=========''', '''
+---+
|   |
O   |
    |
    |
    |
=========''', '''
+---+
|   |
O   |
|   |
    |
    |
=========''', '''
 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''
 +---+
 |   |
 0   |
/|\  |
/ \  |
     |
=========''']


# Método para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))]


# Class the Hangman Game (Classe do Jogo da Forca)
class Hangman:

    # (Método Construtor)
    def __init__(self, word):
        self.word = word.strip()
        self.missed_letters = []
        self.guessed_letters = []

    # (Método que checa o estado atual de jogo)
    def checkGame(self):

        atual = 1

        for i in self.word:
            if i in self.guessed_letters:
                atual *= 1
            else:
                atual *= 0

        if len(self.missed_letters) == len(board) - 1:
            atual = 2

        return atual

    #  (Método que imprime o estado atual de jogo)
    def currentState(self):

        atual = self.checkGame()

        if atual == 1:

            print('Parabens ! Você Ganhou.')
            print('Palavra Correta: ', end='')
            [print(i, end=' ') for i in self.word]
            print('\n')

            return atual

        elif atual == 2:

            print(board[len(self.missed_letters)])
            print('Você Perdeu!')

            return atual

        else:

            print(board[len(self.missed_letters)])

            print('Letra errada:')
            [print(i, end=' ') for i in self.missed_letters]
            print('\n')

            print('Letra Certa:')
            [print(i, end=' ') for i in self.guessed_letters]
            print('\n')

            for i in self.word:
                if i in self.guessed_letters:
                    print(i, end=' ')
                else:
                    print('_', end=' ')

            return atual

    # Method that receives the inserted letter (Método que recebe a letra inserida)
    def inputLetter(self, letter):

        letter = letter.upper()
        list_letter = self.missed_letters + self.guessed_letters

        if not letter in list_letter:

            if len(letter) > 1:
                print('Entre como uma nova Letra!')
            elif letter in self.word:
                self.guessed_letters.append(letter)
                print('"{}" Letra Correta!'.format(letter))
            else:
                self.missed_letters.append(letter)
                print('"{}" Letra Errada!'.format(letter))

        else:
            print('Letra já inserida, tente novamente')


# Method Main - Execution the game (Método Main - Execução do jogo)
def main():
    game = Hangman(rand_word().upper())
    game.currentState()
    print('\n')

    while game.checkGame() == 0:
        new_letter = input('| Nova  Letra: ')
        game.inputLetter(new_letter)
        game.currentState()

    print('Fim do Jogo')


# Starting (Iniciando)
if __name__ == "__main__":
    main()