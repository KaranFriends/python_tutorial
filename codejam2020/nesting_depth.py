from sys import stdin, stdout

T = int(stdin.readline())
# print(T)
ii=0
aa = [0]*T
while ii < T:
    # N = int(stdin.readline())
    e = list(stdin.readline().rstrip())
    e=list(map(int,e))
    open=0
    ans = ""
    # stack=[]
    # print(e)
    for i in range(e[0]):
        ans = ans+"("
        # stack.append("(")
        open += 1
    ans = ans+str(e[0])
    pre = e[0]
    for i in range(1, len(e)):
        temp = e[i]
        # print(pre, temp,ans)
        if temp == 0:
            for i in range(pre):
                # stack.pop()
                open -= 1
                ans = ans+")"
            ans = ans + "0"
            pre = temp
        elif temp == pre:
            ans+=str(temp)
        elif temp > pre:
            for i in range(temp-pre):
                # stack.pop()
                ans = ans+"("
                open += 1
            # for i in range(temp):
            #     # stack.append("(")
            #     ans = ans+"("
            #     open += 1
            ans = ans+str(temp)
            pre = temp
        else:
            for i in range(pre-temp):
                # stack.pop()
                ans = ans+")"
                open -= 1
            ans = ans+str(temp)
            pre = temp
    for i in range(open):
        ans += ")"
    aa[ii] = "Case #%d: " % (ii+1) + ans
    ii += 1

for i in range(T):
    print(aa[i])