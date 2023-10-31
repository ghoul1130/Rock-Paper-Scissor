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
ch = int(input("What do you choose? type 0:Rock 1:Paper 2:Scissor "))
option = [rock,paper,scissors]

if ch>2 or ch<0:
  print("Invalid Choice")
else:
  print("Your choice:")
  print(option[ch])
  
import random
a = random.randint(0,2)
print("COmputer's choice:")
print(option[a])



if ch == 0 and a==0:
  print("Draw")
elif ch==0 and a==1:
  print("You lose")
elif ch==0 and a==2:
  print("You win")

if ch == 1 and a==1:
  print("Draw")
elif ch==1 and a==2:
  print("You lose")
elif ch==1 and a==0:
  print("You win")

if ch == 2 and a==2:
  print("Draw")
elif ch==2 and a==0:
  print("You lose")
elif ch==2 and a==1:
  print("You win")