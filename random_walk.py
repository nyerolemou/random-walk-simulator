import random
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

class RandomWalk:

    directions = [1,2,3,4]

    def __init__(self, x, y, p_up, p_right, p_down, p_left):
        """
        Parameters:

        """
        try:
        	if isinstance(x, int) and isinstance(y, int):
        		self.position = np.array([x,y])
        	else:
        		raise TypeError("positions are not integers")
        except TypeError as exp:
        	print("the type error is: {}\nthe position specified is {} ".format(exp,(x,y)))

        try:
        	prob = p_up + p_right + p_down + p_left
        	if prob == 100:
        		self.probabilities = [p_up, p_right, p_down, p_left]
        	else:
        		raise ValueError("probabilities do not sum to 100")
        except ValueError as exp:
        	print("the value error is: {}\nthe probabilities specified is {} ".format(exp,prob))

        self.trail = [np.array([x,y])]


    def _next_direction(self):
        return random.choices(RandomWalk.directions, weights=self.probabilities)[0]


    def walk(self, num_steps = 10):
        for i in range(num_steps):
            next_direction = self._next_direction()
            if next_direction == 1:
                self.position += [0,1]
            if next_direction == 2:
                self.position += [1,0]
            if next_direction == 3:
                self.position += [0,-1]
            if next_direction == 4:
                self.position += [-1,0]
            self.trail.append(np.copy(self.position))


if __name__ == "__main__":
    walk = RandomWalk(1,0,10,30,5,55)
    walk.walk()
    trail = walk.trail
    # First set up the figure, the axis, and the plot element we want to animate
    #fig = plt.figure()
    #ax = plt.axes(xlim=(0, 2), ylim=(-2, 2))
    #line, = ax.plot([], [], lw=2)

    # initialization function: plot the background of each frame
    #def init():
    #    line.set_data([trail[0][0]],[trail[0][1]])
    #    return line,

    # animation function.  This is called sequentially
    #def animate(i):
    #    line.set_data([trail[i][0]],[trail[i][1]])
    #    return line,

    # call the animator.  blit=True means only re-draw the parts that have changed.
    #anim = animation.FuncAnimation(fig, animate, init_func=init,
    #                               frames=10, interval=20, blit=True)
    #plt.show()
    # First set up the figure, the axis, and the plot element we want to animate
    fig = plt.figure()
    ax = plt.axes(xlim=(0, 2), ylim=(-2, 2))
    line, = ax.plot([], [], lw=2)

    # initialization function: plot the background of each frame
    def init():
        line.set_data([], [])
        return line,

    # animation function.  This is called sequentially
    def animate(i):
        x = np.linspace(0, 2, 1000)
        y = np.sin(2 * np.pi * (x - 0.01 * i))
        line.set_data(x, y)
        return line,

    # call the animator.  blit=True means only re-draw the parts that have changed.
    anim = animation.FuncAnimation(fig, animate, init_func=init,
                                   frames=200, interval=20, blit=True)

    # save the animation as an mp4.  This requires ffmpeg or mencoder to be
    # installed.  The extra_args ensure that the x264 codec is used, so that
    # the video can be embedded in html5.  You may need to adjust this for
    # your system: for more information, see
    # http://matplotlib.sourceforge.net/api/animation_api.html
    #anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

    plt.show()
