# The game of Nim

from random import randint
  
def main():

  '''
     Main method to play the game of Nim
     inputs: player's names, pile number, number of stones 
     output: number of stones in piles, who wins, who loses
  '''
  
  player_one = raw_input("Player One: What is your name? ")
  player_two = raw_input("Player Two: What is your name? ")
  round = player_one
  # Generate random piles
  pile_one = randint(10,50)
  pile_two = randint(10,50)
  pile_three = randint(10,50)
  
  while True:
    print "The 1st pile has {} stones, the 2nd pile has {} stones, and the 3rd pile has {} stones.".format(pile_one, pile_two, pile_three)
    
    if round == player_one:
      # Player 1's Turn
      pile_number = int(raw_input("%s. What pile do you choose: 1, 2, or 3?  " % player_one))
      # Pile 1
      if pile_number >= 1 and pile_number <= 3:
        if pile_number == 1:
          player_1_pile = pile_one
          if pile_one > 0:
            stone_number_1 = int(raw_input("%s. Enter the amount of stones you want to remove?  " % player_one))
            if stone_number_1 > 0 and stone_number_1 <= player_1_pile:
              pile_one -= stone_number_1
              if pile_one == 0 and pile_two == 0 and pile_three == 0:
                print "%s, you lose. %s wins.".format(player_one, player_two)
                break
              else:
                round = player_two
                continue
            else: print "Please select a valid number of stones."    
          else: print "Sorry %s, Pile is empty. Pick again. " % player_one
        # Pile 2
        if pile_number == 2:
          player_1_pile = pile_two
          if pile_two > 0:
            stone_number_1 = int(raw_input("%s. Enter the amount of stones you want to remove?  " % player_one))
            if stone_number_1 > 0 and stone_number_1 <= player_1_pile:
              pile_two -= stone_number_1
              if pile_one == 0 and pile_two == 0 and pile_three == 0:
                print "%s, you lose. %s wins.".format(player_one, player_two)
                break
              else:
                round = player_two
                continue
            else: print "Please select a valid number of stones."
          else: print "Sorry %s, Pile is empty. Pick again. " % player_one
        # Pile 3
        if pile_number == 3:
          player_1_pile = pile_three
          if pile_three > 0:
            stone_number_1 = int(raw_input("%s. Enter the amount of stones you want to remove?  " % player_one))
            if stone_number_1 > 0 and stone_number_1 <= player_1_pile:
              pile_three -= stone_number_1
              if pile_one == 0 and pile_two == 0 and pile_three == 0:
                print "%s, you lose. %s wins.".format(player_one, player_two)
                break
              else:
                round = player_two
                continue
            else: print "Please select a valid number of stones."     
          else: print "Sorry %s, Pile is empty. Pick again. " % player_one  
      else: print "Please select a valid pile number."
        
    if round == player_two:
      # Player 2's Turn
      pile_number = int(raw_input("%s. What pile do you choose: 1, 2, or 3?  " % player_two))
      if pile_number >= 1 and pile_number <= 3:
        # Pile 1
        if pile_number == 1:
          player_2_pile = pile_one
          if pile_one > 0:
            stone_number_2 = int(raw_input("%s. Enter the amount of stones you want to remove?  " % player_two))
            if stone_number_2 > 0 and stone_number_2 <= player_2_pile:
              pile_one -= stone_number_2
              if pile_one == 0 and pile_two == 0 and pile_three == 0:
                print "%s, you lose. %s wins.".format(player_two, player_one)
                break
              else:
                round = player_one
                continue
            else: print "Please select a valid number of stones."    
          else: print "Sorry %s, Pile is empty. Pick again. " % player_two
        # Pile 2
        if pile_number == 2:
          player_2_pile = pile_two
          if pile_two > 0:
            stone_number_2 = int(raw_input("%s. Enter the amount of stones you want to remove?  " % player_two))
            if stone_number_2 > 0 and stone_number_2 <= player_2_pile:
              pile_two -= stone_number_2
              if pile_one == 0 and pile_two == 0 and pile_three == 0:
                print "%s, you lose. %s wins.".format(player_two, player_one)
                break
              else:
                round = player_one
                continue
            else: print "Please select a valid number of stones."
          else: print "Sorry %s, Pile is empty. Pick again. " % player_two      
        # Pile 3
        if pile_number == 3:
          player_2_pile = pile_three
          if pile_three > 0:
            stone_number_2 = int(raw_input("%s. Enter the amount of stones you want to remove?  " % player_two))
            if stone_number_2 > 0 and stone_number_2 <= player_2_pile:
              pile_three -= stone_number_2
              if pile_one == 0 and pile_two == 0 and pile_three == 0:
                print ("%s, you lose.") % player_two
                break
              else:
                round = player_one
                continue
            else: print "Please select a valid number of stones."     
          else: print "Sorry %s, Pile is empty. Pick again. " % player_two 
      else: print "Please select a valid pile number."  
      
# Run main if the script is run from the terminal 
if __name__ == '__main__':
    main()