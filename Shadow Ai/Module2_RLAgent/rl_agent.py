
# rl_agent.py

import numpy as np
import random

class RLEvasionAgent:
    def __init__(self, actions):
        self.actions = actions
        self.q_table = {a: 0.0 for a in actions}
        self.epsilon = 0.1
        self.learning_rate = 0.05
        self.discount = 0.9

    def choose_action(self):
        if random.random() < self.epsilon:
            return random.choice(self.actions)
        return max(self.q_table, key=self.q_table.get)

    def update(self, action, reward):
        current_q = self.q_table[action]
        self.q_table[action] = current_q + self.learning_rate * (reward + self.discount * max(self.q_table.values()) - current_q)

if __name__ == "__main__":
    actions = ['change_entropy', 'obfuscate_strings', 'add_junk_apis']
    agent = RLEvasionAgent(actions)

    for episode in range(10):
        action = agent.choose_action()
        reward = random.uniform(-1, 1)  # mock feedback
        agent.update(action, reward)
        print(f"Episode {episode+1}: Action={action}, Reward={reward}")
