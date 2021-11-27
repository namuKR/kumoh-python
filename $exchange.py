currency = float(input("Input currency ? "))

won = float(input("Input korean money amount ? "))

dollar = won//currency
change = won - (dollar*currency)

print(f"{int(won//currency)} dollar and change is {int(won-won//currency*currency)}")