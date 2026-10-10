import random
print("===NUMBER GUESSING GAME===\n")
while True:
    number=random.randint(1,100)
    attempt=0
    print("===choose difficulty level===\n")
    print("1. EASY(10 attempts)\n 2. MEDIUM(7 attempts\n3.HARD(5 attempts\n")
    choice = int(input("enter your choice ");
    if choice == "1":
        max_attempts = 10
    elif choice == "2":
        max_attempts = 7
    elif choice == "3":
        max_attempts = 5
    else:
        print("invalid choice! starting with EASY\n")
        max_attempts = 10

print("guess a no. between 1 to 100")
while attemps=max_attempts:
    try:
        guess=int(input("enter your guess: "))
    except ValueError:
        print("plz enter valid no.")
        continue
    if guess<1 or guess>100:
        print("choose  no. between 1 to 100 only ")
        conitinue
    attempt += 1
    if guess>number:
        print("so high")
    elif guess<number:
        print("so low")
    else:
        print("wow ! your guess the correct")
        print("you guess in ",attempt,"attempts")

