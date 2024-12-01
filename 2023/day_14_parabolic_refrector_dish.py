def roll(grid):
    new_grid = []
    for r in grid:
        new_grid.append('#'.join([''.join(sorted(g, reverse=True)) for g in r.split('#')]))

    return tuple(new_grid)


def rotate_90(grid, clockwise=True):
    new_grid = []
    x_iter = range(len(grid[0])) if clockwise else range(len(grid[0]) - 1, -1, -1)
    y_iter = range(len(grid) - 1, -1, -1) if clockwise else range(len(grid))
    for x in x_iter:
        new_grid.append(''.join([grid[y][x] for y in y_iter]))

    return tuple(new_grid)


def calculate_load(grid):
    load = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 'O':
                load += len(grid) - y

    return load

def day_14_p1(input):
    grid = input.split('\n')
    return calculate_load(rotate_90(roll(rotate_90(grid, clockwise=False))))


def day_14_p2(input):
    grid = rotate_90(tuple(input.split('\n')), clockwise=False)
    cycles_todo = 1000000000
    seen = {}

    for cycle in range(cycles_todo):
        for i in range(4):
            grid = rotate_90(roll(grid))

        if grid in seen:
            loop_length = cycle - seen[grid]
            cycles_left = (cycles_todo - seen[grid]) % loop_length - 1

            for c in range(cycles_left):
                for i in range(4):
                    grid = rotate_90(roll(grid))

            break
        else:
            seen[grid] = cycle

    return calculate_load(rotate_90(grid))


with open('../input.txt') as f:
    input = f.read()

sample = '''O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....'''

print(day_14_p1(sample))
print(day_14_p2(input))
