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

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients, drink_name):
    """returns true if there is enough ingredients to make the coffee or else returns false."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry not enough {item} to make {drink_name}.")
            return False
    return True


def process_coins():
    """Returns the total calculated amount of the coins inserted."""
    print("Please Insert Coins")
    total = int(input("How many Quarters: ")) * 0.25
    total += int(input("How many Dime: ")) * 0.10
    total += int(input("How many Nickles: ")) * 0.05
    total += int(input("How many Pennies: ")) * 0.01
    return total


def is_transaction_successful(amount_received, drink_cost):
    """returns true if payment is accepted or else returns false"""
    if amount_received >= drink_cost:
        change = round(amount_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, That's not enough amount. Money refunded.")


def make_coffee(drink_name, order_ingredients):
    """Use the required ingredients from the resources"""
    for items in order_ingredients:
        resources[items] -= order_ingredients[items]
    print(f"Here is your {drink_name} ☕, Thank you for your order.")


is_on = True

while is_on:
    print("Welcome to the Coffee Machine.")
    print('Instructions: Type "report" to get info on the resources / Type "off" to switch off the coffee machine.')
    customer_order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if customer_order == "off":
        is_on = False
    elif customer_order == "report":
        print(f'Water: {resources["water"]}ml')
        print(f'Milk: {resources["milk"]}ml')
        print(f'Coffee: {resources["coffee"]}g')
        print(f'Money: ${profit} \n')
    else:
        drink = MENU[customer_order]
        if is_resource_sufficient(drink["ingredients"], customer_order):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(customer_order, drink["ingredients"])
