#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    answer = []
    if my_list:
        for i in my_list:
            if i % 2 == 0:
                answer.append(True)
            else:
                answer.append(False)
    return answer
