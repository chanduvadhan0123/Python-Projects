class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity=1):
        self.items.append({"product": product, "quantity": quantity})

    def view_cart(self):
        total = 0
        print("Cart Contents:")
        for item in self.items:
            product = item["product"]
            quantity = item["quantity"]
            subtotal = product.price * quantity
            total += subtotal
            print(f"{product.name} - Quantity: {quantity} - Subtotal: ${subtotal:.2f}")

        print(f"Total: ${total:.2f}")

# Example Usage:
if __name__ == "__main__":
    # Create some products
    product1 = Product("Laptop", 999.99)
    product2 = Product("Mouse", 19.99)
    product3 = Product("Headphones", 49.99)

    # Create a shopping cart
    cart = ShoppingCart()

    # Add items to the cart
    cart.add_item(product1, 2)
    cart.add_item(product2, 1)
    cart.add_item(product3, 3)

    # View the cart contents
    cart.view_cart()
