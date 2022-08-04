card_one='7'
card_two='8'

if card_one in ['J', 'K', 'Q']: card_one=10
if card_one=='A': card_one=11

if (int(card_one)>=10 or int(card_one)+int(card_two)>=11):
    print(1)
else:
    print(11)
