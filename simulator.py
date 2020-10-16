import gym 
from gym import spaces
class customEnv():
    def __init__(self):
        self.pygame = Rubiks_cube2D()
        self.action_space = spaces.Discrete((12))
        self.observation_space = spaces.Box(np.zeros((6,3,3)),5*np.ones((6,3,3)), dtype= int)
        
    def reset(self):
        del self.pygame
        self.pygame = Rubiks_cube2D()
        obs = self.pygame.observe()
        return obs
    
    def step(self, action):
        self.pygame.action(action)
        obs = self.pygame.observe()
        reward = self.pygame.evaluate()
        done = self.pygame.is_done()
        return obs, reward, done, {}
    
    def render(self):
        self.pygame.view()
        
env = customEnv()