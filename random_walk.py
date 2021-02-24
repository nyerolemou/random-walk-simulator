import os
import random
import numpy as np
import matplotlib
matplotlib.use('agg')
from matplotlib import pyplot as plt
from matplotlib import animation
from celluloid import Camera
from numpngw import AnimatedPNGWriter
import io
from PIL import Image, ImageDraw


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
        ax.grid(True, color='silver', linestyle='-', linewidth=0.5)
        line, = ax.plot([], [], lw=1, color='white')

        def init():
            line.set_data([x[0]], [y[0]])
            return line,

        def animate(i):
            line.set_data(x[0:i], y[0:i])
            return line,

        anim = animation.FuncAnimation(fig, animate, init_func=init,
                                       frames=self.numSteps, interval=2, blit=True)
        #plt.show()

        #camera=Camera(fig)
        #for i in range(self.numSteps):
        #    ax.plot(x[0:i],y[0:i], lw=1, color='white')
        #    camera.snap()

        #animation = camera.animate(interval = 50, repeat=False)
    

        #plt.show()
        return (anim,fig)

    def visualise_bytesio(self):
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
        ax.grid(True, color='silver', linestyle='-', linewidth=1)
        
        frames=[]
        for i in range(self.numSteps):
            ax.plot(x[0:i],y[0:i], lw=1, color='white')
            fobj = io.BytesIO()
            fig.savefig(fobj)
            fobj.seek(0)
            frame = Image.open(fobj)
            frames.append(frame)

        # Save the frames as animated GIF to BytesIO
        animated_gif = io.BytesIO()
        frames[0].save(animated_gif,
                       format='GIF',
                       save_all=True,
                       append_images=frames[1:],      # Pillow >= 3.4.0
                       delay=0.1,
                       loop=0)
        animated_gif.seek(0)
        
        return animated_gif

    def save_vis(self, filename, anim, kwargs):
        """
        Save animation.

        Args:
            path: Path to save anim to.
            anim: Animation to save.
        """
        # warning: this is slow when saving a long walk.
        Writer = animation.writers['pillow']
        writer = Writer(fps=50, metadata=dict(artist='Me'), bitrate=1800)
        anim.save('test.png', writer=writer,*kwargs)


if __name__ == "__main__":
    walk = RandomWalk(0, 0, 25, 25, 25, 25)
    walk.walk(100)
    anim, camera = walk.fig_setup()
    #walk.save_vis('test.png', anim)

    #N = 25          # number of frames

    # Create individual frames
    #frames = []
    #for n in range(N):
    #    frame = Image.new("RGB", (200, 150), (25, 25, 255*(N-n)//N))
    #    draw = ImageDraw.Draw(frame)
    #    x, y = frame.size[0]*n/N, frame.size[1]*n/N
    #    draw.ellipse((x, y, x+40, y+40), 'yellow')
    #    # Saving/opening is needed for better compression and quality
    #    fobj = io.BytesIO()
    #    frame.save(fobj, 'GIF')
    #    frame = Image.open(fobj)
    #    frames.append(frame)

    # Save the frames as animated GIF to BytesIO
    #animated_gif = io.BytesIO()
    #frames[0].save(animated_gif,
    #               format='GIF',
    #               save_all=True,
    #               append_images=frames[1:],      # Pillow >= 3.4.0
    #               delay=0.1,
    #               loop=0)
    #animated_gif.seek(0,2)
    #print ('GIF image size = ', animated_gif.tell())

    # Optional: write contents to file
    #animated_gif.seek(0)
    #open('animated.gif', 'wb').write(animated_gif.read())
