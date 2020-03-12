def main():
    from sys import stdin, stdout
    # n, k = stdin.readline().split()
    # n = int(n)
    # k = int(k)
    #
    # cnt = 0
    # lines = stdin.readlines()
    # for line in lines:
    #     if int(line) % k == 0:
    #         cnt += 1
    #
    # stdout.write(str(cnt))


    def countOne(n):
        ones = 0
        # print(n)
        while n:
            n &= (n - 1)
            ones += 1
        # print(ones)
        return ones


    t = int(stdin.readline())

    while t > 0:
        m, n = stdin.readline().split()
        # m=int(m)
        n=int(n)
        f = [int(m) for m in stdin.readline().split()]
        # f = list(map(int, input().strip().split()))[:m]
        while n > 0:
            odd = 0
            even = 0
            p = int(input())
            for i in f:
                if countOne(i^p) % 2 == 0 :
                    even += 1
                else:
                    odd+=1
            stdout.write(even.__str__()+" "+odd.__str__())
            n-=1
        t-=1

if __name__ == "__main__":
    main()

