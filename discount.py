price=int(input("Enter the price: "))
discount_percent = float(input("Enter the discount percentage: "))

def discount(price, discount_percent):
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    else:
        return price
    
print(f"final price: {discount(price, discount_percent)}")