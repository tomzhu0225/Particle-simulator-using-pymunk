# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 07:43:19 2022

@author: tomkeen
"""

from tkinter import *
import pygame
import random
import pymunk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from wave_mode import game
import wave_mode
from customtkinter import *
# create the window




def labels():
    # creation label des parametres
    relwidth=0.15
    label_par = CTkLabel(window, text="control panel",text_font=("Roboto Medium", -16),
                         fg_color=("white", "gray38"),corner_radius=6)
    label_par.place(relx=0.35, rely=0, relwidth=0.2, relheight=0.1)
    # Labels
    l_win_size=Label(window, text="windows size")
    l_par_num = Label(window, text="particle number")
    l_par_size = Label(window, text="particle size")
    l_par_den = Label(window, text="particle density")
    l_v0 = Label(window, text="max speed")
    l_ela = Label(window, text="elasticity")
    l_p_s = Label(window, text="pusher speed")
    l_p_st = Label(window, text="pusher start time")
    l_p_t = Label(window, text="pusher run time")
    l_p_ela = Label(window, text="pusher elasticity")
    l_cutoff = Label(window, text="frequency of cutoff")
    l_order = Label(window, text="order of filter")
    
    # emplacement des labels
    l_win_size.place(relx=0.1, rely=0.1, relwidth=relwidth, relheight=0.1)
    l_par_num.place(relx=0.1, rely=0.2, relwidth=relwidth, relheight=0.1)
    l_par_size.place(relx=0.1, rely=0.3, relwidth=relwidth, relheight=0.1)
    l_par_den.place(relx=0.1, rely=0.4, relwidth=relwidth, relheight=0.1)
    l_v0.place(relx=0.1, rely=0.5, relwidth=relwidth, relheight=0.1)
    l_ela.place(relx=0.1, rely=0.6, relwidth=relwidth, relheight=0.1)
    l_p_s.place(relx=0.5, rely=0.1, relwidth=relwidth, relheight=0.1)
    l_p_st.place(relx=0.5, rely=0.2, relwidth=relwidth, relheight=0.1)
    l_p_t.place(relx=0.5, rely=0.3, relwidth=relwidth, relheight=0.1)
    l_p_ela.place(relx=0.5, rely=0.4, relwidth=relwidth, relheight=0.1)
    l_cutoff.place(relx=0.5, rely=0.5, relwidth=relwidth, relheight=0.1)
    l_order.place(relx=0.5, rely=0.6, relwidth=relwidth, relheight=0.1)
   
def sliders():
    # Parameters input
    global slider_win_size
    global slider_particle_num
    global slider_particle_size
    global slider_particle_den
    global slider_speed_limit
    global slider_elasticity
    global slider_pusher_speed
    global slider_start_time
    global slider_pusher_run_time
    global slider_pusher_elasticity
    global slider_cutoff
    global slider_order_filter
    slider_win_size = Scale(window, from_=0, to=700, resolution = 100,orient=HORIZONTAL)
    slider_win_size.set(300)
    
    slider_particle_num = Scale(window, from_=1000, to=15000, resolution = 1000,orient=HORIZONTAL)
    slider_particle_num.set(4000)
    
    slider_particle_size = Scale(window, from_=0, to=5, orient=HORIZONTAL)
    slider_particle_size.set(3)
    
    slider_particle_den = Scale(window, from_=0, to=5, orient=HORIZONTAL)
    slider_particle_den.set(1)


    
    slider_speed_limit = Scale(window, from_=0, to=500, orient=HORIZONTAL)
    slider_speed_limit.set(300)
    
    
    slider_elasticity = Scale(window, from_=0, to=1, resolution = 0.1, orient=HORIZONTAL)
    slider_elasticity.set(1)
    
    
    slider_pusher_speed = Scale(window, from_=0, to=500,orient=HORIZONTAL)
    slider_pusher_speed.set(500)
    
    slider_start_time = Scale(window, from_=0, to=100,orient=HORIZONTAL)
    slider_start_time.set(10)
    
    slider_pusher_run_time = Scale(window, from_=0, to=100, orient=HORIZONTAL)
    slider_pusher_run_time.set(10)
    
    
    slider_pusher_elasticity = Scale(window, from_=0, to=1, resolution = 0.1, orient=HORIZONTAL)
    slider_pusher_elasticity.set(1)
    
    
    slider_cutoff = Scale(window, from_=0, to=10, orient=HORIZONTAL)
    slider_cutoff.set(3)

        
    slider_order_filter = Scale(window, from_=0, to=10, orient=HORIZONTAL)
    slider_order_filter.set(5)

    
    # Entry placement
    slider_win_size.place(relx=0.3, rely=0.1, relwidth=0.2, relheight=0.1)
    slider_particle_num.place(relx=0.3, rely=0.2, relwidth=0.2, relheight=0.1)
    slider_particle_size.place(relx=0.3, rely=0.3, relwidth=0.2, relheight=0.1)
    slider_particle_den.place(relx=0.3, rely=0.4, relwidth=0.2, relheight=0.1)
    slider_speed_limit.place(relx=0.3, rely=0.5, relwidth=0.2, relheight=0.1)
    slider_elasticity.place(relx=0.3, rely=0.6, relwidth=0.2, relheight=0.1)
    slider_pusher_speed.place(relx=0.7, rely=0.1, relwidth=0.2, relheight=0.1)
    slider_start_time.place(relx=0.7, rely=0.2, relwidth=0.2, relheight=0.1)
    slider_pusher_run_time.place(relx=0.7, rely=0.3, relwidth=0.2, relheight=0.1)
    slider_pusher_elasticity.place(relx=0.7, rely=0.4, relwidth=0.2, relheight=0.1)
    slider_cutoff.place(relx=0.7, rely=0.5, relwidth=0.2, relheight=0.1)
    slider_order_filter.place(relx=0.7, rely=0.6, relwidth=0.2, relheight=0.1)

def get_parameters():

    
    particle_size = slider_particle_size.get()
    particle_density =  slider_particle_den.get()
    speed_limit = slider_speed_limit.get()
    elasticity = slider_elasticity.get()
    pusher_speed = slider_pusher_speed.get()
    pusher_run_time = slider_pusher_run_time.get()
    pusher_elasticity = slider_pusher_elasticity.get()
    cutoff = slider_cutoff.get()
    order_filter = slider_order_filter.get()
    pusher_start_time=slider_start_time.get()
    num=slider_particle_num.get()
    height=slider_win_size.get()
    wave_mode.particle_size=particle_size
    wave_mode.particle_density = particle_density
    wave_mode.velocity_lim=speed_limit
    wave_mode.elasticity=elasticity
    wave_mode.pusher_velocity=pusher_speed
    wave_mode.pusher_run_time=pusher_run_time
    wave_mode.pusher_elasticity=pusher_elasticity
    wave_mode.cutoff = cutoff
    wave_mode.order_filter = order_filter
    wave_mode.pusher_start_time=pusher_start_time
    wave_mode.height=height
    wave_mode.num_of_balls=num
    wave_mode.run=False
    game()
    print(particle_size,particle_density,speed_limit,elasticity,pusher_speed,pusher_run_time,pusher_elasticity)
def buttons():
    
    # buttons
    start_button = CTkButton(window, text='Start',fg_color=("grey", "black"),command=lambda:get_parameters())
    start_button.place(relx=0.4, rely=0.7)





 ### end here          