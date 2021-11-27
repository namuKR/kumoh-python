# get a starting number, step number and keep minusing the step number from the starting number until the starting number is less than 0


starting_number = int(input("Enter a starting number: "))
step_number = int(input("Enter a step number: "))
print(starting_number)
while starting_number-step_number > 0:
    starting_number -= step_number
    print(starting_number)