from data import MENU, resources, coins


def print_report(resource_values, money_left):
    print(f'Water: {resource_values["water"]}ml')
    print(f'Milk: {resource_values["milk"]}ml')
    print(f'Coffee: {resource_values["coffee"]}g')
    print(f'Money: ${money_left}')


def check_resources(drink, requirements, resources_left):
    for resource in resources_left:
        if requirements[drink][resource] > resources_left[resource]:
            print(f'Sorry, there is not enough {resource}')
            return False
    return True


def process_coins(coins_type):
    cash = 0
    for coin in coins_type:
        count = int(input(f'How many {coin}s? '))
        cash += count * coins_type[coin]
    return cash


money = 0
drink_type = None

while True:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == "report":
        print_report(resources, money)
        continue
    elif user_input == "off":
        print("Machine is offline")
        break
    else:
        drink_type = user_input

    if check_resources(drink_type, MENU, resources):
        money += process_coins(coins)
        if money >= MENU[drink_type]["cost"]:
            money -= MENU[drink_type]["cost"]

