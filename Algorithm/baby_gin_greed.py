import random

random.seed()
rand_list = []
for i in range(6):
    rand_list.append(random.randint(0, 9))


def greed_search(random_list):
    temp_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    dict_bool = [False, False]
    count = 0
    for i in random_list:
        temp_dict[i] += 1
    for i in range(10):
        if temp_dict[i] >= 3:
            temp_dict[i] -= 3
            dict_bool[count] = True
            count += 1
    for i in range(7):
        if temp_dict[i] >= 1 and temp_dict[i + 1] >= 1 and temp_dict[i + 2] >= 1:
            temp_dict[i] -= 1
            temp_dict[i + 1] -= 1
            temp_dict[i + 2] -= 1
            dict_bool[count] = True
            count += 1
    if dict_bool[0] and dict_bool[1]:
        print("베이비진입니다.")
    else:
        print("베이비진이 아닙니다.")


greed_search(rand_list)
print(rand_list)
