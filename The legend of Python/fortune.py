import random

cookie = random.randint(0, 7)
message = [
    "Do not pursue happiness ... create it.",
    "All things are difficult before they are easy",
    "The early bird gets the worm, but the second mouse gets the cheese.",
    "If you eat something and nobody sees you eat it, it has no calories.",
    "Someone in your life needs a letter from you.",
    "Do not just think. Act!",
    "The fortune you search for is in another cookie.",
    "Help! I am being held prisoner in a Chinese bakery!",
]

# print(message[3])

# print(cookie)


def fortune(message, cookie):
    number = int(input("how many cookies do you want?: "))
    for i in range(number):
        inside(message, cookie)


def inside(a, b):
    print(a[b])


fortune(message, cookie)
