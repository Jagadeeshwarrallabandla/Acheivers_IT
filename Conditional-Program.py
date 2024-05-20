#Declaring List of Dictionaries
'''grocery_items = [
    {"name": "Osmania Biscuits", "quantity": "100 Packets", "price": 1000},
    {"name": "Sugar", "quantity": "15 Kg", "price": 4500},
    {"name": "Bread", "quantity": "50 Big Slices", "price": 4000}
]
total_price = 0
for products in grocery_items:
    total_price += products["price"]
print("your Grossery items total bill is =", total_price)

if total_price >= 15000:
    discount_percentage = 15
    amount_to_pay = total_price - (total_price* 15 // 100)    
print("Your total grocery bill is =",total_price, "You got 15% Discount on your bill After Discount You need to pay =", amount_to_pay)

elif (total_price >= 10000 and total_price < 15000):
    discount_percentage = 10
    amount_to_pay = total_price - (total_price * 10 // 100)
print("Your total grocery bill is =",total_price, "You got 10% Discount on your bill After Discount You need to pay =", amount_to_pay)

else :
    discount_percentage = 0
    amount_to_pay = total_price
print("No Discount Available at your Bill !! Thank you", amount_to_pay)'''


grocery_items = [
    {"name": "Osmania Biscuits", "quantity": "100 Packets", "price": 1000},
    {"name": "Sugar", "quantity": "15 Kg", "price": 4500},
    {"name": "Bread", "quantity": "50 Big Slices", "price": 4000}
]
total_price = 0
for products in grocery_items:
    total_price += products["price"]
print("Your Grossery items total bill is =", total_price)

if total_price >= 15000:
    discount_percentage = 15
    amount_to_pay = total_price - (total_price * 15 // 100)    
    print("Your total grocery 	bill is =", total_price, "You got 15% Discount on your bill After Discount You need to pay =", amount_to_pay)

elif (total_price >= 10000 and total_price < 15000):
    discount_percentage = 10
    amount_to_pay = total_price - (total_price * 10 // 100)
    print("Your total grocery bill is =", total_price, "You got 10% Discount on your bill After Discount You need to pay =", amount_to_pay)

else:
    discount_percentage = 0
    amount_to_pay = total_price
    print("No Discount Available on your Bill !! Thank you, Amount to Pay =", amount_to_pay)

    