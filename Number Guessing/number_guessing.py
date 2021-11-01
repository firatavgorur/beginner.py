import random

welcome = {"welcome the game. press 0 for quit"}

print(welcome)

x = random.randint(0,101)
hearth = int(input("how many tries do you want: "))
guess =  int(input("your guess: "))

point  = 100
counter = 0
i = 1

while x != guess:
    hearth -= 1
    counter += 1
    point -= 10
    if guess not in range(0,101):
        print("invalid number, enter between 0,101")
        guess = int(input("your guess: "))

    elif hearth == 0:
        print(f"Game over.Your rights is done.Number is {x}")
        break
        
    elif guess == 0:
        print("Exiting...")
        break

    elif guess > x:
        print("Down")
        guess = int(input(f"Wrong. {hearth} right left. Your guess: "))
    
    elif guess < x:
        print("Up")
        guess = int(input(f"Wrong. {hearth} right left. Your guess: "))

else:
    if guess == x:
        print(f"!!!!Congratulations you won !!!!! You know in {counter} tries. Your point {point} ")

