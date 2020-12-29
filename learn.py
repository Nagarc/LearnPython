import random


random_number = random.randint(1, 20)
print(random_number)
guess = 0
while guess != random_number:
    guess = int(input("Enter a Number "))
    if guess < random_number:
        print('Sorry, guess again. Too low.')
    elif guess > random_number:
        print('Sorry, guess again. Too high.')
print( "Yay, congrats. You have guessed the number" + str(random_number) + "correctly!!")