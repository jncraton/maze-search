import copy
import time

mazes = [
    """
###
#g#
#s#
###
""",
    """
#####
#g#s#
# # #
#   #
#####
""",
    """
########
#s#    #
# # ## #
# # ####
#      #
### ## #
###### #
#g     #
########
""",
    """
##########
#        #
#        #
#        #
#    g   #
#   s    #
#        #
#        #
#        #
##########
""",
    """
##########
#        #
# ### ## #
#   #### #
### ##   #
#   ## # #
# #### # #
#s#g   # #
##########
""",
]

mazes = [[list(r.strip()) for r in m.strip().splitlines()] for m in mazes]

UP = (0, -1)
RIGHT = (1, 0)
DOWN = (0, 1)
LEFT = (-1, 0)


class MazeException(Exception):
    pass


def print_maze(maze):
    """Pretty-prints a maze"""
    for row in maze:
        print("".join(row))


def find_pos(maze, needle):
    """
    Returns the position of a given character in a maze

    >>> find_pos(mazes[0], 's')
    (1, 2)

    >>> find_pos(mazes[0], 'g')
    (1, 1)
    """
    for y, row in enumerate(maze):
        for x, space in enumerate(row):
            if space == needle:
                return (x, y)


def get_pos(maze, pos):
    """
    >>> get_pos(mazes[0], (1,2))
    's'

    >>> get_pos(mazes[1], (4,1))
    '#'
    """

    return maze[pos[1]][pos[0]]


def is_walkable(maze, pos):
    """Returns true if a position is a maze is walkable"""
    return get_pos(maze, pos) != "#"


def move(pos, action):
    """
    Returns new position after applying action

    >>> move((2,2), UP)
    (2, 1)
    """

    return (pos[0] + action[0], pos[1] + action[1])


def check(maze, actions, delay=0.4, quiet=False):
    """
    Check a sequence of actions to confirm that it solves a maze

    >>> check(mazes[1], [DOWN], quiet=True)
    Traceback (most recent call last):
     ...
    search.MazeException: Goal not reached at (3, 2)

    >>> check(mazes[0], [LEFT], quiet=True)
    Traceback (most recent call last):
     ...
    search.MazeException: Moved into wall at (0, 2)

    >>> check(mazes[1], [DOWN, DOWN, LEFT, LEFT, UP, UP], quiet=True)
    """

    pos = find_pos(maze, "s")

    display_maze = copy.deepcopy(maze)

    for action in actions:
        assert(action in {UP, DOWN, LEFT, RIGHT})
        pos = move(pos, action)

        if not quiet:
            display_maze[pos[1]][pos[0]] = "."
            print_maze(display_maze)
            time.sleep(delay)

        if not is_walkable(maze, pos):
            raise MazeException(f"Moved into wall at {pos}")

    if get_pos(maze, pos) != "g":
        raise MazeException(f"Goal not reached at {pos}")


def plan_solution(maze):
    """
    Computes a solution to a given maze

    Returns a list of actions needed to complete the maze

    >>> plan_solution(mazes[0])
    [(0, -1)]
    """

    return []

if __name__ == "__main__":
    for i, m in enumerate(mazes):
        print(f"\nTrying maze {i}")
        solution = plan_solution(m)
        try:
            check(m, solution, quiet=True)
            check(m, solution, delay=0.1)
        except MazeException:
            try:
                check(m, solution, delay=0.4)
            except MazeException as e:
                print(e)
                break
        print(f"Solved in {len(solution)} move(s)")
