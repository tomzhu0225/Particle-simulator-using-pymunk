#Here we're going to test the classes we difined in wave_mode.py
import wave_mode as w
#We now just need to define the variables, and knoing what to expect.
w.velocity_lim=100
w.particle_size=1
w.particle_density=1
w.elasticity=1
w.pusher_start_time=20
w.pusher_velocity=0
w.num_of_balls=1000
w.height=300
w.cutoff=3
w.order_filter=5
w.pusher_run_time=10
w.h=500
w.pusher_elasticity=1
w.game()