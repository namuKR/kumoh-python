char = input("Input character? ")
# if char.lower() == char: # 'A" <= char <= 'Z'
#     char = ord(char)
#     char -= 32
#     char = chr(char)
#     print("Upper case is", char)
    
# elif char.upper() == char: # 'a' <= char <= 'z'
#     char = ord(char)
#     char += 32
#     char = chr(char)
#     print("Lower case is", char)

#small a : 97
# big A : 65

if 'A' <= char <= 'Z':
    char = ord(char)
    print(f"Lower case is {chr(char - ord('A') + ord('a'))}")
elif 'a' <= char <= 'z':
    char = ord(char)
    print(f"Upper case is {chr(char - ord('a') + ord('A'))}")