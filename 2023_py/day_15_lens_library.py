def lens_hash(s):
    cur_val = 0
    for c in s:
        cur_val = (cur_val + ord(c)) * 17 % 256

    return cur_val

def day_15_p1(input):
    result_sum = 0
    for s in input.split(','):
        result_sum += lens_hash(s)

    return result_sum


def day_15_p2(input):
    def remove_lens(boxes, lens, s):
        lens_label = s[:-1]
        box_num = lens_hash(lens_label)

        if lens_label in boxes[box_num]:
            boxes[box_num].remove(lens_label)
            del lens[box_num][lens_label]

        return boxes, lens

    def add_lens(boxes, lens, s):
        lens_label, focal_length = s.split('=')
        focal_length = int(focal_length)
        box_num = lens_hash(lens_label)

        if lens_label not in boxes[box_num]:
            boxes[box_num].append(lens_label)

        lens[box_num][lens_label] = focal_length

        return boxes, lens

    boxes = {k: [] for k in range(256)}
    lens = {k: {} for k in range(256)}

    for s in input.split(','):
        if s.endswith('-'):
            boxes, lens = remove_lens(boxes, lens, s)
        else:
            boxes, lens = add_lens(boxes, lens, s)

    lens_power = 0
    for boxnum, box in boxes.items():
        for lensnum, lens_ in enumerate(box):
            lens_power += (boxnum + 1) * (lensnum + 1) * lens[boxnum][lens_]

    return lens_power


with open('../input.txt') as f:
    input = f.read()

sample = '''rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'''

print(day_15_p1(input))
print(day_15_p2(input))
