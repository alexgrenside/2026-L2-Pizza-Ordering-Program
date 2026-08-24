# Super simple cart test - just add items then see them.

cart = []

while True:
    item = input("What pizza do you want? (type 'x' to stop) ")

    if item == "x":
        break

    qty = int(input("How many? "))

    cart.append([item, qty])

# Display the cart
print("\n--- YOUR CART ---")
for item in cart:
    print(f"{item[1]} x {item[0]}")