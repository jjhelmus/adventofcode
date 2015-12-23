from __future__ import print_function


verbose = False


class Computer(object):

    a = 0
    b = 0
    pointer = 0
    program = None

    def run_program(self, program, a=0):
        self.a = a
        self.b = 0
        self.pointer = 0
        self.program = program
        self.program_length = len(program)
        while self.pointer < self.program_length:
            instruction = self.program[self.pointer]
            self.execute_instruction(instruction)
        return

    def execute_instruction(self, instruction):
        command, register = instruction[0], instruction[1]

        if command == 'hlf':
            if register == 'a':
                self.a /= 2
            else:
                self.b /= 2
            self.pointer += 1

        elif command == 'tpl':
            if register == 'a':
                self.a *= 3
            else:
                self.b *= 3
            self.pointer += 1

        elif command == 'inc':
            if register == 'a':
                self.a += 1
            else:
                self.b += 1
            self.pointer += 1

        elif command == 'jmp':
            self.pointer += int(register)  # register is actually an offset

        elif command == 'jie':
            if {'a,': self.a, 'b,': self.b}[register] % 2 == 0:
                self.pointer += int(instruction[2])
            else:
                self.pointer += 1

        elif command == 'jio':
            if {'a,': self.a, 'b,': self.b}[register] == 1:
                self.pointer += int(instruction[2])
            else:
                self.pointer += 1
        else:
            raise ValueError("invalid instruction:", instruction)
        if verbose:
            print("After instructions: ", instruction)
            print("a:", self.a, "b:", self.b, "pointer:", self.pointer)
        return


# Example
computer = Computer()

example_program = [
    ['inc', 'a'],
    ['jio', 'a,', '+2'],
    ['tpl', 'a'],
    ['inc', 'a']
]

computer.run_program(example_program)
print(computer.a)

# part a
program = [line.split() for line in open('inputs/input23.txt')]
computer.run_program(program)
print(computer.b)

# part b
computer.run_program(program, a=1)
print(computer.b)
