input = [
    '3-5',
    '10-14',
    '16-20',
    '12-18',
    '3-4',
    '\n',
    '1',
    '5',
    '8',
    '11',
    '17',
    '32'
]


def main():
    with open('input/day05.txt') as f:
        input = f.readlines()

    split_index = input.index('\n')

    fresh_ranges = [[int(i.split('-')[0]),int(i.split('-')[1])] for i in input[:split_index]]
    ingredients = [int(i) for i in input[split_index+1:]]

    count_fresh = 0

    for ingredient in ingredients:
        for range in fresh_ranges:
            if ingredient >= range[0] and ingredient <= range[1]:
                # print(ingredient)
                count_fresh += 1
                break

    print(count_fresh)


def count_possible_fresh():
    with open('input/day05.txt') as f:
        input = f.readlines()

    split_index = input.index('\n')

    fresh_ranges = [[int(i.split('-')[0]),int(i.split('-')[1])] for i in input[:split_index]]

    fresh_ranges = sorted(fresh_ranges, key=lambda x: x[0])

    merged = []

    for fresh_range in fresh_ranges:
        if not merged:
            merged.append(fresh_range)
            continue
        if fresh_range[0] <= merged[-1][-1]:
            merged[-1] += fresh_range
        else: 
            merged.append(fresh_range)
        merged[-1] = sorted(merged[-1])

    # print(merged)

    count_possible_fresh = 0

    for element in merged:
        # print(element)
        diff = element[-1] - element[0]
        count_possible_fresh += diff + 1
        # print(diff)

    print(count_possible_fresh)


if __name__=="__main__":
    count_possible_fresh()