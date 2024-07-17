def day_11(input, smushes):
    mirror_sum = 0
    for input in input.split('\n\n'):
        for i, grid in enumerate((input.split('\n'), list(map(''.join, zip(*input.split('\n')))))):
            splits, row_len = {k: 0 for k in range(len(grid[0]))}, len(grid[0])

            for y in range(len(grid)):
                for x in range(1, row_len):
                    mirror_size = min(x, row_len - x)
                    if grid[y][x-mirror_size:x] == grid[y][x:x+mirror_size][::-1]:
                        splits[x] += 1

            split = [x for x in splits.keys() if splits[x] == len(grid) - smushes]
            if split:
                mirror_sum += split[0] * max(i*100, 1)
                break

    return mirror_sum


with open('../input.txt') as f:
    input = f.read()

sample = '''#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#'''

print(day_11(input, 0))
print(day_11(input, 1))
