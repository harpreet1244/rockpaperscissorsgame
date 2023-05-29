##HOW TO MAKE ROCK PAPER SCISSORS GAME
import random
human_wins=0
computer_wins=0
rock_count=0
paper_count=0
scissors_count=0
rock_wins=0
paper_wins=0
scissors_wins=0
b=int(input("enter the rounds:"))
for i in range(b):
     a=0
     while a==0:
          human=input("enter your choice").lower()#choices(rock,paper,scissors)
          if human=="scissors" or human=="rock" or human=="paper":
               a+=1
               if human=="rock":
                  rock_count+=1
               if human=="paper":
                  paper_count+=1
               if human=="scissors":
                  scissors_count+=1
             
          else:
               print("please enter a valid choice")
     if human=="rock":
         print("human choice rock")
     elif human=="paper":
         print("human choice paper")
     elif human=="scissors":
         print("human choice scissors")
     c=["rock","paper","scissors"]#COMPUTER CHOICES
     computer=random.choice(c)
     print("computer select:",computer)
     if human==computer:#IF THEY HAVE CHOOSED SAME 
        print("tie")
     elif (human=="rock" and computer=="scissors"):
           human_wins+=1
           rock_wins+=1
           print("human won")
     elif (human=="paper" and computer=="rock"):
           human_wins+=1
           paper_wins+=1
           print("human won")
     elif(human=="scissors"and computer=="paper"):
          human_wins+=1
          scissors_wins+=1
          print("human won")
     
        
     else:
        computer_wins+=1
        print("computer won")
print("human won",human_wins,"times")
print("computer won",computer_wins,"times")
#to calculate the percentage
print("HOW MANY TIME ROCK CHOOSED",rock_count/b*100)#HOW MANY TIME ROCK CHOOSED
print("when rock wins",rock_wins/b*100)#when rock wins
print("HOW MANY TIMES PAPER CHOOSED",paper_count/b*100)#HOW MANY TIMES PAPER CHOOSED
print("when paper wins",paper_wins/b*100)#when paper wins
print("HOW MANY TIMES SCISSORS CHOOSED",scissors_count/b*100)#HOW MANY TIMES SCISSORS CHOOSED
print("scissors wins",scissors_wins/b*100)#scissors wins


