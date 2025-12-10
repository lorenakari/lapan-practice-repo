import gym

if __name__ == "__main__":
    env = gym.make("CartPole-v0")
    total_reward = 0.0
    total_steps = 0
    obs = env.reset()

    while True:
        action = env.action_space.sample()
        obs, reward, terminated, truncated, _ = env.step(action)
        done = terminated or truncated
        total_reward += reward
        total_steps += 1
        if done:
            break

    print(f"Episode done in {total_steps:d} steps\nTotal reward: {total_reward:.2f}")
