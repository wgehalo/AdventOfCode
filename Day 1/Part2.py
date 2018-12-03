def find_repeat(input):
    sum = 0
    previous_sums = {}
    with open(input) as f:
        line = f.readline()
        while line:
            sum = sum + int(line)
            if sum in previous_sums:
                return sum
            previous_sums[sum] = 1
            line = f.readline()
            if not line:
                f.seek(0)
                line = f.readline()


print(find_repeat('Day 1/input.txt'))
