n, k = map(int, input().split())

N = [0] * (n+1)
for i in range(1,n+1):
    N[i] = int(input())
print(N)

d = [[0] * (k + 1)] * (n + 1)
print(d)
for i in range(1,n):
    # print(d[i - 1][0] + N[i])
    d[i][0] = max(d[i - 1][0] + N[i], 0)
    print(d[i][0])
    for j in range(1,k):
        d[i][j] = max(d[i - 1][j] + N[i], d[i - 1][j - 1])

    print(print(d[i][0], d[i][1], d[i][2]))

# print(d)
ans = 0
for i in range(k + 1):
    ans = max(d[n][i], ans)

for i in range(n):
    print(d[i][0], d[i][1], d[i][2],"\n")
print(ans)
