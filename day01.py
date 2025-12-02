# input = ['L68',
#          'L30',
#          'R48',
#          'L5',
#          'R60',
#          'L55',
#          'L1',
#          'L99',
#          'R14',
#          'L82',
#          'R1000',
#          'L1000']

def main():
    with open('input/day1.txt') as f:
        input = f.readlines()

    total_0 = 0
    
    number = 50

    for i in input:
        i = i.strip()

        move = int(i[1:]) % 100
        total_0 += int(i[1:]) // 100

        previous_number = number
        if i[0] == 'L':
            number = number - move
        if i[0] == 'R':
            number = number + move
            
        if previous_number < 100 and number > 100:
            total_0 += 1
        if previous_number > 0 and number < 0:
            total_0 += 1

        if number < 0:
            number = 100 + number
        if number > 100:
            number = number - 100
        if number == 100:
            number = number - 100

        if number == 0:
            total_0 += 1

        # print(i, " ", move, " ", number)
        # print(total_0)

    print(total_0)


if __name__=="__main__":
    main()
