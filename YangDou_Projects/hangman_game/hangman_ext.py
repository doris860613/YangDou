"""
File: hangman.py
Name: Doris
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    This program is the classic letter guessing game called Hangman.
    """
    ans = random_word()
    guessing(ans)


def guessing(ans):
    """
    :param ans: str, a random English word.
    Player first see a dashed word, trying to figure the correct word by inputting
    one letter each round.
    If the letter in the word is guessed, show the updated word on the console.
    Player has N_TURNS chances to try and win this game.
    """
    old_guess = '-' * len(ans)
    n = N_TURNS
    print('THe word looks like ' + old_guess)
    print('You have ' + str(n) + ' wrong guesses left.')
    seven()  # Show the image on the console according to the number of player's chances.
    while True:
        input_ch = input('Your guess: ').upper()  # Cause this program is case-insensitive.
        guess = ''
        if input_ch in ans:
            print('You are correct!')
            for i in range(len(ans)):
                ch = ans[i]
                old = old_guess[i]
                if input_ch == ch:
                    guess += ch
                else:
                    guess += old
            old_guess = guess
            if guess != ans:
                print('The word looks like ' + old_guess)
                print('You have ' + str(n) + ' wrong guesses left.')
                # Show the image on the console according to the number of player's chances.
                if n == 7:
                    seven()
            else:
                break
        elif not input_ch.isalpha() or len(input_ch) != 1:
            # If the player doesn't input English alphabet or input more than one letter.
            print('Illegal format.')
        else:
            print('There is no ' + input_ch + '\'s in the word.')
            if n != 0:
                # If the letter not in the word, one less chance to guess the word.
                n -= 1
            # Show the image on the console according to the number of player's chances.
            if n == 6:
                six()
            elif n == 5:
                five()
            elif n == 4:
                four()
            elif n == 3:
                three()
            elif n == 2:
                two()
            elif n == 1:
                one()
            else:
                break
            print('The word looks like ' + old_guess)
            print('You have ' + str(n) + ' wrong guesses left.')
    if n == 0:
        # Show the image on the console according to the number of player's chances.
        zero()
        print('You are completely hung : (')
        print('The word was: ' + ans)
    else:
        print('You win!!')
        print('The word was: ' + ans)


def seven():
    """
    When the player has 7 chances, print only a gallows on the console.
    """
    print('　' + '＿＿＿＿＿')
    print('|/　')
    print('| 　')
    print('|　　 ')
    print('|')
    print('|')
    print('－')


def six():
    """
    When the player has 6 chances, adds a rope to the gallows.
    """
    print('　' + '＿＿＿＿＿')
    print('|/　' + '　|')
    print('| 　')
    print('|　　 ')
    print('|')
    print('|')
    print('－')


def five():
    """
    When the player has 5 chances, adds a head under the rope.
    """
    print('　' + '＿＿＿＿＿')
    print('|/　' + '　|')
    print('| 　' + '　O')
    print('|　　 ')
    print('|')
    print('|')
    print('－')


def four():
    """
    When the player has 4 chances, adds a body to the stick man.
    """
    print('　' + '＿＿＿＿＿')
    print('|/　' + '　|')
    print('| 　' + '　O')
    print('|　　 ' + '|')
    print('|')
    print('|')
    print('－')


def three():
    """
    When the player has 3 chances, adds a left hand to the stick man.
    """
    print('　' + '＿＿＿＿＿')
    print('|/　' + '　|')
    print('| 　' + '　O')
    print('|　　/' + '|')
    print('|')
    print('|')
    print('－')


def two():
    """
    When the player has 2 chances, adds a right hand to the stick man.
    """
    print('　' + '＿＿＿＿＿')
    print('|/　' + '　|')
    print('| 　' + '　O')
    print('|　　/' + '|\\')
    print('|')
    print('|')
    print('－')


def one():
    """
    When the player has 1 chance, adds a left arm to the stick man.
    """
    print('　' + '＿＿＿＿＿')
    print('|/　' + '　|')
    print('| 　' + '　O')
    print('|　　/' + '|\\')
    print('|　　/')
    print('|')
    print('－')


def zero():
    """
    When the player doesn't have any chances,
    adds a right arm to the stick man, and show 'you = dead!'.
    """
    print('　' + '＿＿＿＿＿')
    print('|/　' + '　|')
    print('| 　' + '　O')
    print('|　　/' + '|\\')
    print('|　　/' + ' \\')
    print('|' + 'you = dead!')
    print('－')


def random_word():
    """
    This function will return a random English word.
    """
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
