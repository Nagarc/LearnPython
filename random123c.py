import random

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
random_number = random.randint(num1, num2)
guess = 0
while guess != random_number:
    guess = int(input(f"Guess a number between {num1} and {num2}: "))
    if guess < random_number:
        print("Sorry, too low.")
    elif guess > random_number:
        print("Sorry, too high.")

print(f"Yay congrats. You have guessed the number {random_number} correctly!!!")




