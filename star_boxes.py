# get width and height and print a square with asterisks

input_str = input("Enter width and height: ")
width, height = input_str.split(',')
width, height = int(width), int(height)
i = 1
v=1
while True:
    if i == 1 or i == height:
        print('*'*width)
        if i == height:
            break
    else:
        v = 1
        while True:
            if v == 1 or v == width:
                print('*', end='')
                if v == width:
                    break
            else:
                print(' ', end='')
            v += 1
        print()
    i += 1