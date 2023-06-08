Gryffindor = 0
Hufflepuff = 0
Slytherin = 0
RavenClaw = 0

Q1 = int(input("what you preffer? 1- Dawn or 2- Dusk? : "))
Q2 = int(
    input(
        "After your time in this world what would you like to be remembered 1- The Good 2- The Great 3- The Wise 4- The Bold : "
    )
)
Q3 = int(
    input(
        "what type of instrument is more pleasant for you? 1- Violin 2- Trumpet 3- Piano 4- Drums : "
    )
)

if Q1 == 1:
    Gryffindor += 1
    RavenClaw += 1
elif Q1 == 2:
    Slytherin += 1
    Hufflepuff += 1
else:
    print("invalid answer")

if Q2 == 1:
    Hufflepuff += 2
elif Q2 == 2:
    Slytherin += 2
elif Q2 == 3:
    RavenClaw += 2
elif Q2 == 4:
    Gryffindor += 2
else:
    print("invalid answer")


if Q3 == 1:
    Slytherin += 4
elif Q3 == 2:
    Hufflepuff += 4
elif Q3 == 3:
    RavenClaw += 4
elif Q3 == 4:
    Gryffindor += 4
else:
    print("invalid answer")

maxpoints = max(Gryffindor, Slytherin, RavenClaw, Hufflepuff)

if RavenClaw == maxpoints:
    print("RAVENCLAW")
elif Hufflepuff == maxpoints:
    print("HUFFLEPUFF")
elif Slytherin == maxpoints:
    print("SLYTHERIN")
elif Gryffindor == maxpoints:
    print("GRYFFINDOR")
else:
    print("we need more data")
