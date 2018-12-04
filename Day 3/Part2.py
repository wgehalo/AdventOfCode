import re
import timeit

start = timeit.default_timer()

all_claims = set()
overlapped_claims = set()
overlap_count = 0


def create_matrix(x, y):
    return [[[0, 0] for y in range(y)] for x in range(x)]


def add_rectangle(x, y, width, height, id):
    global overlap_count
    all_claims.add(id)
    for x_n in range(x, x + width):
        for y_n in range(y, y + height):
            current_square = fabric[y_n][x_n]
            if current_square[0] == 0:
                fabric[y_n][x_n] = [1, id]
            elif current_square[0] == 1:
                overlap_count = overlap_count + 1
                overlapped_claims.add(id)
                overlapped_claims.add(current_square[1])
                fabric[y_n][x_n] = [2, id]
            else:
                overlapped_claims.add(id)


with open('Day 3/input.txt') as f:
    fabric = create_matrix(1000, 1000)
    lines = f.readlines()
    for line in lines:
        parsed = re.search(r'^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$', line)
        id = parsed.group(1)
        x = int(parsed.group(2))
        y = int(parsed.group(3))
        width = int(parsed.group(4))
        height = int(parsed.group(5))
        add_rectangle(x, y, width, height, id)

    print(f'Total overlapping square: {overlap_count}')
    print(f'This one did not overlap: {all_claims - overlapped_claims}')

stop = timeit.default_timer()
total_time = stop - start

print(f'Total Time: {total_time}')
