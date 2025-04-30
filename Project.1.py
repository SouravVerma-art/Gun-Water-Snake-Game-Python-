import random

print("********** SNAKE, WATER, GUN GAME **********")
# choices 
choices = ['g', 's', 'w']

print("Choices!")
print("1. Snake --> [S/s]")
print("2. Gun --> [G/g]")
print("3. Water --> [W/w]")

while True:
    # computer input 
    Computer = random.choice(choices)
    # user inpuit
    m = input("Enter your choice [S/G/W]: ")
    Player = m.lower()

    # if player choose random choice!
    if Player not in ['g', 'w', 's']:
        print("Invalid Choice! Please choose [S/G/W].")
        continue 

  # Show computer's choice
    print(f"Computer chose: {Computer.upper()}")

    if Computer == Player:
        print("TIE!")

    # You win conditions
    elif (Player == 'g' and Computer == 's') or (Player == 's' and Computer == 'w') or (Player == 'w' and Computer == 'g'):
        print("You win!")
        break
    
    # Computer wins conditions
    else:
        print("Computer wins!")

print("\n********** GAME OVER **********")
