'''
Ultimate Guessing Game Project
By Rowen Daly
Completed 12/13/2021
'''
import random

count = 0 # number of guesses user has taken

userName = input("Please enter your name: \n")

response = input("Would you like to play a game? Type 'y' if so: \n")

def verify_guess(g): 
  while not g.isdigit() or int(g) < 1 or int(g) > 100:  
    if not g.isdigit():
      g = input("You did not enter an integer. guess again") 
    else: 
      g = input("Your guess has to be between 1 and 100. Try again.")
  g = int(g) #now we know we can turn it into an int
  return g


#MAIN starts here
while response == "y": 
  #code to play ga;e me
  secret = random.randint(1, 100)
  guess = verify_guess(input("Guess a number from 1 to 100. \n"))
  count += 1 # THIS IS THE SAME AS COUNT = COUNT +1
  while secret != guess: #runs while the user has not guessed correctly
    if guess < secret:
      guess = verify_guess(input("Too low. Guess again. \n"))
      count = count + 1
    else:
      guess = verify_guess(input("Too high. Guess again. \n"))
      count = count + 1
  if count == 1:
    print("You got it! it only took " + str(count) + " guess. Thanks for playing.")
  else:
    print("You got it! it only took " + str(count) + " guesses. Thanks for playing.")
  response = input("Would you like to play again? Type 'y' if so: \n") #would you like to play again message 
print("OK, goodbye.")
# ur syntax is ugly
