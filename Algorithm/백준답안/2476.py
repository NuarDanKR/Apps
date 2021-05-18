import sys

# 자바의 경우는 아래처럼 max 함수를 구현해야함

# 버블 정렬로 숫자를 정렬하는 것
def bubble_sort(arr):
    length = len(arr)-1
    for i in range(length):
        for j in range(length):
            if arr[j] > arr[j+1]:
                arr[j+1],arr[j] = arr[j],arr[j+1]
    return arr

# 정렬된 숫자 맨 마지막을 max로 return
def max_num(arr):
    nums = bubble_sort(arr)
    max = nums[-1]
    return max

# 파이썬은 아래만 하면 됨

def prize(a,b,c): 
    if a==b==c:
        return a*1000+10000
    elif a==b!=c:
        return a*100 + 1000
    elif a==c!=b:
        return a*100 + 1000
    elif b==c!=a:
        return b*100 + 1000
    else:
        return max(a,b,c)*100 



n = int(sys.stdin.readline())
x=[]

for i in range(n):
    a,b,c = map(int, sys.stdin.readline().split())     
    
    x.append(prize(a,b,c)) 

print(max(x))

'''

print(prize([3,3,6]))
print(prize([2,2,2]))
print(prize([6,2,5]))
'''