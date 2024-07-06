def check(guess,ans):
    global score
    still_guessing=True
    attempt=0
    while still_guessing and attempt<3:
        if guess==ans:
            print("correct answer!")
            score+=1
            still_guessing=False
        else:
            if attempt<2:
                guess=input("Sorry wrong answer,try again")
            attempt+=1
    if attempt==3:
        print("The correct answer is",ans)
score=0
print("Guess the Animal")
g1=input("what is the national animal of India?")
check(g1,"Tiger")
g2=input("which is the largest animal?") 
check(g2,"Blue whale")
print("Score is"+str(score))       