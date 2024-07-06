from datetime import datetime
from playsound import playsound
alarm_time=input("Enter the time:HH:MM:SS\n")
alarm_hr=alarm_time[0:2]
alarm_min=alarm_time[3:5]
alarm_sec=alarm_time[6:8]
alarm_period=alarm_time[9:11].upper()
print('setting up alarm')
while True:
    now=datetime.now()
    current_hr=now.strftime("%I")
    current_min=now.strftime("%M")
    current_sec=now.strftime("%S")
    current_period=now.strftime("%p")
    if(alarm_period==current_period):
        if(alarm_hr==current_hr):
            if(alarm_min==current_min):
                if(alarm_sec==current_sec):
                    print("Wake Up!")
                    playsound('C:\Users\Bhavya Danala\Desktop\60 py proj\Basic py proj\heatwaves.mp3')
                    break
    