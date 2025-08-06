from oop_assignment1 import Superhero
class IronMan(Superhero):
    def __init__(self, name, alias, team, suit_model):
        super().__init__(name, alias, "Advanced Technology", team)
        self.suit_model = suit_model

    def use_power(self):
        return f"{self.alias} activates {self.suit_model} suit and fires repulsor beams!"

class SpiderMan(Superhero):
    def __init__(self, name, alias, team, web_type):
        super().__init__(name, alias, "Spider Powers", team)
        self.web_type = web_type

    def use_power(self):
        return f"{self.alias} swings using {self.web_type} and performs acrobatics!"
