import random
from art import logo


def play_game():
    level = input("do you want the EASY LEVEL or the HARD LEVEL ").upper()
    tries=0
    if level=="EASY":
        tries=10
    elif level=="HARD":
        tries=5
    num_to_guess=random.randint(1,100)
    game_over=False
    while not game_over:

        guess = int(input("guess a number between 1 to 100 "))
        if guess < num_to_guess:
            print("too low")
            tries-=1
        elif guess>num_to_guess:
            print("too high")
            tries-=1
        else:
            print("you got the guess right")
            game_over=True
        if tries>0:
            print(f"you have {tries} left")
        else:
            print(f"you have {tries} left, the correct guess was {num_to_guess} you lose")
            game_over=True

game=input("do wanna play the guess game: ").lower()
if game=="y":
    print("\n"*30)
    print(logo)
    play_game()