lines = [line for line in open('inputs/input19.txt')]

medicine = lines[-1].strip()

# LHS, RHS sorted with largest LHS first
replacements = [(l.split()[-1], l.split()[0]) for l in lines if '=>' in l]
replacements.sort(key=lambda x: len(x[0]))
replacements = replacements[::-1]

# greedy replacement on medicine, counting steps
total = 0
while medicine != 'e':
    for lhs, rhs in replacements:
        if lhs in medicine:
            medicine = medicine.replace(lhs, rhs, 1)
            total += 1
            break
print(total)
