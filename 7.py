from collections import defaultdict
f = open("7.txt", "r")
lines = f.readlines()

'''
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k

- / (dir)
  - a (dir)
    - e (dir)
      - i (file, size=584)
    - f (file, size=29116)
    - g (file, size=2557)
    - h.lst (file, size=62596)
  - b.txt (file, size=14848514)
  - c.dat (file, size=8504156)
  - d (dir)
    - j (file, size=4060174)
    - d.log (file, size=8033020)
    - d.ext (file, size=5626152)
    - k (file, size=7214296)
'''

dirs = defaultdict(int)

# present directory
pd = []
for line in lines:
    tokens = line.strip().split()
    if tokens[1] == "cd":
        if tokens[2] == "..":
            pd.pop()
        else:
            pd.append(tokens[2])

    elif tokens[1] == "ls":
        continue

    elif tokens[0] == "dir":
        continue

    else:
        for i in range(1, len(pd)+1):
            dirs['/'.join(pd[:i])] += int(tokens[0])

p1 = 0
for key, val in dirs.items():
    if val <= 100000:
        p1 += val

print(p1)

free_space = 70000000 - dirs["/"]
target = 30000000 - free_space
p2 = 70000000

for key, val in dirs.items():
    if val >= target and val < p2:
        p2 = val

print(p2)
