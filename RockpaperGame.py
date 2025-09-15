import random

options = ("rock", "Paper", "scissor")
player = None
player_pt = 0
computer_pt = 0

is_running = True
while is_running:
    computer = random.choice(options)
    player = input("Enter a choice (rock, paper, scissor (quit to exit):")
    print(f"computer : {computer}")
    if player == "rock" or player == "scissor" or player == "paper" or player == "quit":
       if computer== "rock" and player == "paper":
        player_pt += 1
       elif computer== "rock" and player == "scissor":
        computer_pt +=1
       elif  computer=="scissor" and player== "paper" :
        computer_pt +=1
       elif computer == "scissor" and player == "rock":
        player_pt += 1
       elif computer == "paper" and player == "rock":
        computer_pt += 1       
       elif computer == "paper" and player == "scissor":
        player_pt +=1     
       elif player == "quit":
        is_running=False  
           
    else:
      print("Enter valid choice") 
       
print(f"Score is: player>{player_pt}  computer>{computer_pt}")
     
     
 
      
 
      
    