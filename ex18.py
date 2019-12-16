"""
Exercise 18: Cows And Bulls
Create a program that will play the “cows and bulls” game with the user.
The game works like this:
Randomly generate a 4-digit number. Ask the user to guess a 4-digit number.
For every digit that the user guessed correctly in the correct place,
they have a “cow”. For every digit the user guessed correctly in the wrong
place is a “bull.” Every time the user makes a guess, tell them
how many “cows” and “bulls” they have. Once the user guesses the correct
number, the game is over. Keep track of the number of guesses the user
makes throughout teh game and tell the user at the end.

Say the number generated by the computer is 1038. An example
interaction could look like this:

Welcome to the Cows and Bulls Game!
Enter a number:
>>> 1234
2 cows, 0 bulls
>>> 1256
1 cow, 1 bull
...
Until the user guesses the number.
"""

import random


def cows_bulls():
    random_num = random.randint(1000, 9999)
    counter = 0

    while True:
        user_num_input = input("Try to guess the number (1000-9999): ")
        if user_num_input.isnumeric() is False or len(user_num_input) != 4 or \
                int(user_num_input) < 1000:
            print("Invalid input! Try again: ")
            continue
        else:
            cows = 0
            bulls = 0
            counter += 1
            # numbers conversion to string and list
            random_num_copy = list(str(random_num))
            user_num = list(str(user_num_input))

            """checking for cows; and deleting from list to ensure that this
               numbers won't be duplicated in bulls"""
            for i in range(3, -1, -1):
                if user_num[i] == random_num_copy[i]:
                    cows += 1
                    random_num_copy.pop(i)
                    user_num.pop(i)

            # checking for bulls
            for j in range(len(user_num)-1, -1, -1):
                if user_num[j] in random_num_copy:
                    bulls += 1
                    random_num_copy.remove(user_num[j])
                    user_num.pop(j)

            if cows == 4:
                print(f"Correct! Your attempts: {counter}")
                break
            else:
                print(f"Cows: {cows}. Bulls: {bulls}.\nTry again!")
                continue


if __name__ == "__main__":
    cows_bulls()