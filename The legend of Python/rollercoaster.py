height = int(input("how tall are you?: "))
money = int(input("how much you have?: "))

if height >= 137 and money >= 10:
    print("Enjoy the ride!")
elif height < 137 or money < 10:
    print("GET OUT OF HERE")
else:
    print("invalid answers")
