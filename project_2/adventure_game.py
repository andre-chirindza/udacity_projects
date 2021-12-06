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
    return print_sleep(['Seems like the '+ animal +' has disapeared.',
                        'You have won the game',
                        'Press (q) to leave the play',
                        'Press (1) to play again'])

# @title case loose
# @params animal
# @return string
def lose(animal):
    return print_sleep(['The '+ animal +' has jumped and reached you',
                        'So you did not sarvive',
                        'You loose the game',
                        'Press (q) to leave the play',
                        'Press (1) to play again'])

# @title wrong choice
# @params none
# @return string
def wrong_choice():
    return print_sleep(['Wrong number selected',
                        'Press (q) to leave the play',
                        'Press (1) to play again'])

# @title The base logic are here
# @params none
# @return string
def main():
    animals1 = ['Lion','Zebra','Jaguar','Black Caiman']
    animals2 = ['Green Anaconda','Bull Shark','crocodile']
    end_choice = '1';   
    print('Wellcome!')
    while end_choice == '1':
        animal_aquatic = random.choice(animals2)
        animal_predator = animals1[random.randint(0,3)]
        choice = print_sleep(['Pay attention for the moviment you have to make.', 
                    'You are in a wild island. \nYou are running away from a '+ animal_predator +' and desperate to find a way out,'
                     +'\nyou find out you have two choices go to the river or climb a tree. '
                     +'\nThe river has '+ animal_aquatic +' in his extention but you are a good swimmer.',
                    'Press (1) to climb the tree.',
                    'Press (2) to swim in the river.'])

        if choice == '1' or choice == '2':

            if choice == '1':
                second_choice = print_sleep(['You choose the highest tree and start climb.',
                                'You are doing that so fast that you get tired in the middle of the tree.',
                                'To keep climbing press (1)',
                                'To stop climbing press (2)'])
                if second_choice == '1':
                    end_choice = win(animal_predator)
                elif second_choice == '2':
                    end_choice = lose(animal_aquatic)
                else:
                    end_choice = wrong_choice()
            elif choice == '2':
                end_choice = print_sleep(['I have tried to swim but the crocodile reached you',
                                    'So you did not sarvive',
                                    'You loose the game',
                                    'Press (q) to leave the play',
                                    'Press (1) to play again'])
            else:
                end_choice = wrong_choice()
        else:
            main()
              
    
# @title Calling the function main       
main()