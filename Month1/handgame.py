import random
b = ["scissiors", "paper", "rock"]
def game():
    while True:
        opp_chc = random.choice(b)
        user_chc = str(input("Enter your choice ")).lower()
        print("You chose " +user_chc)
        print("Opponent chose " +opp_chc)
        if opp_chc == "scissiors" and user_chc == "rock":
            print("You win!!")
            break
        elif opp_chc == "scissiors" and user_chc == "paper":
            print("You loose!!")
            break
        elif opp_chc == "rock" and user_chc == "paper":
            print("You win!!")
            break
        elif opp_chc == "rock" and user_chc == "scissiors":
            print("You loose!!")
            break
        elif opp_chc =="paper" and user_chc =="scissiors":
            print("You win!!")
            break
        elif opp_chc == "paper" and user_chc == "rock":
            print("You loose!!")
            break
        elif opp_chc == user_chc:
            print("Draw!! Try again")
        else:
            print('Invalid Input!!!')
game()