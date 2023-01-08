import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def getCryptogram():
    ready = False
    while ready == False:
        puzzle = input('Please enter the Cryptogram puzzle:\n')
        correct = input(f'\nIs this correct?\n{puzzle}\n').lower()
        if correct == 'y' or correct == 'yes':
            ready = True
    return puzzle

def getBlanks(puzzle):
    convert_letters_to_blanks = []
    for letter in puzzle:
        if letter == ' ':
            convert_letters_to_blanks.append(' ')
        else:
            convert_letters_to_blanks.append('_')
    blanks = ' '.join(convert_letters_to_blanks)
    return blanks


# later - find the indexes of the spaces and print puzzle on multiple lines
def printBoard(blanks, puzzle):
    cls()
    print(blanks)
    print(' '.join(puzzle))


def getStarted():
    cls()
    puzzle = getCryptogram()
    blanks = getBlanks(puzzle)
    printBoard(blanks, puzzle)


getStarted()