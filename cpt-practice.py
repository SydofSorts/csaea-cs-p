import random 
import time

# Player's goal is to get $10,000


player_savings = 0
player_inventory = []
items_sold = []
wallet = random.randint(1, 20)
pocket = ["phone", wallet, "chapstick", "car keys", "coupon", "wired earbuds"]

# If the haggling works or not
def haggle(number):
    coinflip_chance = random.randint(1, 4)
    if coinflip_chance == 3:
        new_price = number * 2
        print(f"You drive a hard bargain. And I give a fair price. I'll give you {new_price} dollars.")
        print(f"You've gained ${new_price}")
        player_savings += new_price
    else:
        print(f"No can do. I gave you a fair price.")
        player_savings += number

# If the player haggles or not
def haggle_check(given_price, haggle_answer):
    if haggle_answer.lower() == "yes":
        number = input(f"Enter previously given price: ")
        if number == given_price:
            haggle(number)
        else:
            print("That ain't the price I gave you.")
            number = input(f"Enter previously given price: ")
    elif haggle_answer.lower() == "no":
        print(f"You've gained ${given_price}")
        player_savings += given_price
    else:
        print(f"I need a clear 'yes' or 'no', kid.")
        haggle_answer = input("Would you like to haggle?")

# What the player is selling
def selling(items_sold):
    for item in items_sold:
        if item == "phone":
            given_price = random.randint(300.00, 900.00)
            print(f"I'll give you {given_price} dollars.")
            
            haggle_answer = input("Would you like to haggle?")
            haggle(given_price, haggle_answer)


            
                                   
                                   
                   
            
                
                   
                              
                



    





