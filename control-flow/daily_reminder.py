# control-flow/daily_reminder.py

task = input("Enter your task: ")
reminders = int(input("How many times should I remind you? "))

count = 0
while count < reminders:
    print(f"Reminder: {task}")
    count += 1
