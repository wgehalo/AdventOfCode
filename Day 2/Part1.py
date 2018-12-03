with open('input.txt') as f:
    threes = 0
    twos = 0
    line = f.readline()
    while line:
        foundThree = False
        foundTwo = False
        for c in line:
            if foundThree and foundTwo:
                break

            cnt = line.count(c)
            if cnt == 2:
                foundTwo = True
                continue
            if cnt == 3:
                foundThree = True
                continue

        if foundTwo:
            twos = twos + 1
        if foundThree:
            threes = threes + 1
        line = f.readline()

    checksum = twos * threes
    print(checksum)
