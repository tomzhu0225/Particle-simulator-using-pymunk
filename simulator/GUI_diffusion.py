from tkinter import *
from tkinter import font
import pygame
import random
import pymunk
import os
import diffusion_mode as d
from customtkinter import CTkButton, set_appearance_mode

# create the window


# getting width and height of display
def open_pop(title,error_message):
   bot= Toplevel(window)
   bot.geometry("600x150")
   bot.title(title)
   Label(bot, text= error_message).place(x=200,y=80)

# creation label des parametres
def layout():
    global slider_particle_size1
    global slider_speed_1
    global slider_speed_2
    global slider_elasticity
    global slider_particle_size2
    global slider_num_particles1
    global  slider_num_particles2 
    label_par = Label(window, text="Control panel")
    label_par['font'] = font.Font(size=20)
    label_par.place(relx=0, rely=0, relwidth=1, relheight=0.1)
    # Labels
    size = 12
    l_par_size1 = Label(window, text="Particle size",fg='red')
    l_par_size1['font'] = font.Font(size=size)
    l_v1 = Label(window, text="Max speed",fg='red')
    l_v1['font'] = font.Font(size=size)
    l_ela = Label(window, text="Elasticity",fg='purple')
    l_ela['font'] = font.Font(size=size)
    l_par_size2 = Label(window, text="Particle size",fg='blue')
    l_par_size2['font'] = font.Font(size=size)
    num_par1 = Label(window, text="Number of particles",fg='red')
    num_par1['font'] = font.Font(size=size)
    num_par2 = Label(window, text="Number of particles",fg='blue')
    num_par2['font'] = font.Font(size=size)
    l_v2 = Label(window, text="Max speed",fg='blue')
    l_v2['font'] = font.Font(size=size)
    # emplacement des labels
    l_par_size1.place(relx=0, rely=0.1, relwidth=0.5, relheight=0.1)
    l_par_size2.place(relx=0, rely=0.2, relwidth=0.5, relheight=0.1)
    l_v1.place(relx=0, rely=0.3, relwidth=0.5, relheight=0.1)
    l_v2.place(relx=0, rely=0.4, relwidth=0.5, relheight=0.1)
    l_ela.place(relx=0, rely=0.5, relwidth=0.5, relheight=0.1)
    num_par1.place(relx=0, rely=0.6, relwidth=0.5, relheight=0.1)
    num_par2.place(relx=0, rely=0.7, relwidth=0.5, relheight=0.1)
    # Parameters input
    slider_particle_size1 = Scale(window, from_=1, to=5, orient=HORIZONTAL)
    slider_particle_size1.set(1)
    
    slider_speed_1 = Scale(window, from_=0, to=500, orient=HORIZONTAL)
    slider_speed_1.set(100)
    
    slider_speed_2 = Scale(window, from_=0, to=500, orient=HORIZONTAL)
    slider_speed_2.set(100)
    slider_elasticity = Scale(window, from_=0, to=1,
                              digits=3, resolution=0.1, orient=HORIZONTAL)
    slider_elasticity.set(1)
    
    slider_particle_size2 = Scale(window, from_=1, to=5,
                                  orient=HORIZONTAL)
    slider_particle_size2.set(1)
    
    slider_num_particles1 = Scale(window, from_=0, to=2500, orient=HORIZONTAL)
    slider_num_particles1.set(1000)
    
    slider_num_particles2 = Scale(window, from_=0, to=2500, orient=HORIZONTAL)
    slider_num_particles2.set(1000)
    
    
    # Entry placement
    slider_particle_size1.place(relx=0.5, rely=0.12, relwidth=0.5, relheight=0.1)
    slider_particle_size2.place(relx=0.5, rely=0.22, relwidth=0.5, relheight=0.1)
    slider_speed_1.place(relx=0.5, rely=0.32, relwidth=0.5, relheight=0.1)
    slider_speed_2.place(relx=0.5, rely=0.42, relwidth=0.5, relheight=0.1)
    slider_elasticity.place(relx=0.5, rely=0.52, relwidth=0.5, relheight=0.1)
    slider_num_particles1.place(relx=0.5, rely=0.62, relwidth=0.5, relheight=0.1)
    slider_num_particles2.place(relx=0.5, rely=0.72, relwidth=0.5, relheight=0.1)
    

    
    start_button = CTkButton(master=window, text='Start',fg_color=("grey", "black"), command=start)
    start_button.place(relx=0.25, rely=0.78, relwidth=0.5)

    poof_button = CTkButton(master=window, text='Wall Poof', fg_color=("grey", "black"), command=poof)
    poof_button.place(relx=0.25, rely=0.83, relwidth=0.5)

    graph_button = CTkButton(master=window, text='Graphing diffused particles',
                          fg_color=("grey", "black"), command=graphing)
    graph_button.place(relx=0.25, rely=0.88, relwidth=0.5)

    stop_graphing=stop_button = CTkButton(master=window, text='Stop graphing', fg_color=("grey", "black")
                        , command=stop)
    stop_button.place(relx=0.25, rely=0.93, relwidth=0.5)


def getting_parameters():
    global particle_size1
    particle_size1 = slider_particle_size1.get()
    global speed_limit1
    speed_limit1 = slider_speed_1.get()
    global speed_limit2
    speed_limit2 = slider_speed_2.get()
    global elasticity
    elasticity = slider_elasticity.get()
    global particle_size2
    particle_size2 = slider_particle_size2.get()
    global num_par1
    num_par1 = slider_num_particles1.get()
    global num_par2
    num_par2 = slider_num_particles2.get()


# Importing simulation objects


# Importing the code for the simulation


def start(): #for the button start
    height = int(1*h/3) 
    width = int(0.75*w)
    
    d.run = False #To stop any running simulation
    d.window = window 

    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0, 30)
    d.display = pygame.display.set_mode(
        (width, height))
    d.clock = pygame.time.Clock()
    d.space = pymunk.Space()
    pygame.init()
    getting_parameters()
    d.num_of_balls_1 = num_par1
    d.num_of_balls_2 = num_par2
    d.el = elasticity
    d.speed_limit1 = speed_limit1
    d.speed_limit2 = speed_limit2
    d.particle_size1 = particle_size1
    d.particle_size2 = particle_size2
    d.game(width, height) #It gives the green light to d.running (implicitly gives )
    d.running() #Simulation!


def poof(): #poof!!
    try:    
        d.poof_wall.delete()
    except:
        open_pop('No more Poofs...','The wall has already been Poofed!') #Wall already poofed

def graphing():
    d.nerd_mode = True #Start plotting


def stop():
    d.nerd_mode = False #Stop plotting for a more fluid animation

# buttons




def exit_also_py(): #Stops the excecution properly (also stops the animation so it doesn't get blocked)
    d.run = False
    window.destroy()



