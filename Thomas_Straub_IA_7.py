#Thomas Straub
#Assignment 7
#Dice game

import random

# Global variables to track total game wins for each player
player1_total_wins = 0
player2_total_wins = 0


def roll_dice():
    # Returns a random number between 1 and 6
    return random.randint(1, 6)


def play_round(player1, player2):
    # Display each player's roll
    print(f"Player 1 rolled: {player1}")
    print(f"Player 2 rolled: {player2}")

    # Compare rolls and determine round winner
    if player1 > player2:
        print("Player 1 wins the round")
        return 1  # Return 1 for Player 1 win
    elif player2 > player1:
        print("Player 2 wins the round")
        return 2  # Return 2 for Player 2 win
    else:
        print("The round is a tie")
        return 0  # Return 0 for a tie


def main():
    # Allow modification of global win counters
    global player1_total_wins, player2_total_wins

    # Get number of rounds from user with input validation
    try:
        num_rounds = int(input("How many rounds would you like to play? "))
        if num_rounds <= 0:
            print("Please enter a positive number of rounds.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    # Initialize counters for rounds won and ties in this game
    player1_wins = 0
    player2_wins = 0
    ties = 0

    # Play each round
    for round_num in range(1, num_rounds + 1):
        print(f"\nRound {round_num}:")
        # Roll dice for both players
        p1_roll = roll_dice()
        p2_roll = roll_dice()
        # Play round and get result
        result = play_round(p1_roll, p2_roll)

        # Update round win and tie counters
        if result == 1:
            player1_wins += 1
        elif result == 2:
            player2_wins += 1
        else:
            ties += 1

    # Display game results
    print("\nGame Results:")
    print(f"Player 1 won {player1_wins} rounds")
    print(f"Player 2 won {player2_wins} rounds")
    print(f"Ties: {ties}")

    # Determine and record overall game winner
    if player1_wins > player2_wins:
        print("Player 1 wins this game!")
        player1_total_wins += 1
    elif player2_wins > player1_wins:
        print("Player 2 wins this game!")
        player2_total_wins += 1
    else:
        print("This game is a tie!")

    # Show running total of game wins
    print(f"\nTotal Wins Across All Games:")
    print(f"Player 1: {player1_total_wins}")
    print(f"Player 2: {player2_total_wins}")


if __name__ == "__main__":
    # Main game loop to allow multiple games
    while True:
        # Run a single game
        main()
        # Ask if user wants to play another game
        play_again = input("\nWould you like to play another game? (yes/no): ").lower()
        # Exit loop if user doesn't want to continue
        if play_again != 'yes':
            # Display final total wins
            print("\nFinal Total Wins:")
            print(f"Player 1: {player1_total_wins}")
            print(f"Player 2: {player2_total_wins}")
            # Check if total wins are tied
            if player1_total_wins == player2_total_wins:
                print("The overall result is a tie!")
            else:
                # Declare overall winner based on total wins
                winner = "Player 1" if player1_total_wins > player2_total_wins else "Player 2"
                print(f"{winner} is the overall winner!")
            print("Thanks for playing!")
            break