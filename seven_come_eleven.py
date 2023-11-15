from random import randint

def roll():
    """Return the sum of two randomly rolled six-sided dice."""
    return randint(1, 6) + randint(1, 6)

def simulate_craps(num_iterations):
    """
    Simulate num_iterations rounds of Craps to estimate the winning probability of a Pass bet.
    
    :param num_iterations: Number of iterations to simulate
    :return: Estimated winning probability
    """
    WINNING_NUMBERS = {7, 11}
    LOSING_NUMBERS = {2, 3, 12}

    wins = sum(1 for _ in range(num_iterations) if simulate_round(WINNING_NUMBERS, LOSING_NUMBERS))
    return wins / num_iterations * 100

def simulate_round(WINNING_NUMBERS, LOSING_NUMBERS):
    come_out_roll = roll()
    if come_out_roll in WINNING_NUMBERS:
        return True
    if come_out_roll in LOSING_NUMBERS:
        return False

    point = come_out_roll
    while True:
        roll_result = roll()
        if roll_result == point:
            return True
        if roll_result == 7:
            return False

def main():
    num_iterations = 1000000
    win_probability = simulate_craps(num_iterations)
    print(f"Your chance of winning the bet is {win_probability:.2f} percent.")

if __name__ == '__main__':
    main()
