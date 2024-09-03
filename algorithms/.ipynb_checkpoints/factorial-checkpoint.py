def rec_factorial(num):
    if num == 1:
        return 1
    else:
        temp=rec_factorial(num-1)
        return temp*num

num=5
print(rec_factorial(num))
