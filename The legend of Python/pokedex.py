class Pokemon:
    def __init__(self, entry, name, tipe, description, is_caught):
        self.entry = entry
        self.name = name
        self.type = tipe
        self.description = description
        self.is_caught = is_caught

    def speak(self):
        sound = self.entry
        return sound
