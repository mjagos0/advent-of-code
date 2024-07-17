from queue import PriorityQueue

lookup_dict = {
    (1, 0): ((1, 0), (0, 1), (0, -1)),
    (-1, 0): ((-1, 0), (0, 1), (0, -1)),
    (0, 1): ((0, 1), (1, 0), (-1, 0)),
    (0, -1): ((0, -1), (1, 0), (-1, 0)),
    (0, 0): ((0, 1), (1, 0))
}


def day_17_p1(input, queue, node, vec, convec, heatloss, visited_nodes):
    arr = input.split('\n')
    while node != (len(arr)-1, len(arr[0])-1):
        y, x = node
        con_y, con_x = convec
        lookup = lookup_dict[vec]
        three_blocks_straight = con_y in (-3, 3) or con_x in (-3, 3)
        if three_blocks_straight:
            lookup = lookup[1:]

        for change_y, change_x in lookup:
            next_y, next_x = y + change_y, x + change_x
            next_node = (next_y, next_x)
            next_convec = (con_y + change_y, con_x + change_x) if (con_y and change_y) or (con_x and change_x) else (
            change_y, change_x)
            if (next_node, next_convec) not in visited_nodes and 0 <= next_y < len(arr) and 0 <= next_x < len(arr[0]):
                next_heatloss = heatloss + int(arr[next_y][next_x])
                visited_nodes.add((next_node, next_convec))
                queue.put((next_heatloss, (next_node, (change_y, change_x), next_convec, next_heatloss)))

        node, vec, convec, heatloss = queue.get()[1]

    return heatloss


def day_17_p2(input, queue, node, vec, convec, heatloss, visited_nodes):
    arr = input.split('\n')
    while node != (len(arr)-1, len(arr[0])-1) or max(convec) < 4:
        y, x = node
        con_y, con_x = convec
        lookup = lookup_dict[vec]
        if max(abs(con_y), abs(con_x)) < 4 and max(abs(con_y), abs(con_x)) != 0:
            lookup = (lookup[0],)
        elif abs(max(abs(con_y), abs(con_x))) == 10:
            lookup = lookup[1:]

        for change_y, change_x in lookup:
            next_y, next_x = y + change_y, x + change_x
            next_node = (next_y, next_x)
            next_convec = (con_y + change_y, con_x + change_x) if (con_y and change_y) or (con_x and change_x) else (
            change_y, change_x)
            if (next_node, next_convec) not in visited_nodes and 0 <= next_y < len(arr) and 0 <= next_x < len(arr[0]):
                next_heatloss = heatloss + int(arr[next_y][next_x])
                visited_nodes.add((next_node, next_convec))
                queue.put((next_heatloss, (next_node, (change_y, change_x), next_convec, next_heatloss)))

        node, vec, convec, heatloss = queue.get()[1]

    return heatloss


with open('../input.txt') as f:
    input = f.read()

sample = r'''2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533'''

sample2 = '''111111111111
999999999991
999999999991
999999999991
999999999991'''

print(day_17_p1(input, PriorityQueue(), (0, 0), (0, 0), (0, 0), 0, set()))
print(day_17_p2(input, PriorityQueue(), (0, 0), (0, 0), (0, 0), 0, set()))
