screen_width = 720
screen_height = 495
class Rubiks_cube2D():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.update()
        self.clock = pygame.time.Clock()
        self.cube = rubics_cube()
        self.cube.scramble(self.clock,self.screen)
        self.eval_prev= 0
    
    def action(self,action):
        self.cube.act(action)
        
    def evaluate(self):
        rew = 0
        for i in range(6):
            for row in range(3):
                if self.cube.state[i,row,0]==self.cube.state[i,row,1]==self.cube.state[i,row,2]:
                    rew+=1
            for col in range(3):
                if self.cube.state[i,0,col]==self.cube.state[i,1,col]==self.cube.state[i,2,col]:
                    rew+=1
        reward = rew - self.eval_prev          
        self.eval_prev= rew
        return reward
    
    def is_done(self):
        if self.evaluate()==36:
            return True
        else:
            return False
        
    def observe(self):
        return self.cube.state
    
    def view(self):
        self.cube.draw(self.screen)
        pygame.display.update()