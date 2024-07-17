import math


def generate_modules(input):
    modules = {}
    broadcaster_outputs = None
    for module in input.split('\n'):
        left, right = module.split(' -> ')
        target = tuple(right.split(', '))
        if left == 'broadcaster':
            broadcaster_outputs = target
        else:
            type = left[0]
            name = left[1:]
            targets = target
            modules[name] = Module(name, type, targets)

    target_module = None
    for module in modules.values():
        for output in module.outputs:
            if output not in modules.keys():
                target_module = output
            elif modules[output].type == '&':
                modules[output].memory[module.name] = 'low'

    if target_module:
        modules[target_module] = Module(target_module, 'target', ())

    return modules, broadcaster_outputs


class Module:
    def __init__(self, name, type, outputs):
        self.name = name
        self.type = type
        self.outputs = outputs

        if type == '%':
            self.memory = False
        elif type == '&':
            self.memory = {}
        else:
            self.memory = None

    def __repr__(self):
        return self.name + "{type=" + self.type + ", outputs=" + str(self.outputs) + ", memory=" + str(mem_out) + '}'

    def run_flip_flop(self, pulse):
        if pulse == 'high':
            return ()

        self.memory = not self.memory
        pulse_out = 'high' if self.memory else 'low'
        return ((self.name, pulse_out, o) for o in self.outputs)

    def run_conjunction(self, source, pulse):
        self.memory[source] = pulse
        if all(m == 'high' for m in self.memory.values()):
            pulse_out = 'low'
        else:
            pulse_out = 'high'

        return ((self.name, pulse_out, o) for o in self.outputs)

    def run_target(self):
        return ()

    def run_module(self, source, pulse):
        if self.type == '%':
            return self.run_flip_flop(pulse)
        elif self.type == '&':
            return self.run_conjunction(source, pulse)
        else:
            return self.run_target()


def broadcaster():
    return [('broadcaster', 'low', o) for o in broadcaster_outputs]


def day_20_p1():
    def push_button(queue, pulses):
        if not queue:
            return

        source, pulse, target = queue.pop(0)
        pulses[pulse] += 1
        outputs = modules[target].run_module(source, pulse)
        queue.extend(outputs)

        return push_button(queue, pulses)

    pulses = {'low': 0, 'high': 0}
    for push in range(1000):
        pulses['low'] += 1
        push_button(broadcaster(), pulses)

    return pulses['low'] * pulses['high']


def day_20_p2():
    def push_button(queue, cycles, presses):
        if not queue:
            return

        source, pulse, target = queue.pop(0)
        outputs = modules[target].run_module(source, pulse)
        queue.extend(outputs)

        module = modules[target]
        if module.name == 'hf' and pulse == "high" and not cycles[source]:
            cycles[source] = presses

        return push_button(queue, cycles, presses)

    required_module = modules['hf']
    cycles = {m: None for m in required_module.memory.keys()}
    presses = 0
    while not all(cycles.values()):
        presses += 1
        push_button(broadcaster(), cycles, presses)

    return math.lcm(*cycles.values())


with open('../input.txt') as f:
    input = f.read()

sample = '''broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a'''

sample2 = '''broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output'''


run = input
modules, broadcaster_outputs = generate_modules(run)
print(day_20_p1())
print(day_20_p2())