import random

player1=input("First player, what is your name? ")
player2=input("Second player, what is your name? ")
# player1="Maria"
# player2="Josh"

def shuffled_deck():
    basic_deck = list(range(2, 15)) * 4
    random.shuffle(basic_deck)
    return basic_deck

deck=shuffled_deck()
p1_wins=0
p2_wins=0
# play1_deck=deck[0:27]
# play2_deck=deck[27:53]

# print(play1_deck)
# print(play2_deck)

def player_turn(name):
  if len(deck)==0:
    return "over"

  else:
    drawn=deck.pop(0)
    print(name,"drew card",drawn)
    return drawn

def compare(a,b):
  if a>b:
    #print("a won")
    return a
  elif b>a:
    return b
  else:
    print("Declare war!")
    return "war"

# def war():
#   p1_war1=player_turn(player1)
#   p1_war2=player_turn(player1)

#   p2_war1=player_turn(player2)
#   p2_war2=player_turn(player2)

#   winner2=compare(p1_war2,p2_war2)

#     if winner2==p1_war2:
#       print(player1,"drew the high WAR card")
#       p1_wins=p1_wins+p1+p2+p1_war1+p1_war2+p2_war1+p2_war2
#   elif winner==p2_war2:
#       print(player2,"drew the high WAR card")
#       p2_wins=p2_wins+p1+p2+p1_war1+p1_war2+p2_war1+p2_war2


while len(deck)>0:

  p1=player_turn(player1)
  if p1=="over":
    print("Not enough cards in the deck to continue")
    break
  p2=player_turn(player2)
  if p2=="over":
    print("Not enough cards in the deck to continue")
    break

  print("\n")
  winner=compare(p1,p2)

  if winner==p1:
    print(player1,"drew the high card")
    p1_wins=p1_wins+p1+p2
  elif winner==p2:
    print(player2,"drew the high card")
    p2_wins=p2_wins+p1+p2
  else:
    p1_war1=player_turn(player1)
    if p1_war1=="over":
      print("Not enough cards in the deck to continue")
      break
    p1_war2=player_turn(player1)
    if p1_war2=="over":
      print("Not enough cards in the deck to continue")
      break

    p2_war1=player_turn(player2)
    if p2_war1=="over":
      print("Not enough cards in the deck to continue")
      break
    p2_war2=player_turn(player2)
    if p2_war1=="over":
      print("Not enough cards in the deck to continue")
      break

    winner2=compare(p1_war2,p2_war2)

    if winner2==p1_war2:
      print(player1,"drew the high WAR card")
      p1_wins=p1_wins+p1+p2+p1_war1+p1_war2+p2_war1+p2_war2
    elif winner2==p2_war2:
      print(player2,"drew the high WAR card")
      p2_wins=p2_wins+p1+p2+p1_war1+p1_war2+p2_war1+p2_war2
    # else:
    #   p1_war3=player_turn(player1)
    #   p1_war4=player_turn(player1)

    #   p2_war3=player_turn(player2)
    #   p2_war4=player_turn(player2)

    #   winner3=compare(p1_war4,p2_war4)

    #   if winner3==p1_war2:
    #   print(player1,"drew the high WAR card")
    #   p1_wins=p1_wins+p1+p2+p1_war1+p1_war2+p2_war1+p2_war2
    # elif winner3==p2_war2:
    #   print(player2,"drew the high WAR card")
    #   p2_wins=p2_wins+p1+p2+p1_war1+p1_war2+p2_war1+p2_war2



  print("\n")
  print(player1,"score:",p1_wins)
  print(player2,"score:",p2_wins)

  print("\n")

print("Game over")

if p1_wins>p2_wins:
  print(player1,"wins with",p1_wins,"points")
else:
  print(player2,"wins with",p2_wins,"points")
