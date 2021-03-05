import string
import random
"""
This is a password generator that allows users to specify the number of characters, number of uppercase, lowercase, numbers and symbols they want in their password.
"""
print('Welcome to Password Generator!')
print('Your password should be a minimum of 6 characters!')
length_of_password = int(input('Please enter the length of your desired password: '))
num_of_upper_letters = int(input('Please enter the number of upper case letters in desired password: '))
num_of_lower_letters = int(input('Please enter the the number of lower case letters in desired password: '))
num_of_numbers = int(input('Please enter the the number of digits in desired password: '))
num_of_symbols = int(input('Please enter the the number of symbols in password: '))

symbols = [random.choice(string.punctuation) for character in range(num_of_symbols)]
upper = [random.choice(string.ascii_uppercase) for character in range(num_of_upper_letters)]
lower =  [random.choice(string.ascii_lowercase) for character in range(num_of_lower_letters)]
num =  [random.choice(string.digits) for character in range(num_of_numbers)]

psswrd = ''.join(symbols + upper + lower + num)
psswrd = list(psswrd)
random.shuffle(psswrd)
psswrd=''.join(psswrd)
print(psswrd)

    