def sumOfDigits(x):
    op = []
    for i in x:
        i = str(i)
        r = 0
        for j in i:
            r = r+int(j)
        op.append(r)
    return op

def sumOfDigits2(x):
    op = []
    for i in x:
        res=0
        while i>0:
            res = res+(i%10)
            i = i//10
        op.append(res)
    return op

if __name__ == "__main__":
    x = [i for i in range(1000000)]

    print(sumOfDigits(x))