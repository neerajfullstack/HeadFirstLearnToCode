import random

winner = ''

choices = ['rock', 'paper', 'scissors']

computer_choice = random.choice(choices)

user_choice = input('rock, paper or scissors?')

# Evaluate the results
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

# Display the winner

if winner == 'Tie':
    print('We both chose', computer_choice, 'play again.')
else:
    print(winner, 'won, I chose', computer_choice + '.')



