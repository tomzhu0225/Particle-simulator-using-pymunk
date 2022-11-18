import matplotlib.pyplot as plt
Fps=120
fig = plt.figure()
def plotting(t,X,Y,p):
    plt.clf()
    plt.plot(t,X,'r')
    plt.plot(t,Y,'b')
    plt.pause(p)
    plt.ioff()

