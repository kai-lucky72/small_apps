from math import factorial


def iterate(n):
    fact = 1

    for i in range(2, n + 1):
        fact *= i
    return fact


def permutations(str):
    for p in range(factorial(len(str))):
        print(''.join(str))
        i = len(str) - 1
        while i > 0 and str[i - 1] > str[i]:
            i -= 1
        str[i:] = reversed(str[i:])

        if i > 0:
            q = i

            while str[i - 1] > str[q]:
                q += 1
            temp = str[i - 1]
            str[i - 1] = str[q]
            str[q] = temp


s = 'abc'
s = list(s)
permutations(s)
