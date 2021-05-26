import sys

n = int(sys.stdin.readline())

for i in range(n):
    OX = sys.stdin.readline()
    score = 0
    n = 0
    for k in OX:
        if k == "O":
            n += 1
            score += n
        else:
            n = 0
    print(score)



    # data = list(map(str, sys.stdin.readline().split("X")))
    # a = data[-1].split("\n")
    # data[-1] = a[0]
    # print(data)
    # for k in range(len(data)):
    #     pop(" ")
    # print(data)