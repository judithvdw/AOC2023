from collections import defaultdict, deque, Counter


def get_pipe_locations(grid):
    symbols = {}
    for y in range(len(grid[0])):
        for x in range(len(grid)):
            if grid[x][y] in neighboormapping:
                symbols[(x, y)] = grid[x][y]
                if grid[x][y] == "S":
                    s = (x, y)
    return symbols, s


def get_adjacency_graph(pipemap, neighboormapping):
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


def clean_raw(raw, loop):
    clean_raw = []
    for y, line in enumerate(raw):
        clean_raw_line = ""
        for x, cell in enumerate(line):
            if (y, x) in loop:
                if cell == "S":
                    clean_raw_line += "7"
                else:
                    clean_raw_line += cell
            else:
                clean_raw_line += "."
        clean_raw.append(clean_raw_line)
    return clean_raw


def find_inside_cells(loop, raw):
    not_loop = {(x, y) for x in range(len(raw)) for y in range(len(raw[0]))} - loop
    inside_cells = []
    cleanraw = clean_raw(raw, loop)
    for cell in sorted(not_loop):
        x, y = cell
        left_view = cleanraw[x][y:]
        overview = Counter(left_view)
        walls = overview["|"] + min(overview["L"], overview["7"]) + min(overview["F"], overview["J"])
        if walls % 2 == 1:
            inside_cells.append(cell)
    return inside_cells


with open("inputs/10.txt") as f:
    raw = f.read().splitlines()

neighboormapping = {
    "-": ((0, -1), (0, 1)),
    "|": ((-1, 0), (1, 0)),
    "F": ((1, 0), (0, 1)),
    "7": ((1, 0), (0, -1)),
    "J": ((-1, 0), (0, -1)),
    "L": ((-1, 0), (0, 1)),
    "S": ((1, 0), (0, -1)),  # Determined by hand actual input
    # "S": ((1, 0), (0, 1))  # Testinput
}

pipemap, start = get_pipe_locations(raw)
graph = get_adjacency_graph(pipemap, neighboormapping)
loop = dfs(graph, start)
print(f"Part 1: {len(loop) // 2}")
print(f"Part 2: {len(find_inside_cells(loop, raw))}")
