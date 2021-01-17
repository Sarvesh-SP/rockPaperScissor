from random import randint
from rpsPack import randi, result
p_update = 0
c_update = 0

print("Welcome to a game of Rock, Paper, Scissors")

rounds = int(input("How many rounds would you like to play: "))

for x in range(rounds):

  print(f"Round: {x+1}")
  print(f"Player: {p_update}\t\t Computer: {c_update}")
  p_choice = input("Time to pick....rock, paper, scissors: ").lower()
  if p_choice in ["rock", "paper", "scissors"]:
    c_val = randint(1, 3)
    c_choice = randi(c_val)
    res = result(p_choice, c_choice)
    print(f"Computer: {c_choice}")
    print(f"Player: {p_choice}")
    if (res == 2):
      print("\t\tIt is a tie, how boring!\n\t\tThis round was a tie\n\n")
    elif res == 1:
      print("\t\tComputer Wins.\n\n")
      c_update += 1
    else:
      print("\t\tPlayer Wins.\n\n")
      p_update += 1
  else:
    print("\t\tThis is not a valid game option.\n\n")

  
print(f"Final scores\n \tPlayer: {p_update}\t\t\t Computer: {c_update}")




