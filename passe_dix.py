# Estimate the value of winning Passe-Dix the Monte Carlo simulation

from random import randint

def main():

  '''
     Main method to estimate winning Passe-Dix
     inputs:none
     output: print the estimate
  '''
  
  # Parameters
  num_iterations = 1000000
  
  # State variables
  num_wins = 0
  
  # Loop over all simulated trials
  for iteration in range(num_iterations):
      dice_one = randint(1,6)
      dice_two = randint(1,6)
      dice_three = randint(1,6)
      
      result = dice_one + dice_two + dice_three
      
      if result > 10:
        num_wins += 1
        
  # Post trial calculations
  estimate = float(num_wins) / float(num_iterations) * 100
  print " Your chance of winning Passe-Dix is %.2f percent." % (estimate)
  
  # Run main if the script is run from the terminal 
if __name__ == '__main__':
    main()
