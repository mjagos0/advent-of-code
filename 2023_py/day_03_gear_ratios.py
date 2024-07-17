NON_CAPTURING_SYMBOL_P1 = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.')
CAPTURING_SYMBOL_P2 = '*'

def has_adjacent_symbol(input, num_buffer, c, r):
    for x in range(max(c-(len(num_buffer)+1), 0), min(c+1, len(input[0]))):
        for y in range(max(r-1, 0), min(r+2, len(input))):
            if input[y][x] not in NON_CAPTURING_SYMBOL_P1:
                return True

    return False


def day_3_gear_ratios_p1(input):
    input = input.split('\n')[:-1]
    engine_sum = 0

    for r in range(len(input)):
        num_buffer = ''
        for c in range(len(input[r])):
            ch = input[r][c]
            if ch.isnumeric():
                num_buffer += ch

            if not ch.isnumeric() or len(input[r])-1 == c:
                if num_buffer:
                    c = c + 1 if len(input[r])-1 == c and ch.isnumeric() else c
                    if has_adjacent_symbol(input, num_buffer, c, r):
                        engine_sum += int(num_buffer)
                        print(f'valid number: {num_buffer}')

                    num_buffer = ''

    return engine_sum


def had_adjacent_gear(input, num_buffer, c, r):
    for x in range(max(c-(len(num_buffer)+1), 0), min(c+1, len(input[0]))):
        for y in range(max(r-1, 0), min(r+2, len(input))):
            if input[y][x] == CAPTURING_SYMBOL_P2:
                return (y, x)

    return None


def day_3_gear_ratios_p2(input):
    input = input.split('\n')[:-1]
    gears = {}
    gears_sum = 0

    for r in range(len(input)):
        num_buffer = ''
        for c in range(len(input[r])):
            ch = input[r][c]
            if ch.isnumeric():
                num_buffer += ch

            if not ch.isnumeric() or len(input[r])-1 == c:
                if num_buffer:
                    c = c + 1 if len(input[r])-1 == c and ch.isnumeric() else c
                    gear_loc = had_adjacent_gear(input, num_buffer, c, r)
                    if gear_loc:
                        if gear_loc in gears.keys():
                            gears_sum += int(num_buffer) * gears[gear_loc]
                            del gears[gear_loc]
                        else:
                            gears[gear_loc] = int(num_buffer)

                    num_buffer = ''

    return gears_sum


with open('../input.txt') as f:
    input = f.read()

sample = '''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
'''

print(day_3_gear_ratios_p1(input))
print(day_3_gear_ratios_p2(input))