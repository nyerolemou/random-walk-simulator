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
    walk = RandomWalk(0,0,25,25,25,25)
    walk.walk(10000)
    trail = walk.trail
    # First set up the figure, the axis, and the plot element we want to animate
    fig = plt.figure()
    ax = plt.axes(xlim=(-50, 50), ylim=(-50, 50))
    line, = ax.plot([], [], lw=1)
    x_cords = [trail[i][0] for i in range(len(trail))]
    y_cords = [trail[i][1] for i in range(len(trail))]
    # initialization function: plot the background of each frame
    def init():
        line.set_data([x_cords[0]],[y_cords[0]])
        return line,

    # animation function.  This is called sequentially
    def animate(i):
        line.set_data(x_cords[0:i],y_cords[0:i])
        return line,

    # call the animator.  blit=True means only re-draw the parts that have changed.
    anim = animation.FuncAnimation(fig, animate, init_func=init,
                                   frames=10000, interval=100, blit=True)
    plt.show()
