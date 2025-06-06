import gym, numpy as np
from gym import spaces

class TradingEnv(gym.Env):
    def __init__(self, data, fee=0.001):
        super().__init__()
        self.data = data  # price series and features
        self.fee = fee    # transaction fee (e.g. 0.1%)
        self.action_space = spaces.Discrete(3)
        self.observation_space = spaces.Box(low=-np.inf, high=np.inf, shape=(window_size, num_features))
        self.reset()
    def reset(self):
        self.current_step = 0
        self.balance = 1.0    # starting capital
        self.position = 0     # 0 = no position, 1 = long
        self.total_profit = 0
        return self._get_observation()
    def step(self, action):
        # Execute trade and update balance and position
        done = False
        # Example: if action=1 (buy) and not already long, buy one unit:
        price = self.data['price'][self.current_step]
        if action == 1 and self.position == 0:
            self.position = 1
            self.entry_price = price
            self.balance -= self.fee * self.balance
        elif action == 2 and self.position == 1:
            # Close position
            pnl = (price - self.entry_price) / self.entry_price
            self.balance *= (1 + pnl)
            self.balance -= self.fee * self.balance
            self.total_profit += pnl
            self.position = 0
        self.current_step += 1
        if self.current_step >= len(self.data) - 1:
            done = True
        reward = self.balance + self.total_profit  # or other reward metric
        obs = self._get_observation()
        info = {'profit': self.total_profit}
        return obs, reward, done, info
    def _get_observation(self):
        # return recent price window + indicators
        end = self.current_step + 1
        start = max(0, end - window_size)
        obs = self.data[['price', 'ema', 'macd']].iloc[start:end].values
        return obs
