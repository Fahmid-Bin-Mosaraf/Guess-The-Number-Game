import random
number = random.randint(1,10)
guess = 0
while guess != number:
        guess = int(input("Guess a number: "))

        if(guess < number):
                print("Guess Higher!")
        elif (guess > number):
                print("Guess Lower!")
        else:
                print("Congratulation you have guess the number!")
