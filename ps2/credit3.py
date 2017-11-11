balance = 999999
annualInterestRate = 0.18
lower=balance/12
monthlyrate=annualInterestRate /12
higher=balance*pow(1+monthlyrate,12)/12
middle=(lower+higher)/2

def ok(fixed,remaining_balance):
    for i in range(1,13):
        unpaid=remaining_balance-fixed
        interest=unpaid*annualInterestRate/12
        remaining_balance=unpaid+interest
    if remaining_balance<=0:
        return True
    elif remaining_balance>0:
        return False
   
    

while higher-lower>0.01:
    remaining_balance=balance
    if ok(middle,remaining_balance):
        higher=middle
        middle=(lower+higher)/2
    else:
        lower=middle
        middle=(lower+higher)/2
print round((lower+higher)/2,2)

