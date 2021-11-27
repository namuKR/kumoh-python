bill = int(input("Input amount? "))

_500_won_ = bill // 500
_100_won_ = (bill-500*_500_won_) // 100
_50_won_ = (bill-500*_500_won_-100*_100_won_) // 50
_10_won_ = (bill-500*_500_won_-100*_100_won_-50*_50_won_) // 10

print(f"500 won = {_500_won_} 개\n100 won = {_100_won_} 개\n50 won = {_50_won_} 개\n10 won = {_10_won_} 개")