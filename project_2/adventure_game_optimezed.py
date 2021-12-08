import random
import time

# @title randomize animal using choice method
# @params none
# @return string


def animal_choice():
    animals = ['Green Anaconda', 'Bull Shark', 'crocodile']
    return random.choice(animals)

# @title randomize animal using randint method
# @params none
# @return string


def animal_randint():
    animals = ['Lion', 'Zebra', 'Jaguar', 'Black Caiman']
    return animals[random.randint(0, len(animals) - 1)]

# @title print the messages
# @params array of messages
# @return the given value


def print_sleep(messages):
    for message in messages:
        print(message)
        time.sleep(0.75)

# @title validation for input values
# @params string message
# @return the given value
# Provided by the Reviewer of Udacity


def input_validate(message, options):
    while True:
        option = input(message + '\n').lower()
        if option in options:
            return option
        print_sleep([f'Sorry, the option "{option}" is invalid'])

# @title win message
# @params animal
# @return the given value


def win(animal):
    print_sleep([f'Seems like the "{animal}" has disapeared.',
                'You have won the game'])
    return input_validate(
        'Press (q) to leave the play or (1) to play again', ['1', 'q'])

# @title case loose
# @params animal
# @return string


def lose(animal):
    print_sleep(
        [f'The "{animal}" has jumped and reached you',
            'So you did not sarvive', 'You loose the game'])
    return input_validate(
        'Press (q) to leave the play or (1) to play again', ['1', 'q'])

# @title play again
# @params option
# @return void


def play_again(option):
    if option == 'q':
        print_sleep(['Thanks for playing! See you later!'])
        exit(0)

# @title The base logic are here
# @params none
# @return string


def main():
    while True:
        aquatic = animal_choice()
        predator = animal_randint()
        print_sleep(['Pay attention for the moviment you have to make.',
                    f'You are in a wild island.\nYou are running away from' +
                    f' a "{predator}" and desperate to find a way out,\n' +
                    f'you find out you have two choices go to the river' +
                    f'or climb a tree. \nThe river has "{aquatic}"' +
                    ' in his extention but you are a good swimmer.'])
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
