import time

# @title print the messages
# @params array of messages
# @return the given value


def print_sleep(messages):
    for message in messages:
        print(message)
        time.sleep(0.75)


def input_validate(message, options):
       while True:
              option = input(message)
              if option in options:
                  return option
              print_sleep(f'Sorry, the option "{option}" is invalid')
              