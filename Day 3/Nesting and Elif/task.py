print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("what's you're age kid: "))
    if age < 12:
        print("the bill is $5")
    elif age > 18:
        print("the bill is $18")
    else:
        print("you're bill is $7")

else:
    print("Sorry you have to grow taller before you can ride.")
