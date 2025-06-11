import random
import numpy as np
import matplotlib.pyplot as plt

class QLearningAgent:
    """ El Q-Learning es un algoritmo de aprendizaje por refuerzo (Reinforcement Learning, RL) que 
    permite a un agente aprender cómo actuar en un entorno para maximizar una recompensa acumulada. 
    
    Es un algoritmo off-policy, lo que significa que aprende la mejor política independientemente 
    de las acciones que realmente se estén tomando.

    Q-Learning busca aprender la Q-función óptima Q*(s, a) usando una tabla (o red neuronal en 
    versiones avanzadas). Cada valor Q representa la calidad de tomar una acción a desde 
    un estado s.
    """
    def __init__(self, states, actions):
        # Inicializar arbitrariamente la tabla Q(s, a).
        self.q = np.zeros(states, actions)
        # Inicializar arbitrariamente la tabla de estadísticas por episodio.
        self.stats_per_episode = []

    # Decidir una accion para interactuar con el entorno. Te pregunta que es lo que vas a hacer.
    def next_action(self, obs):
        pass

    def train_agent(self, env, episodes=1000, epsilon=.9, gamma=.9, alpha=.99, episode_render_qty=100):
        # Episode: An episode refers to a sequence of actions taken by the agent in 
        # the environment until it reaches a terminal state.            

        # Hiperparámetros: Estos son clave para que el aprendizaje sea efectivo:
        #   alpha (learning rate): qué tanto se ajustan los valores aprendidos.
        #   gamma (discount factor): cuánto valorás las recompensas futuras.
        #   epsilon (exploration rate): comenzá alto (explora más) y reducilo gradualmente.
        for episode in range(episodes):
            episode_stats = self.new_episode(self, env, epsilon, gamma, alpha)
            self.stats_per_episode.append(episode_stats) # Guardo estadisticas
            if (episode % episode_render_qty == 0):
                env.render()

    def test_agent(self, env, episodes=10):

        # Después de cierto número de episodios:
        # Probá al agente sin exploración (ε = 0) para ver si aprendió a comportarse bien.
        # Medí métricas: número de pasos por episodio, recompensa acumulada, tasa de éxito, etc.

        pass

    def new_episode(self, env, epsilon, gamma, alpha):
        """
        Ejecuta Q-Learning para un episodio.
        Args:
            env (float64): Entorno/Ambiente.
            epsilon: Tasa de exploración.
        Returns:
            bool: True si se cumple cierta condición, False en caso contrario.
        """
        s,_ = env.reset()
        # print(s) # s = obs
        done = False
        total_reward = 0
        step_count = 0
        while not done:
            a = self.epsilon_greedy_policy(env, s, epsilon)
            sN, r, done, _, _ = env.step(a)
            self.q[s][a] = self.q[s][a] + alpha * (r + gamma * np.max(self.q[sN]) - self.q[s][a])
            s = sN
            total_reward += r
            step_count += 1
        print('total_reward', total_reward)
        print('total_steps', step_count)
        return total_reward, step_count

    def epsilon_greedy_policy(self, env, state, epsilon):
        explore = np.random.binomial(1, epsilon)
        if explore:
            action = env.action_space.sample()
            print('explore')
        else:
            action = np.argmax(self.q[state])
            print('exploit')
        return action
    
    def optimal_policy(self, state):
        # Devuelve cual es el valor maximo que tengo en el estado en el que estoy parado.
        action = np.argmax(self.q[state])
        return action