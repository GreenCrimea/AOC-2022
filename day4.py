file1 = open('day4', 'r')
lines = file1.readlines()

count = 0
count2 = 0

for line in lines:
    l = str(line).split(',')
    x = l[0].split('-')
    y = l[1].split('-')
    x[0] = int(x[0])
    x[1] = int(x[1])
    y[0] = int(y[0])
    y[1] = int(y[1][:-1])

    var1 = ""
    var2 = ""

    n = 0
    var1 = var1 + str(x[0])
    for i in range(x[0] + 1, x[1]):
        var1 = var1 + str(i) 

    var2 = var2 + str(y[0])
    for i in range(y[0] + 1, y[1]):
        var2 = var2 + str(i) 



    if var1 != var2:
        if var1 in var2:
            count = count + 1
            n = 1
        if var2 in var1 and n == 0:
            count = count + 1
    

    xr = range(x[0], x[1] + 1)
    yr = range(y[0], y[1] + 1)
    
    if set(xr).intersection(set(yr)):
        count2 = count2 + 1



    

    print(count2)

 