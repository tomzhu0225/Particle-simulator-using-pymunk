# The Particles Collision Simulator





***

# README







## Description
This project aims to use pygame and pymunk to simulate the behaviour of gas/fluid particles. The simulation is done in 2D (as pymunk is a 2D physics engine) and the particles is idealized as **rigid body balls** with varing size, elasticity, fiction and so on.

Due to the limitation of the game engine and cpu performance, we only simulate the behaviour of at most 10000 particles, which is quiet different from real world situation. Because of the deviation from the real world, we are more than exited to see how the paritcles behave compared to the real world situation.
***
### **Features**
The simulator allows user to alter the number of particles, size of the particles, initial speed distribution, elasticity and other relative parameters via a Graphical interface. 
***
The simulator should allow user to switch between different simulation modes. 

For example: *wave measurement mode* would give the particle a small pertubation and simulate the propagation of wave.

In *diffusion mode*, there are two chambers consisting of different types of particles, thus one can simluate the diffusion effect of different types of particles
***
The simulation should give the distribution of pariticle velocity at real time. In different simulation mode, the simulator should give out different simulation satistics like: pressure, tempurature, average particle speed and save the data into csv file for following analysis.

For example, in *wave measurement mode*, the simulator should give out the 1D particle distribution with respect to the coordinate.

In *diffusion mode*, the simulator should give out the particle diffusion rate.
***
### **Objectives**
+ Objective 1 : simulate the particles idealized as **rigid body balls** using pymunk and pygame or matplotlib (settling in the end on pymunk and pygame) --> our MVP!
+ Objective 2 : collect the different physical properties of the simulated system of particles (density,     velocity, number of diffused particles).
+ Objective 3 : plot the physical properties collected in real time using matplotlib.
+ Objective 4 : build the graphical interface for each mode, implementing different sliders for the parameters and practical buttons using Tkinter and customtkinter.
+ Objective 5 : integrate the simulator and the plots to the GUI interface 
+ Objective 6 : refactoring the code and making it as modular as possible.






## Visuals
Update 12/11/2022

![Wave like behaviour of particles](https://media.giphy.com/media/fj0YZa5EkzHrQioMew/giphy-downsized-large.gif) 

Update 15/11/2022

![Adding statistics](visual_1.gif) 

Update 17/11/2022
![Two modes done](visual_2.gif) 

## Installation

The simulator consists of folowing file:  

diffusion_mode.py 

GUI_diffusion.py 

wave_mode.py

GUI_wave.py

plot_diffusion.py

main.py
***
the simulator should be launched in main.py
***
The simulator requires the following python packages:

pymunk

pygame

matplotlib

numpy

pandas

scipy

customtkinter
## Usage

As shown in Visual, the usage of the simulator is easy and intuiative. 

Run the main script and select the mode accordingly. In different mode there would be different parameters to alter the simulation parameters.
***
### wave mode
In wave mode, after you have set the parameters, click on start to launch the simulation. Tempurature,average speed and pressure will be shown in the topleft corn of the screen and the density distribution with respect to x coordinate and velocity distribution will be shown below.

Click x on simulator window(the black one) to end the simulation. The data will be writen on a file named: data.csv. **Be sure to rename it before launching the next simulation if you want to save it**. You can readjust the parameters and click start again to simulate.
***

### diffusion mode 
In wave mode, after you have set the parameters, click on start to launch the simulation. 
To remove the separator press the 'wall poof' button,to graph the number of diffused particles press 'Graphing density' button. To pause the graphing : press 'stop graphing' button and to resume graphing press 'Graphing density' button.
To reset the parameters : stop graphing -> quit the plot window -> reset -> start.
To quit : quit pygame window first and then GUI interface.


## Support
If you have any problem with the simulator. 

Please contact Bowen.zhu@student-cs.fr


## Authors and acknowledgment
This project is made for the Codingweek of CentraleSupelec. And It is made by team physiX(Group 17). 
Its members including:

Alae Taoudi

Bastien Li

Bowen Zhu

Lezhi Pu

Mohamed Taha Afif

Yassine Ouchna







