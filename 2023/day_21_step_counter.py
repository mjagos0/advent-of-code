import sys
sys.setrecursionlimit(1000000)

moves = ((1, 0), (-1, 0), (0, 1), (0, -1))


def count_reachable_nodes(grid, start_node, steps, even_grid):
    reachable_nodes = 0
    seen = set(start_node)
    queue = [(start_node, 0)]

    while queue:
        node, step = queue.pop(0)
        y, x = node
        if step % 2 == even_grid:
           reachable_nodes += 1
        if step == steps:
            continue

        for ny, nx in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
            nnode = (ny, nx)
            if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]) and grid[ny][nx] == '.' and nnode not in seen:
                queue.append((nnode, step + 1))
                seen.add(nnode)

    return reachable_nodes


def day_21_p1(grid, steps, even_grid):
    start_node = [(y, x) for y in range(len(grid)) for x in range(len(grid[0])) if grid[y][x] == 'S'][0]
    return count_reachable_nodes(grid, start_node, steps, even_grid)


def day_21_p2(grid, steps):
    grid_size = len(grid)
    start_node = [(y, x) for y in range(len(grid)) for x in range(len(grid[0])) if grid[y][x] == 'S'][0]
    grids = steps // grid_size
    odd_grids, even_grids = (grids + 1) ** 2, grids ** 2
    odd_grid_points = count_reachable_nodes(grid, start_node, grid_size * 2, True)
    even_grid_points = count_reachable_nodes(grid, start_node, grid_size * 2, False)

    corner_t = count_reachable_nodes(grid, (130, 65), 130+1, False)
    corner_r = count_reachable_nodes(grid, ((grid_size-1)//2, grid_size-1), grid_size, False)
    corner_b = count_reachable_nodes(grid, (0, (grid_size-1)//2), grid_size, False)
    corner_l = count_reachable_nodes(grid, ((grid_size-1)//2, 0), grid_size, False)

    tl_even = count_reachable_nodes(grid, (grid_size-1, 0), grid_size // 2, True)
    tr_even = count_reachable_nodes(grid, (grid_size-1, grid_size-1), grid_size // 2, True)
    bl_even = count_reachable_nodes(grid, (0, 0), grid_size // 2, True)
    br_even = count_reachable_nodes(grid, (0, grid_size-1), grid_size // 2, True)

    tl_odd = count_reachable_nodes(grid, (grid_size-1, 0), grid_size // 2, False)
    tr_odd = count_reachable_nodes(grid, (grid_size-1, grid_size-1), grid_size // 2, False)
    bl_odd = count_reachable_nodes(grid, (0, 0), grid_size // 2, False)
    br_odd = count_reachable_nodes(grid, (0, grid_size-1), grid_size // 2, False)

    return (odd_grids * odd_grid_points + even_grids * even_grid_points
            + corner_t + corner_b + corner_l + corner_r
            - (grid_size+1) * (tl_odd + tr_odd + bl_odd + br_odd)
            + grid_size * (tl_even + tr_even + bl_even + br_even))




with open('../input.txt') as f:
    data = f.read()

sample = '''...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........'''

sample_args = (sample.split('\n'), 6, False)
input_args = (data.split('\n'), 64, False)
# print(day_21_p1(*sample_args))
print(day_21_p1(*input_args))
print(day_21_p2(data.split('\n'), 26501365))