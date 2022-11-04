groceryList = []
itemPrices = []


print("Welcome to the checkout counter! How many items are you purchasing today?")
numOfItems = int(input())
 
for number in range(numOfItems):
    print("Please enter the name of item " + str(number+1))
    groceryList.append(input())
    print("How much does " + str(groceryList[number]) + " cost?")
    print("$") itemPrices.append(float(input()))
    
print("Your order was:")
for number in range(len(groceryList)):
    print(str(groceryList[number]) + " $" + str(itemPrices[number]))
    
subtotal = sum(itemPrices)
totalPrice = round((subtotal * 0.09) + subtotal, 2)

print("Your subtotal comes to $" + str(subtotal) + ". With 9% sales tax, your total is $" + str(totalPrice) + ". Please enter cash amount: ")

userCash = float(input())
amountOwed = userCash - totalPrice

print("I owe you back $" + str(amountOwed) + ". Thank you for shopping with us!")