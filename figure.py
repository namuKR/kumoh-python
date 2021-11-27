shape = input("Input shape type (R, T, C) ? ")

if shape == "C":
    radius = int(input("Input radius ? "))
    
    print(f"Area of Circle (radius = {radius}deg) is {3.14*radius*radius}")
elif shape == "R":
    width = int(input("Input width ? "))
    height = int(input("Input height ? "))
    print(f"Area of rectangle (width={width}, height = {height}) is {width*height}")
else:
    width = int(input("Input width ? "))
    height = int(input("Input height ? "))
    print(f"Area of triangle (width={width}, height={height}) is {width*height/2}")