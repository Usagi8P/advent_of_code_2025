# input = [
#     '987654321111111',
#     '811111111111119',
#     '234234234234278',
#     '818181911112111'
#     ]


def main():
    with open('input/day03.txt') as f:
        input = f.readlines()

    best_joltages = []

    for battery in input:
        battery = battery.strip()
        highest_jolt = []
        jolt_index = 0

        battery_size = 12

        for i in range(battery_size):
            ending_index = battery_size-i
            res, jolt_index = text_looper(battery, jolt_index, ending_index)
            highest_jolt.append(res)
            jolt_index += 1

        # for i, jolt in enumerate(battery[:-1]):
        #     if int(jolt) > highest_jolt_10s:
        #         highest_jolt_10s = int(jolt)
        #         jolt_index = i
        #     if highest_jolt_10s == 9:
        #         break

        # for jolt in battery[jolt_index+1:]:
        #     if int(jolt) > highest_jolt_1s:
        #         highest_jolt_1s = int(jolt)
        #     if highest_jolt_1s == 9:
        #         break

        best_joltages.append(calculate_joltage(highest_jolt))

    # print(best_joltages)
    print(sum(best_joltages))


def text_looper(battery, starting_index, ending_index) -> tuple[int, int]:
    highest_jolt = 0
    jolt_index = 0
    ending_index = len(battery)-ending_index+1

    for i, jolt in enumerate(battery[starting_index:ending_index]):
        if int(jolt) > highest_jolt:
            highest_jolt = int(jolt)
            jolt_index = i
        if highest_jolt == 9:
            break

    # print(battery)
    # print(ending_index)
    # print(battery[starting_index:ending_index])
    # print(highest_jolt)
    # print(jolt_index)

    return highest_jolt, jolt_index+starting_index


def calculate_joltage(highest_jolt):
    joltage = 0

    for i, jolt in enumerate(highest_jolt):
        position = len(highest_jolt) - (i+1)
        joltage += jolt * 10**position

    return joltage


if __name__=="__main__":
    main()