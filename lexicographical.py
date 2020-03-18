def prevPermutation(str):

    n = len(str) - 1
    i = n

    while (i > 0 and str[i - 1] <= str[i]):
        i -= 1

    if (i <= 0):
        return False

    j = i - 1
    while (j + 1 <= n and
           str[j + 1] <= str[i - 1]):
        j += 1

    str = list(str)
    temp = str[i - 1]
    str[i - 1] = str[j]
    str[j] = temp
    str = ''.join(str)

    str[::-1]

    return True, str

if __name__ == '__main__':
    str = "fjadchbegi"

    b, str = prevPermutation(str)

    if (b == True):
        print("Previous permutation is", str)
    else:
        print("Previous permutation doesn't exist")
