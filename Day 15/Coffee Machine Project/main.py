
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]>= resources[item]:
            print(f"sorry there is not much {item}")
            return False
    return True

def process_coins():
    """:returns total calculated money"""
    total=int(input("please insert quaters: "))*0.25
    total+=int(input("please insert dimes: "))*0.15
    total+=int(input("please insert nickles: "))*0.10
    total+=int(input("please input pennies"))*0.05
    return total

def transaction_status(money_received,drink_cost):
    if money_received>=drink_cost:
        change=round(money_received-drink_cost,2)
        print(f"here is your change{change}")
        global profit
        profit+=drink_cost
        return True
    else:
        print("insufficient money, money refunded")
        return False

def make_coffee(drink_name, order_ingredients):
    """deduct ingredients from resources"""
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"here is your drink {drink_name} ")

profit=0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
machine_operation=True

while machine_operation:
    choice=input("would you want a espresso/latte/cappuccino: ")
    if choice=='turn off':
        machine_operation=False
    elif choice=='report':
        print(f"water:{resources['water']}")
        print(f"milk:{resources['milk']}")
        print(f"coffee:{resources['coffee']}")
        print(f"money made:{profit}")
    else:
        drink=MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
            payment=process_coins()
            if transaction_status(payment,drink['cost']):
                make_coffee(choice,drink['ingredients'])

