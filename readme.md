Maze Search
===========

A search-based Python maze solver.

![A pair of adorable robots having fun solving a maze - FLUX.1-dev](https://github.com/user-attachments/assets/c8409a36-ef04-4f77-b854-fb235588754e)

Learning Objectives
-------------------

After completing this lab, students will be able to:

- Model certain agent problems as actions that enact transitions from one state to another
- Solve a basic search problem using the Python programming language

Task
----

Handout code is provided in [search.py](search.py). This file includes a number of example mazes along with code to display them visually and test that an agent is able to solve them. This file can be run directly to confirm that all mazes are solved:

```sh
python3 search.py
```

This program assumes that an agent is given access to all information about the maze including their start position, goal, and locations of walls. Mazes are represented as 2-dimensional arrays of characters and have the following form:

```
##########
#        #
# ### ## #
#   #### #
### ##   #
#   ## # #
# #### # #
#s#g   # #
##########

s = Start state
g = Goal state
# = Wall
```

Your task is to implement the `plan_solution` function so that it is able to return a list of actions that will solve the provided maze. Your solution does not have to be optimal, but it may not contain moves that would result in the agent attepting to run through walls. The allowed actions that can be returned are `UP`, `DOWN`, `LEFT`, and `RIGHT`.
