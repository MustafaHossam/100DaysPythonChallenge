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
randNum = random.randint(0,2)
yourChoice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
if(yourChoice == 0) : 
    print(rock)
elif yourChoice == 1 : 
    print(paper)
else :
    print(scissors)

print("Computer chose:")
if(randNum == 0) : 
    print(rock)
elif randNum == 1 : 
    print(paper)
else :
    print(scissors)

#All Win Cases
if (yourChoice == 0 and randNum == 2) or (yourChoice == 1 and randNum ==0) or (yourChoice == 2 and randNum == 1):
    print("You win!")
#Draw Case
elif(yourChoice == randNum) :
    print("Draw")
else :
    print("You Lose!")