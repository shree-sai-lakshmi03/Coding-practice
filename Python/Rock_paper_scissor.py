import random
print("Welcome to the rock paper scissor game")
game_elements=["rock","paper","scissor"]
print("This is a game of 11 rounds, its against you and the computer and the team which wins the most rounds will be the final winner")
print("type your answer in lower case. eg:scissor,paper,rock")
comp_wins=0
user_wins=0
draw_rounds=0
for k in range(11):
    n=str(input("Enter your choice:"))
    computer=random.choice(game_elements)
    if n=="rock":
        if computer=="scissor":
            user_wins+=1
            print("computer chose scissor")
            print("yay!!! you won this round")
        elif computer=="paper":
            comp_wins+=1
            print("computer chose paper")
            print("oof!! computer outsmarted you, its okay:)")
        else:
            draw_rounds+=1
            print("computer chose rock")
            print("its a draw round!!!")
    elif n=="paper":
        if computer=="scissor":
            comp_wins+=1
            print("computer chose scissor")
            print("oof!! computer outsmarted you, its okay:)")
        elif computer=="rock":
            user_wins+=1
            print("computer chose rock")
            print("yay!!! you won this round")
        else:
            draw_rounds+=1
            print("computer chose paper")
            print("its a draw round!!!")
    elif n=="scissor":
        if computer=="paper":
            user_wins+=1
            print("computer chose paper")
            print("yay!!! you won this round")
        elif computer=="rock":
            comp_wins+=1
            print("computer chose rock")
            print("oof!! computer outsmarted you, its okay:)")
        else:
            draw_rounds+=1
            print("computer chose scissor")
            print("its a draw round!!!")
    else:
        print("invalid input!!! try again")
print("Game over!! excited to see the results? i hope its a yes!! ill show it anyway lol")
print("computer wins:",comp_wins)
print("your wins:",user_wins)
print("Draw rounds:",draw_rounds)
if comp_wins>user_wins:
    print("computer won")
elif user_wins>comp_wins:
    print("you win")
elif user_wins==comp_wins:
    print("still a draw!!!! :()")
print("okay byw bywwwwww!!!!!")
