from math import lcm

def day_8_p1(input):
    instructions, nodes = input.split('\n\n')
    nodes = nodes.replace('(', '').replace(')', '')
    nodes = {n.split(' = ')[0]: {'L': n.split(' = ')[1].split(', ')[0], 'R': n.split(' = ')[1].split(', ')[1]}
             for n in nodes.split('\n')}

    cur_node = 'AAA'
    steps = 0
    instructions_cur = 0

    while cur_node != 'ZZZ':
        if instructions_cur == len(instructions):
            instructions_cur = 0

        instruction = instructions[instructions_cur]
        cur_node = nodes[cur_node][instruction]
        steps += 1
        instructions_cur += 1

    return steps


def day_8_p2(input):
    instructions, nodes = input.split('\n\n')
    nodes = nodes.replace('(', '').replace(')', '')
    nodes = {n.split(' = ')[0]: {'L': n.split(' = ')[1].split(', ')[0], 'R': n.split(' = ')[1].split(', ')[1]}
             for n in nodes.split('\n')}

    start_nodes = [n for n in nodes if n.endswith('A')]
    nodes_steps = []
    instructions_cur = 0

    for node in start_nodes:
        cur_node = node
        steps = 0
        while not cur_node.endswith('Z'):
            if instructions_cur == len(instructions):
                instructions_cur = 0

            instruction = instructions[instructions_cur]
            cur_node = nodes[cur_node][instruction]
            steps += 1
            instructions_cur += 1

        nodes_steps.append(steps)

    return lcm(*nodes_steps)


with open('../input.txt') as f:
    input = f.read()

sample1 = '''RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)'''

sample2 = '''LR
11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)'''

print(day_8_p1(input))
print(day_8_p2(input))
