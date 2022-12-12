amazon_website = [("watch", 5000), ("phone", 10000), ("laptop", 50000), ("shirt", 1000)]
print("****** WELCOME TO AMAZON ******")
user_input = int(input("What you want?(0 for watch,1 for phone,2 for laptop and 3 for shirt) "))
quantity = int(input("Please enter your quantity: "))
total_bill = 0

for i in range(0,quantity):
    if user_input <4:
        user_selection = amazon_website[user_input][0]
        bill = amazon_website[user_input][1] * quantity
        total_bill = bill
    else :
        print("Your Product is Currently Not Available !")


print("******* YOUR CART *******")
print(f"Your Selected item is {user_selection}")
print(f"You Want {quantity} quantity")
print(f"Your Total Amount is {total_bill}")
print("THANK YOU FOR PURCHASING......")
