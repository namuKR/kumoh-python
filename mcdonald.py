# Bigmac 9000won
# Chicken 5000won
# cola 2500won
# ice crean 800won

print(
    """
    1.BigMac 9000원
    2.Chicken 5000원
    3.Cola 2500원
    4.Ice-cream 800원
    """
)
menus = input("Input (menu,quantity,amount) ? ").split(',')

menu = menus[0]
quantity = int(menus[1])
amount = int(menus[2])

if menu == 'BigMac':
    price = amount-9000*quantity
elif menu == 'Chicken':
    price = amount-5000*quantity
elif menu == 'Cola':
    price = amount-2500*quantity
else:
    price = amount-800*quantity

if price >= 0:
    print(f"Change is {price}원")
else:
    print(f"Insufficient amount ({price}원)")