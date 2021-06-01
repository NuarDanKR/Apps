import sys

N = int(sys.stdin.readline())

count = 0

for i in range(1000, -1, -1):
    for k in range(5):
        if i*5 + k*3 == N:
            count = i + k


if count == 0:
    print(-1)
else:
    print(count)