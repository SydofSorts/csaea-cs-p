import random 
import time

# Player's goal is to get $10,000
player_savings = 0
steal_counter = 0
player_inventory = []
items_sold = []
pocket = ["phone", "wallet", "chapstick", "car keys", "coupon", "wired earbuds"]

# If the haggling works or not
def haggle(number, player_savings):
    coinflip_chance = random.randint(1, 4)
    if coinflip_chance == 3:
        new_price = number * 2
        print(f"You drive a hard bargain. And I give a fair price. I'll give you {new_price} dollars.")
        print(f"You've gained ${new_price}\n")
        player_savings += new_price
        selling(player_inventory, player_savings)
    else:
        print(f"No can do. I gave you a fair price.\n")
        player_savings += number
        selling(player_inventory, player_savings)

# If the player haggles or not
def haggle_check(given_price, haggle_answer, player_savings):
    if haggle_answer.lower() == "yes":
        print("---------------------------------------------------------------------------")
        time.sleep(1.5)
        number = float(input(f"Enter previously given price AS A NUMBER (no dollar sign): "))
        print("---------------------------------------------------------------------------")
        if number == given_price:
            haggle(number, player_savings)
        else:
            print("That ain't the price I gave you.")
            haggle_check(given_price, haggle_answer, player_savings)
    elif haggle_answer.lower() == "no":
        print(f"You've gained ${given_price}\n")
        player_savings += given_price
        selling(player_inventory, player_savings)
    else:
        print(f"I need a clear 'yes' or 'no', kid.")
        haggle_answer = input("Would you like to haggle?   ")
        haggle_check(given_price, haggle_answer, player_savings)

# What the player is selling
def selling(player_inventory, player_savings):
    for item in (player_inventory):
        if item == "a phone":
            player_inventory.pop(0)
            given_price = round(random.uniform(300.00, 900.00), 2)
            print(f"Impressive. Getting a phone. I'll give you {given_price} dollars.")
            
            haggle_answer = input("Would you like to haggle?   ")
            haggle_check(given_price, haggle_answer, player_savings)
            items_sold.append(item)
        elif item == "wallet":
            player_inventory.pop(0)
            given_price = round(random.uniform(1.00, 50.00), 2)
            print("I'll give you the cash in this wallet.")
            print(f"You've gained ${given_price}.")
            player_savings += given_price
            items_sold.append(item)
            selling(player_inventory, player_savings)
        elif item == "chapstick":
             player_inventory.pop(0)
             given_price = round(random.uniform(1.50, 2.50),2)
             print(f"My lips are pretty dry. Could use this chapstick. I'll give you {given_price} dollars.")
                        
             haggle_answer = input("Would you like to haggle?   ")
             haggle_check(given_price, haggle_answer, player_savings)
             items_sold.append(item)
        elif item == "car keys":
            player_inventory.pop(0)
            given_price = round(random.uniform(100.00, 250.00),2)
            print(f"These car keys are useless to me, but I'll give you {given_price} dollars.")
                                    
            haggle_answer = input("Would you like to haggle?   ")
            haggle_check(given_price, haggle_answer, player_savings)
            items_sold.append(item)
        elif item == "coupon":
            player_inventory.pop(0)
            given_price = round(random.uniform(1.00, 10.00), 2)
            print(f"Not my favorite store, but I'll take it. A coupon's a coupon. I'll give you {given_price} dollars.")
                                    
            haggle_answer = input("Would you like to haggle?   ")
            haggle_check(given_price, haggle_answer, player_savings)
            items_sold.append(item)
        elif item == "wired earbuds":
            player_inventory.pop(0)
            given_price = round(random.uniform(5.00, 35.00),2)
            print(f"I'm was always fonder of wired earbuds. I'll give you {given_price} dollars.")
                                    
            haggle_answer = input("Would you like to haggle?   ")
            haggle_check(given_price, haggle_answer, player_savings)
            items_sold.append(item)




# Game Introduction
print("You are in debt to loansharks and need $10,000 as quick as possible to pay them off.")
time.sleep(1)
print("You don't have a job, but you're pretty sly.")
time.sleep(1)
print("Pick-pocket people to get items. Sell what you can to me. I'll give you cash for it.\n")

# Main Loop
running = True
while running and player_savings < 10000:
    answer = input("Are you ready to do this?   ")

    if answer.lower() == "no":
            print("You decide your fault doesn't give you the right to do harm. " 
            "Maybe there are other ways to get out of this.")
            running = False
    elif answer.lower() == "yes":
        scenario = ["You see a woman jogging.", "You see a man sitting at a bus stop.", "You see a teen on their phone.",
                    "You see a couple laughing on a walk.", "You see a guy sleeping on a bench.", 
                    "You see a mother with three kids.", "You see a contruction worker.", "You see someone in a trenchcoat."]
        print(random.choice(scenario))
        player_ready = input("Pick-pocket them?: ")
        if player_ready.lower() == "yes":
            caught = random.randint(1,2)
            if caught == 1:
                if steal_counter < 3:
                    steal_counter += 1
                    item_gotten = random.choice(pocket)
                    print(f"You got {item_gotten}.")
                    player_inventory.append(item_gotten)
                    print(player_inventory, "\n")
                elif steal_counter == 3:
                    print("---------------------------------------------------------------------------")
                    time.sleep(1.5)
                    print("Your inventory is full, you should sell your items to me to make money.")
                    sell_choice = input("Sell your items?   ")
                    print("---------------------------------------------------------------------------")
                    print("\n")
                    if sell_choice.lower() == "yes":
                        selling(player_inventory, player_savings)
                        steal_counter = 0
                    elif sell_choice.lower() == "no":
                        print("You're pockets are stuffed, can't fit another penny. You'll be the one getting stolen from.")
                        sell_choice = input("Sell your items?   ")
                    else:
                        print("Can't understand you, kid. Need a yes or no.")
                        sell_choice = input("Sell your items?   ")
            else:
                print("You got caught, but ran away just in time. Good thing that you're fast.\n")
        elif player_ready.lower() == "no":
            print("Your loss. Neither of your lives change.\n")
        else:
            print("You need to make a clear decision, kid. Yes or No?\n")
            player_ready = input("Pick-pocket them?: ")
    else:
        print("You need to make a clear decision, kid. Yes or No?\n")


