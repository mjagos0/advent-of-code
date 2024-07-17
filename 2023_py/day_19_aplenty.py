ops = {
    '>': int.__gt__,
    '<': int.__lt__,
}

def process_workflows(workflows_str):
    workflows, parts = {}, []
    for w in workflows_str.split('\n'):
        name, rules = w[:-1].split('{')
        rules = rules.split(',')
        workflows[name] = ([], rules.pop())
        for rule in rules:
            comparison, target = rule.split(':')
            key = comparison[0]
            op = comparison[1]
            n = int(comparison[2:])
            workflows[name][0].append((key, op, n, target))

    return workflows


def process_parts(process_parts_str):
    parts = []
    for n, p in enumerate(process_parts_str.split('\n')):
        parts.append({})
        for item in p[1:-1].split(','):
            subject, value = item.split('=')
            parts[n][subject] = int(value)

    return parts


def apply_workflow(part, name):
    if name == 'A':
        return True
    elif name == 'R':
        return False

    workflow, fallback = workflows[name]
    for key, op, n, target in workflow:
        if ops[op](part[key], n):
            return apply_workflow(part, target)

    return apply_workflow(part, fallback)


def day_19_p1():
    total = 0
    name = 'in'
    for part in parts:
        if apply_workflow(part, name):
            total += sum(part.values())

    return total


def multiply(lst):
    prod = 1
    for i in lst:
        prod *= i

    return prod


def search_workflow(part, name, combinations):
    if name == 'A':
        combinations[0] += multiply([r[1] - r[0] + 1 for r in part.values()])
        return
    elif name == 'R':
        return

    workflow, fallback = workflows[name]
    for key, op, n, target in workflow:
        if op == '>' and part[key][1] > n:
            new_part = part.copy()
            new_part[key] = (n+1, part[key][1])
            part[key] = (part[key][0], n)
            search_workflow(new_part, target, combinations)
        elif op == '<' and part[key][0] < n:
            new_part = part.copy()
            new_part[key] = (part[key][0], n-1)
            part[key] = (n, part[key][1])
            search_workflow(new_part, target, combinations)

        if part[key][0] > part[key][1]:
            return

    search_workflow(part, fallback, combinations)


def day_19_p2():
    combinations = [0]
    search_workflow({'x': (1, 4000), 'm': (1, 4000), 'a': (1, 4000), 's': (1, 4000)}, 'in', combinations)
    return combinations


with open('../input.txt') as f:
    input = f.read()

sample = r'''px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}'''

run = input
workflows_str, parts_str = run.split('\n\n')
workflows = process_workflows(workflows_str)
parts = process_parts(parts_str)

print(day_19_p1())
print(day_19_p2())
