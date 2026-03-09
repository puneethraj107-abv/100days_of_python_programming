import random
from art import logo
def deal_card():
    """deal a card"""
    cards=[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(cards)
    return card
def calculate_score(cards):
    """take a list of cards and return the calculated score from the cards"""
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(u_score, c_score):
    if u_score==c_score:
        return "its a draw"
    elif c_score==0:
        return "dealer has a blackjack, you lose"
    elif u_score==0:
        return "black jack, you win"
    elif u_score>21:
        return "score out of bound, you lose"
    elif c_score>21:
        return "opponent went over, you win"
    elif u_score>c_score:
        return "you win"
    else:
        return "you lose"

def playgame():
    user_cards=[]
    computer_cards=[]
    user_score=-1
    computer_score=-1
    game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)

        print(f"your cards are {user_cards}, and score is {user_score}")
        print(f"dealers first hand is {computer_cards[0]}")
        if user_score==0 or computer_score==0 or user_score>21:
            game_over=True
        else:
            user_should_deal=input("want another card (y)/(n): ")
            if user_should_deal=="y":
                user_cards.append(deal_card())
            else:
                game_over=True

    while computer_score!=0 and computer_score<17:
        computer_cards.append(deal_card())
        computer_score=calculate_score(computer_cards)

    print(f"your final hand is {user_score} and {user_cards}")
    print(f"dealers final hand is {computer_score} and {computer_cards}")
    print(compare(user_score,computer_score))


print(logo)
while input("do you wanna play a game of blackjack(bj)")=="bj":
    print("\n"*30)
    playgame()
