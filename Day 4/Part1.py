import datetime
import re

# Read file line by line
# Parse date, action, guard ID
# Sort by date, ascending
# Place holder for highest amount of sleeping.
# Don't worry about =, just use greatest, because only 1 will have the most and by the end of it
# We should have that value. Store total minutes + guard ID.
# Each Guard should have it's own list of 0 -59 with the number of times that minute was slept on.
#


def parse_input(file):
    with open(file) as f:
        parsed_input = []
        line = f.readline()

        while line:
            parsed = re.search(
                r'^\[(\d+)-(\d+)-(\d+)\s(\d\d):(\d\d)\]\s(Guard|wakes|falls)\s#?(\d+)?', line)

            year = int(parsed.group(1))
            month = int(parsed.group(2))
            day = int(parsed.group(3))
            hour = int(parsed.group(4))
            minute = int(parsed.group(5))
            action = parsed.group(6)
            guard_id = parsed.group(7)
            dt = datetime.datetime(year, month, day, hour, minute)

            parsed_input.append(
                {"guard_id": guard_id, "action": action, "dt": dt})
            line = f.readline()
    return parsed_input


parsed_list = parse_input('Day 4/input.txt')
sorted_list = sorted(parsed_list, key=lambda guard: guard['dt'])

most_minutes = {"guard_id": 0, "minutes": 0}
current_sleep_total = 0
fell_asleep_at = 0
current_guard_id = 0
guard_data = {}


# TODO - Fix this so we have total sleep time per guard, pretty sure this is causing the failure.
for row in sorted_list:
    if row['action'] == "Guard":
        current_sleep_total = 0
        current_guard_id = row['guard_id']
        guard_data[current_guard_id] = [0 for x in range(60)]
        current_guard = guard_data[current_guard_id]
    elif row['action'] == 'falls':
        fell_asleep_at = row['dt'].minute
    elif row['action'] == 'wakes':
        time_slept = row['dt'].minute - fell_asleep_at
        current_sleep_total = current_sleep_total + time_slept
        if current_sleep_total > most_minutes['minutes']:
            most_minutes['minutes'] = current_sleep_total
            most_minutes['guard_id'] = current_guard_id
        for x in range(fell_asleep_at, time_slept):
            current_guard[x] = current_guard[x] + 1

print(
    f'Guard  #{most_minutes["guard_id"]} slept the most: {most_minutes["minutes"]}')

sleepiest_guard = guard_data[most_minutes['guard_id']]
mode = sorted(sleepiest_guard)[59]

print(mode)

# with open('Day 4/input.txt') as f:
#     line = f.readline()
#     while line:
#         parsed = re.search
#         x = int(parsed.group(1))
#         y = int(parsed.group(2))
#         width = int(parsed.group(3))
#         height = int(parsed.group(4))
#         add_rectangle(x, y, width, height)
#         line = f.readline()

# print(overlap_count)
