import random as r

win_list = [['Paper', 'Rock'],['Scissors', 'Paper'], ['Rock', 'Scissors']]
lose_list = [['Rock', 'Paper'],['Paper', 'Scissors'],['Scissors', 'Rock']]

def rps():
    player_one = input("Rock, paper, scissors: ")
    player_two = r.choice(["Rock", "Paper", "Scissors"])
    print(f"Computer chose: {player_two}")

    print([player_one, player_two])

    if player_one == player_two:
        print("It's a tie!")
        return
    
    elif [player_one, player_two] in win_list:
        print("You win!")
        return

    elif [player_one, player_two] in lose_list:
        print("Computer wins!")
        return

rps()