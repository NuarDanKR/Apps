import sys

n = int(sys.stdin.readline())
score = list(map(int, sys.stdin.readline().split()))

m = max(score)
# m = 0
# for i in range(n):
#     if score[i] > m:
#         m = score[i]


for i in range(n):
    score[i] = (score[i]/m)*100

s = 0
for i in range(n):
    s += score[i]

print(s/n)
