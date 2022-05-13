import heapq

import motion_and_perception as robot
from constants import *

def construct_path(begin_position, begin_orientation, end_position, dp):
    [y, x] = end_position

    orientation = FRONT
    for i in range(4):
        if dp[y][x][i] and (dp[y][x][i] < dp[y][x][orientation] or not dp[y][x][orientation]):
            orientation = i

    ans = ""
    
    #print(orientation)
    while (y, x) != begin_position:
        #print(y, x)
        #FROM fwd
        if orientation == FRONT and y < 8 and dp[y+1][x][FRONT] == dp[y][x][orientation]-1:
            orientation = FRONT
            [y, x] = [y+1, x]
            ans += str('f')
        elif orientation == RIGHT and x > 0 and dp[y][x-1][RIGHT] == dp[y][x][orientation]-1:
            orientation = RIGHT
            [y, x] = [y, x-1]
            ans += str('f')
        elif orientation == BACK and y > 0 and dp[y-1][x][BACK] == dp[y][x][orientation]-1:
            orientation = BACK
            [y, x] = [y-1, x]
            ans += str('f')
        elif orientation == LEFT and x < 3 and dp[y][x+1][LEFT] == dp[y][x][orientation]-1:
            orientation = LEFT
            [y, x] = [y, x+1]
            ans += str('f')
        #from left
        elif orientation == FRONT and y < 8 and dp[y+1][x][RIGHT] == dp[y][x][orientation]-3:
            orientation = RIGHT
            [y, x] = [y+1, x]
            ans += str('l')
        elif orientation == RIGHT and x > 0 and dp[y][x-1][BACK] == dp[y][x][orientation]-3:
            orientation = BACK
            [y, x] = [y, x-1]
            ans += str('l')
        elif orientation == BACK and y > 0 and dp[y-1][x][LEFT] == dp[y][x][orientation]-3:
            orientation = LEFT
            [y, x] = [y-1, x]
            ans += str('l')
        elif orientation == LEFT and x < 3 and dp[y][x+1][FRONT] == dp[y][x][orientation]-3:
            orientation = FRONT
            [y, x] = [y, x+1]
            ans += str('l')
        #from right
        elif orientation == FRONT and y < 8 and dp[y+1][x][LEFT] == dp[y][x][orientation]-3:
            orientation = LEFT
            [y, x] = [y+1, x]
            ans += str('r')
        elif orientation == RIGHT and x > 0 and dp[y][x-1][FRONT] == dp[y][x][orientation]-3:
            orientation = FRONT
            [y, x] = [y, x-1]
            ans += str('r')
        elif orientation == BACK and y > 0 and dp[y-1][x][RIGHT] == dp[y][x][orientation]-3:
            orientation = RIGHT
            [y, x] = [y-1, x]
            ans += str('r')
        elif orientation == LEFT and x < 3 and dp[y][x+1][BACK] == dp[y][x][orientation]-3:
            orientation = BACK
            [y, x] = [y, x+1]
            ans += str('r')
        #FROM back
        if orientation == FRONT and y > 0 and dp[y-1][x][FRONT] == dp[y][x][orientation]-100:
            orientation = FRONT
            [y, x] = [y-1, x]
            ans += str('b')
        elif orientation == RIGHT and x < 3 and dp[y][x+1][RIGHT] == dp[y][x][orientation]-100:
            orientation = RIGHT
            [y, x] = [y, x+1]
            ans += str('b')
        elif orientation == BACK and y < 8 and dp[y+1][x][BACK] == dp[y][x][orientation]-100:
            orientation = BACK
            [y, x] = [y+1, x]
            ans += str('b')
        elif orientation == LEFT and x > 0 and dp[y][x-1][LEFT] == dp[y][x][orientation]-100:
            orientation = LEFT
            [y, x] = [y, x-1]
            ans += str('b')

    ans = ''.join(reversed(ans))
    return ans

def find_shortest_path(begin_position, begin_orientation):
    dp = [[[0 for a in range(4)] for a in range(4)] for a in range(9)] #x, y, orientation

    priority_queue = [(1, begin_position, begin_orientation)]
    heapq.heapify(priority_queue)

    while len(priority_queue):
        cost = priority_queue[0][0]
        [y, x] = priority_queue[0][1]
        orientation = priority_queue[0][2]
        heapq.heappop(priority_queue)

        if grid[y][x] == 1:
            continue

        if dp[y][x][orientation]:
            continue
        dp[y][x][orientation] = cost
        
        #move front
        if orientation == FRONT and y > 0:
            heapq.heappush(priority_queue, (cost+1, (y-1, x), FRONT))
        if orientation == RIGHT and x < 3:
            heapq.heappush(priority_queue, (cost+1, (y, x+1), RIGHT))
        if orientation == BACK and y < 8:
            heapq.heappush(priority_queue, (cost+1, (y+1, x), BACK))
        if orientation == LEFT and x > 0:
            heapq.heappush(priority_queue, (cost+1, (y, x-1), LEFT))

        #move right
        if orientation == FRONT and x < 3:
            heapq.heappush(priority_queue, (cost+3, (y, x+1), RIGHT))
        if orientation == RIGHT and y < 8:
            heapq.heappush(priority_queue, (cost+3, (y+1, x), BACK))
        if orientation == BACK and x > 0:
            heapq.heappush(priority_queue, (cost+3, (y, x-1), LEFT))
        if orientation == LEFT and y > 0:
            heapq.heappush(priority_queue, (cost+3, (y-1, x), FRONT))

        #move left
        if orientation == FRONT and x > 0:
            heapq.heappush(priority_queue, (cost+3, (y, x-1), LEFT))
        if orientation == RIGHT and y > 0:
            heapq.heappush(priority_queue, (cost+3, (y-1, x), FRONT))
        if orientation == BACK and x < 3:
            heapq.heappush(priority_queue, (cost+3, (y, x+1), RIGHT))
        if orientation == LEFT and y < 8:
            heapq.heappush(priority_queue, (cost+3, (y+1, x), BACK))

        #move back
        if orientation == FRONT and y < 8:
            heapq.heappush(priority_queue, (cost+100, (y+1, x), FRONT))
        if orientation == RIGHT and x > 0:
            heapq.heappush(priority_queue, (cost+100, (y, x-1), RIGHT))
        if orientation == BACK and y > 0:
            heapq.heappush(priority_queue, (cost+100, (y-1, x), BACK))
        if orientation == LEFT and x < 3:
            heapq.heappush(priority_queue, (cost+100, (y, x+1), LEFT))

    return dp

def generate_path(begin_position, begin_orientation, end_position):
    dp = find_shortest_path(begin_position, begin_orientation)
    #print("dp done")
    #print((dp[1][0][LEFT], dp[1][1][LEFT]))
    return construct_path(begin_position, begin_orientation, end_position, dp)


def follow_path(path):
    """
    follow the path given on a string
    each character indicates some instruction

    'r' = move right
    'l' = move left
    'f' = move front
    'b' = move back
    """
    for instruction in path:
        if instruction == 'f':
            robot.move_front()
        if instruction == 'b':
            robot.move_back()
        if instruction == 'r':
            robot.move_right()
        if instruction == 'l':
            robot.move_left()