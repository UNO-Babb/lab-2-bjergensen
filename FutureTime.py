#FutureTime.py
#Name:
#Date:
#Assignment:

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = (now.hour - 6) % 24
  currentMinute = now.minute


  #TODO:
  #Ask user for hours
  #Ask user for minutes
  hours_to_add = int(input("How many hours? "))
  minutes_to_add = int(input("how many minutes? "))
  
  
  #Calculate the time after the user-supplied time has passed.
  total_minutes = currentMinute + minutes_to_add
  futureMins = total_minutes % 60
  extraHour = (total_minutes // 60) + hours_to_add

  futureHour = (currentHour + extraHour) % 24

  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"
  print(f"Future time: {futureHour:02}:{futureMins:02}")

if __name__ == '__main__':
  main()
