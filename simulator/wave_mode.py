# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 11:21:23 2022

@author: tomkeen
"""

import pygame
import random
import pymunk
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import butter, lfilter, freqz
import pandas as pd
import matplotlib


Fps=60
### Created on Nov 14 11:24:23 2022


wall_thickness=100
### end here
#myfont=pygame.font.SysFont("C:\Windows\Fonts\Arial",15)


class Ball():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.body=pymunk.Body()
        self.body.position=x,y
        #100 in velocity means 100 frames per sec
        self.body.velocity=random.uniform(-velocity_lim,velocity_lim),random.uniform(-velocity_lim,velocity_lim) #random float nunber
        self.shape = pymunk.Circle(self.body,particle_size)
        self.shape.density=particle_density
        self.shape.elasticity =elasticity
        
        space.add(self.body,self.shape)
   
    def draw(self):
        x,y=self.body.position
       
        pygame.draw.circle(display,(255,255,255),(int(x),int(y)),particle_size)
    
    ### Created on Nov 14 9:35:23 2022
    def get_velocity(self):
        e = self.body.velocity
        vx=e[0]
        vy=e[1]
        v= np.sqrt(vx*vx+vy*vy)
        return v 
    def get_xposition(self):
        r= self.body.position
        x=r[0]
        return x
    def get_velocity_left(self):
        e = self.body.velocity
        return e[0]
    def get_v_energie(self):
        e = self.body.velocity
        # * (self.shape.density) * (4 * np.pi * particle_size^3 / 3) 质量
        E = 0.5 * (e[0]*e[0] + e[1]*e[1])
        return E

    ### end here
    


class Satistic_Wall():
    def __init__(self,p1,p2):
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.shape = pymunk.Segment(self.body, p1 ,p2, wall_thickness) # I don't quite understand it here
        self.shape.elasticity = 1
        space.add(self.shape, self.body)

class Kinematic_Wall():
    def __init__(self,p1,p2):
        self.body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
        self.shape = pymunk.Segment(self.body, p1 ,p2, wall_thickness)
        self.shape.body.velocity = (0, 0)
        self.shape.elasticity = pusher_elasticity
        self.time=0
        space.add(self.shape, self.body)
    def stop(self):
        self.time=self.time+1
        if self.time<pusher_start_time:
            self.shape.body.velocity = (0, 0)
        elif self.time>pusher_run_time+pusher_start_time:
           self.shape.body.velocity = (0, 0)
        else:
           self.shape.body.velocity = (pusher_velocity, 0) 
        
 ### Created on Nov 14 9:35:23 2022

# Low pass filter
def butter_lowpass(cutoff, fs, order):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y

# calculate statistic
def Ec_A(list_1):
    E_tot = 0
    for i in list_1:
        E_tot = i + E_tot
    return E_tot  / num_of_balls

def V_A(list_1):
    v_a = 0
    for i in list_1:
        v_a = v_a + i
    v_a = v_a / num_of_balls
    return v_a

# the pressure term has problem
def press_right(list1, list2):
    F_tot = 0
    for i in range(num_of_balls):
        if list1[i] * (1/Fps) >= width-list2[i]: #其实是大于等于到墙壁的位置
            F_tot = F_tot + 2 * np.abs(list1[i])
    
    press = F_tot/height
    return press
def move_figure(f, x, y):
    """Move figure's upper left corner to pixel (x, y)"""
    backend = matplotlib.get_backend()
    if backend == 'TkAgg':
        f.canvas.manager.window.wm_geometry("+%d+%d" % (x, y))
    elif backend == 'WXAgg':
        f.canvas.manager.window.SetPosition((x, y))
    else:
        # This works for QT and GTK
        # You can also use window.setGeometry
        f.canvas.manager.window.move(x, y)



 ### end here          
def texts(statics):
   font=pygame.font.Font(None,30)
   color=(255,255,0)
   font_size=4
   staticstext1=font.render("Temp:"+str(statics[0]), font_size,color)
   staticstext2=font.render("Average speed:"+str(statics[1]), font_size,color)
   staticstext3=font.render("pressure:"+str(statics[2]), font_size,color)
   staticstext4=font.render("wave speed:"+str(statics[3]), font_size,color)
  
   display.blit(staticstext1, (0,0))
   display.blit(staticstext2, (0,30))
   display.blit(staticstext3, (0,60))
   display.blit(staticstext4, (0,90))

    
def game():
    global display
    global space
    global width
    ylimit=3*num_of_balls/50+100
    width=3*height
    pygame.init()
    clock=pygame.time.Clock()
    display = pygame.display.set_mode((width,height))
    space=pymunk.Space()
    
    balls = [Ball(random.randint(0,width),random.randint(0,height)) for i in range(num_of_balls)]
    # collision handler
    
    pushers=[Kinematic_Wall((0-wall_thickness,0), (0-wall_thickness,height))]
  
    walls= [Satistic_Wall((0,-wall_thickness),(width,-wall_thickness)),
            Satistic_Wall((width+wall_thickness,0),(width+wall_thickness,height)),
            Satistic_Wall((0,height+wall_thickness),(width,height+wall_thickness))
            ]
    
    global run
    run=True
    wave_max=[]#calculate average speed of the wave
    counter=0      
    csv_flag=1
    timer=0
    plt.close(1)
    plt.close(2)
    while run: # one while loop equals one frame
        timer=timer+1
        ### Created on Nov 14 9:35:23 2022
        
        v_live=[]   
        x_live=[]
        E_live=[]
        v_left=[]

        counter=counter+1
        
        ### end here       
        
        
        
        
        display.fill((0,0,0))
        
        for ball in balls:
            ball.draw()

            #get data for each frame
            v_live.append(ball.get_velocity())   
            x_live.append(ball.get_xposition())
            E_live.append(ball.get_v_energie())
            v_left.append(ball.get_velocity_left())

       
        global figurex 
        figurex=plt.figure('x',figsize=(10,7))
        
        plt.clf()
        
        plt.subplot(2,1,1)
        
        plt.grid()
        plt.xlim(0,width)
        bins_spacial=50
        result1, result2 = np.histogram(x_live,bins=bins_spacial)
        result2 = result2[:-1]
        filted_distribution = butter_lowpass_filter(result1-(num_of_balls/bins_spacial), cutoff, 30.0, order_filter)
        #tracking wave
        wave_max.append(np.argmax(filted_distribution))
        average_over=10 # average wave speed over 10 frames
        if counter==average_over:
            v_wave=((wave_max[-1]-wave_max[0])*(width/bins_spacial))/(average_over/Fps)
            wave_max=[]
            counter=0
        T_a = Ec_A(E_live)
        v_a = V_A(v_live)
        press = press_right(v_left, x_live)
        #print the statistic in pygame
        
        #export number to csv
        if timer<pusher_start_time+pusher_run_time+average_over:
            v_wave=0
        #print(v_wave)
        texts((round(T_a),round(v_a),round(press),round(v_wave)))
        dataframe = pd.DataFrame({'temperature':[T_a],'average velocity':[v_a],
                                  'pressure':[press],'wave speed':[v_wave]})      
        if csv_flag==1:
            dataframe.to_csv("data.csv",index=False,sep=',')
            csv_flag=0
        else:
            dataframe.to_csv("data.csv",mode='a',header=False,index=False,sep=',')
        
        
        #plot the distribution
        plt.plot(result2, result1)
        
        plt.plot(result2, filted_distribution+(num_of_balls/bins_spacial))
        plt.xlabel('density distribution')
        plt.subplot(2,1,2)
        plt.hist(v_live,bins=50)
        plt.ylim(0,ylimit)
        plt.xlabel('velocity distribution')
        plt.pause(1/Fps) 
        plt.ioff()
        move_figure(figurex, 0, h/3)
        
          
        pushers[0].stop()
        
        clock.tick(Fps)
        pygame.display.update()
        space.step(1/Fps)
        for event in pygame.event.get():
            
            
            if event.type == pygame.QUIT:
                run = False # when click x make sure it close
                plt.close(figurex)
                break
    pygame.quit()
 
