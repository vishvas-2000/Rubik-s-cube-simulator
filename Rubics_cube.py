import pygame
import sys
import random
import numpy as np

class rubics_cube():
    def __init__(self):
        self.side = 3
        self.side_l = int(135/(self.side))
        self.width = self.side_l-2
        self.colors =  [(255,0,0),(255,255,0),(255,162,0),(255,255,255),(0,0,255),(0,255,0),]
        self.orientation = np.zeros((6,4),dtype=int)
        self.orientation[0,:] = [4,1,5,3] #R->0,C->n-1,R->n-1,C->0
        self.orientation[1,:] = [4,2,5,0] #R->0,C->n-1,R->n-1,C->0
        self.orientation[2,:] = [4,3,5,1] #R->0,C->n-1,R->n-1,C->0
        self.orientation[3,:] = [4,0,5,2] #R->0,C->n-1,R->n-1,C->0
        self.orientation[4,:] = [3,2,1,0] #R->0,C->n-1,R->n-1,C->0
        self.orientation[5,:] = [1,2,3,0] #R->0,C->n-1,R->n-1,C->0
        self.state = np.zeros((6,self.side,self.side),dtype=int)
        self.random = 100
        for i in range(6):
            self.state[i,:,:] = i
            
            
    def scramble(self,clock,screen):
        for i in range(self.random):
            self.act(random.choice([0,1,2,3,4,5,6,7,8,9,10,11]))
            self.draw(screen)

    def draw(self,screen):
        for i in range(self.side):
            for j in range(self.side):
                pygame.draw.rect(screen,self.colors[self.state[0,j,i]],((90+self.side_l*i,180+self.side_l*j),(self.width,self.width)))
                pygame.draw.rect(screen,self.colors[self.state[1,j,i]],((225+self.side_l*i,180+self.side_l*j),(self.width,self.width)))
                pygame.draw.rect(screen,self.colors[self.state[2,j,i]],((360+self.side_l*i,180+self.side_l*j),(self.width,self.width)))
                pygame.draw.rect(screen,self.colors[self.state[3,j,i]],((495+self.side_l*i,180+self.side_l*j),(self.width,self.width)))
                pygame.draw.rect(screen,self.colors[self.state[4,j,i]],((225+self.side_l*i,45+self.side_l*j),(self.width,self.width)))
                pygame.draw.rect(screen,self.colors[self.state[5,j,i]],((225+self.side_l*i,315+self.side_l*j),(self.width,self.width)))
                pygame.display.update()
                
    def act(self,action):
        plane = int(action//2)
        clockwise = int(action//6)
        if plane<4:
            if clockwise:
                    self.state[plane] = np.rot90(self.state[plane],-1)
                    n = -1
                    line = np.zeros((4,self.side))
                    for plane_2 in self.orientation[plane]:
                        n+=1
                        if n==1 or n==3:
                            if n==1:
                                line[n] = self.state[plane_2,:,0]
                            elif n==3:
                                line[n] = self.state[plane_2,:,-1]
                        elif plane== 0:
                            line[n] = self.state[plane_2,:,0]
                        elif plane== 1:
                            if n==0:
                                line[n] = self.state[plane_2,-1,:]
                            else:
                                line[n] = self.state[plane_2,0,:]
                        elif plane== 2:
                            line[n] = self.state[plane_2,:,-1]
                        elif plane== 3:
                            if n==0:
                                line[n] = self.state[plane_2,0,:]
                            else:
                                line[n] = self.state[plane_2,-1,:]

                    n = -1
                    for plane_2 in self.orientation[plane]:
                        n+=1
                        if n==1 or n==3:
                            if n==1:
                                if plane==2 or plane==3:
                                    self.state[plane_2,:,0] = line[n-1][::-1]
                                else:
                                    self.state[plane_2,:,0] = line[n-1]
                            elif n==3:
                                if plane==0 or plane==3:
                                    self.state[plane_2,:,-1] = line[n-1][::-1]
                                else:
                                    self.state[plane_2,:,-1] = line[n-1]
                        elif plane== 0:
                            if n== 2:
                                self.state[plane_2,:,0] = line[n-1]
                            else:
                                self.state[plane_2,:,0] = line[n-1][::-1]
                        elif plane== 1:
                            if n==0:
                                self.state[plane_2,-1,:] = line[n-1][::-1]
                            else:
                                self.state[plane_2,0,:] = line[n-1][::-1]
                        elif plane== 2:
                            if n==2:
                                self.state[plane_2,:,-1] = line[n-1][::-1]
                            else:
                                self.state[plane_2,:,-1] = line[n-1]
                        elif plane== 3:
                            if n==0:
                                self.state[plane_2,0,:] = line[n-1]
                            else:
                                self.state[plane_2,-1,:] = line[n-1]
                                    
                        
            elif not clockwise:
                    self.state[plane] = np.rot90(self.state[plane],1)
                    n = -1
                    line = np.zeros((4,self.side))
                    for plane_2 in self.orientation[plane]:
                        n+=1
                        if n==1 or n==3:
                            if n==1:
                                line[n] = self.state[plane_2,:,0]
                            elif n==3:
                                line[n] = self.state[plane_2,:,-1]
                        elif plane== 0:
                            line[n] = self.state[plane_2,:,0]
                        elif plane== 1:
                            if n==0:
                                line[n] = self.state[plane_2,-1,:]
                            else:
                                line[n] = self.state[plane_2,0,:]
                        elif plane== 2:
                            line[n] = self.state[plane_2,:,-1]
                        elif plane== 3:
                            if n==0:
                                line[n] = self.state[plane_2,0,:]
                            else:
                                line[n] = self.state[plane_2,-1,:]

                    n = -1
                    for plane_2 in self.orientation[plane]:
                        n+=1
                        if n==1 or n==3:
                            if n==1:
                                if plane==2 or plane==1:
                                    self.state[plane_2,:,0] = line[n+1][::-1]
                                else:
                                    self.state[plane_2,:,0] = line[n+1]
                            elif n==3:
                                if plane==0 or plane==1:
                                    self.state[plane_2,:,-1] = line[0][::-1]
                                else:
                                    self.state[plane_2,:,-1] = line[0]
                        elif plane== 0:
                            if n==0:
                                self.state[plane_2,:,0] = line[n+1]
                            else:
                                self.state[plane_2,:,0] = line[n+1][::-1]
                        elif plane== 1:
                            if n==0:
                                self.state[plane_2,-1,:] = line[n+1]
                            else:
                                self.state[plane_2,0,:] = line[n+1]
                        elif plane== 2:
                            if n==2:
                                self.state[plane_2,:,-1] = line[n+1]
                            else:
                                self.state[plane_2,:,-1] = line[n+1][::-1]
                        elif plane== 3:
                            if n==0:
                                self.state[plane_2,0,:] = line[n+1][::-1]
                            if n==2:
                                self.state[plane_2,-1,:] = line[n+1][::-1]

        else:
            if not clockwise:
                self.state[plane] = np.rot90(self.state[plane],1)
                line = np.zeros((4,self.side))
                if plane== 4:
                    n = -1
                    for plane_2 in self.orientation[plane]:
                        n+=1
                        line[n] = self.state[plane_2,0,:]

                    n = -1
                    for plane_2 in self.orientation[plane]:
                        n+=1
                        if n == len(line)-1:
                            self.state[plane_2,0,:] = line[0].copy()
                        else:
                            self.state[plane_2,0,:] = line[n+1].copy()

                else:
                    n = -1
                    for plane_2 in self.orientation[plane]:
                        n+=1
                        line[n] = self.state[plane_2,-1,:]

                    n = -1
                    for plane_2 in self.orientation[plane]:
                        n+=1
                        if n==len(line)- 1:
                            self.state[plane_2,-1,:] = line[0].copy()
                        else:
                            self.state[plane_2,-1,:] = line[n+1].copy()


            if clockwise:
                self.state[plane] = np.rot90(self.state[plane],-1)
                line = np.zeros((4,self.side))
                if plane== 4:
                    n = -1
                    for plane_2 in self.orientation[plane]:
                        n+=1
                        line[n] = self.state[plane_2,0,:]

                    n = -1
                    for plane_2 in self.orientation[plane]:
                        n+=1
                        self.state[plane_2,0,:] = line[n-1]

                else:
                    n = -1
                    for plane_2 in self.orientation[plane]:
                        n+=1
                        line[n] = self.state[plane_2,-1,:]

                    n = -1
                    for plane_2 in self.orientation[plane]:
                        n+=1
                        self.state[plane_2,-1,:] = line[n-1]