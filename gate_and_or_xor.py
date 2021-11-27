gate = input("Input gates (and, or, xor) ? ")

if gate not in ['and', 'or', 'xor']:
    print("Error - gate is not AND or OR or XOR")
    raise TypeError("Error")

fst = int(input("Input 1 (0 or 1) ? "))
sec = int(input("Input 2 (0 or 1) ? "))

if fst not in [0, 1] or sec not in [0, 1]:
    raise TypeError('first or second value is not 0 or 1')

if gate == 'and':
    print(f"{fst} and {sec} = {fst*sec}")
elif gate == 'or':
    if fst + sec >= 1:
        print(f"{fst} or {sec} = 1")
    else:
        print(f"{fst} or {sec} = 0")
elif gate == 'xor':
    print(f"{fst} xor {sec} = {fst+sec % 2}")