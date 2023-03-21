from models import Cars, Customer
from order_module import Order

car1 = Cars(12500, 'Mercedes Benz C300', 'Cabrio')
car2 = Cars(10000, 'BMW 528i', 'Sedan')
car3 = Cars(50000, 'BMW 730', 'Sedan')
car4 = Cars(250_000, 'Urus', 'SUV')

customer1 = Customer('Stepan', 'Bandera', '+380970000001', 'Ukraine: Lviv, str. tra-la-la, 28')
customer2 = Customer('Isaak', 'Avraamovich', '+380970000002', 'Israel: Petakh-Tikva, str. ola-la, 1/2')

order = Order(customer2)
order.add_item(car1, 1)
order.add_item(car2, 2)
order.add_item(car3, 3)
order.add_item(car4, 1)
print(order)
print('*' * 50)
print(customer2)
