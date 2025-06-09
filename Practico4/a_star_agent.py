import numpy as np
from priority_queue import PriorityQueue


class AStarAgent:
    def __init__(self, model):
        self.model = model
        self.action_list = []

    def loop(self, env):
        start_state_flatten = env.reset()
        done = False
        step_counter = 0
        all_rewards = 0
        env.render()

        while not done:
            action = self.next_action(start_state_flatten.reshape(3, 3))
            obs, reward, done_env, _ = env.step(action)
            all_rewards += reward
            done = done_env
            env.render()
            step_counter += 1

        return all_rewards, step_counter

    def next_action(self, state):
        pass

    def heuristic(self, state):
        return 0

    def is_goal(self, state):
        return np.array_equal(state.flatten(), np.array([1, 2, 3, 4, 5, 6, 7, 8, 0]))

    def a_star(self, start_state):
        pass
