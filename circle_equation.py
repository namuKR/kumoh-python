# numbers : list = []
# for i in range(4):
#     numbers.append(int(input()))

# print((numbers[0]-numbers[2])**2 + (numbers[1]-numbers[3])**2)

# r = int(input("Enter radius: "))

# # while True:
# for i in range(r*2+1): # x axis
#     for j in range(r*2+1): # y axis
#         if (i-r)**2 + (j-r)**2 <= r**2:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()


# x1.y1 과 x2.y2 거리의 제곱 = (x1-x2)**2 + (y1-y2)**2

input_str = input("Enter x,y and difference")

x = int(input_str.split(",")[0])
y = int(input_str.split(",")[1])
diff = int(input_str.split(",")[2])

x1 = x-diff
y1 = y-diff
x2 = x+diff
y2 = y+diff
x3 = x-diff
y3 = y+diff
x4 = x+diff
y4 = y-diff

for i in range(int(x1), int(x2)+1):
    for j in range(int(y1), int(y2)+1):
        print("*", end="")
    print()