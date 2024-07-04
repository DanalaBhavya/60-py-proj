import random
pwlen=int(input("Enter the length of password:"))
s="abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
password="".join(random.sample(s,pwlen))
print(password)
