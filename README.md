# The Compleat Gamester


## Instructions
- Complete Python programs to answer the following questions. Each program should be a separate `.py` script.
- Adhere to good programming style and use clear comments.
- Avoid debugging messages in your final output. Only print what is necessary to answer the question.
- Remove any extra print statements before submitting your final code.

## Problems

### Passe-Dix
- Implement a simulation to evaluate the probability of winning in Passe-Dix, a dice game.
- Rules: Roll three six-sided dice. If the sum exceeds 10, you win; otherwise, you lose.
- Hint: Utilize the `random` module for generating random integers.

### 7 Come 11
- Create a simulation to estimate the odds of winning the "Pass" bet in Craps.
- Basic Rules:
  - Roll two six-sided dice.
  - If the roll is 7 or 11, you win; if it's 2, 3, or 12, you lose.
  - Other values set a "point".
  - Continue rolling to hit the point again before rolling a 7. Rolling the point wins; rolling a 7 loses.

### Nim
- Develop a Python script for two players to play Nim with three piles of stones.
- Randomly generate the number of stones in each pile at the start.
- Players remove stones from one pile per turn. The player forced to take the last stone loses.
- Ensure valid input: positive whole numbers, non-empty piles, and appropriate number of stones.
- Use a three-element list to track the number of stones in each pile.
- Tips: Use `raw_input` and `int()` for handling user inputs.

