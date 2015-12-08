from __future__ import print_function


class Wire(object):

    def __init__(self, line):
        self._line = line
        self.parse_line(line)

    def parse_line(self, line):
        lline = line.split()
        self.output = lline[-1]

        left = lline[:-2]
        self.op = 'ASSIGN'
        for op in ['NOT', 'AND', 'OR', 'LSHIFT', 'RSHIFT']:
            if op in left:
                self.op = op
                left.remove(op)
        self.inputs = [int(i) if i.isdigit() else i for i in left]

    def reset(self):
        self.parse_line(self._line)

    def evaluate(self):
        if self.op == 'ASSIGN':
            return int(self.inputs[0])
        elif self.op == 'NOT':
            return int(65535 - self.inputs[0])
        elif self.op == 'AND':
            return int(self.inputs[0] & self.inputs[1])
        elif self.op == 'OR':
            return int(self.inputs[0] | self.inputs[1])
        elif self.op == 'LSHIFT':
            return int(self.inputs[0] << self.inputs[1])
        elif self.op == 'RSHIFT':
            return int(self.inputs[0] >> self.inputs[1])
        else:
            raise ValueError('invalid operator')

    def fill_inputs(self, signals):
        self.inputs = [signals[i] if i in signals else i for i in self.inputs]

    def iscomplete(self):
        return all([isinstance(i, int) for i in self.inputs])


with open('inputs/input07.txt') as f:
    wires = [Wire(line) for line in f]
wires_copy = list(wires)


def evaluate_circuit(wires, signals):
    local_wires = list(wires)
    while len(local_wires) != 0:
        new_wires = []
        for wire in wires:
            if wire.iscomplete():
                signals[wire.output] = wire.evaluate()
            else:
                wire.fill_inputs(signals)
                new_wires.append(wire)
        local_wires = new_wires
    return signals


signals = evaluate_circuit(wires, {})
print('a', signals['a'])

[wire.reset() for wire in wires]
wires = [wire for wire in wires if wire.output != 'b']
signals = evaluate_circuit(wires, {'b': signals['a']})
print('a', signals['a'])
