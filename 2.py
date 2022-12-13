f = open('2.txt', 'r')
lines = f.readlines()

sum = 0
prs_opp = ['A', 'B', 'C'] # rock, paper, scissors
prs_self = ['X', 'Y', 'Z'] # rock, paper, scissors
# 0 vs 0 --> 3  (0)
# 0 vs 1 --> 0  (-1)
# 0 vs 2 --> 6  (-2)
# 1 vs 0 --> 6  (1)
# 1 vs 1 --> 3  (0)
# 1 vs 2 --> 0  (-1)
# 2 vs 0 --> 0  (2)
# 2 vs 1 --> 6  (1)
# 2 vs 2 --> 3  (0)
score = {0: 3, -1: 0, -2:6, 1:6, 2:0}

# Part 1
for line in lines:
    matchup_key = prs_self.index(line[2]) - prs_opp.index(line[0])
    sum += prs_self.index(line[2]) + 1 + score[matchup_key]

print(sum)

prs_res = ['X', 'Y', 'Z'] # lose, draw, win

# Part 2
sum = 0
for line in lines:
    if line[2] == 'X':
        score2 = 0
        self_key = (prs_opp.index(line[0]) - 1) % 3
    elif line[2] == 'Y':
        score2 = 3
        self_key = prs_opp.index(line[0])
    else:
        score2 = 6
        self_key = (prs_opp.index(line[0]) + 1) % 3
    # print(sum)
    sum += self_key + 1 + score2

print(sum)
