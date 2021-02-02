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
[x,x,x,x,g,x],
[x,p,x,x,p,x],
[x,p,x,p,p,x],
[x,p,p,p,p,x],
[x,p,x,x,p,x],
[x,s,x,x,x,x],
[x,x,x,x,x,x],
]

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

def act(maze, direction):

G = nx.Graph()
G.pos = []
G.colors = []

i = 0
for x in range(0,6):
    for y in range(0,7):
        if maze[y][x] != 'a':
            G.add_node(i)
            G.pos.append((x,-y))
            i += 1

            if maze[y][x] == s:
                G.colors.append(1)
            elif maze[y][x] == x:
                G.colors.append(2)
            elif maze[y][x] == p:
                G.colors.append(3)
            elif maze[y][x] == g:
                G.colors.append(4)
            else:
                G.colors.append(0)


#G.add_edge(1, 2, weight=2.0)
#G.add_edge(1, 3)
#G.add_edge(2, 4)
#G.add_edge(2, 5)

#nx.draw(G, graphviz_layout(G, pos=prog="dot"))
print(G, G.pos)
nx.draw(G, G.pos, node_color=G.colors)
plt.show()
