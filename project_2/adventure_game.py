import time
import random

# @title print the messages
# @params array of messages
# @return the given value


def print_sleep(messages):
    for message in messages:
        print(message)
        time.sleep(0.75)
    return input('Please enter your option\n')


# @title case winner
# @params animal
# @return string


def win(animal):
    return print_sleep(['Seems like the ' + animal + ' has disapeared.',
                        'You have won the game',
                        'Press (q) to leave the play',
                        'Press (1) to play again'])

# @title case loose
# @params animal
# @return string


def lose(animal):
    return validate_input(['The ' + animal + ' has jumped and reached you',
                        'So you did not sarvive',
                        'You loose the game',
                        'Press (q) to leave the play',
                        'Press (1) to play again'], 'end')


# @title validate the values given by user
# @params array of creatures
# @return string


def validate_input(messages, method):
    while_condition = False;
    response = print_sleep(messages)
    if method != 'end':
        or_resp = response == '1' or response == '2'
        if len(response) < 2 and or_resp:
            while_condition = True
        else:
            while_condition = False
        while (while_condition):
            return response
        else:
            print('You have entered a wrong key.')
            response = validate_input(messages, 'not')
        
    else:
        or_resp = response == '1' or response == 'q'
        if len(response) == 1 and or_resp :
            while_condition = True
        else:
            while_condition = False
        while while_condition:
            return response
        else:
            print('You have entered a wrong key.')
            response = validate_input(messages, 'end')
        

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


# @title The base logic are here
# @params none
# @return string


def main():
    end_choice = '1'
    print('Wellcome!')
    while end_choice == '1':
        animal_aquatic = animal_choice()
        animal_predator = animal_randint()
        choice = validate_input(
                    ['Pay attention for the moviment you have to make.',
                    'You are in a wild island.'
                    + '\nYou are running away from a ' + animal_predator
                    + ' and desperate to find a way out,'
                    + '\nyou find out you have two choices go to the river'
                    + 'or climb a tree. \nThe river has ' + animal_aquatic
                    + ' in his extention but you are a good swimmer.',
                    'Press (1) to climb the tree.',
                    'Press (2) to swim in the river.'], 'not')
        
        #I think is redundantly but when i remove the line bellow
        #some errors happens
        if choice == '1' or choice == '2': 

            if choice == '1':
                second_choice = validate_input(
                                ['You choose the highest tree and start climb.',
                                'You are doing that so fast that you get'
                                + ' tired in the middle of the tree.',
                                'To keep climbing press (1)',
                                'To stop climbing press (2)'], 'not')
                if second_choice == '1':
                    end_choice = win(animal_predator)
                elif second_choice == '2':
                    end_choice = lose(animal_aquatic)
            elif choice == '2':
                end_choice = validate_input(
                                    ['I have tried to swim but the'
                                    + ' crocodile reached you',
                                    'So you did not sarvive',
                                    'You loose the game',
                                    'Press (q) to leave the play',
                                    'Press (1) to play again'], 'end')
        else:
            main()
    else:
        print('Thank you! See you later!')         
# @title Calling the function main       


main()