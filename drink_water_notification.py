from plyer import notification
import time
title = input("Enter the title: ")
msg = input("Enter the message: ")
duration = input("Enter the repeat time duration in seconds: ")
while true: 
    notification.notify(title = title, message = msg, timeout = 10)
    time.sleep(duration)  #seconds