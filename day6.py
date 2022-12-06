file1 = open('day6', 'r')
lines = file1.readlines()
n = 0



for line in lines:

    for i in range(14, len(line)):
        x = [str(line[i]), str(line[i-1]), str(line[i-2]), str(line[i-3]), str(line[i-4]), str(line[i-5]), str(line[i-6]), str(line[i-7]), str(line[i-8]), str(line[i-9]), str(line[i-10]), str(line[i-11]), str(line[i-12]), str(line[i-13])]
        s = set(x)
        if len(s) == len(x) and n == 0:
            print(i)
            print(s, x)
            n = 1

