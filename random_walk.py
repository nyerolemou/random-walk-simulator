import random
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib import animation

class RandomWalk:

    directions = [1,2,3,4]

    def __init__(self, x, y, p_up, p_right, p_down, p_left):
        """
        Args:
            x: Initial x coordinate in Z.
            y: Initial y coordinate in Z.
            p_up: Probability of moving one step up from current state.
            p_right: Probability of moving one step right from current state.
            p_down: Probability of moving one step down from current state.
            p_left: Probability of moving one step left from current state.

        Returns:
            Returns a RandomWalk object.

        Raises:
            TypeError: If initial position (x,y) is not in Z^2.
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
        self.numSteps = 1000


    def _next_direction(self):
        """
        Finds the next direction based on probabilities.

        Returns:
            An int from [1,2,3,4].
        """
        return random.choices(RandomWalk.directions, weights=self.probabilities)[0]


    def walk(self, num_steps = 1000):
        """
        Computes a random walk for given number of steps.

        Args:
            num_steps: Number of steps in the walk.
        """
        self.numSteps = num_steps
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


    def visualise(self):
        """
        Plots animation of the object's random walk.
        """
        fig = plt.figure()
        plt.title('Random Walk with {} Steps and Probabilities {}'.format(self.numSteps, self.probabilities))

        x = [self.trail[i][0] for i in range(self.numSteps)]
        y = [self.trail[i][1] for i in range(self.numSteps)]
        xlim = max([abs(k) for k in x]) + 5
        ylim = max([abs(k) for k in y]) + 5

        ax = plt.axes(xlim=(-xlim, xlim), ylim=(-ylim, ylim))
        ax.set_xticks(np.arange(-xlim,xlim))
        ax.set_yticks(np.arange(-ylim,ylim))
        ax.axes.xaxis.set_visible(False)
        ax.axes.yaxis.set_visible(False)
        ax.set_facecolor('darkslategrey')
        #ax.grid(True, color='silver', linestyle='-', linewidth=0.5)
        line, = ax.plot([], [], lw=1, color='white')

        def init():
            line.set_data([x[0]], [y[0]])
            return line,

        def animate(i):
            line.set_data(x[0:i], y[0:i])
            return line,

        anim = animation.FuncAnimation(fig, animate, init_func=init,
                                       frames=self.numSteps, interval=50, blit=True)
        plt.show()




if __name__ == "__main__":
    walk = RandomWalk(0,0,25,25,25,25)
    walk.walk(1000)
    walk.visualise()
