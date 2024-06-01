from random import randint


max_num = 100
min_num = 1
amount_ques = 3


def gcd_ques_gen(max, min, amount):
    num_list = []
    i = 1
    while i <= amount * 2:
        num_list.append(randint(min, max))
        i += 1

    ques_list = []
    i = 0

    while i <= amount * 2 - 2:
        question = f'{num_list[i]} {num_list[i + 1]}'

        if num_list[i] == num_list[i + 1]:
            answer = num_list[i]

        elif num_list[i] > num_list[i + 1]:
            for item in range(num_list[i], 0, -1):
                if num_list[i] % item == 0 and num_list[i + 1] % item == 0:
                    answer = item
                    break

        elif num_list[i] < num_list[i + 1]:
            for item in range(num_list[i + 1], 0, -1):
                if num_list[i] % item == 0 and num_list[i + 1] % item == 0:
                    answer = item
                    break

        ques_list.append(question)
        ques_list.append(str(answer))
        i += 2

    return ques_list
