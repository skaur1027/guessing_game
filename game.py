#import random number

import random
from tokenize import cookie_re

from numpy import append, number

# Greeting the player

greeting = 'Hi player! Welcome to the game!'
print(greeting)

# Get player's name

player_name = input('What is your name? ')
print('Welcome to the game, {}!'.format(player_name))

# Give option for computer to play

computer = input('Would you like the computer to play? Y/N; ')
user_number = 50
if computer == 'Y':
    ran_number = random.randint(1, 101)
    lower_bound = 1
    upper_bound = 101
    print("Computer's guess: {}".format(ran_number))
    user_response = input('How close was the computer to your number: ')

    while user_response != 'you won':
        if user_response == 'too high':
            upper_bound = ran_number
            ran_number = random.randint(lower_bound, upper_bound+1)
            print("Computer's guess: {}".format(ran_number))
            user_response = input('How close was the computer to your number: ')
        elif user_response == 'too low':
            lower_bound = ran_number
            ran_number = random.randint(lower_bound, upper_bound+1)
            print("Computer's guess: {}".format(ran_number))
            user_response = input('How close was the computer to your number: ')            

        

# Ask the user to set the range bounds
start = int(input('Pick a starting number: '))
stop = int(input('Please pick an ending number: '))
# Prompt the player to guess a number
correct_guesses = []
restart_game = 'Y'
while restart_game == 'Y':

    game_number = random.randint(start, stop + 1)
    # Choose random number
    print(game_number, 'random number')
    while True:
        try:
            number_guess = input('Please guess a number: ')
            number_guess = int(number_guess)
            break
        except ValueError:
            print('Oops! This is not a valid number. Please pick a valid number.')

    turn = 1 
    while number_guess != game_number:
        
        if number_guess < 0 or number_guess > 100:
            print('Bad guess!')
            print('Turn number: {}'.format(turn))
        elif number_guess < game_number:
            print('Your guess is too low!')
            print('Turn number: {}'.format(turn))
        elif number_guess > game_number:
            print('Your guess is too high!')
            print('Turn number: {}'.format(turn))

        if turn == 5:
            print("Too many tries!")
            restart_game = input('Would you like to play again? Y/N: ')
            break

        while True:
            try:
                number_guess = input('Please guess a number: ')
                number_guess = int(number_guess)
                break
            except ValueError:
                print('Oops! This is not a valid number. Please pick a valid number.')


        turn = turn + 1 

    if number_guess == game_number:
        print('You won!')
        print('Turn number: {}'.format(turn))
        correct_guesses.append(turn)
        print(correct_guesses)
        restart_game = input('Would you like to play again? Y/N: ')
        lowest = min(correct_guesses)
        if restart_game == 'N':
            print('Congrats, your lowest number of guesses was: {}'.format(lowest))



