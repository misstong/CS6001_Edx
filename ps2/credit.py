balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
sum=0
for i in range(1,13):
    payment=balance*monthlyPaymentRate
    unpaid_balance=balance-payment
    interst=unpaid_balance*annualInterestRate/12
    balance=unpaid_balance+interst
    sum=sum+payment
    print "Month:"+str(i)
    print "Minimum monthly payment:"+str("%.2f"%payment)
    print "Remaining balance:"+str("%.2f"%balance)
print "Total paid:"+str("%.2f"%sum)
print "Remaining balance:"+str("%.2f"%balance)
