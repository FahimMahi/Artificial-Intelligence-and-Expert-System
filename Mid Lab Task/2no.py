def tip_amount(bill, service): 	
    if bill<25.00:
        tip = 6.0
    else:
        if service==True:
            tip = (0.27 * bill)
        else:
            tip = (0.13 * bill)
    return tip
    
print(tip_amount(23.37, True))
print(tip_amount(23.37, False))
print(tip_amount(81.75, True))
print(tip_amount(63.59, True))
print(tip_amount(63.59, False))  