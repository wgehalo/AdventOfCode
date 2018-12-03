with open('input.txt') as f:
    sum = 0
    line = f.readline()
    while line:
        sum = sum + int(line)
        line = f.readline()

print(sum)
