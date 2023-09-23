#!/usr/bin/env python3
import ipdb
class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = []

    def reset_register_totals(self):
        self.total = 0

    def add_item(self, title, price, qty=1):
        for i in range(qty):
            self.items.append(title)
        self.lastprice = price * qty
        self.total += price * qty
    
    def apply_discount(self):
        if self.discount > 0:
            self.total = int(self.total - (self.total * self.discount / 100))
            print (f"After the discount, the total comes to ${self.total}.")
        else:
            print ("There is no discount to apply.")

    def void_last_transaction(self):
        self.total -= self.lastprice

# ipdb.set_trace()