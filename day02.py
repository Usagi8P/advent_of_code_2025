# input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"


def main():
    with open('input/day02.txt') as f:
        input = f.readline()

    numbers = input.split(',')
    # print(numbers)

    collection = []

    factors_lookup = {}

    for number in numbers:
        a,b = number.split('-')

        for n in range(int(a), int(b)+1):
            n_str = str(n)
            n_len = len(n_str)

            if n_len not in factors_lookup:
                factors_lookup[n_len] = []
                for i in range(1,n_len):
                    if n_len%i == 0:
                        factors_lookup[n_len].append(i)

            for factor in factors_lookup[n_len]:
                slices = [n_str[i:i+factor] for i in range(0, n_len, factor)]

                if len(set(slices)) == 1:
                    # print(slices)
                    collection.append(n)
                    break

            # From Part 1 only split 50-50:
            #  if n_len%2 == 0:
            #     if n_str[:int(n_len/2)] == n_str[int(n_len/2):]:
            #         # print(n)
            #         collection.append(n)

    print(factors_lookup)
    print(sum(collection))


if __name__=="__main__":
    main()
