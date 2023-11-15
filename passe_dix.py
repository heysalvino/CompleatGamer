from random import randint

def estimate_winning_passe_dix():
    """
    Estimate the chance of winning Passe-Dix using Monte Carlo simulation.
    Outputs: Estimated winning percentage
    """
    # Parameters
    num_iterations = 1000000

    # State variables
    num_wins = 0

    # Loop over all simulated trials
    for iteration in range(num_iterations):
        dice_one = randint(1, 6)
        dice_two = randint(1, 6)
        dice_three = randint(1, 6)

        result = dice_one + dice_two + dice_three

        if result > 10:
            num_wins += 1

    # Post-trial calculations
    estimate = (num_wins / num_iterations) * 100
    print(f'Your chance of winning Passe-Dix is {estimate:.2f} percent.')

# Run the estimation if the script is run from the terminal
if __name__ == '__main__':
    estimate_winning_passe_dix()
