import random
import time

""" Randomize animal using choice method
:param none
:return: string"""


def animal_choice():
    animals = ['Green Anaconda', 'Bull Shark', 'crocodile']
    return random.choice(animals)


"""Randomize animal using randint method
:param none
:return: string"""


def animal_randint():
    animals = ['Lion', 'Zebra', 'Jaguar', 'Black Caiman']
    return animals[random.randint(0, len(animals) - 1)]


""" Print the messages
:param array: List of messages
:return: void"""


def print_sleep(messages):
    for message in messages:
        print(message)
        time.sleep(0.75)


""" Validation for input values
:param message: The massage displayed options: List of options
:return: the given value
Provided by the Reviewer of Udacity"""


def input_validate(message, options):
    while True:
        option = input(message + '\n').lower()
        if option in options:
            return option
        print_sleep([f'Sorry, the option "{option}" is invalid'])


""" Win message
:param animal
:return: string (response)"""


def win(animal):
    print_sleep([f'Seems like the "{animal}" has disapeared.',
                'You have won the game'])
    return input_validate(
        'Press (q) to leave the play or (1) to play again', ['1', 'q'])


""" Case loose
:param animal
:return: string"""


def lose(animal):
    print_sleep(
        [f'The "{animal}" has jumped and reached you',
            'So you did not sarvive', 'You loose the game'])
    return input_validate(
        'Press (q) to leave the play or (1) to play again', ['1', 'q'])


""" Play again
:param option
:return: void"""


def play_again(option):
    if option == 'q':
        print_sleep(['Thanks for playing! See you later!'])
        exit(0)


""" The base logic are here
:param void:
:return: string"""


def main():
    while True:
        aquatic = animal_choice()
        predator = animal_randint()
        print_sleep(
                    ['Pay attention for the moviment you have to make.',
                        f'You are in a wild island.\nYou are running ' +
                        f'away from a "{predator}" and desperate to ' +
                        f'find a way out,\nyou find out you have ' +
                        f'two choices go to the river or climb a tree. ' +
                        f'\nThe river has "{aquatic}"' +
                        f' in his extention but you are a good swimmer.'])
        choice = input_validate(
                    'Press (1) to climb the tree or (2) to swim in the river.',
                    ['1', '2'])

        if choice == '1':
            print_sleep(
                ['You choose the highest tree and start climb.',
                    'You are doing that so fast that you get tired' +
                    ' in the middle of the tree.'])
            another_choice = input_validate(
                                'To keep climbing press (1) /n' +
                                ' To stop climbing press (2)',
                                ['1', '2'])
            if another_choice == '1':
                win(predator)
            else:
                play_again(lose(predator))
        else:
            print_sleep(
                        ['I have tried to swim but the crocodile reached you',
                            'So you did not sarvive',
                            'You loose the game'])
            play_again(input_validate(
                'Press (q) to leave the play or (1) to play again', ['1', 'q']
            ))


if __name__ == '__main__':
    main()
