# Initial inventory (item: quantity)
inventory = {
    "Keyboards": 30,
    "Adaptors": 25,
    "Laptops": 50,
    "Books": 100
}

# Display current inventory
print("Current Inventory:")
for item, quantity in inventory.items():
    print(f"{item}: {quantity} in stock")

# Update inventory
print("\nUpdate Inventory (type 'done' to finish):")
while True:
    item_to_update = input("Enter item name to update (or 'done'): ")

    if item_to_update.lower() == "done":
        break

    if item_to_update in inventory:
        try:
            new_quantity = int(input(f"Enter new quantity for {item_to_update}: "))
            inventory[item_to_update] = new_quantity
        except ValueError:
            print("Please enter a valid number.")
    else:
        print(f"{item_to_update} is not in the inventory.")

# Display updated inventory
print("\nUpdated Inventory:")
for item, quantity in inventory.items():
    print(f"{item}: {quantity} in stock")
