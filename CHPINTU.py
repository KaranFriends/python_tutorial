t = int(input())
# type(t)
while t > 0:
    m, n=input().split()
    m=int(m)
    n=int(n)
    f = list(map(int, input().strip().split()))[:m]
    p = list(map(int, input().strip().split()))[:m]

    # use = dict(zip(test_keys, test_values))
    # print(p)
    ans={}

    for key in f:
        for value in p:
            if key in ans:
                ans[key] = ans[key]+value
            elif key <= n:
                ans[key]=value

            p.remove(value)
            break
    # print("******")
    # print(ans)
    # print("******")
    print(sorted(ans.items(), key=lambda kv: (kv[1], kv[0]))[0][1])
    t-=1