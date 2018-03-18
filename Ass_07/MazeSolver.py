## Tyrel Kostyk, tck290, 11216033
## CMPT145-04, Lab Section 04
## A7q7; MazeSolver.py, due Saturday March 17th, 2018, 10pm

def MazeSolver(m, s, g):
    '''
    Determines IF a path from a start point to an end point of a given maze exists; displays path
    :params:
    m - 2D list, initially read from file then recursively updated
        - 0's indicate an open cell, 1's are blocked cells, P's are the path (also blocked)
    s - tuple, start point (updated recursively); FORMAT -> (y, x), this is how 2D lists are indexed
    g - tuple, end point (static); FORMAT -> (y, x), this is how 2D lists are indexed
    :returns:
    if path exists - True, maze showing succesful path through maze
    if not - False
    '''
    # obtain y & x coordinates, update maze
    y, x = s
    m[y][x] = 'P'

    # base case: reached destination point
    if s == g:
        return True, m

    # check each cardinal direction for possible path; if open, begin recursive call in that direction
    else:
        # Check east
        if (x+1 < len(m[0])) and (m[y][x+1] == 0):
            valid, maze = MazeSolver(m, (y,x+1), g)
            # if recursive returns True, it returns True & the updated map
            if valid:
                return valid, maze
                # otherwise, it exits the "check east" block & proceeds to "check south" block

        # check south
        if (y+1 < len(m)) and (m[y+1][x] == 0):
            valid, maze = MazeSolver(m, (y+1,x), g)
            if valid:
                return valid, maze

        # check north
        if (m[y-1][x] == 0) and (y > 0):
            valid, maze = MazeSolver(m, (y-1,x), g)
            if valid:
                return valid, maze

        # check west
        if (m[y][x-1] == 0) and (x > 0):
            valid, maze = MazeSolver(m, (y,x-1), g)
            if valid:
                return valid, maze

        # if none of the cardinal directions worked, return False
        # the previous call will either try a different direction, or return False as well
        return False, None
    return False, None

# create maze from Maze1.txt
maze_file = open('Maze1.txt', 'r')
m1 = []
for line in maze_file:
    line = line.split()
    for i in range(len(line)):
        line[i] = int(line[i])
    m1.append(line)

# create maze from Maze2.txt
maze_file = open('Maze2.txt', 'r')
m2 = []
for line in maze_file:
    line = line.split()
    for i in range(len(line)):
        line[i] = int(line[i])
    m2.append(line)

# create maze from Maze3.txt
maze_file = open('Maze3.txt', 'r')
m3 = []
for line in maze_file:
    line = line.split()
    for i in range(len(line)):
        line[i] = int(line[i])
    m3.append(line)

# set start & end points
s1, g1 = (0,3), (4,5)
s2, g2 = (0,0), (8,9)
s3, g3 = (3,0), (23,30)

# test the programs
print(MazeSolver(m1, s1, g1))
print(MazeSolver(m2, s2, g2))
print(MazeSolver(m3, s3, g3))
