# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    line = line.rstrip()
    print(line.upper())

# Crypto Trading function that takes deposits and operations as arguments
def cryptoTrading(deposits, operations):


    output = []


    total_users = len(deposits)


    users_shares = [0]*total_users


    for each in (operations):


        split_each = each.split()


        operation = split_each[0]

        #
        user_id = int(split_each[1]) - 1


        if operation == 'deposit':
            amount = int(split_each[2])


            deposits[user_id] = deposits[user_id] + amount


            output.append(deposits[user_id])

        elif operation == 'buy':
            shares = int(split_each[2])
            stock_price = int(split_each[3])


            needed_money = shares * stock_price
            available_user_money = deposits[user_id]


            if available_user_money >= needed_money:


                deposits[user_id] = deposits[user_id] - needed_money


                users_shares[user_id] = users_shares[user_id] + shares


                output.append(deposits[user_id])


            else:

                output.append(deposits[user_id])

        elif operation == 'sell':
            shares = int(split_each[2])
            stock_price = int(split_each[3])


            if users_shares[user_id] >= shares:


                money_gained = shares * stock_price


                deposits[user_id] = deposits[user_id] + money_gained


                users_shares[user_id] = users_shares[user_id] - shares


                output.append(deposits[user_id])


            else:


                output.append(deposits[user_id])


    return output


r = cryptoTrading(deposits = [9, 7, 12],

operations = [
  "buy 1 3 2",
  "sell 1 4 10",
  "deposit 2 12",
  "buy 2 10 2",
  "buy 2 6 3"
])

# Print the return array
print(r)


def camelCaseSeparation(words,variableName):
    s=""
    flag=0
    for i in variableName:
        if(flag==0):
            s+=i.lower()
            flag=1
        elif(i.isupper()):
            if s not in words:
                return "false"
            else:
                s=""
                s+=i.lower()
        else:
            s+=i
    if(s!=""):
        if s not in words:
            return "false"
        s=""
    return "true"




#words declaration
words=["is","valid","right"]

variableName="isValid"
print("camelCaseSeparation(words,variableName) =",camelCaseSeparation(words,variableName))
