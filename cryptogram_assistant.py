import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def quitCheck(input):
    if input == 'QUIT':
        os._exit(0)
    return


def intro():
    cls()
    print('''
Welcome to the Cryptogram Assistant!!
You can enter a Cryptogram Puzzle and this program will help manage your progress

A couple of things to keep in mind:
You can stop at any time by typing 'QUIT'
This program will make sure you don't use the same letter more than once
If you do want to use a letter you've already used, you will have to replace it before you can use it again
You can restore a letter back to a blank entry by using any non alpha character as the replacement letter
If you enter multiple letters, the program will use the first letter you entered
    ''')
    ready = False
    while not ready:
        start = input('\nAre you ready to begin?\n').upper()
        quitCheck(start)
        if start == 'Y' or start == 'YES':
            ready = True
    return True



def getCryptogram():
    ready = False
    while not ready:
        cls()
        puzzle = input('Please enter the Cryptogram puzzle:\n').upper()
        quitCheck(puzzle)
        correct = input(f'\nIs this correct?\n{puzzle}\n').upper()
        quitCheck(correct)
        if correct == 'Y' or correct == 'YES':
            ready = True
    return list(puzzle)


def getBlanks(puzzle):
    convert_letters_to_blanks = []
    for letter in puzzle:
        if letter == ' ':
            convert_letters_to_blanks.append(' ')
        elif letter == "'":
            convert_letters_to_blanks.append("'")
        elif letter == ',':
            convert_letters_to_blanks.append(',')
        elif letter == '.':
            convert_letters_to_blanks.append('.')
        elif letter == '?':
            convert_letters_to_blanks.append('?')
        elif letter == '!':
            convert_letters_to_blanks.append('!')
        else:
            convert_letters_to_blanks.append('_')
    return convert_letters_to_blanks


# later - find the indexes of the spaces and print puzzle on multiple lines
def printBoard(blanks, puzzle):
    cls()
    print(f"{' '.join(blanks)}\n")
    print(' '.join(puzzle))


def replaceLetter(solution, puzzle):
    letter = input('\nWhich letter would you like to change?\n').upper()
    quitCheck(letter)
    letter = letter[0]
    if letter.isalpha():
        new_letter = input('What letter would you like to replace it with?\n').upper()
        quitCheck(new_letter)
        new_letter = new_letter[0]
        if not new_letter.isalpha():
            new_letter = '_'
        elif new_letter in solution:
            print("You've used this letter already\nPlease replace letter before using again\n")
            new_letter = '_'
        for i in range(len(puzzle)):
            if puzzle[i] == letter:
                solution[i] = new_letter
    printBoard(solution, puzzle)
    return solution


def checkSolution(solution):
    correct = input(f"\nIs {''.join(solution)} the solution?\n").upper()
    quitCheck(correct)
    if correct == 'Y' or correct == 'YES':
        return True
    return False


def playAgain():
    again = input('\nDo you want to do another puzzle?\n').upper()
    if again == 'Y' or again == 'YES':
        getStarted()
    else:
        os._exit(0)


def getStarted():
    intro()
    cls()
    puzzle = getCryptogram()
    blanks = getBlanks(puzzle)
    printBoard(blanks, puzzle)
    solved = False
    while not solved:
        solution = blanks
        solution = replaceLetter(solution, puzzle)
        if '_' not in solution:
            correct = checkSolution(solution)
            if correct:
                print('\nAwesome!!')
                solved = True
            else:
                cls()
                printBoard(solution, puzzle)
    playAgain()

getStarted()