class Price_check(Exception):
    pass


class Cars:
    def __init__(self, price, description, type):
        if price <= 0:
            raise Price_check('Price canna be Zero or less')
        self.price = price
        self.description = description
        self.type = type

    def __str__(self):
        return f"This is a {self.description}, equipment here is: {self.type} and price is {self.price}"


class Customer:
    def __init__(self, name, surname, number, delivery_address):
        self.name = name
        self.surname = surname
        self.number = number
        self.delivery_address = delivery_address

    def __str__(self):
        return f"Customer name: {self.name}, {self.surname}, {self.number}, \n{self.delivery_address}."