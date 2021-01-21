# An alarm clock is a clock with a function that can be activated to ring at a time set in advance, used to wake someone up

# our task here is to write a python script that creates an alarm clock.
# For this task, I will be using the DateTime module in Python to create an alarm clock and
# the sound library in Python to play the alarm sound.

from datetime import datetime
from playsound import playsound

alarm_time = input("Enter the time of alarm to be set:HH:MM:SS\n")
alarm_hour = alarm_time[0:2]
# print(alarm_hour)
alarm_minute = alarm_time[3:5]
# print(alarm_minute)
alarm_seconds = alarm_time[6:8]
# print(alarm_seconds)
alarm_period = alarm_time[9:11].upper()
# print(alarm_period)
print("Setting up alarm..")

while True:
    now = datetime.now()
    current_hour = now.strftime("%I") #%I Hour 00-12
    current_minute = now.strftime("%M")
    current_seconds = now.strftime("%S")
    current_period = now.strftime("%p") # %p AM/PM

    if alarm_period == current_period:
        if alarm_hour == current_hour:
            if alarm_minute == current_minute:
                if alarm_seconds == current_seconds:
                    print("Wake Up!")
                    playsound('audio.mp3')
                    break