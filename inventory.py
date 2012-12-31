#inventory.py

"""
This will keep track of inventory for the tea shoppe.
"""

class tea:
    type = 'none'
    stock = 0
    price = 0
    def buy(self,num):
        self.stock = self.stock + num
    def sell(self,num):
        self.stock = self.stock - num

oolong = tea()
oolong.type = 'black'
oolong.stock = 10
oolong.price = 10
print oolong.type
print oolong.stock
print oolong.price

oolong.buy(2)
print oolong.stock
