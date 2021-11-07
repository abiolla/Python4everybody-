text = "X-DSPAM-Confidence:    0.8475"

pos = text.find(' ')

number = text[pos+1 : ]

print(float(number))
