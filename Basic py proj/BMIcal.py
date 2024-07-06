H=float(input("Enter your height in cm:"))
W=float(input("Enter your weight in kg:"))
H=H/100
BMI=W/(H*H)
print("Your body mass index is: ",BMI)
if(BMI>0):
    if(BMI<=18.5):
        print("You are underweight")
    elif(BMI<=25):
        print("you are healthy")
    else:
        print("you are overweight")
else:
    print("enter valid details")        
                
        