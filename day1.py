file1 = open('day1', 'r')
lines = file1.readlines()

one = 0
two = 0
three = 0
var = 0

for line in lines:

    if line != '\n':
        var = var + int(line)

    if line == '\n':

        if var > one:
            three = two
            two = one
            one = var
        elif var > two:
            three = two
            two = var
        elif var > three:
            three = var
            
        var = 0

print(one + two + three)