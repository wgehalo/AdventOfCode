import re

def create_matrix(x, y):
   return [[0 for y in range(y)] for x in range(x)]

def add_rectangle(x, y, width, height, id):
    global overlap_count
    global no_overlap
    overlapped = False
    for x_n in range(x, x + width):
        for y_n in range(y, y + height):
            current_square = fabric[y_n][x_n]
            if current_square == 0:
                fabric[y_n][x_n] = 1
            elif current_square == 1:
                overlap_count = overlap_count + 1
                fabric[y_n][x_n] = 2
            elif current_square == 2:
                overlapped = True
    if not overlapped:
        no_overlap = id

overlap_count = 0
fabric = create_matrix(1000, 1000)
no_overlap = ''

with open('Day 3/input.txt') as f:
    line = f.readline()
    while line:
        parsed = re.search(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', line)
        id = parsed.group(1)
        x = int(parsed.group(2))
        y = int(parsed.group(3))
        width = int(parsed.group(4))
        height = int(parsed.group(5))
        add_rectangle(x, y, width, height, id)
        line = f.readline()

    print(f'Total overlapping square: {overlap_count}')
    f.seek(0)
    line = f.readline()
    while line:
        parsed = re.search(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', line)
        id = parsed.group(1)
        x = int(parsed.group(2))
        y = int(parsed.group(3))
        width = int(parsed.group(4))
        height = int(parsed.group(5))
        add_rectangle(x, y, width, height, id)
        line = f.readline()



print(f'This one did not overlap: {no_overlap}')