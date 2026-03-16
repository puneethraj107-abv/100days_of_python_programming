import random
from art import logo,vs
from game_data import data

print(logo)

#chose a random item for a list and add it to list a

comparison_list = []


game_over=False
score=0
b_item = random.choice(data)

while not game_over:

    b_value = b_item['follower_count']
    a_item = random.choice(data)
    if a_item==b_item:
        a_item=random.choice(data)
    a_value=a_item['follower_count']


    print(f"compare B: the personality is {b_item["name"]}, he/she is a {[b_item["description"]]} from {b_item["country"]} \n\n\n")
    print(f"{vs}\n\n\n")
    print(f"compare A: the personality is {a_item["name"]}, he/she is a {[a_item["description"]]} from {a_item["country"]} \n\n\n")
    guess=input("guess is A higher or lower ").lower()


    if guess=='higher' and b_value<a_value:
        print("congratulation you were right\n")
        score+=1
        b_item=a_item



    elif guess=='lower' and b_value>a_value:
        print("congratulation you were right\n")
        score+=1
        b_item=a_item


    else:
        print("you were wrong, better luck next time")
        print(f"your score is {score}")
        game_over = True


