import numpy as np
import random
import pickle

ACTIONS = ['BUY', 'SELL', 'HOLD']

class QTrader:
    def __init__(self, alpha=0.1, gamma=0.95, epsilon=1.0, epsilon_decay=0.995):
        self.q_table = {}  # State-Action -> Value
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.epsilon_decay = epsilon_decay

    def get_state_key(self, state):
        return tuple(np.round(state, 2))  # Discretize state

    def choose_action(self, state):
        key = self.get_state_key(state)
        if random.random() < self.epsilon:
            return random.choice(ACTIONS)
        if key not in self.q_table:
            self.q_table[key] = {a: 0.0 for a in ACTIONS}
        return max(self.q_table[key], key=self.q_table[key].get)

    def learn(self, state, action, reward, next_state):
        state_key = self.get_state_key(state)
        next_key = self.get_state_key(next_state)

        if state_key not in self.q_table:
            self.q_table[state_key] = {a: 0.0 for a in ACTIONS}
        if next_key not in self.q_table:
            self.q_table[next_key] = {a: 0.0 for a in ACTIONS}

        current_q = self.q_table[state_key][action]
        max_future_q = max(self.q_table[next_key].values())
        self.q_table[state_key][action] += self.alpha * (reward + self.gamma * max_future_q - current_q)
        self.epsilon *= self.epsilon_decay

    def save(self, path):
        with open(path, 'wb') as f:
            pickle.dump(self.q_table, f)

    def load(self, path):
        with open(path, 'rb') as f:
            self.q_table = pickle.load(f)
