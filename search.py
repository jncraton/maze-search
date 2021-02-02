x='#'
p='.'
s='s'
g='g'

maze = """
#####g#
#.###.#
#.....#
#.###.#
#...###
###s###
"""

maze = [
[x,x,x,x,x,x],
[x,x,x,x,g,x],
[x,p,x,p,p,x],
[x,p,x,x,p,x],
[x,p,p,p,p,x],
[x,p,x,x,p,x],
[x,s,x,x,x,x],
[x,x,x,x,x,x],
]

UP = (0,-1)
RIGHT = (1, 0)
DOWN = (0, 1)
LEFT = (-1, 0)

def find_pos(maze, needle):
    """

    >>> find_pos(maze, 's')
    (1, 6)
    
    >>> find_pos(maze, 'g')
    (4, 1)
    """
    for y, row in enumerate(maze):
        for x, space in enumerate(row):
            if space == needle:
                return (x, y)

def print_maze(maze):
    for row in maze:
        print(''.join(row))

def get_pos(maze, pos):
    """
    >>> get_pos(maze, (1,2))
    '.'
    
    >>> get_pos(maze, (4,1))
    'g'
    """

    return maze[pos[1]][pos[0]]

def is_walkable(maze, pos):
    return get_pos(maze, pos) != '#'

def check(maze, actions):
    """

    >>> check(maze, [UP])
    Traceback (most recent call last):
     ...
    Exception: Goal not reached at [1, 5]
    
    >>> check(maze, [DOWN])
    Traceback (most recent call last):
     ...
    Exception: Moved into wall at [1, 7]

    >>> check(maze, [UP, UP, RIGHT, RIGHT, RIGHT, UP, UP, UP])
    """

    pos = list(find_pos(maze, 's'))

    for action in actions:
        for i in range(2):
            pos[i] += action[i]

        if not is_walkable(maze, pos):
            raise Exception(f"Moved into wall at {pos}")

    if get_pos(maze, pos) != 'g':
        raise Exception(f"Goal not reached at {pos}")

def agent(maze, position):
    return [UP]

if __name__ == '__main__':
    #check(maze, [UP])
    print_maze(maze)