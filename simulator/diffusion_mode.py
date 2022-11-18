from tkinter import *
import pygame
import random
import os
import pymunk
import matplotlib.pyplot as plt
import numpy as np
from plot_diffusion import *

# Initializing paramters
height = 350
width = 1060
num_of_balls_1 = 5000
num_of_balls_2 = 5000
Fps = 120
fat = 20
el = 1
speed_limit1 = 500
speed_limit2 = 500
particle_size1 = 1
particle_size2 = 1
color1 = (255, 0, 0)
color2 = (0, 0, 255)


class Ball(): #Creating a ball class
    def __init__(self, x, y, particle_size, speed_limit):
        self.size = particle_size
        self.x = x
        self.y = y
        self.body = pymunk.Body()
        self.body.position = x, y
        # 100 in velocity means 100 frames per sec
        # random float nunber
        self.body.velocity = random.uniform(-speed_limit,
                                            speed_limit), random.uniform(-speed_limit, speed_limit)
        self.shape = pymunk.Circle(self.body, self.size)
        self.shape.density = 1
        self.shape.elasticity = el
        space.add(self.body, self.shape)

    def draw(self, color):
        x, y = self.body.position
        pygame.draw.circle(display, color,
                           (int(x), int(y)), self.size)


class Satistic_Wall(): #For segments
    def __init__(self, p1, p2):
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        # I don't quite understand it here
        self.shape = pymunk.Segment(self.body, p1, p2, 20)
        self.shape.elasticity = 1
        space.add(self.shape, self.body)

    def delete(self):
        space.remove(self.shape, self.body)


def game(width, height): #function that does the simulation
    #fig = plt.figure()
    #move_figure(fig, 0, height+25)
    global window                 # Need window from the GUI to make it dynamic

    global display
    display = pygame.display.set_mode((width, height))

    global clock
    clock = pygame.time.Clock()

    global space
    space = pymunk.Space()

    balls_1 = [Ball(random.randint(0, width//2-fat), random.randint(0, height), particle_size1, speed_limit1)
               for i in range(num_of_balls_1)]
    balls_2 = [Ball(random.randint(width//2+fat, width),
                    random.randint(0, height), particle_size2, speed_limit2) for i in range(num_of_balls_2)]

    walls = [Satistic_Wall((0, 0), (width, 0)),
             Satistic_Wall((width, 0), (width, height)),
             Satistic_Wall((0, height), (width, height)),
             Satistic_Wall((0, 0), (0, height))
             ]

    global poof_wall
    poof_wall = Satistic_Wall((width/2, 0), (width/2, height))

    global nerd_mode
    nerd_mode = False

    global run
    run = True

    global time, T, num_ball_diffused1,num_ball_diffused2
    time = 0
    T = []
    num_ball_diffused1 = []
    num_ball_diffused2 = []
    global running
    def running():
 
        global run
        if run:
            global time, T, num_ball_diffused1,num_ball_diffused2
            display.fill((0, 0, 0))
            compteur1 = 0
            compteur2 = 0

            for ball in balls_1:
                ball.draw(color1)
                if ball.body.position[0] > width/2 and time % 10 == 0:
                    compteur1 += 1
            for ball in balls_2:
                ball.draw(color2)
                if ball.body.position[0] < width/2 and time % 10 == 0:
                    compteur2 += 1
            if time % 10 == 0:
                num_ball_diffused1.append(compteur1)
                num_ball_diffused2.append(compteur2)
                T.append(time)
            
            time += 1

            if nerd_mode:
                plotting(T, num_ball_diffused1,num_ball_diffused2,1/1000)
            clock.tick(Fps)
            try:
                window.update()
            except:
                run=False

            try:
                #To ignore the rest of the loop step after clicking on the "X" button
                pygame.display.update()
                space.step(1/Fps)
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        run=False
                        break                
            except:
                run = False

        if not run:
            pygame.quit()
            plt.close()

        window.after(1,running) #appelle la fonction chaque 0.1 ms

