import random
import numpy as np

class RandomWalk:

	direction_list = [1,2,3,4]

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
        	print("the type error is {}\nthe position specified is {} ".format(exp,(x,y)))

        try:
        	prob = p_up + p_right + p_down + p_left
        	if prob == 1:
        		self.probabilities = [p_up, p_right, p_down, p_left]
        	else:
        		raise ValueError("probabilities do not sum to 1")
        except ValueError as exp:
        	print("the value error is {}\nthe probabilities specified is {} ".format(exp,prob))
        
        self.trail = [[x,y]]

    def _next_direction(self):
    	return random.choices(direction_list, weights=self.probabilities)

    def walk(self, num_steps):
    	for i in range(num_steps):
    		next_direction = _next_direction()
    		if next_direction is 1:
    			self.position += np.array([0,1])
        return ""



if __name__ == "__main__":
    walk=RandomWalk(1.2,0,0.8,0.2,1,2)