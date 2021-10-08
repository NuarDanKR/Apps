import sys

K = int(sys.stdin.readline())
data = []
for i in range(K):
    data.append(int(sys.stdin.readline()))
    if data[-1] == 0:
        data.pop()
        data.pop()
    # n = int(sys.stdin.readline())
    # if n == 0:
    #     data.pop()
    # else:
    #     data.append(n)

sum = 0
for i in data:
    sum += i
print(sum)
