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
    print('start; s, g:', s, g)

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

	# "Disply" path by changing value of cell block to P after traveling through it
	# (represents path, & can't be accessed afterwards)

	# perhaps a recursive call/loop for every cardinal direction? each iteration, if a direction is open then go
        # need a system to determine if a given cell block is available or not
        # map[y +/- 1][x +/- 1] ? for indexing the map, where (y, x) is the current block location
        #
	# If returns false, begin iterating over next direction. Do this every call (obviously)
	# If returns True, also return true, & probably most updated map as well (store in tuple)
        # if MazeSolver(m, s, g):
            # return MazeSolver(m, s, g)


    return False

m = [[0, 0, 0, 0, 1],
     [0, 1, 1, 0, 1],
     [1, 1, 1, 0, 1],]
s = (0,0)
g = (2, 3)

m = [[0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
     [0, 1, 1, 1, 1, 1, 0, 0, 0, 1],
     [0, 1, 1, 0, 1, 0, 0, 1, 1, 1],
     [0, 0, 0, 0, 1, 0, 1, 1, 0, 0],
     [0, 1, 0, 1, 1, 0, 0, 0, 1, 0],
     [0, 1, 1, 0, 1, 1, 1, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
s = (0,0)
g = (3, 8)


print(len(m[0]))
print(MazeSolver(m,s,g))
