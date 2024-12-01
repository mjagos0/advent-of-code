def day_2_cube_conundrum_p1(input):
    rows = input.split('\n')
    game_sum = 0

    for r in rows:
        game = r.split(': ')
        game_num = int(game[0].split(' ')[1])
        game_possible = True
        for pull in game[1].split('; '):
            limits = {'red': 12, 'green': 13, 'blue': 14}
            for item in pull.split(', '):
                num, color = item.split(' ')
                limits[color] -= int(num)
                if limits[color] < 0:
                    game_possible = False
                    break

            if not game_possible:
                break

        if game_possible:
            game_sum += game_num

    return game_sum


def day_2_cube_conundrum_p2(input):
    rows = input.split('\n')
    game_sum = 0

    for r in rows:
        game = r.split(': ')
        cube_max = {'red': 0, 'green': 0, 'blue': 0}
        for pull in game[1].split('; '):
            cube_cur = {'red': 0, 'green': 0, 'blue': 0}
            for item in pull.split(', '):
                num, color = item.split(' ')
                cube_cur[color] += int(num)

            for color in cube_cur:
                cube_max[color] = max(cube_cur[color], cube_max[color])

        game_sum += cube_max['red'] * cube_max['green'] * cube_max['blue']

    return game_sum


sample = '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'''

with open('../input.txt') as f:
    input = f.read()

print(day_2_cube_conundrum_p1(input))
print(day_2_cube_conundrum_p2(input))
