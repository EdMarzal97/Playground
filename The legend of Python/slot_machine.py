import random

symbols = ["🍒", "      🍇", "''''''🍉", "7️⃣"]

results = random.choices(symbols, k=3)


print(f"|{results}|")
