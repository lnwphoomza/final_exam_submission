class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f'Hi, I\'m {self.name}.')

class Customer(Person):
    def __init__(self, name, address):
        super().__init__(name)
        self.address = address

    def place_order(self, item):
        x1 = DeliveryOrder(alice.name, item)
        x2 = DeliveryOrder(bob.name, item)
    
class Driver(Person):
    def __init__(self, name, item, vehicle):
        super().__init__(name)
        self.item = item
        self.vehicle = vehicle

    def deliver(self, order):
        self.item = order
        print(f'David is delivering {self.item} to {self.name} using {self.vehicle}.')
        status = "delivered"
        self.status = status

class DeliveryOrder:
    def __init__(self, customer, item, status="preparing"):
        self.customer = customer
        self.item = item
        self.status = status

    def assign_driver(self, driver):
        self.driver = driver
    def summary(self):
        return f"Order Summary:\nItem: {self.item}\nCustomer: {self.customer}\nStatus: {self.status}\nDriver: David"
        
alice = Person("Alice") #customer
bob = Person("Bob") #customer
david = Person('David') #driver

print(alice.introduce())
print(bob.introduce())
print(david.introduce())
print()

driver1 = Driver("David", "Laptop", "motorcycle")
driver2 = Driver("David", "Headphones", "motorcycle")

d1 = DeliveryOrder(alice.name, "Laptop", "preparing")
d2 = DeliveryOrder(bob.name, "Headphones", "preparing")

print(d1.summary())
print()
print(d2.summary())
print()

print(driver1.deliver("Laptop"))
print(driver1.deliver("Headphones"))
print()

print(f'Final Status:\nOrder for {driver1.item} → delivered\nOrder for {driver2.item} → delivered')

#Tanisorn Pisittanphat 6810545671




        
              
