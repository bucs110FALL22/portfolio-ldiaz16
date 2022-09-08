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
# converts total into string to be more mutable
sDot = strTotal.index('.')
#finds index of '.' to seperate dollars form cents
strCents = strTotal[sDot+1:sDot+3]
#Since the max amount of cents can only be 2 digits, strCents takes the digit next to the '.' and the one after that
strDollars = strTotal[0:sDot]
#takes all digits from the beginning to the '.'
dollars = int(strDollars)
#converts strDollars back into int for easier operation 
cents = int(strCents)
#^^
print("After the service fee has been applied, you have", dollars,"dollars and",cents,"Cents")
     