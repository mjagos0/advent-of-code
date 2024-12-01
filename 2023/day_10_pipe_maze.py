import sys
sys.setrecursionlimit(20000)

PIPES = {
    '┌': [(0, 1), (1, 0)],
    '└': [(0, 1), (-1, 0)],
    '┘': [(0, -1), (-1, 0)],
    '┐': [(0, -1), (1, 0)],
    '│': [(1, 0), (-1, 0)],
    '─': [(0, 1), (0, -1)]
}


def day_10_p1(input):
    arr = [list(r) for r in input.split('\n')]
    start_node = [(y, x) for y in range(len(arr)) for x in range(len(arr[y])) if arr[y][x] == 'S'][0]
    arr[start_node[0]][start_node[1]] = '┐'

    def bfs(queue, visited, steps):
        node = queue.pop(0)
        if node in visited:
            return int(steps/2)

        visited.append(node)
        y, x = node
        pipe = arr[y][x]

        next_moves = PIPES[pipe]
        for move in next_moves:
            next_node = (y+move[0], x+move[1])
            if next_node not in visited:
                queue.append(next_node)

        return bfs(queue, visited, steps+1)

    steps = bfs([start_node], [], 0)

    return steps


def day_10_p2(input):
    arr = [list(r) for r in input.split('\n')]
    start_node = [(y, x) for y in range(len(arr)) for x in range(len(arr[y])) if arr[y][x] == 'S'][0]
    arr[start_node[0]][start_node[1]] = '┐'

    def bfs(queue, visited, steps):
        node = queue.pop(0)
        if node in visited:
            return visited

        visited.append(node)
        y, x = node
        pipe = arr[y][x]

        next_moves = PIPES[pipe]
        for move in next_moves:
            next_node = (y+move[0], x+move[1])
            if next_node not in visited:
                queue.append(next_node)

        return bfs(queue, visited, steps+1)

    loop_nodes = bfs([start_node], [], 0)
    outside_tiles = 0
    for y in range(len(arr)):
        inside = False
        last_corner_pipe = None
        for x in range(len(arr[y])):
            pipe = arr[y][x]
            if (y, x) in loop_nodes:
                if pipe in ('└', '┌'):
                    last_corner_pipe = pipe
                elif pipe in ('┘', '┐'):
                    if (pipe == '┘' and last_corner_pipe == '┌') or (pipe == '┐' and last_corner_pipe == '└'):
                        inside = not inside
                elif pipe == '│':
                    inside = not inside

            elif inside:
                # print(x, y)
                outside_tiles += 1

    return outside_tiles


with open('../input.txt') as f:
    input = f.read()

sample_p1_1 = '''.....
.S-7.
.|.|.
.L-J.
.....'''

sample_p1_2 = '''
..F7.
.FJ|.
SJ.L7
|F--J
LJ...'''

sample_p2_1 = '''...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........'''

sample_p2_2 = '''..........
.S------7.
.|F----7|.
.||....||.
.||....||.
.|L-7F-J|.
.|..||..|.
.L--JL--J.
..........'''

sample_p2_3 = '''.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...'''

sample_p2_4 = '''FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L'''


input = input.replace('J', '┘').replace('L', '└').replace('7', '┐').replace('F', '┌').replace('-', '─').replace('|', '│')

print(day_10_p1(input))
print(day_10_p2(input))
