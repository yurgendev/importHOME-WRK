class Order:
    def __init__(self, customer):
        self.customer = customer
        self.items = {}

    def add_item(self, item, quantity=1):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity

    def get_total_price(self):
        total_price = 0
        for item, quantity in self.items.items():
            total_price += item.price * quantity
        return total_price

    def __str__(self):
        items_str = "\n".join(
            [f"{item.description} x {quantity} - {item.price * quantity}$" for item, quantity in self.items.items()])
        return f"Order by {self.customer.name} {self.customer.surname}:\n{items_str}\nTotal price: {self.get_total_price()}$"

