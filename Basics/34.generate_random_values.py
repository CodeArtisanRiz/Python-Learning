import random

# print random 3 numbers in 10-20
for i in range(3):
    print(random.randint(10, 20))

# print a random string from list
members = ["Riz", "Sourav", "Ujjayi"]
leader = random.choice(members)
print(leader)