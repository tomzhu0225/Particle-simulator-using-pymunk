#Now we're going to set the pusher's speed to a non null value
import wave_mode as w
w.velocity_lim=100
w.particle_size=1
w.particle_density=1
w.elasticity=1
w.pusher_start_time=20
w.pusher_velocity=500
w.num_of_balls=1000
w.height=300
w.cutoff=3
w.order_filter=5
w.pusher_run_time=10
w.h=500
w.pusher_elasticity=1
w.game() #The particles are properly pushed, so so far everything is good.