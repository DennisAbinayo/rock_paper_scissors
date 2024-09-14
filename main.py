import random
import time

print(("\nWelcome to the rock, paper, scissors game!\n").upper())
time.sleep(3)
print("You have 5 rounds to play against the computer.")
print("Enter 'rock', 'paper', or 'scissors' to make your choice.")
time.sleep(4)
print("\nGood luck!")
time.sleep(3)


rounds = 5
user_count = 0
computer_count = 0

while 0 < rounds <= 5:
    computer_choice = random.choice(['scissors', 'rock', 'paper'])
    
    user_choice = input('\nMake a choice between (rock, paper, scissors): ').lower()
    if user_choice not in ['rock', 'paper', 'scissors']:
        print("\nInvalid choice. Please choose rock, paper, or scissors.")
        continue

    if user_choice == computer_choice:
        tie_result = "It's a Tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        user_result = 'User wins!'
        user_count += 1
    else:
        computer_result = 'Computer wins!'
        computer_count += 1

    rounds -= 1

    if user_count == 3 or computer_count == 3:
        break

    time.sleep(1)  

# Final score and result
print("\nGame over!")
print(f'Result:\nUser score: {user_count} Computer score: {computer_count}')
if user_count > computer_count:
    print(f"\n{user_result}")
elif user_count < computer_count:
    print("\n{computer_result}")
else:
    print("\nIt's a tie!")