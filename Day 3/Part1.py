import re
# Initialize the array
overlap_count = 0


def create_matrix(x, y):
    matrix = [[0 for y in range(y)] for x in range(x)]

    # matrix = []
    # for n in range(0, x):
    #     row = []
    #     for n_2 in range(0, y):
    #         row.append(0)
    #     matrix.append(row)
    return matrix


def add_rectangle(x, y, width, height):
    global overlap_count
    for x_n in range(x, x + width + 1):
        for y_n in range(y, y + height + 1):
            current_square = fabric[x_n][y_n]
            if current_square == 0:
                fabric[x_n][y_n] = 1
            elif current_square == 1:
                overlap_count = overlap_count + 1
                fabric[x_n][y_n] = 2


fabric = create_matrix(1001, 1001)

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
        # 1 @ 935,649: 22x22

print(overlap_count)
