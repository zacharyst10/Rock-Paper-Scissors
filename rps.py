import random

wins = 0
losses = 0
ties = 0

def results():
    return f'\n{wins} Wins | {losses} Losses | {ties} Ties\n'

while True:
    user_choice = input('Choose one (rock, paper, scissors): ')
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    print(f'\nYou chose {user_choice}, the computer chose {computer_choice}. \n')

    if user_choice == computer_choice:
        ties += 1 
        print(f'Both players selected {user_choice}. It is a tie')
        print(results())
    elif user_choice == 'rock':
        if computer_choice == 'scissors':
            wins += 1
            print('rock smashes scissors, you win')
            print(results())
        else:
            losses += 1 
            print('paper covers rock, you lose')
            print(results())
    elif user_choice == 'paper':
        if computer_choice == 'rock':
            wins += 1 
            print('paper covers rock, you win')
            print(results())
        else:
            losses += 1 
            print('scissors cut paper, you lose')
            print(results())
    elif user_choice == 'scissors':
        if computer_choice == 'paper':
            wins += 1 
            print('scissors cut paper, you win')
            print(results())
        else:
            losses +=1 
            print('rock smashes scissors, you lose')
            print(results())

    play_again = input('play again? (y/n): ')
    if play_again.lower() != 'y':
        break






