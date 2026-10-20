from abc import ABC, abstractmethod


class PaymentGateway(ABC):
    @abstractmethod
    def pay(self):
        pass


class MaxPay(PaymentGateway):
    def pay(self):
        print("Paying using MaxPay...")


class RazorPay(PaymentGateway):
    def pay(self):
        print("Paying using RazorPay...")


class Purchase:
    def __init__(self, gateway):
        self.gateway = gateway

    def checkout(self):
        print("Checking out...")
        self.gateway.pay()


gateway1 = RazorPay()
gateway2 = MaxPay()

purchase = Purchase(gateway1)
purchase.checkout()
