import sys
T = int(input())
for i in range(T):
    vps = stdin.readline()
    vps_arr = []
    for i in vps:
        if i == "(":
            vps_arr.append(-1)
        elif i == ")":
            vps_arr.append(1)
    total = 0
    for i in vps_arr:
        total += i
        if total > 0:
            break
    if total == 0:
        print("YES")
    else:
        print("NO")
