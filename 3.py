f = open('3.txt', 'r')
lines = f.readlines()
alpha = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

p1 = 0
for line in lines:
    # print(int(len(line.strip())/2))
    sub1 = line[:(int(len(line.strip())/2))]
    sub2 = line[(int(len(line.strip())/2)):]
    sub1_ind = []
    for char in sub1:
        sub1_ind.append(alpha.index(char))
    char_found = ''
    for char in sub2:
        if char in sub1:
            char_found = char
    # print(alpha.index(char_found))
    p1 += alpha.index(char_found)

print(p1)

p2 = 0
ln = 1
char_found = ''
line1 = ''
line2 = ''
line3 = ''

for line in lines:
    if ln == 1:
        line1 = line.strip()
        ln += 1
    elif ln == 2:
        line2 = line.strip()
        ln += 1
    else:
        line3 = line.strip()
        ln = 1
        for char in line1:
            if char in line2:
                if char in line3:
                    char_found = char
        p2 += alpha.index(char_found)

print(p2)

