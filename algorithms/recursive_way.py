def recursive(n):
    if n <= 1:
        return 1
    else:
        temp = recursive(n - 1)
        return temp * n


def permute(string, pocket=""):
    if len(string) == 0:
        print(pocket)
    else:
        for i in range(len(string)):
            letter = string[i]
            front = string[0:i]
            back = string[i + 1:]
            together = front + back
            permute(together, letter + pocket)
