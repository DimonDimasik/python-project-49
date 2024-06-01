from random import randint


min_num = 2
max_num = 100
amount_ques = 3


def prime_ques_gen(min, max, amount):
    i = 1
    num_list = []
    while i <= amount:
        num_list.append(randint(min, max))
        i += 1

    i = 0
    ques_list = []
    while i < amount:
        if num_list[i] == 2 or num_list[i] == 3:
            question = num_list[i]
            answer = 'yes'

        else:
            half = num_list[i] // 2
            question = num_list[i]

            for item in range(half, min - 1, -1):
                if num_list[i] % item == 0:
                    answer = 'no'
                    break

                else:
                    answer = 'yes'

        ques_list.append(question)
        ques_list.append(answer)
        i += 1

    return ques_list
