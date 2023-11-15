from random import randint

def play_nim_game():
    """
    Main function to play the game of Nim.
    Inputs: player's names, pile number, number of stones
    Output: number of stones in piles, who wins, who loses
    """
    player_one = input("Player One: What is your name? ")
    player_two = input("Player Two: What is your name? ")
    current_player = player_one

    # Generate random piles
    pile_one = randint(10, 50)
    pile_two = randint(10, 50)
    pile_three = randint(10, 50)

    while True:
        print(f"The 1st pile has {pile_one} stones, the 2nd pile has {pile_two} stones, and the 3rd pile has {pile_three} stones.")

        if current_player == player_one:
            current_pile = pile_one
        elif current_player == player_two:
            current_pile = pile_two

        pile_number = int(input(f"{current_player}, what pile do you choose: 1, 2, or 3?  "))

        if 1 <= pile_number <= 3:
            if current_pile > 0:
                stone_number = int(input(f"{current_player}, enter the amount of stones you want to remove?  "))

                if 1 <= stone_number <= current_pile:
                    if current_player == player_one:
                        pile_one -= stone_number
                    elif current_player == player_two:
                        pile_two -= stone_number

                    if pile_one == 0 and pile_two == 0 and pile_three == 0:
                        print(f"{current_player}, you lose. {player_two if current_player == player_one else player_one} wins.")
                        break
                    else:
                        current_player = player_two if current_player == player_one else player_one
                else:
                    print("Please select a valid number of stones.")
            else:
                print(f"Sorry {current_player}, Pile is empty. Pick again.")
        else:
            print("Please select a valid pile number.")

# Run the game if the script is run from the terminal
if __name__ == '__main__':
    play_nim_game()
