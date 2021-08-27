
def main():
  import random
  dice_rolls = int(input('how many di(c)e would you like to roll? '))
  dice_size = int( input('How may sides are the di(c)e?'))
  dice_sum = 0
  for i in range(0,dice_rolls):
   roll = random.randint(1,dice_size)
   dice_sum = dice_sum + roll
  
  if roll == 1:
    print(f'You rolled a {roll}! Crit fail my friend')
  elif roll == dice_size:
    print(f'You rolled a {roll}! Great Success!')
  else:
    print(f'You rolled a {roll}')
  print(f'You rolled a a total of {dice_sum}')  


if __name__== "__main__":
  main()