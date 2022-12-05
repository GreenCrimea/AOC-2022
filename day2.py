file1 = open('day2', 'r')
lines = file1.readlines()

score = 0
index = 0

for line in lines:
    x = line.split(' ')
    x[1] = x[1][:-1]
    
    if x[1] == 'X':             #rock
        score = score + 1
        if x[0] == 'C':         
            score = score + 6
        elif x[0] == 'A':
            score = score + 3
    elif x[1] == 'Y':           #paper
        score = score + 2
        if x[0] == 'A':
            score = score + 6
        elif x[0] == 'B':
            score = score + 3
    elif x[1] == 'Z':           #scissors
        score = score + 3
        if x[0] == 'B':
            score = score + 6
        elif x[0] == 'C':
            score = score + 3
    else:
        pass#print(f'1 = {x[0]}, 2 = {x[1]}, index = {index}')

    index = index + 1

score = 0
index = 0

for line in lines:
    x = line.split(' ')
    x[1] = x[1][:-1]

    if x[0] == 'A':
        if x[1] == 'X':
            score = score + 3
        elif x[1] == 'Y':
            score = score + 4
        elif x[1] == 'Z':
            score = score + 8
        else:
            print(index, line)

    elif x[0] == 'B':
        if x[1] == 'X':
            score = score + 1
        elif x[1] == 'Y':
            score = score + 5
        elif x[1] == 'Z':
            score = score + 9
        else:
            print(index, line)


    elif x[0] == 'C':
        if x[1] == 'X':
            score = score + 2
        elif x[1] == 'Y':
            score = score + 6
        elif x[1] == 'Z':
            score = score + 7
        else:
            print(index, line)
    index = index + 1


print(score)