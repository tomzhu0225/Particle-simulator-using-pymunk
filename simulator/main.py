# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 07:46:06 2022

@author: tomkeen
"""

from tkinter import *
import tkinter as tk
import pygame
import random
import pymunk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
from GUI_wave import *
import GUI_wave
from GUI_diffusion import *
import GUI_diffusion
from customtkinter import CTkButton, set_appearance_mode
import os
def awake_wave_mode():
    
    
    set_appearance_mode('System')  


    
    window = tk.Toplevel()
    window.title('wave simulator')
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" %(50,50)
    GUI_wave.window=window
    
    ###test    
    #create_form(f)
    # getting width and height of display
    w = window.winfo_screenwidth()
    h = window.winfo_screenheight()
    wave_mode.h=h
    window.geometry("%dx%d" % (0.5*w, h-50) + '+' + str(int(0.5*w)) + '+' + '0')
    
    labels()
    sliders()
    buttons()    
def awake_diffusion_mode():
    window1 = tk.Toplevel()
    window1.title('Diffusion simulator')
    GUI_diffusion.window=window1
    w = window1.winfo_screenwidth()
    h = window1.winfo_screenheight()
    GUI_diffusion.w=w
    GUI_diffusion.h=h
    window1.geometry("%dx%d" % (0.25*w, h-50) + '+' + str(int(0.75*w)) + '+' + '0')
    window1.protocol("WM_DELETE_WINDOW", GUI_diffusion.exit_also_py)
    layout()
    
if __name__=='__main__':
    app = tk.Tk()
    set_appearance_mode('System')  
    w = app.winfo_screenwidth()
    h = app.winfo_screenheight()
    app.title('particle simulator')
    app.geometry("%dx%d" % (w/4.5, h/2))
    app.lift()
    photo1 = tk.PhotoImage(file = "./wave_mode.png")
    photo2 = tk.PhotoImage(file = "./diffusion_mode.png")
    button_wave = tk.Button(app, 
                  text="wave mode", background='gray',fg = "white",image=photo1, 
                  command=awake_wave_mode)
    button_diffusion = tk.Button(app, 
                  text="diffusion mode",background = "red", fg = "white",image=photo2,
                  command=awake_diffusion_mode)
    # button_wave = tk.Button(app, 
    #                text="wave mode", background='blue',fg = "white",
    #                command=awake_wave_mode)
    # button_diffusion = tk.Button(app, 
    #                text="diffusion mode",background = "red", fg = "white",
    #                command=awake_diffusion_mode)
    button_wave.pack(side = TOP, expand = True, fill = BOTH)
    
    button_diffusion.pack(side = TOP, expand = True, fill = BOTH)
    
    
    app.mainloop()

