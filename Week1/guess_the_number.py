"""
This program allows you guess a computer generated number.  
"""

import random

print("Welcome to Guess the Number")
user_number = int(input('Please enter your number between 1-20: '))
computer_number = random.randint(0, 20)
if user_number == computer_number:
    print('You are correct!!!')
elif user_number < computer_number:
    print('Your guess is too low!!!')
else:
    print('Your guess is too high!!!')