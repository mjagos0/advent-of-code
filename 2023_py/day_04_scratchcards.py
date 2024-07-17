import re

def day_4_scratchcards_p1(input):
    input = input.split('\n')[:-1]
    guess_sum = 0

    for l in input:
        winning_numbers, guessed_numbers = l.split(' | ')
        winning_numbers = winning_numbers.split(': ')[1]
        winning_numbers = re.findall('\d+', winning_numbers)
        guessed_numbers = re.findall('\d+', guessed_numbers)

        good_guesses = len([gn for gn in guessed_numbers if gn in winning_numbers])
        to_add = 0
        for i in range(good_guesses):
            to_add = 1 if to_add == 0 else to_add * 2

        guess_sum += to_add

    return guess_sum


def day_4_scratchcards_p2(input):
    input = input.split('\n')[:-1]
    scratchcards = {k: v for k, v in [(x, 1) for x in range(1, 215)]}

    for l in input:
        winning_numbers, guessed_numbers = l.split(' | ')
        card_num, winning_numbers = winning_numbers.split(': ')
        winning_numbers = re.findall('\d+', winning_numbers)
        guessed_numbers = re.findall('\d+', guessed_numbers)
        card_num = int(re.findall('\d+', card_num)[0])

        good_guesses = len([gn for gn in guessed_numbers if gn in winning_numbers])
        for i in range(card_num+1, card_num+good_guesses+1):
            scratchcards[i] += scratchcards[card_num]

    return sum(scratchcards.values())

with open('../input.txt') as f:
    input = f.read()

sample = '''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
'''

# print(day_3_scratchcards_p1(input))
print(day_3_scratchcards_p2(input))