for i in range(10):
    for v in range(10):
        if (i*10+v) % 4 == 0 or (i+v) % 3 == 0:
            print(" *", end=' ')
        else:
            print("%2d" % (i*10 + v), end= ' ')
    print('')

# for i in range(100):
#     print("{:2} ".format(i), end='')
#     if (i+1) % 10 == 0:
#         print("")