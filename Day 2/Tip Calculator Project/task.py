print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

total_bill=(bill/100)*tip+bill
split_amount=total_bill/people
print(total_bill)
print(f"each person has to pay ${split_amount}")
