file1 = open('day7', 'r')

d = [lines.strip().split(" ") for lines in file1.readlines()]

fs = {}
max = []
current = fs

for x in d:
    if x[0] == '$':
        if x[1] == 'cd':
            if x[2] == '/':
                current = fs
                upper = []
            elif x[2] == '..':
                current = upper.pop()
            else:
                upper.append(current)
                current = current[x[2]]
        else:
            continue
    else:
        if x[0] == 'dir':
            dir = {}
            current[x[1]] = dir
        else:
            current[x[1]] = int(x[0])



def size(d, name, dirsize):
    if type(d) == int:
        return d
    s = 0
    for o in d:
        s = s + size(d[o],o,dirsize)
    if dirsize != None:
        dirsize.append((name, s))
    return s

dirsize = []
n = size(fs, '/', dirsize)


print(sum([s for n,s in dirsize if s < 100000]))

def pt2(fs):
    dirsize = []
    t = size(fs, "/", dirsize)  
    space = 70000000
    needed = 30000000
    for n,s in sorted(dirsize, key=lambda x: x[1]):
        if space - t + s > needed:
            return s

print(pt2(fs))
        
