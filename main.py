import random

player_input = input("What do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors.")

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

choices = [rock, paper, scissors]

player_choice = choices[int(player_input)]

computer_choice = choices[random.randint(0,2)]

if player_choice == computer_choice:
  print(player_choice + f"\n Computer chose: \n {computer_choice} \n Draw" )
elif player_choice == "rock" and computer_choice == "scissors":
    print(player_choice + f"\n Computer chose: \n {computer_choice} \n You win" )
elif player_choice == "scissors" and computer_choice == "paper":
    print(player_choice + f"\n Computer chose: \n {computer_choice} \n You win" )
elif player_choice == "paper" and computer_choice == "rock":
    print(player_choice + f"\n Computer chose: \n {computer_choice} \n You win" )
else:
  print(player_choice + f"\n Computer chose: \n {computer_choice} \n You lose" )
