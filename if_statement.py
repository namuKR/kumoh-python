char = input("Input character ? ")

# if a % 2 == 0:
#     print(f"{a} is even number")

# if a % 2 == 1:
#     print(f"{a} is odd number")

# # b = a//2

# # if a/2-b == 0:
# #     print(f"{int(a)} is even number")
# # else:
# #     print(f"{int(a)} is odd number")

# # # if a >> 1 << 1 == a:
# # #     print(f"{a} is even number")
# # # else:
# # #     print(f"{a} is odd number")

# if a >= 0 and a % 2:
#     print(f"{a} is positive and odd")
# elif a >= 0 and not a % 2:
#     print(f"{a} is positive and even")
# elif a <= 0 and a % 2:
#     print(f"{a} is negative and odd")
# else:
#     print(f"{a} is negative and even")


# # a = char.lower()

# # if a in "a e i o u":
# #     print(f"{char} is vowel")
# # else:
# #     print(f"{char} is consonant")

# print("Grade : A") if score >= 90 else (print("Grade : B") if score >= 80 else (print("Grade : C") if score >= 70 else (print("Grade : D") if score >= 60 else print("Grade : E")) ) )

# # # if score >= 90:
# # #     print("Grade: A")
# # # elif score >= 80:
# # #     print("Grade : B")
# # # elif score >= 70:
# # #     print("Grade : C")
# # # elif score >= 60:
# # #     print("Grade : D")
# # # else:
# # #     print("Grade : E")

if char >= "a" and char <= 'z':
    print(char, "is lower case")
elif char >= 'A' and char <= 'Z':
    print(char, "is upper case")