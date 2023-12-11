from collections import defaultdict, deque

neighboormapping = {
    "-": ((0, -1), (0, 1)),
    "|": ((-1, 0), (1, 0)),
    "F": ((1, 0), (0, 1)),
    "7": ((1, 0), (0, -1)),
    "J": ((-1, 0), (0, -1)),
    "L": ((-1, 0), (0, 1)),
    # "S": ((1, 0), (0, -1)),  # Determined by hand actual input
    "S": ((1, 0), (0, 1))  # Testinput
}


def get_pipe_locations(grid):
    symbols = {}
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] in neighboormapping:
                symbols[(x, y)] = grid[x][y]
                if grid[x][y] == "S":
                    s = (x, y)
    return symbols, s


def get_adjacency_graph(pipemap):
    graph = defaultdict(list)
    for location, symbol in pipemap.items():
        neigbours = neighboormapping[symbol]
        for neigbour in neigbours:
            if ((location[0] + neigbour[0]), (location[1] + neigbour[1])) in pipemap:
                graph[location].append(((location[0] + neigbour[0]), (location[1] + neigbour[1])))
    return graph


def get_outer_bounds(x, y):
    a = set(zip([-1] * (x + 2), range(-1, x + 1)))
    b = set(zip(range(-1, y + 1), [-1] * (y + 2)))
    c = set(zip([x] * (x + 2), range(-1, x + 1)))
    d = set(zip(range(-1, y + 1), [y] * (y + 2)))

    return a | b | c | d


def dfs(graph, source):
    visited = set()
    stack = deque()
    stack.appendleft(source)

    while stack:
        s = stack.popleft()
        if s not in visited:
            visited.add(s)
        else:
            continue
        for neighbour in graph[s]:
            stack.appendleft(neighbour)

    return visited


with open("inputs/10t2.txt") as f:
    raw = f.read().splitlines()

pipemap, start = get_pipe_locations(raw)
graph = get_adjacency_graph(pipemap)

loop = dfs(graph, start)
print(len(loop) // 2)
