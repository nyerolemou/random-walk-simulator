import os
import random
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation


class RandomWalk:

    directions = {1 : [0, 1], 2 : [1, 0], 3 : [0, -1], 4: [-1, 0]}

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
            ValueError: If probabilities don't sum to 100.
        """
        try:
            if isinstance(x, int) and isinstance(y, int):
                self.position = np.array([x, y])
            else:
                raise TypeError("positions are not integers")
        except TypeError as exp:
            print("the type error is: {}\nthe position specified is {} ".format(
                exp, (x, y)))

        try:
            prob = p_up + p_right + p_down + p_left
            if prob == 100:
                self.probabilities = [p_up, p_right, p_down, p_left]
            else:
                raise ValueError("probabilities do not sum to 100")
        except ValueError as exp:
            print(
                "the value error is: {}\nthe probabilities specified is {} ".format(exp, prob))

        self.trail = [np.array([x, y])]
        self.numSteps = 1000

    def _next_direction(self):
        """
        Finds the next direction based on probabilities.

        Returns:
            An int from [1, 2, 3, 4] = [up, right, down, left].
        """
        directions = list(RandomWalk.directions.keys())
        return random.choices(directions, weights=self.probabilities)[0]

    def walk(self, num_steps=1000):
        """
        Computes a random walk for given number of steps.

        Args:
            num_steps: Number of steps in the walk.
        """
        self.numSteps = num_steps
        for i in range(num_steps):
            next_direction = self._next_direction()
            self.position += RandomWalk.directions[next_direction]
            self.trail.append(np.copy(self.position))

    def visualise(self):
        """
        Plots animation of the object's random walk.
        """
        fig = plt.figure(figsize=(7,7))
        fig.suptitle('Random Walk with {} Steps and Probabilities {}'.format(
            self.numSteps, self.probabilities))

        x,y=list(zip(*self.trail))
        xlim_max = max(x)
        xlim_min = min(x)
        ylim_max = max(y)
        ylim_min = min(y)
        axes_min = min(xlim_min, ylim_min) - 5
        axes_max = max(xlim_max, ylim_max) + 5

        ax = plt.axes()
        ax.set_xlim([axes_min, axes_max])
        ax.set_ylim([axes_min, axes_max])
        ax.axes.xaxis.set_visible(False)
        ax.axes.yaxis.set_visible(False)
        ax.set_aspect('equal')
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
                                       frames=self.numSteps, interval=2, blit=True)
        plt.show()

        return anim

    def save_vis(self, filename, anim):
        """
        Save animation.

        Args:
            path: Path to save anim to.
            anim: Animation to save.
        """
        # warning: this is slow when saving a long walk.
        Writer = animation.writers['ffmpeg']
        writer = Writer(fps=50, metadata=dict(artist='Me'), bitrate=1800)
        anim.save(os.path.join("animations", filename), writer=writer)


if __name__ == "__main__":
    walk = RandomWalk(0, 0, 25, 25, 25, 25)
    walk.walk(5000)
    anim = walk.visualise()
    walk.save_vis('test.mp4', anim)
