import sys

A, B = map(str, sys.stdin.readline().split())

if int(A[-1]) > int(B[-1]):
    print(A[-1] + A[1] + A[0])
elif int(A[-1]) < int(B[-1]):
    print(B[-1] + B[1] + B[0])
else:
    if int(A[1]) > int(B[1]):
        print(A[-1] + A[1] + A[0])
    elif int(A[1]) < int(B[1]):
        print(B[-1] + B[1] + B[0])
    else:
        if int(A[0]) > int(B[0]):
            print(A[-1] + A[1] + A[0])
        else:
            print(B[-1] + B[1] + B[0])