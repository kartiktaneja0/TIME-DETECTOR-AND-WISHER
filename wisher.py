import time
hour= int(time.strftime('%H'))
if hour>12 and hour<=18:
    print("Good afternoon sir")
elif hour>18:
    print("Good evening sir")
else:
    print("Good morning sir")
