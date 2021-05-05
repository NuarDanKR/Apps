import random


random.seed(0)
rand_list = []
for i in range(6):
    rand_list.append(random.randint(0, 9))
temp_list = []

for i in range(6):
    for j in range(6):
        for k in range(6):
            for x in range(6):
                for y in range(6):
                    for z in range(6):
                        if i != j and i != k and i != x and i != y and i != z and j != k and j != x and j != y and j != z and k != x and k != y and k != z and x != y and x != z and y != z:
                            temp_list.append(list(
                                [rand_list[i], rand_list[j], rand_list[k], rand_list[x], rand_list[y], rand_list[z]]))


def exhaustive_search(random_list):
    for i in random_list:
        front = i[:3]
        back = i[3:]
        f_bool = False
        b_bool = False
        if ((front[0] + 1) == front[1] and (front[2] - 1) == front[1]) or (front[0] == front[1] and front[1] == front[2]):
            f_bool = True
        if ((back[0] + 1) == back[1] and (back[2] - 1) == back[1]) or (back[0] == back[1] and back[1] == back[2]):
            b_bool = True
        if f_bool and b_bool:
            print("베이비 진입니다.")
            return None
    print("베이비진이 아닙니다.")


exhaustive_search(temp_list)
print(rand_list)
