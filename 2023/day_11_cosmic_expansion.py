def day_11(input, empty_space):
    arr = [list(r) for r in input.split('\n')]

    galaxies, galaxies_presence_y, galaxies_presence_x = [], set(), set()

    for y in range(len(arr)):
        for x in range(len(arr[y])):
            if arr[y][x] == '#':
                galaxies.append((y, x))
                galaxies_presence_y.add(y)
                galaxies_presence_x.add(x)

    y_map, x_map = {}, {}
    unocupied_y, unocupied_x = 0, 0
    for distance in range(len(arr)):
        if distance not in galaxies_presence_y:
            unocupied_y += empty_space
        if distance not in galaxies_presence_x:
            unocupied_x += empty_space

        y_map[distance] = distance + unocupied_y
        x_map[distance] = distance + unocupied_x

    pair_distances = 0
    for g1 in range(len(galaxies)):
        for g2 in range(g1+1, len(galaxies)):
            pair_distances += abs(y_map[galaxies[g1][0]] - y_map[galaxies[g2][0]]) + abs(x_map[galaxies[g1][1]] - x_map[galaxies[g2][1]])

    return pair_distances


with open('../input.txt') as f:
    input = f.read()

sample = '''...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....'''


print(day_11(input, 1))
print(day_11(input, 999999))
