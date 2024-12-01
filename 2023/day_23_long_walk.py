with open('../input.txt') as f:
    data = f.read()

sample = '''#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#'''

gate_directions = {
    '<': (0, -1),
    '>': (0, 1),
    '^': (-1, 0),
    'v': (1, 0),
    'e': (1, 0),
    's': (1, 0)
}


def get_start_end(grid):
    start = tuple([(0, int(x)) for x in range(len(grid[0])) if grid[0][x] == '.'][0])
    end = tuple([(len(grid) - 1, int(x)) for x in range(len(grid[-1])) if grid[-1][x] == '.'][0])
    grid[start[0]][start[1]] = 's'
    grid[end[0]][end[1]] = 'e'

    return grid, start, end


def day_23_p1(grid):
    def valid_gate(gate, last_move):
        return gate_directions[gate] == last_move

    def search_region(node, move, steps, grid, visited, gate_from, gate_paths):
        node = (node[0] + move[0], node[1] + move[1])
        visited.add(node)
        y, x = node
        if grid[y][x] in ('<', '>', 'v', '^', 'e'):
            if valid_gate(grid[y][x], move):
                if gate_from not in gate_paths:
                    gate_paths[gate_from] = {}

                gate_paths[gate_from][node] = max(gate_paths[gate_from].get(node, 0), steps)

            return

        for move in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            next_node = (y + move[0], x + move[1])
            ny, nx = next_node
            if next_node not in visited and 0 <= ny < len(grid) and 0 <= nx < len(grid[0]) and grid[ny][nx] in (
                    '.', '<', '>', 'v', '^', 'e'):
                search_region(node, move, steps + 1, grid, visited.copy(), gate_from, gate_paths)

    def get_gate_paths(grid, start, end):
        gate_paths, gate_seen, gate_queue = {}, set(), [start]
        gate_seen.add(start)
        gate_seen.add(end)
        while gate_queue:
            start_node = gate_queue.pop(0)
            next_move = gate_directions[grid[start_node[0]][start_node[1]]]
            search_region(start_node, next_move, 1, grid, {start_node}, start_node, gate_paths)
            new_gates = [g2 for g1 in gate_paths.values() for g2 in g1.keys() if g2 not in gate_seen]
            gate_queue.extend(new_gates)
            gate_seen.update(new_gates)

        return gate_paths

    def get_longest_path(gate_paths, start, end):
        queue = [(start, 0)]
        longest_path = 0
        while queue:
            gate, steps = queue.pop(0)
            if gate == end:
                longest_path = max(steps, longest_path)
                continue

            next_gate = [(g[0], g[1] + steps) for g in gate_paths.get(gate, {}).items()]
            queue.extend(next_gate)

        return longest_path

    grid, start, end = get_start_end(grid)
    gate_paths = get_gate_paths(grid, start, end)
    return get_longest_path(gate_paths, start, end)


def day_23_p2(grid):
    def in_direction_gate(gate, last_move):
        return gate_directions[gate] == last_move

    def search_region(node, move, steps, grid, visited, gate_from, gate_paths, dir):
        node = (node[0] + move[0], node[1] + move[1])
        visited.add(node)
        y, x = node
        if grid[y][x] in gate_directions.keys():
            gate_dir = 'in_direction' if in_direction_gate(grid[y][x], move) else 'ag_direction'
            gate_paths[gate_from][dir][node] = (max(gate_paths[gate_from][dir].get(node, (0, 'dummy'))[0], steps), gate_dir)
            return

        for move in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            next_node = (y + move[0], x + move[1])
            ny, nx = next_node
            if next_node not in visited and 0 <= ny < len(grid) and 0 <= nx < len(grid[0]) and grid[ny][nx] != '#':
                search_region(node, move, steps + 1, grid, visited.copy(), gate_from, gate_paths, dir)

    grid, start, end = get_start_end(grid)
    gates = [(y, x) for x in range(len(grid[0])) for y in range(len(grid)) if grid[y][x] in (gate_directions.keys())]
    gate_paths = {}
    for gate in gates:
        y, x = gate
        gate_paths[gate] = {}
        gate_paths[gate]['in_direction'] = {}
        gate_paths[gate]['ag_direction'] = {}
        move_in = gate_directions[grid[y][x]]
        move_out = (move_in[0] * -1, move_in[1] * -1)

        if gate != end:
            search_region(gate, move_in, 1, grid, {gate}, gate, gate_paths, 'in_direction')
        if gate != start:
            search_region(gate, move_out, 1, grid, {gate}, gate, gate_paths, 'ag_direction')

    longest_path = 0
    queue = [(start, {start}, 'in_direction', 0)]
    while queue:
        gate, visited, dir, steps = queue.pop(0)
        if gate == end:
            longest_path = max(longest_path, steps)

        next_gates = gate_paths[gate][dir]
        for next_gate, info in next_gates.items():
            steps_to_next_gate, next_dir = info
            if next_gate not in visited:
                next_visited = visited.copy()
                next_visited.add(next_gate)
                queue.append((next_gate, next_visited, next_dir, steps + steps_to_next_gate))

    return longest_path




print(day_23_p1([list(r) for r in data.split('\n')]))
print(day_23_p2([list(r) for r in data.split('\n')]))
