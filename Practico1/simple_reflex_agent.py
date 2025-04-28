# https://gymnasium.farama.org/introduction/basic_usage/

class SimpleReflexAgent:
    def __init__(self):
        self.plan = [
            (0, 1),  # A y B cruzan
            (0, 0),  # A vuelve solo
            (2, 3),  # C y D cruzan
            (1, 1),  # B vuelve solo
            (0, 1)   # A y B cruzan otra vez
        ]
        self.step = 0

    def act(self, observation):
        if self.step >= len(self.plan):
            raise Exception("No more planned actions.")
        action = self.plan[self.step]
        self.step += 1
        return action