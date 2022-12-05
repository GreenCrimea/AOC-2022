file1 = open('day3', 'r')
lines = file1.readlines()

import math

index = 1
index2 = 0
a = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11, 
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17, 
    'r': 18, 
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26,
    'A': 27,
    'B': 28,
    'C': 29,
    'D': 30,
    'E': 31,
    'F': 32,
    'G': 33,
    'H': 34,
    'I': 35,
    'J': 36,
    'K': 37,
    'L': 38,
    'M': 39,
    'N': 40,
    'O': 41,
    'P': 42,
    'Q': 43,
    'R': 44,
    'S': 45,
    'T': 46,
    'U': 47,
    'V': 48,
    'W': 49,
    'X': 50,
    'Y': 51,
    'Z': 52,
    }

answer = 0

for line in lines:
    l = line[:-1]
    z = len(l)//2
    x, y = l[:z], l[z:]
    loop = 0
    for i in range(z):
        for j in range(z):
            if x[i] == y[j] and loop == 0:
                answer = answer + a[x[i]]
                loop = 1

answer = 0
x = ''
y = ''
z = ''

for line in lines:
    l = line[:-1]
    loop = 0
    if index % 3 == 2:
        x = x + str(l)
    if index % 3 == 1:
        y = y + str(l)
    if index % 3 == 0:
        z = z + str(l)
        for i in range(len(x)):
            for j in range(len(y)):
                if x[i] == y[j]:
                    for k in range(len(z)):
                        if x[i] == z[k] and y[j] == z[k] and loop == 0:
                            answer = answer + a[x[i]]
                            loop = 1
                            print(f'{x[i]}, {y[j]}, {z[k]}, {i}, {j}, {k}')

                
        index = 1
        x = ''
        y = ''
        z = ''
    else:
        index = index + 1
    
    index2 = index2 + 1
                
                


print(answer)
