# write 'hello world' to the console
print('hello world')
import random
#Write code to create game where the computer will be user's opponent and can randomly choose one of the elements (rock, paper, or scissors) for each move, just like user. User's interaction in the game will be through the console (Terminal).
#The player can choose one of the three options rock, paper, or scissors and should be warned if they enter an invalid option.
# At each round, the player must enter one of the options in the list and be informed if they won, lost, or tied with the opponent.
# By the end of each round, the player can choose whether to play again.
# Display the player's score at the end of the game.

# Initialize player's score
player_score = 0

# Define the valid options for the game
valid_options = ['rock', 'paper', 'scissors']

# Game loop
while True:
    # Get the player's choice
    player_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    
    # Check if the player's choice is valid
    if player_choice not in valid_options:
        print("Invalid option. Please choose rock, paper, or scissors.")
        continue
    
    # Generate the computer's choice
    computer_choice = random.choice(valid_options)
    
    # Print the choices
    print(f"Player's choice: {player_choice}")
    print(f"Computer's choice: {computer_choice}")
    
    # Determine the winner
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == 'rock' and computer_choice == 'scissors') or (player_choice == 'paper' and computer_choice == 'rock') or (player_choice == 'scissors' and computer_choice == 'paper'):
        print("You won!")
        player_score += 1
    else:
        print("You lost!")
    
    # Ask the player if they want to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break

# Print the player's score
print(f"Your score: {player_score}")
#The minigame must handle user inputs, putting them in lowercase and informing the user if the option is invalid.
 




