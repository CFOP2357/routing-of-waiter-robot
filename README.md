# routing-of-waiter-robot

This project has the objective of simulating the routing of a waiter robot when it needs to deliver food in a restaurant.
The robot needs to arrive at 4 different positions and then return to the origin position. The environment is grid limited by black lines; each corner represents a different position.

The robots receive as input where obstacles are and to which positions it needs to arrive, and it always begins at a defined orientation and position. The current position of the robot is defined by the position of the light sensors and on each position, it can be at 4 different orientations.

The robot has four possible movements: move front, move and turn right, move and turn left and move back. Each movement has a different probability of failure, the robot needs to reduce the probability of failure in his route so it can be completed.

With the use of Dijkstra’s algorithm, the robot plans the route to his next goal position (next table), the first goal is to reduce the probability of failure and the second one is to finish as fast as possible.
