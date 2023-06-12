class City:
    def __init__(self, name, country, landmarks, population, localtime):
        self.name = name
        self.country = country
        self.landmarks = landmarks
        self.population = population
        self.localtime = localtime


new_york = City("New York", "USA", ["Timesquare"], 9523541, "19:02")

print(vars(new_york))
