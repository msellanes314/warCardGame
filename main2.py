




  #####################OLD
  import random

def shuffled_deck():
  basic_deck = list(range(2, 15)) * 4
  random.shuffle(basic_deck)
  return basic_deck

def compare_scores(play1,play2):
  if play1==play2:
    print("War has been declared")

    if len(p1_unused)<5:
      print("Maria does not have enough cards for war")
      return "p1 lost"

    elif len(p2_unused)<5:
      print("Josh does not have enough cards for war")
      return "p2 lost"
    

    if p1_unused[4]>p2_unused[4] and len(p1_unused)>=5 and len(p2_unused)>=5:
      print(player1,"has high card____-1")

      #original
      p1_wins.append(p1_unused[0])
      p1_wins.append(p2_unused[0])

      p1_unused.pop(0) 
      p2_unused.pop(0)

      #I
      p1_wins.append(p1_unused[0])
      p1_wins.append(p2_unused[0])

      p1_unused.pop(0) 
      p2_unused.pop(0) 

      #de
      p1_wins.append(p1_unused[0])
      p1_wins.append(p2_unused[0])

      p1_unused.pop(0) 
      p2_unused.pop(0) 

      #clare
      p1_wins.append(p1_unused[0])
      p1_wins.append(p2_unused[0])

      p1_unused.pop(0) 
      p2_unused.pop(0) 

      #war
      p1_wins.append(p1_unused[0])
      p1_wins.append(p2_unused[0])

      p1_unused.pop(0) 
      p2_unused.pop(0) 


    elif p2_unused[4]>p1_unused[4] and len(p1_unused)>=5 and len(p2_unused)>=5 :

      print(player2,"has high card___0")

      #original
      p2_wins.append(p1_unused[0])
      p2_wins.append(p2_unused[0])

      p1_unused.pop(0) 
      p2_unused.pop(0)

      #I
      p2_wins.append(p1_unused[0])
      p2_wins.append(p2_unused[0])

      p1_unused.pop(0) 
      p2_unused.pop(0) 

      #de
      p2_wins.append(p1_unused[0])
      p2_wins.append(p2_unused[0])

      p1_unused.pop(0) 
      p2_unused.pop(0) 

      #clare
      p2_wins.append(p1_unused[0])
      p2_wins.append(p2_unused[0])

      p1_unused.pop(0) 
      p2_unused.pop(0) 

      #war
      p2_wins.append(p1_unused[0])
      p2_wins.append(p2_unused[0])

      p1_unused.pop(0) 
      p2_unused.pop(0) 

  elif play1>play2:
    print(player1,"has high card__1")
    p1_wins.append(p1_unused[0])
    p1_wins.append(p2_unused[0])

    p1_unused.pop(0)
    p2_unused.pop(0)

    return play1
    
    # p1_unused.remove(p1_unused[0])
    # p2_unused.remove(p2_unused[0])

    # del p1_unused[0]
    # del p2_unused[0]

    #return play1

  else:
    print(player2,"has high card__2")
    p2_wins.append(p1_unused[0])
    p2_wins.append(p1_unused[0])

    p1_unused.pop(0)
    p2_unused.pop(0)

    return play2 
  

    # del p1_unused[0]
    # del p2_unused[0]

    # p1_unused.remove(p1_unused[0])
    # p2_unused.remove(p2_unused[0])

    #return play2

player1=input("First player, what is your name? ")
player2=input("Second player, what is your name? ")

print("Let us shuffle the deck...")
deck=shuffled_deck()

print("Let us split in half...")
p1_unused=deck[0:26]
p2_unused=deck[26:53]

#print(p1_unused)
#print(p2_unused)

# print(len(p1_unused))
# print(len(p2_unused))

# p1_unused.pop(0)
# p2_unused.pop(0)

# print(len(p1_unused))
# print(len(p2_unused))

p1_wins=[]
p2_wins=[]


while len(p1_unused)>0 or len(p2_unused)>0:
  p1_card=p1_unused[0]
  print(player1,"drew card",p1_card)
  p2_card=p2_unused[0]
  print(player2,"drew card",p2_card)

  compare_scores(p1_card,p2_card)

  print(player1,"score:",sum(p1_wins))      
  print(player2,"score:",sum(p2_wins))

  print("the lists")
  print(p1_unused)
  print(p2_unused)

  print("the lengths")
  print(len(p1_unused))
  print(len(p2_unused))

  if len(p1_unused)==0 or len(p2_unused)==0:
    break

  if compare_scores(p1_card,p2_card)=="p1 lost" or compare_scores(p1_card,p2_card)=="p2 lost":
    break

print("game over")

#################works so FutureWarning
#import random

# def shuffled_deck():
#   basic_deck = list(range(2, 15)) * 4
#   random.shuffle(basic_deck)
#   return basic_deck

# def compare_scores(play1,play2):
#   if play1==play2:
#     #if p1_unused[0]
#     pass
#     #WAR??
#   elif play1>play2:
#     print(player1,"has high card")
#     p1_wins.append(p1_unused[0])
#     p1_wins.append(p2_unused[0])

#     p1_unused.pop(0)
#     p2_unused.pop(0)

    
#     # p1_unused.remove(p1_unused[0])
#     # p2_unused.remove(p2_unused[0])

#     # del p1_unused[0]
#     # del p2_unused[0]

#     #return play1

#   else:
#     print(player2,"has high card")
#     p2_wins.append(p1_unused[0])
#     p2_wins.append(p1_unused[0])

#     p1_unused.pop(0)
#     p2_unused.pop(0)

#     # del p1_unused[0]
#     # del p2_unused[0]

#     # p1_unused.remove(p1_unused[0])
#     # p2_unused.remove(p2_unused[0])

#     #return play2

# player1=input("First player, what is your name? ")
# player2=input("Second player, what is your name? ")

# print("Let us shuffle the deck...")
# deck=shuffled_deck()

# print("Let us split in half...")
# p1_unused=deck[0:26]
# p2_unused=deck[26:53]

# print(p1_unused)
# print(p2_unused)

# # print(len(p1_unused))
# # print(len(p2_unused))

# # p1_unused.pop(0)
# # p2_unused.pop(0)

# # print(len(p1_unused))
# # print(len(p2_unused))

# p1_wins=[]
# p2_wins=[]


# i=0

# while len(p1_unused)>0 or len(p2_unused)>0:
#   p1_card=p1_unused[0]
#   print(player1,"drew card",p1_card)
#   p2_card=p2_unused[0]
#   print(player2,"drew card",p2_card)

#   compare_scores(p1_card,p2_card)

#   print(player1,"score:",sum(p1_wins))      
#   print(player2,"score:",sum(p2_wins))

#   print("the lists")
#   print(p1_unused)
#   print(p2_unused)

#   print("the lengths")
#   print(len(p1_unused))
#   print(len(p2_unused))

#   if len(p1_unused)==0 or len(p2_unused)==0:
#     break

# print("game over")


  #for i in range(0,min(len(p1_unused),len(p2_unused))):
      
#       if len(p1_unused)+1==0:
#         round=round+1
#         p1_unused=p1_unused+p1_wins
#         print("this ran")
    
#       elif len(p2_unused)+1==0:
#         round=round+1
#         p2_unused=p2_unused+p2_wins
#         print("this random")
      
   

#       winner=compare_scores(p1_card,p2_card)

#       p1_unused.remove(p1_unused[i])
#       p2_unused.remove(p2_unused[i])

#       print(player1,":",sum(p1_wins))
#       print(player2,":",sum(p2_wins))

      

#     if sum(p1_wins)==0 or sum(p2_wins)==0:
#       round=="end"
#       gameState=="Game Over"



##################################################
###   NEW
##############################################

# import random

# def shuffled_deck():
#   basic_deck = list(range(2, 15)) * 4
#   random.shuffle(basic_deck)
#   return basic_deck

# def compare_scores(play1,play2):
#   if play1>play2:
#     print(player1,"has high card")
#     p1_wins.append(p1_current[0])
#     p1_wins.append(p2_current[0])

#     del p1_current[0]
#     del p2_current[0]

#     return play1

#   elif play2>play1:
#     print(player2,"has high card")
#     p2_wins.append(p1_current[0])
#     p2_wins.append(p2_current[0])

#     del p1_current[0]
#     del p2_current[0]

#     return play2

#   elif play1==play2:
#     if len(p1_current)<6:
#       print(player1,"doesnt have enough cards to go to war")
#       return "player 1 loses"

#     elif len(p2_current)<6:
#       print(player2,"doesnt have enough cards to go to war")
#       return "player 2 loses"

#     elif len(p1_current)>=5 and len(p1_current)>=5:
#       print(" I declare war")
#       war1=p1_current[4]
#       war2=p2_current[4]

#       if war1>war2:
#         print(player1,"won this war")
      
#         p1_wins+p1_current[0:5]
#         p1_wins+p2_current[0:5]
      
#         del p1_current[0:5]
#         del p2_current[0:5]

#       elif war2>war1:
#         print(player2,"won this war")
      
#         p2_wins+p1_current[0:5]
#         p2_wins+p2_current[0:5]
      
#         del p1_current[0:5]
#         del p2_current[0:5]

# player1=input("First player, what is your name? ")
# player2=input("Second player, what is your name? ")

# print("Let us shuffle the deck...")
# deck=shuffled_deck()

# print("Let us split in half...")
# p1_current=deck[0:26]
# p2_current=deck[26:53]

# p1_wins=[]
# p2_wins=[]

# round1="ongoing"

# while round1=="ongoing":

#   p1_card=p1_current[0]
#   print(player1,"drew card",p1_card)
#   p2_card=p2_current[0]
#   print(player2,"drew card",p2_card)

#   compare_scores(p1_card,p2_card)

#   print(player1,"score:",sum(p1_wins))
#   print(player2,"score:",sum(p2_wins))

#   if compare_scores(p1_card,p2_card)=="player 1 loses":
#     round1="over"
#     print(player2," wins")

#   elif compare_scores(p1_card,p2_card)=="player 2 loses":
#     round1="over"
#     print(player1," wins")

#   if len(p1_current)==0 or len(p2_current)==0:
#     round1="over"

# print("game over")
  
