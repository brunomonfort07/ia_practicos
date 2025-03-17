from agent import Agent
from random import choice as randomchoice

# Codifique un agente que ejecute acciones aleatorias sobre el ambiente.
# Agente = Tiene una observación y hace algo con respecto a esa observación
class RandomAgent(Agent):
    
    def __init__(self):
        pass

    # Decidir una accion random para interactuar con el entorno.
    def next_action(self, obs):
        ret = self.parse_random_action()
        return ret
    
    def parse_random_action(self):
        charToPerson = {"A": 0, "B": 1, "C": 2, "D": 3 }
        charToDirection = { "R": 1, "L": 0 }

        directions = list(charToDirection.keys())
        persons = list(charToPerson.keys())

        direction = randomchoice(directions)
        person1 = randomchoice(persons)
        #p1 must be different to p2
        person2 = person1
        while person2 == person1:
            person2 = randomchoice(persons)

        p1 = charToPerson[person1]
        p2 = charToPerson[person2]
        d = charToDirection[direction]

        ret = {"direction": d, "person1": p1, "person2": p2}
        return ret