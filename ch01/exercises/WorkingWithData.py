print(10 * 5)
print(10 ** 2)
print(15 / 10)
print(15 // 10)
print(-15 // 10)
print(15 % 10)
print(10 % 15)
print(10 % 10)
print(0 % 10)
print(10/15)
# doesnt print right

rate = float(input("What is the current exchange rate for 1 Euro to Dollars? "))
print("The exchange rate is 1 Euro to ",rate,"dollars")

amount = float(input("How many Euros are you exchanging? "))
print("You have entered", amount, "Euros")

total = rate * amount
total = total - 3

strTotal = str(total)
sDot = strTotal.index('.')

for i in range(len(strTotal)):
  if i == sDot+3:
    strTotal = strTotal[0:i]

strCents = strTotal[sDot+1:sDot+3]
strDollars = strTotal[0:sDot]

dollars = int(strDollars)
cents = int(strCents)

print("After the service fee has been applied, you have", dollars,"dollars and",cents,"Cents")
     