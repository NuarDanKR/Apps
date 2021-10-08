import sys

N, K = map(int, sys.stdin.readline().split())
lst = list(range(1, N+1))
ans = []

for i in range(N):
    if K == 1:
        ans.append(lst[i])
    else:
        if len(lst) >= K:
            ans.append(lst.pop(K-1))
            for j in range(K-1):
                lst.append(lst.pop(0))
        elif len(lst) > 2:
            ans.append(lst.pop(K-(len(lst)+1)))
            for j in range(K-(len(lst)+1)-1):
                lst.append(lst.pop(0))
        else:
            if K % 2 == 1:
                ans.append(lst.pop(0))
            else:
                ans.append(lst.pop(-1))

answer = str(ans)

print("<", end="")
print(answer[1:-1], end="")
print(">")
