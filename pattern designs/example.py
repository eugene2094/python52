from abc import ABC, abstractmethod


# ========================
# STRATEGY: Payment
# ========================

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Processing CARD payment: {amount}")


class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Processing PayPal payment: {amount}")


class CryptoPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Processing CRYPTO payment: {amount}")


# ========================
# STRATEGY: Discount
# ========================

class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, amount):
        pass


class NoDiscount(DiscountStrategy):
    def apply(self, amount):
        return amount


class TenPercentDiscount(DiscountStrategy):
    def apply(self, amount):
        return amount * 0.9


# ========================
# FACTORY: Notification
# ========================

class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass


class EmailNotification(Notification):
    def send(self, message):
        print(f"Sending EMAIL: {message}")


class SMSNotification(Notification):
    def send(self, message):
        print(f"Sending SMS: {message}")


class NotificationFactory:
    @staticmethod
    def create_notification(type_):
        if type_ == "email":
            return EmailNotification()
        elif type_ == "sms":
            return SMSNotification()
        else:
            raise ValueError("Unknown notification type")


# ========================
# REPOSITORY
# ========================

class OrderRepository:
    def save(self, order):
        print("Order saved to database")


# ========================
# ORDER (чистий клас)
# ========================

class Order:
    def __init__(self, customer, amount,
                 payment_strategy: PaymentStrategy,
                 discount_strategy: DiscountStrategy):
        self.customer = customer
        self.amount = amount
        self.payment_strategy = payment_strategy
        self.discount_strategy = discount_strategy

    def process(self):
        final_amount = self.discount_strategy.apply(self.amount)
        self.payment_strategy.pay(final_amount)
        return final_amount