f = open('1.txt', 'r')
lines = f.readlines()

sum = 0
elf_cals = []
for line in lines:
    if line == '\n':
        elf_cals.append(sum)
        sum = 0
    else:
        sum += int(line.strip())
        # print(sum)

elf_cals.sort(reverse=True)
print(elf_cals)
print(max(elf_cals))

print(elf_cals[0] + elf_cals[1] + elf_cals[2])
