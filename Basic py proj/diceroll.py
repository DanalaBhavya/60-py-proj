import random
min=1
max=6
roll="yes"
while roll=="yes" or roll=="y":
    print("Rolling the dice")
    print("the values are:")
    print(random.randint(min,max))
    print(random.randint(min,max))
    roll=input("roll the dices again?")
    