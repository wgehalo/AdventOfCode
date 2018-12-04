import re

def create_matrix(x, y):
   return [[0 for y in range(y)] for x in range(x)]

def add_rectangle(x, y, width, height):
    global overlap_count
    for x_n in range(x, x + width):
        for y_n in range(y, y + height):
            current_square = fabric[y_n][x_n]
            if current_square == 0:
                fabric[y_n][x_n] = 1
            elif current_square == 1:
                overlap_count = overlap_count + 1
                fabric[y_n][x_n] = 2

overlap_count = 0
fabric = create_matrix(1000, 1000)

with open('Day 3/input.txt') as f:
    line = f.readline()
    while line:
        parsed = re.search(r'#\d+ @ (\d+),(\d+): (\d+)x(\d+)', line)
        x = int(parsed.group(1))
        y = int(parsed.group(2))
        width = int(parsed.group(3))
        height = int(parsed.group(4))
        add_rectangle(x, y, width, height)
        line = f.readline()

print(overlap_count)