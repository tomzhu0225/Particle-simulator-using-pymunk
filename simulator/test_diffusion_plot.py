import plot_diffusion as dp
#here we are simply going to test our plot, it is for the number of diffused particles, this one uses plt.ioffs
#instead of plt.show(0, since our tests showed that show() blocks the other simulations and there
#is no way to go on with the code and put new plots if we only use plt.show(block=False).
dp.plotting([0,1],[1,0],[2,3],2)
dp.plotting([0,2],[2,0],[2,3],5)
#We should see two lines, one red, one blue, the first plot should stay for 2 seconds, and the other for 5
#This test was a success.