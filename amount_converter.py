# won = int(input("Input amount (maximum 99999) ? "))

# man = won // 10000
# cheon = (won-10000*man) // 1000
# baek = (won-10000*man- 1000*cheon) // 100
# sip = (won-10000*man- 1000*cheon - 100*baek) // 10
# il = (won-10000*man- 1000*cheon - 100*baek - 10*sip)

# print(f"{f'{man}만' if man != 0 else ''}{f'{cheon}천' if cheon != 0 else ''}{f'{baek}백' if baek != 0 else ''}{f'{sip}십' if sip != 0 else ''}{f'{il}원' if il != 0 else ''}")


won = int(input("Input amount (maximum 99999) ? "))

man = won // 10000
cheon = (won-10000*man) // 1000
baek = (won-10000*man- 1000*cheon) // 100
sip = (won-10000*man- 1000*cheon - 100*baek) // 10
il = (won-10000*man- 1000*cheon - 100*baek - 10*sip)


en_kr = ['영','일','이','삼','사','오','육','칠','팔','구']

if man == 0:
    man = ""
else:
    man = f"{en_kr[man]}만"

if cheon == 0:
    cheon = ""
else:
    cheon = f"{en_kr[cheon]}천"

if baek == 0:
    baek = ""
else:
    baek = f"{en_kr[baek]}백"

if sip == 0:
    sip = ""
else:
    sip = f"{en_kr[sip]}십"

if il == 0:
    il = ""
else:
    il = f"{en_kr[il]}"

print(f"{man}{cheon}{baek}{sip}{il}원")