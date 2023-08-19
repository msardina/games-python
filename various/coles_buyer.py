import time
import random
robbed = 0
print("Welcome to food getter")
time.sleep(2)
instructions = input("Instructions(y/n) ")
if instructions == "y":
    # print instructions
    print("To win the game you must get all the new items.")
    print("To get items you must buy all items available using your money.")
    print("If you run out of money you need to work. Working gives you $10 but takes away an item.")
    print("You may get robbed...")

# value of items
menu = {'chicken' : random.randint(0, 10)}
new_items = ["alfajor", "soda", "cocacola", "water", "coffee"]


#setup
money = 20
items_on_menu = 1
items_got = 0
items_collected = []

counter_of_new_items = 0
def print_menu(money, menu):
    print("")
    print(f"Money: ${money}")
    n = 1
    for food in menu:
        print(f"{n}.{food} = ${menu[food]}")
        n = n + 1
        
def work(cash, menu):
    for i in range(0, random.randint(1, 25)):
            print("working... Please wait")
            cash = cash + 1
            time.sleep(0.1)
    keys_of_menu = menu.keys()
    menu.pop(random.choice(list(keys_of_menu)))
    return cash

def collected_all_menu(menu, collected):
    for food in menu:
        if not food in collected:
            return False

    return True

while money > 0:
    robbed = random.randint(5, 10)
    if collected_all_menu(menu, items_collected):
        print("NEW  ITEM!!!")
        items_collected = []
        new_item = random.choice(new_items)
        while new_item in items_collected:
            new_item = random.choice(new_items)
            
        print(new_item)
        menu[new_item] = random.randint(0, 10) 

    if robbed == 5:
        print("YOU GOT ROBBED!")
        print('YOU LOSE $5')
        money = money - 5

    print_menu(money, menu)
    print(f'You have these items: {items_collected}')
    get_item = input("Buy item or x to work: ")
    if get_item == "x":
        money = work(money, menu)
        items_got = items_got - 1
    elif get_item in menu.keys():
        money = money - menu[get_item]
        items_collected.append(get_item)
    else: # Item selected is not in menu
        print("")
        print("Sorry not in menu. :(, we may serve that another time(time: never)")
        
# You lose!!!!!!
print("YOU LOSE!!!")
print("You lost you money!")
        