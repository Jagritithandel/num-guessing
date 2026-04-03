import random
number=random.randint(1,100)
guess=0
attempt=0
print("welcome to smart guessig game")
print("guess a no. between 1 to 100")
while guess!=number:
    guess=int(input("enter your guess : "))
    attempt += 1
    if guess>number:
        print("so high")
    elif guess<number:
        print("so low")
    else:
        print("wow ! your guess the correct")
        print("you guess in ",attempt,"attempts")

