#polymorphism
class Payment:
    def pay(self):
        print("Processing payment")

class UPI(Payment):
    def pay(self):
        print("Payment made using UPI")

class Card(Payment):
    def pay(self):
        print("Payment made using Card")

payments = [UPI(), Card()]

for payment in payments:
    payment.pay()
