class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity

    def apply_discount(self, percent):
        if 0 <= percent <= 100:
            discount_amount = self.price * (percent / 100)
            self.price -= discount_amount
            print(f"{self.name}: {percent}% discount applied. New price: {self.price}")
        else:
            print("Discount percent must be between 0 and 100.")

    def show_info(self):
        print(f"{self.name} | Price: {self.price} | Qty: {self.quantity} | Value: {self.total_value()}")


class ElectronicItem(Item):
    def __init__(self, name, price, quantity, warranty_years):
        super().__init__(name, price, quantity)
        self.warranty_years = warranty_years

    def show_info(self):
        print(f"{self.name} (Electronic) | Price: {self.price} | Qty: {self.quantity} | Warranty: {self.warranty_years} years | Value: {self.total_value()}")


class GroceryItem(Item):
    def __init__(self, name, price, quantity, expiry_date):
        super().__init__(name, price, quantity)
        self.expiry_date = expiry_date

    def show_info(self):
        print(f"{self.name} (Grocery) | Price: {self.price} | Qty: {self.quantity} | Expiry: {self.expiry_date} | Value: {self.total_value()}")


# Test
i1 = ElectronicItem("Laptop", 800, 3, 2)
i2 = GroceryItem("Milk", 2, 10, "2026-03-01")
i3 = ElectronicItem("Headphones", 50, 5, 1)

items = [i1, i2, i3]

print("Before discount:")
for item in items:
    item.show_info()

print("\nApplying 10% discount to Laptop...\n")
i1.apply_discount(10)

print("\nAfter discount:")
for item in items:
    item.show_info()
