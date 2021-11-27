weight = float(input("Input weight? "))
height = float(input("Input height? "))

obesity = (height - 110) / weight

print("Weight %.2f, Height %.2f, Obesity %.2f" % (weight, height, obesity))