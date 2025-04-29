from abc import ABC, abstractmethod

# ABC Abstract Based Class
class Agent(ABC):
    @abstractmethod
    def __init__(self, env):
        pass

    @abstractmethod
    def next_action(self, obs):
        pass