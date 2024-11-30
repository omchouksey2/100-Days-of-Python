import random 
Rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''

paper='''
    _______
---'   ____)____
          ______)
          _______)
          _______)
---.__________)'''

scissor='''
    _______
---'   ____)____
          ______)
        __________)
      (____)
---.__(___)'''

list=[Rock,paper,scissor]
random_vriable=random.randint(0,2)
Your_choice=int(input("Enter 0 for Rock, 1 for Paper, 2 for Scissor. "))
print("\nComputer choice: \n",list[random_vriable])
if Your_choice==random_vriable:
      print("Draw")
elif Your_choice==0:
    print("\nYour Choice",'''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)    ''')
    if Your_choice==0 and random_vriable==1:
            print("Computer win's! You Lose.")
    if Your_choice==0 and random_vriable==2:
                print("You win!")
elif Your_choice==1:
    print("\nYour Choice",'''
    _______
---'   ____)____
          ______)
          _______)
          _______)
---.__________)''')                 
    if Your_choice==1 and random_vriable==0:
        print("You win!")
    if Your_choice==1 and random_vriable==2:
                print("You lose!")
elif Your_choice==2:
    print("\nYour Choice",'''
    _______
---'   ____)____
          ______)
        __________)
      (____)
---.__(___)''')                
    if Your_choice==2 and random_vriable==0:
        print("computer win's! You lose.")
    if Your_choice==2 and random_vriable==1:
            print("You win!")
else:
    print("Invalid choice")


