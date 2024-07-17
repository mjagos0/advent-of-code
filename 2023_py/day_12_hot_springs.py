# Solved this problem with help of:
# https://www.reddit.com/r/adventofcode/comments/18hbbxe/2023_day_12python_stepbystep_tutorial_with_bonus/
import functools


@functools.lru_cache(maxsize=None)
def count_arrangements(record, groups):
    if not groups:
        return 1 if '#' not in record else 0

    if groups[0] > len(record):
        return 0

    next_elem = record[0]
    next_grp = groups[0]

    def dot():
        return count_arrangements(record[1:], groups)

    def hash():
        if record[:next_grp].replace('?', '#') != '#' * next_grp:
            return 0

        if len(record) == next_grp:
            if len(groups) == 1:
                return 1
            else:
                return 0

        if record[next_grp] in '.?':
            return count_arrangements(record[next_grp+1:], groups[1:])
        else:
            return 0

    def qmark():
        out = hash() + dot()

        return out
    
    if next_elem == '.':
        out = dot()
    elif next_elem == '#':
        out = hash()
    else:
        out = qmark()

    return out


def day_11(input, duplication_rate):
    arrangements = 0
    for r in input.split('\n'):
        record, groups = r.split(' ')
        groups = tuple(map(int, groups.split(','))) * duplication_rate
        record = '?'.join([record] * duplication_rate)
        arrangements += count_arrangements(record, groups)

    return arrangements

with open('../input.txt') as f:
    input = f.read()

sample = '''???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1'''

sample1 = '''#.#.### 1,1,3
.#...#....###. 1,1,3
.#.###.#.###### 1,3,1,6
####.#...#... 4,1,1
#....######..#####. 1,6,5
.###.##....# 3,2,1'''

print(day_11(input, 5))
