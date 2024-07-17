import re

def day_1_trebuchet_p1(lines):
    out = 0

    for l in lines:
        for c in l:
            if c.isnumeric():
                out += int(c)*10
                break

        for c in l[::-1]:
            if c.isnumeric():
                out += int(c)
                break

    return out

def day_1_trebuchet_p2(lines):
    nums = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    out = 0

    for l in lines:
        g1 = re.search('(\d|one|two|three|four|five|six|seven|eight|nine)', l).group(1)
        g2 = re.search('(\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin)', l[::-1]).group(1)
        out += int(g1) * 10 if g1.isnumeric() else nums[g1] * 10
        out += int(g2) if g2.isnumeric() else nums[g2[::-1]]
        # print(l, int(g1) * 10 if g1.isnumeric() else nums[g1] * 10, int(g2) if g2.isnumeric() else nums[g2])

    return out

with open('input.txt') as f:
    lines = f.readlines()

nums = day_1_trebuchet_p1(lines)
print(nums)

nums = day_1_trebuchet_p2(lines)
print(nums)