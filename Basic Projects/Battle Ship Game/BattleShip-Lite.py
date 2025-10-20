import random 

# Function to display the current state of the game board
def show_grid(board):
    index=0
    print(f"{board[0]}  | {board[1]} | {board[2]}")
    print("---+---+---")
    print(f"{board[3]}  | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f"{board[6]}  | {board[7]} | {board[8]}")

# Function to display the pattern reference for player input (positions 1–9)
def show_pattern():
    print("1  | 2 | 3")
    print("---+---+---")
    print("4  | 5 | 6")
    print("---+---+---")
    print("7  | 8 | 9")

# Core game logic function
def play_game():
    all_guesses=[]                         # To store player's previous guesses
    battle_ship=random.randint(1,9)        # Randomly select position for the hidden battleship
    total_attempt=0                        # Track total attempts

    # Player gets 3 chances to find the battleship
    for i in range(1,4):
        total_attempt+=1
        try:
            # Ask the player for their guess
            choice=int(input(f"\nAttempt {i} to find Battle Ship choose b/w (1-9):  "))
            if choice not in all_guesses :
                if (1<=choice<=9) :
                    all_guesses.append(choice)   # Add valid guess to list
                    if choice==battle_ship:
                        # If player guesses correctly, mark the ship and end the game
                        print(f"You found the Battle Ship at position {battle_ship}\n")
                        board[choice-1]="🚢"
                        show_grid(board)
                        break
                    else:
                        # Incorrect guess; mark with X
                        print("\nWrong Guess\n")
                        board[choice-1]="X"
                        show_grid(board)
                else:
                    # Input not in valid range
                    print(" ❌ Please choose a number between 1 and 9. ")
            else:
                # Player tried a previously guessed position
                print("⚠️ You already guessed that position. Try another.")
        except ValueError:
            # Handle non-integer inputs
            print("\n❌ Invalid input. Enter a number between 1 and 9.")

    # If player fails all 3 attempts, reveal battleship position
    if total_attempt==3:
        print(f"\nAll attempt ended Battle Ship was at {battle_ship}\n")
        board[battle_ship-1]="🚢"
        show_grid(board)

# Main program loop for repeating or exiting the game
stop_game=0
while True:
    x=input("\nDo you Want to Play?(Y/N) : ").lower()
    if x=="y":
        stop_game+=0                        # Continue playing
    elif x=="n":
        print("\n<-----Game Ended!!!----->") # Exit message
        stop_game+=1
    else:
        # Handle invalid yes/no responses
        print("\nPlease a Valid Answer (Y/N):  ")
        continue

    if stop_game!=0:
        # Ends the while loop if user chose to quit
        break
    else:
        # Start a new game with a fresh board
        board=["_","_","_",
        "_","_","_",
        "_","_","_"]
        print("\n<-----Battle Ship Lite Game is Started----->\n")
        show_pattern()      # Display grid pattern for reference
        play_game()         # Call the main gameplay function
