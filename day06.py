input = [
    '123 328  51 64 ',
    ' 45 64  387 23 ',
    '  6 98  215 314',
    '*   +   *   +  ',
]


def main():
    with open('input/day06.txt') as f:
        input = f.readlines()

    clean_input = []

    prev_i = 0
    for i, sign in enumerate(input[-1]):
        if i !=0 and (sign == '*' or sign == '+'):
            problem = []
            for row in input:
                problem.append(row[prev_i:i-1])
            clean_input.append(problem)
            prev_i=i

    problem = []
    for row in input:
        problem.append(row[prev_i:-1])

    clean_input.append(problem)

    # print(clean_input)

    problems = []
    for problem in clean_input:
        clean_problem = []
        # print(problem)
        for i in range(len(problem[0])):
            text = ''
            for chars in problem[:-1]:
                text += chars[-i-1]
            clean_problem.append(text.strip())
        clean_problem.append(problem[-1].strip())

        problems.append(clean_problem)

    # print(problems)
        # for text in problem[:-1]:
        #     for char in text[::-1]:
        #         print(char)

    # problems = []
    # for i in range(len(clean_input[0])):
    #     problem_collection = []
    #     for j in range(len(clean_input)):
    #         problem_collection.append(clean_input[j][i])
    #     problems.append(problem_collection)

    # # print(problems)

    total = 0

    for problem in problems:
        # print(problem)
        # print(problem[-1])
        # print(problem[:-1])
        if problem[-1] == '+':
            problem_total = 0
            for number in problem[:-1]:
                problem_total += int(number)
        if problem[-1] == '*':
            problem_total = 1
            for number in problem[:-1]:
                problem_total *= int(number)

        # print(problem_total)
        total += problem_total

    print(total)


if __name__=="__main__":
    main()