class Superhero:
    def __init__(self, name, alias, power, team):
        self.name = name            # Real name
        self.alias = alias          # Superhero name
        self.power = power
        self.team = team
        self.__location = "Unknown"  # Encapsulated attribute

    def introduce(self):
        return f"I am {self.alias}, also known as {self.name}, part of {self.team}."

    def use_power(self):
        return f"{self.alias} uses {self.power}!"

    def set_location(self, location):
        self.__location = location

    def get_location(self):
        return f"{self.alias} is currently in {self.__location}."
