with open('../input.txt') as f:
    data = f.read()

sample = '''1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9'''


def build_bricks_space(bricks):
    bricks = [list(map(int, b.replace('~', ',').split(','))) for b in bricks]
    return sorted(bricks, key=lambda x: x[2])


def bricks_intersect(b1, b2):
    return max(b1[0], b2[0]) <= min(b1[3], b2[3]) and max(b1[1], b2[1]) <= min(b1[4], b2[4])


def drop_bricks(bricks):
    for index, brick in enumerate(bricks):
        max_z = 1
        for check in bricks[:index]:
            if bricks_intersect(brick, check):
                max_z = max(max_z, check[5] + 1)
        brick[5] -= brick[2] - max_z
        brick[2] = max_z

    return bricks

def get_support_dict(bricks):
    supported_by, supports = {b: set() for b in range(len(bricks))}, {b: set() for b in range(len(bricks))}
    for j in range(len(bricks)):
        for i in range(len(bricks)):
            supported_brick = bricks[j]
            supporting_brick = bricks[i]
            if supporting_brick[5] == supported_brick[2]-1 and bricks_intersect(supported_brick, supporting_brick):
                supported_by[j].add(i)
                supports[i].add(j)

    return supported_by, supports


def day_21(bricks):
    bricks = build_bricks_space(bricks)
    bricks = drop_bricks(bricks)
    supported_by, supports = get_support_dict(bricks)

    can_disintegrate = 0
    for b in range(len(bricks)):
        if all(len(supported_by[j]) >= 2 for j in supports[b]):
            can_disintegrate += 1

    disintegration_effect = 0
    for brick in range(len(bricks)):
        queue = [j for j in supports[brick] if len(supported_by[j]) < 2]
        falling = set(queue)
        falling.add(brick)

        while queue:
            falling_brick = queue.pop()
            for k in supports[falling_brick]:
                if supported_by[k] <= falling:
                    queue.append(k)
                    falling.add(k)

        disintegration_effect += len(falling) - 1

    return can_disintegrate, disintegration_effect

print(day_21(data.split('\n')))
