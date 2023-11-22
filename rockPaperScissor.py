def rock_paper_scissor(num1,num2,bit1,bit2):
    p1=int(num1[bit1])%3
    p2=int(num2[bit2])%3
    if(player_one[p1]==player_two[p2]):
        print("Draw!")
    elif(player_one[p1]=="rock" and player_two[p2]=="scissor"):
        print("Player one wins!")
    elif(player_one[p1]=="rock" and player_two[p2]=="paper"):
        print("Player two wins!")
    elif(player_one[p1]=="paper" and player_two[p2]=="scissor"):
        print("Player two wins!")
    elif(player_one[p1]=="paper" and player_two[p2]=="rock"):
        print("Player one wins!")
    elif(player_one[p1]=="scissor" and player_two[p2]=="rock"):
        print("Player two wins!")
    elif(player_one[p1]=="scissor" and player_two[p2]=="paper"):
        print("Player one wins!")
player_one =  {0:'rock', 1:'paper', 2:'scissor'}
player_two =  {0:'rock', 1:'paper', 2:'scissor'}
while(1):
    num1=input("Player 1: Enter your choice: ")
    num2=input("Player 2: Enter your choice: ")
    bit1=int(input("player 1: Enter your secret bit position: "))
    bit2=int(input("player 2: Enter your secret bit position: "))
    rock_paper_scissor(num1,num2,bit1,bit2)
    ch=input("Do you want to continue? (y/n): ")
    if(ch=='n'):
        break

player_one =  {0:'rock', 1:'paper', 2:'scissor'}
player_two =  {0:'rock', 1:'paper', 2:'scissor'}
while(1):
    num1=input("Player 1: Enter your choice: ")
    num2=input("Player 2: Enter your choice: ")
    bit1=int(input("player 1: Enter your secret bit position: "))
    bit2=int(input("player 2: Enter your secret bit position: "))
    ch=input("Do you want to continue? (y/n): ")
    if(ch=='n'):
        break

