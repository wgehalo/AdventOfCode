def get_oneOff(input):
    with open(input) as f:
        text = f.readlines()
        end = len(text)
        for i in range(0, end):
            for x in range(i+1, end):
                line_one = text[i].replace('\n', '')
                line_two = text[x].replace('\n', '')
                mismatched = 0
                result_string = ''
                for z in range(0, len(line_one)):
                    if line_one[z] != line_two[z]:
                        mismatched = mismatched + 1
                        result_string = line_one[:z] + line_one[z+1:]
                if mismatched == 1:
                    return(result_string)


print(get_oneOff('Day 2/input.txt'))
