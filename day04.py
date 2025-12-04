from pprint import pprint


# input = [
#     '..@@.@@@@.',
#     '@@@.@.@.@@',
#     '@@@@@.@.@@',
#     '@.@@@@..@.',
#     '@@.@@@@.@@',
#     '.@@@@@@@.@',
#     '.@.@.@.@@@',
#     '@.@@@.@@@@',
#     '.@@@@@@@@.',
#     '@.@.@@@.@.'
# ]


def main():
    with open('input/day04.txt') as f:
        input = f.readlines()

    input_clean = adjust_input(input)

    accessable = 0
    accessable_current_loop = 1000

    while accessable_current_loop != 0:
        # pprint(input_clean)
        # print(accessable_current_loop)
        accessable_current_loop = 0
        moved = []

        for i, row in enumerate(input_clean):
            for j, char in enumerate(row):
                if char == '@':
                    adjacent = 0
                    for up_down in range(-1, 2):
                        for left_right in range(-1, 2):
                            if up_down == 0 and left_right == 0:
                                continue
                            if input_clean[i+up_down][j+left_right] == '@':
                                adjacent +=1

                    if adjacent < 4:
                        accessable_current_loop += 1
                        moved.append((i,j))

        for moved_i, moved_j in moved:
            input_clean[moved_i][moved_j] = '.'

        accessable += accessable_current_loop

    print(accessable)            


def adjust_input(input):
    input_clean = []

    input_clean.append(['.']*(len(input[0])+2))

    for row in input:
        input_clean.append(['.'] + [char for char in row] + ['.'])

    input_clean.append(['.']*(len(input[0])+2))

    # print(input_clean)
    return(input_clean)


if __name__=="__main__":
    main()
