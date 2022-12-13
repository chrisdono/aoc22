f = open('5.txt', 'r')
lines = f.readlines()

# brute force initialize a list with the data below
# instead of trying to parse the input for these lines
'''
                [M]     [V]     [L]
[G]             [V] [C] [G]     [D]
[J]             [Q] [W] [Z] [C] [J]
[W]         [W] [G] [V] [D] [G] [C]
[R]     [G] [N] [B] [D] [C] [M] [W]
[F] [M] [H] [C] [S] [T] [N] [N] [N]
[T] [W] [N] [R] [F] [R] [B] [J] [P]
[Z] [G] [J] [J] [W] [S] [H] [S] [G]
 1   2   3   4   5   6   7   8   9 

'''

stacks = [
            [],
            ['Z', 'T', 'F', 'R', 'W', 'J', 'G'],
            ['G', 'W', 'M'],
            ['J', 'N', 'H', 'G'],
            ['J', 'R', 'C', 'N', 'W'],
            ['W', 'F', 'S', 'B', 'G', 'Q', 'V', 'M'],
            ['S', 'R', 'T', 'D', 'V', 'W', 'C'],
            ['H', 'B', 'N', 'C', 'D', 'Z', 'G', 'V'],
            ['S', 'J', 'N', 'M', 'G', 'C'],
            ['G', 'P', 'N', 'W', 'C', 'J', 'D', 'L']]

# part 1
for line in lines[10:]:
    tokens = line.split()
    moves = int(tokens[1])
    start = int(tokens[3])
    end = int(tokens[5])
    # print(moves, start, end)
    for move in range(0,moves):
        if len(stacks[start]) > 0:
            stacks[end].append(stacks[start].pop())

p1_list = []
for stack in stacks:
    if len(stack) > 0:
        p1_list.append(stack.pop())

p1 = ''.join(p1_list)
print(p1)

# part 2
stacks = [
            [],
            ['Z', 'T', 'F', 'R', 'W', 'J', 'G'],
            ['G', 'W', 'M'],
            ['J', 'N', 'H', 'G'],
            ['J', 'R', 'C', 'N', 'W'],
            ['W', 'F', 'S', 'B', 'G', 'Q', 'V', 'M'],
            ['S', 'R', 'T', 'D', 'V', 'W', 'C'],
            ['H', 'B', 'N', 'C', 'D', 'Z', 'G', 'V'],
            ['S', 'J', 'N', 'M', 'G', 'C'],
            ['G', 'P', 'N', 'W', 'C', 'J', 'D', 'L']]

for line in lines[10:]:
    tokens = line.split()
    moves = int(tokens[1])
    start = int(tokens[3])
    end = int(tokens[5])
    print(moves, start, end)
    temp = []
    for move in range(0,moves):
        if len(stacks[start]) > 0:
            temp.append(stacks[start].pop())
    for x in range(len(temp)):
        stacks[end].append(temp.pop())
    # print(stacks)

p2_list = []
for stack in stacks:
    if len(stack) > 0:
        p2_list.append(stack.pop())

p2 = ''.join(p2_list)
print(p2)
