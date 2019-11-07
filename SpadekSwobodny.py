from numpy import sin, cos
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as animation

Ho=10.0
g=9.81
r=Ho*0.01
mi=17.08*(10**(-6))
t_koncowe=np.sqrt(2*Ho/g)+1

def derivs(state, t):
    dydx = np.zeros_like(state)
    dydx[0] = state[1]
    dydx[1] =-g
    
    return dydx

dt = 0.05
t = np.arange(0.05, 10, dt)

h1=Ho
v1=0.0
state=[h1,v1]

y = integrate.odeint(derivs, state, t)
y = [[e,s] for e,s in y if e > 0]

h2=0.0
v2=-0.8*y[-1][1]

state=[h2,v2]
y2 = integrate.odeint(derivs, state, t)
y2 = [[e,s] for e,s in y2 if e > 0]

h3=0.0
v3=-0.8*y2[-1][1]

state=[h3,v3]
y3 = integrate.odeint(derivs, state, t)
y3 = [[e,s] for e,s in y3 if e > 0]

h4=0.0
v4=-0.8*y3[-1][1]

state=[h4,v4]
y4 = integrate.odeint(derivs, state, t)
y4 = [[e,s] for e,s in y4 if e > 0]
y= y+ y2 + y3 + y4

x1=[0 for e,s in y]
y1=[e for e,s in y]

fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-0.6*Ho, 0.6*Ho), ylim=(0, Ho),frameon=False,picker=None)

line, = ax.plot([], [], '', lw=2)
time_template = 'time = %.1fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

def init():
    line.set_data([], [])
    time_text.set_text('')
    return line, time_text

def animate(i):
    circle = plt.Circle((0, y1[i]), r , fc='green')
    plt.gca().add_patch(circle)
    time_text.set_text(time_template % (i*dt))
    return circle, time_text

ani = animation.FuncAnimation(fig, animate, np.arange(1, len(y)), interval=25, blit=True, init_func=init)
ani.save('spadekswobodny.htm', fps=15)

plt.show()