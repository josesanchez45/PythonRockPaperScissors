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
if userChoice == computerChoice:
    print(f"{rockPaperScissors[userChoice]}\n{rockPaperScissors[computerChoice]}\n Its a Draw")
elif userChoice == 0 and computerChoice == 1:
    print(f"{rockPaperScissors[userChoice]}\n{rockPaperScissors[computerChoice]}\n You Lose")
elif userChoice == 1 and computerChoice == 2:
    print(f"{rockPaperScissors[userChoice]} \n{rockPaperScissors[computerChoice]}\n You Lose")
elif userChoice == 2 and computerChoice == 0:
    print(f"{rockPaperScissors[userChoice]}{rockPaperScissors[computerChoice]} You Lose")
else:
    print(f"{rockPaperScissors[userChoice]}{rockPaperScissors[computerChoice]} You Win")
