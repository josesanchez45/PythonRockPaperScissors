import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
rockPaperScissors = [rock, paper, scissors]
choice = input("Choose an option: 0 for rock, 1 for paper and 2 for scissors\n")
userChoice= int(choice)
computerChoice = random.randint(0,2)
if(userChoice != 1 or userChoice != 0 or userChoice != 2):
    print("Sorry not a valid number")
if userChoice == computerChoice:
    print(f"Your Choice: {rockPaperScissors[userChoice]}\n Computer chooses: {rockPaperScissors[computerChoice]}\n Its a Draw")
elif userChoice == 0 and computerChoice == 1:
    print(f"Your Choice:{rockPaperScissors[userChoice]}\nComputer chooses: {rockPaperScissors[computerChoice]}\n You Lose")
elif userChoice == 1 and computerChoice == 2:
    print(f"Your Choice:{rockPaperScissors[userChoice]} \n Computer chooses: {rockPaperScissors[computerChoice]}\n You Lose")
elif userChoice == 2 and computerChoice == 0:
    print(f"Your Choice:{rockPaperScissors[userChoice]}\nComputer chooses: {rockPaperScissors[computerChoice]}\n You Lose")
else:
    print(f"Your Choice:{rockPaperScissors[userChoice]}\nComputer chooses: {rockPaperScissors[computerChoice]}\n You Win")
