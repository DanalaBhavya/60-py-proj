import random
choices=["rock","paper","scissors"]
computer=random.choice(choices)
player=False
cscore=0
pscore=0
while True:
    player=input("rock,paper,scissors?").capitalize()
    if player==computer:
        print("tie")
    elif player=="rock":
        if computer=="paper":
            print("player lose")
            cscore+=1
        else:
            print("player win")
            pscore+=1
    elif player=="paper":
        if computer=="scissors":
            print("player lose")
            cscore+=1
        else:
            print("player win")
            pscore+=1
    elif player=="scissors":
        if computer=="rock":
            print("player lose")
            cscore+=1
        else:
            print("player win")
            pscore+=1
    elif player=="End":
        print("final scores:")
        print("Player score:",pscore)
        print("computer score:",cscore)
        break        
                