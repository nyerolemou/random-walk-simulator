import random

class RandomWalk:
    def __init__(self, x, y, p_up, p_right, p_down, p_left):
        """
        Parameters:

        """
        self.position = [x,y]
        self.probabilities = [p_up, p_right, p_down, p_left]
        self.trail = [[x,y]]

    def _next_direction(self):
        # todo
        return ""

    def walk(self, num_iterations):
        return ""
