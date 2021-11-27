discount = 0.9

def today():
    print('가격: %s' % (discount*1000))

def tomorrow():
    global discount
    discount = 0.5
    print('가격: %s' % (discount*1000))

today()

tomorrow()
print(discount)