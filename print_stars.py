a = int(input("Input number? "))
# a = 1
# b = 1
# while True:
#     if a > i:
#         break
#     b = 1
#     while True:
#         if b > i:
#             break
#         print('*', end='')
#         b += 1
#     print('')
#     a += 1


# # for i in range(a):
# #     for v in range(a):
# #         print('*', end='')]

# # # for i in range(a):
# # #     for v in range(a):
# # #         if i == 0 or i == a-1:
# # #             print('*', end='')
# # #         elif v == 0 or v == a-1:
# # #             print('*', end='')
# # #         else:
# # #             print(' ', end='')
# # #     print('')

c = ' '
d = '*'
for i in range(a,0, -1):
    for v in range(a-i):
        print(' ', end='')
    for _ in range(i):
        print('*', end='')
    print('')