# Estimate the value of winning the "Pass" bet in Craps using the Monte Carlo simulation

from random import randint

# Function to generate random roll
def roll():
  dice_one = randint(1,6)
  dice_two = randint(1,6)
  return dice_one + dice_two
  
def main():

  '''
     Main method to estimate winning the "Pass" bet in Craps
     inputs:none
     output: print the estimate
  '''
  
  # Parameters
  num_iterations = 1000000
  
  # State variables
  num_wins = 0
  
  # Loop over all simulated trials
  for iteration in range(num_iterations):
      come_out = roll()
      if come_out == 7 or come_out == 11:
        num_wins += 1
      elif come_out == 2 or come_out == 3 or come_out == 12:
         continue
        
      else:
        point = come_out
        while True: 
          result = roll()
          if result == point:
            num_wins += 1
            break
          if result == 7:
            break
          
          
  # Post trial calculations
  estimate = float(num_wins)/ float(num_iterations) * 100
  print " Your chance of winning the bet is %.2f percent." % (estimate)
  
  # Run main if the script is run from the terminal 
if __name__ == '__main__':
    main()
        
        
        
        
        
        
        
        
        
        
        