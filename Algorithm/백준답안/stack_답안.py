def command(*args):
    if len(args) == 2 :
        return stack.append(args[1])

    else :
        if args[0]=="pop":
            if len(stack) == 0 :
                print(-1)
            else :
                print(stack[-1])
                return stack.pop()

        if args[0]=="top":
            if len(stack) == 0 :
                print(-1)
                
            else :
                print(stack[-1])
                

        elif args[0]=="size":
            print(len(stack))
        
        elif args[0]=="empty":
            if len(stack) == 0 :
                print(1)
            else :
                print(0)



###main###
stack=[]


# 입력단
n = int(input())
lines = ""
for i in range(n):
    lines+=input()+"\n"


# 출력단
words = lines.split('\n')


for i in range(n):
    word = words[i].split()
    command(*word)

