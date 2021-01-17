
def result(p1, c1):
  if ((p1 == "paper" and c1 == "scissors") or (p1 == "scissors" and c1 == "rock") or (p1 == "rock" and c1 == "paper")):
    return 1
  elif ((c1 == "paper" and p1 == "scissors") or (c1 == "scissors" and p1 == "rock") or (c1 == "rock" and p1 == "paper")):
    return 0
  else:
    return 2

def randi(val):
  if val == 1:
    return "rock"
  elif val == 2:
    return "paper"
  else:
    return "scissors"