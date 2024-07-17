def day_5_p1(input):
    categories = input.split('\n\n')
    mappings = []
    seeds = map(int, categories[0].split(': ')[1].split(' '))
    categories = categories[1:]

    for n, cat in enumerate(categories):
        mappings.append({})
        for r in cat.split('\n')[1:]:
            val_to, val_from, r = map(int, r.split(' '))
            mappings[n][(val_from, val_from+r-1)] = (val_to, val_to+r-1)

    closest_location = float('inf')
    for s in seeds:
        val = s
        for m in mappings:
            for val_from, val_to in m.items():
                if val_from[0] <= val <= val_from[1]:
                    val = val_to[0]+(val-val_from[0])
                    break

        if val < closest_location:
            closest_location = val

    return closest_location


def day_5_p2(input):
    categories = input.split('\n\n')
    seeds = categories[0].split(': ')[1].split(' ')
    seeds_ranges = []
    for start, r in zip(seeds[0::2], seeds[1::2]):
        seeds_ranges.append([int(start), int(start)+int(r)])

    categories = categories[1:]
    mappings = []

    for n, cat in enumerate(categories):
        mappings.append({})
        for r in cat.split('\n')[1:]:
            val_to, val_from, r = map(int, r.split(' '))
            mappings[n][(val_from, val_from+r-1)] = val_to - val_from

    for m in mappings:
        new_seeds_ranges = []
        for s_valfrom in seeds_ranges:
            s_valto = []
            for m_valfrom, modifier in m.items():
                if s_valfrom[0] >= m_valfrom[0] and s_valfrom[1] <= m_valfrom[1]:
                    s_valto.append((s_valfrom[0]+modifier, s_valfrom[1]+modifier))
                    break
                elif m_valfrom[0] <= s_valfrom[0] <= m_valfrom[1]:
                    s_valto.append((s_valfrom[0]+modifier, m_valfrom[1]+modifier))
                    s_valfrom = (m_valfrom[1]+1, s_valfrom[1])
                elif m_valfrom[0] <= s_valfrom[1] <= m_valfrom[1]:
                    s_valto.append((m_valfrom[0]+modifier, s_valfrom[1]+modifier))
                    s_valfrom = (s_valfrom[0], m_valfrom[0]-1)
            else:
                s_valto.append((s_valfrom[0], s_valfrom[1]))

            new_seeds_ranges.extend(s_valto)

        seeds_ranges = new_seeds_ranges.copy()

    closest_location = float('inf')
    for r in seeds_ranges:
        closest_location = min(r[0], closest_location)

    return closest_location


with open('../input.txt') as f:
    input = f.read()

sample = '''seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4'''

print(day_5_p1(input))
print(day_5_p2(input))
