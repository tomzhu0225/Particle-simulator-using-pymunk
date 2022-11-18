import diffusion_simulation as d
d.game(700,300)
d.running() #The file we imported has only the simulation, we see that it's working and there is a wall between
#the two groups of particles.
#The problem caused, sometimes, by clicking the X button (the display wants to be updated but it can't
# because it already was destoyed) was solved by using a try except structure.