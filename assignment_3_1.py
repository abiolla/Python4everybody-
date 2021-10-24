hrs = float(input('Enter Hours:'))
rate = float(input('Enter rate per hour:'))

if hrs <= 40 :
    pay = hrs * rate
    print(pay)
else:
    pay = (40 * rate ) + ((hrs - 40) * rate * 1.5)
    print(pay)
