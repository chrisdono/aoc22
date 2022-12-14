f = open('6.txt', 'r')
lines = f.readlines()

def find_index(qlen):
    char_queue = []
    index = 1
    result = 0
    for c in lines[0]:
        char_queue.append(c)
        unique = True
        if len(char_queue) > qlen:
            char_queue.pop(0)
            for i in range(qlen):
                for j in range(i + 1, qlen):
                    if(char_queue[i] == char_queue[j]):
                        unique = False
            if unique:
                result = index
                break
            else:
                index += 1
        else:
            index += 1
    return result

# part 1
print(find_index(4))
# part 2
print(find_index(14))
