import sys
sys.setrecursionlimit(20000)


def get_next_moves(vec, obj):
    if obj == '.':
        return (vec,)
    elif obj == '|':
        if vec[0]:
            return (vec,)
        else:
            return ((-1, 0), (1, 0))
    elif obj == '-':
        if vec[0]:
            return ((0, -1), (0, 1))
        else:
            return (vec, )
    elif obj == '/':
        if vec[0]:
            return ((0, -vec[0]),)
        else:
            return ((-vec[1], 0),)
    else:
        if vec[0]:
            return ((0, vec[0]),)
        else:
            return ((vec[1], 0),)


def traverse(arr, loc, vec, visited_loc):
    loc = (loc[0] + vec[0], loc[1] + vec[1])
    if loc[0] < 0 or loc[0] >= len(arr) or loc[1] < 0 or loc[1] >= len(arr[0]): # left grid
        return
    if (loc, vec) in visited_loc:
        return

    visited_loc.add((loc, vec))
    obj = arr[loc[0]][loc[1]]
    for vec_next in get_next_moves(vec, obj):
        traverse(arr, loc, vec_next, visited_loc)

    return visited_loc


def day_16_p1(input):
    arr = input.split('\n')
    visited_loc = traverse(arr, (0, -1), (0, 1), set())

    return len(set([loc[0] for loc in visited_loc]))


def day_16_p2(input):
    arr = input.split('\n')

    max_energized = 0
    for y in range(len(arr)):
        for x in range(len(arr[0])):
            loc = (y, x)
            if y == 0 or x == 0:
                for vec in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    visited_loc = traverse(arr, loc, vec, set())
                    max_energized = max(max_energized,
                                        len(set([loc[0] for loc in visited_loc])) if visited_loc is not None else 0)

    return max_energized


with open('../input.txt') as f:
    input = f.read()

sample = r'''.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....'''

print(day_16_p1(input))
print(day_16_p2(input))