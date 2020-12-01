# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), 
# compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

# Remember the rules:

# - Rock beats scissors
# - Scissors beats paper
# - Paper beats rock

print("""Welcome to a two-player Rock-Paper-Scissors game.

Please choose one:
Rock
Paper
Scissors\n""")

while True:
    p1 = input("Player one's choice: ")
    p1 = p1.lower()
   
    if p1 != 'rock' and p1 != 'paper' and p1 != 'scissors':
        print("Invalid choice.\n")
        continue
   
    p2 = input("Player two's choice: ")
    p2 = p2.lower()

    if p2 != 'rock' and p2 != 'paper' and p2 != 'scissors':
        print("Invalid choice.\n")
        continue
    print("\n")
    if p1 == p2:
        print("It was a tie!")
    elif p1 == 'rock':
        if p2 == 'scissors':
            print("Player one wins!")
        elif p2 == 'paper':
            print("Player two wins!")
    elif p1 == 'scissors':
        if p2 == 'paper':
            print("Player one wins!")
        elif p2 == 'rock':
            print("Player two wins!")
    elif p1 == 'paper':
        if p2 == 'rock':
            print("Player one wins!")
        elif p2 == 'scissors':
            print("Player two wins!")
    
    restart = input("\nWould you like to start a new game?: ")
    restart = restart.lower()

    if restart == 'yes':
        print("\n")
        continue
    else:
        break