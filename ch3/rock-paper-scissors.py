# here we are doing some setup by importing the random module
# and setting up the winner variable

import random

winner = ''

# The computer randomly chooses one item from the list below

choices = ['rock', 'paper', 'scissors']

computer_choice = random.choice(choices)

# get the user's choice with a simple input statement

user_choice = input('rock, paper or scissors?')

# Here's our game logic which checks to see if the computer wins or not
# and makes the appropriate change to the winner var

if user_choice == computer_choice:
    winner = 'Tie'
elif computer_choice == 'paper' and user_choice == 'rock':
    winner = 'Computer'
elif computer_choice == 'rock' and user_choice == 'scissors':
    winner = 'Computer'
elif computer_choice == 'scissors' and user_choice == 'paper':
    winner = 'Computer'
else:
    winner = 'User'

# Here we announce the game was a tie or winner along with the
# computer's choice

if winner == 'Tie':
    print('We both chose', computer_choice, 'play again.')
else:
    print(winner, 'won, I chose', computer_choice + '.')



