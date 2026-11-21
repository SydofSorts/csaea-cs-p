import random 
import time

# Player's goal is to get $10,000
player_savings = 0
player_inventory = []
items_selling = []
items_sold = []
pocket = ["phone", "wallet", "chapstick", "car keys", "coupon", "wired earbuds"]

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
def selling(items_selling):
    for item in items_selling:
        if item == "a phone":
            given_price = random.randint(300.00, 900.00)
            print(f"I'll give you {given_price} dollars.")
            
            haggle_answer = input("Would you like to haggle?")
            haggle(given_price, haggle_answer)


print("You are in debt to loansharks and need $10,000 to pay them off.")
time.sleep(1)
print("You don't have a job, but you're pretty sly.")
time.sleep(1)
print("Pick-pocket people to get items. Sell what you can to Dan. He'll give you cash.\n")
            
while player_savings < 10000:
    scenario = ["You see a woman jogging.", "You see a man sitting at a bus stop.", "You see a teen on their phone.",
                "You see a couple laughing on a walk.", "You see a guy sleeping on a bench.", 
                "You see a mother with three kids.", "You see a contruction worker.", "You see someone in a trenchcoat."]
    print(random.choice(scenario))
    player_ready = input("Pick-pocket them?: ")
    if player_ready.lower() == "yes":
        caught = random.randint(1,2)
        if caught == 1:
            item_gotten = random.choice(pocket)
            print(f"You got {item_gotten}.")
            player_inventory.append(item_gotten)
            print(player_inventory, "\n")
        else:
            print("You got caught, but ran away just in time. Good thing that you're fast.\n")
    elif player_ready.lower() == "no":
        print("Your loss.\n")
        

    

                                   
                   
            
                
                   
                              
                



    





