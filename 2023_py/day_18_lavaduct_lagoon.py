direction_dict_p1 = {
    'R': (0, 1),
    'L': (0, -1),
    'D': (1, 0),
    'U': (-1, 0)
}

direction_dict_p2 = {
    '0': (0, 1),
    '1': (1, 0),
    '2': (0, -1),
    '3': (-1, 0)
}


def get_vertices(input, part1):
    instructions = input.split('\n')
    vertices = [(0, 0)]
    perimeter = 0
    y, x = 0, 0
    for i in instructions:
        d, s, c = i.split(' ')
        if part1:
            size = int(s)
            y_dir, x_dir = direction_dict_p1[d][0], direction_dict_p1[d][1]
        else:
            # breakpoint()
            size = int(c[2:7], 16)
            y_dir, x_dir = direction_dict_p2[c[-2]][0], direction_dict_p2[c[-2]][1]

        y += y_dir * size
        x += x_dir * size

        vertices.append((y, x))
        perimeter += abs(y_dir * size + x_dir * size)

    return vertices, perimeter


def shoelaces(vertices):
    area = 0
    for i in range(len(vertices)-1):
        area += vertices[i][1]*vertices[i+1][0] - vertices[i+1][1]*vertices[i][0]

    area = abs(area + vertices[-1][1] * vertices[0][0] - vertices[0][1] * vertices[-1][0]) / 2

    return area


def day_18(input, part1):
    vertices, perimeter = get_vertices(input, part1=part1)
    area = shoelaces(vertices)

    return int(perimeter/2 + 1 + area)




with open('../input.txt') as f:
    input = f.read()

sample = r'''R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)'''

print(day_18(input, part1=True))
print(day_18(input, part1=False))
