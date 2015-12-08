from __future__ import print_function
import re

verbose = False


def size_in_memory(string):
    assert string[0] == '"'
    assert string[-1] == '"'
    in_mem = string[1:-1]
    in_mem = in_mem.replace("\\\\", "x")
    in_mem = in_mem.replace("\\\"", "x")
    in_mem, _ = re.subn('\\\\x..', 'x', in_mem)
    return len(in_mem)


def size_escaped(string):
    escaped = string
    escaped = escaped.replace("\\", "\\\\")
    escaped = escaped.replace('"', '\\"')
    escaped = '"' + escaped + '"'
    return len(escaped)


f = open('inputs/input08.txt')
# uncomment to run test strings
#f = ['""', '"abc"', '"aaa\\"aaa"', '"\\x27"']

total_chars_code = 0
total_chars_memory = 0
total_chars_escaped = 0

for line in f:
    line = line.strip()

    chars = len(line)
    in_mem = size_in_memory(line)
    escaped = size_escaped(line)
    if verbose:
        print(line, chars, in_mem, escaped)

    total_chars_code += len(line)
    total_chars_memory += size_in_memory(line)
    total_chars_escaped += escaped

print("total characters in string codes:", total_chars_code)
print("total characters in memory:", total_chars_memory)
print("total characters escaped", total_chars_escaped)
print("")
print("code - memory:", total_chars_code - total_chars_memory)
print("escaped - code:", total_chars_escaped - total_chars_code)
