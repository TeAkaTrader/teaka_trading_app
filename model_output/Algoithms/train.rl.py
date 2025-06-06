import gym
from algorithms.dqn_agent import DQNAgent
from simulation.env import TradingEnv

env = TradingEnv(data, fee=0.001)
agent = DQNAgent(state_dim=env.observation_space.shape[0], action_dim=env.action_space.n)
# Training loop
for episode in range(1000):
    state = env.reset()
    done = False
    while not done:
        action = agent.select_action(state)      # implement epsilon-greedy inside agent
        next_state, reward, done, info = env.step(action)
        agent.memorize(state, action, reward, next_state, done)
        agent.learn()  # update DQN using replay buffer
        state = next_state
    print(f"Episode {episode}: Total Profit={info['profit']:.4f}")
