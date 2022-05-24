import random

def get_user_choice():
    return input("Enter: ")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def get_winner():
    winner = ''
    computer_wins = 0
    user_wins = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print("Computer choice:", computer_choice)

        if (computer_choice == user_choice):
            print("draw")
        elif (user_choice == "rock") and (computer_choice == "paper"):
            print("you have lost")
            computer_wins += 1
            print(computer_wins)
        elif (user_choice == "rock") and (computer_choice == "scissors"):
            print("you have won")
            user_wins += 1
            print(user_wins)
        elif (user_choice == "paper") and (computer_choice == "rock"):
            print("you have won")
            user_wins += 1
            print(user_wins)
        elif (user_choice == "paper") and (computer_choice == "scissors"):
            print("you have won")
            user_wins += 1
            print(user_wins)
        elif (user_choice == "scissors") and (computer_choice == "rock"):
            print("you have lost")
            computer_wins += 1
            print(computer_wins)
        elif (user_choice == "scissors") and (computer_choice == "paper"):
            print("you have won")
            user_wins += 1
            print(computer_wins)

        if user_wins == 3 or computer_wins == 3:
            break

    print("User Wins: ", user_wins)
    print("Computer Wins: ", computer_wins)

def play():
    get_winner()
    print()
 
play()


""" 
if person 1 = rock & person 2 = rock -> draw
if person 1 = rock & person 2 = scissors -> person 1 wins
if person 1 = rock & person 2 = paper -> person 1 loses

 """
