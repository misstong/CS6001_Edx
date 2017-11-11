balance = 3329
annualInterestRate = 0.2
fixed=0
while True:
    remaining_balance=balance
    for i in range(1,13):
        unpaid=remaining_balance-fixed
        interest=unpaid*annualInterestRate/12
        remaining_balance=unpaid+interest
    if remaining_balance<=0:
        print "Lowest Payment:"+str(fixed)
        break
    fixed=fixed+10
