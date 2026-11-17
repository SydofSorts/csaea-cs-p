import random 

# Player's goal is to get $1,000


goal = 0
wallet = random.randint(1, 20)
inventory = ["phone", wallet, "chapstick", "car keys", "coupon", "wired earbuds"]

def selling():
    

# 1. Checks item given by user (item must be string)
# 2. Gives random price (rand.int)
# 3. Prints price
# 4. User can haggle higher
# 5. If user haggles higher
#       chance (%50)
#           if user gets a higher price:
#               print("I suppose that's fair.")
#               chance becomes half of what it was before