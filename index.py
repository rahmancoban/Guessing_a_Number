import random

top_of_range = input("Type a number for the top of the range: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print('Please type a number larger than 0 next time.')
        quit()
else:
    print('Please type a number next time.')
    quit()

random_number = random.randint(0,top_of_range)
number_of_guesses = 0

while True:
    number_of_guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
        if user_guess>top_of_range:
            print("Please type a number smaller than top of the range")
            user_guess = input("Make a guess: ")
    else:
        print('Please type a number next time.')
        continue
    if user_guess == random_number:
        print("Well Done!")
        break
    elif user_guess > random_number:
        print("You were above")
    else:
        print("You were below")

print("You got it in", number_of_guesses, "guesses")








