def getAvg(*args):
    for i in args:
        print(i)
    return sum(args)/len(args)

print(getAvg(1,2,3,4,5,6,7,8,9,10)) 