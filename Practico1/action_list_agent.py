from agent import Agent
from typing import List, Dict

class ActionListAgent(Agent):
    
    def __init__(self, predefinedActions: List[Dict[str, int]]):
        self.predefinedActions = predefinedActions
        self.currentActionIndex = 0
    
    def next_action(self, obs):
        if self.currentActionIndex >= len(self.predefinedActions):
            print("No more actions left! ")
            input_status = False
        else:
            ret = self.predefinedActions[self.currentActionIndex]
            self.currentActionIndex += 1
            input_status = True
        return ret