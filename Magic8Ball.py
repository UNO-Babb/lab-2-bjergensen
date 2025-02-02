#Magic8Ball.py
#Name:
#Date:
#Assignment:

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  print("Gag Magic 8 Ball")
  #Prompt the user for their question.
  answers = ["yes", "No", "Maybe so", "I can't help you, I am a simple program"]
  input("what is your question?")
  #Answer question randomly with one of the options from your earlier list.
  response = random.choice(answers)
  print(response)

if __name__ == '__main__':
  main()
