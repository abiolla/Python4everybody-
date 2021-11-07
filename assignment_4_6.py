def computepay(h, r):
    if h <= 40:
        pay = h * r
        return pay
    else:
        pay = (40 * r) + ((h - 40) * r * 1.5)
        return pay

hrs = float(input("Enter Hours:"))
rate = float(input("Enter rate per hour:"))
p = computepay(hrs , rate)
print("Pay", p)
