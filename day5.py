file1 = open('day5', 'r')
lines = file1.readlines()

a1 = ['W', 'D', 'G', 'B', 'H', 'R', 'V']
b2 = ['J', 'N', 'G', 'C', 'R', 'F']
c3 = ['L', 'S', 'F', 'H', 'D', 'N', 'J']
d4 = ['J', 'D', 'S', 'V']
e5 = ['S', 'H', 'D', 'R', 'Q', 'W', 'N', 'V']
f6 = ['P', 'G', 'H', 'C', 'M']
g7 = ['F', 'J', 'B', 'G', 'L', 'Z', 'H', 'C']
h8 = ['S', 'J', 'R']
i9 = ['L', 'G', 'S', 'R', 'B', 'N', 'V', 'M']

arr = [a1, b2, c3, d4, e5, f6, g7, h8, i9]

for line in lines:
    l = str(line)
    x = l.split(' ')
    x[5][:-1]
    am = int(x[1])
    f = int(x[3]) - 1
    t = int(x[5]) - 1

    var = []


    for i in range(am):
        var_n = arr[f].pop()
        var.append(var_n)
    
    
    var.reverse()
    for i in range(am):

        arr[t].append(var[i])
    

print(arr)
