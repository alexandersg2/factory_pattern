from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    @abstractmethod
    def make_payment(self, amount):
        ...


class StripePaymentProcessor(PaymentProcessor):
    def make_payment(self, amount: float):
        # Do some Stripe specific payment stuff
        # Process the payment
        print(f"Made a Stripe payment of {amount}")


class AdyenPaymentProcessor(PaymentProcessor):
    def make_payment(self, amount: float):
        # Do some Adyen specific payment stuff
        # Process the payment
        print(f"Made an Adyen payment of {amount}")


class PaymentService:
    @abstractmethod
    def create_payment_processor(self):
        ...

    def make_payment(self, amount: float):
        payment_processor = self.create_payment_processor()
        payment_processor.make_payment(amount)


class StripePaymentService(PaymentService):
    def create_payment_processor(self):
        return StripePaymentProcessor()


class AdyenPaymentService(PaymentService):
    def create_payment_processor(self):
        return AdyenPaymentProcessor()


def get_provider():
    provider = None
    while True:
        provider = input("Use Stripe or Adyen? ").lower()
        if provider in ("adyen", "stripe"):
            return provider


def get_amount():
    amount = None
    while True:
        amount = input("Enter transaction amount: ")
        try:
            amount = float(amount)
            return amount
        except ValueError:
            ...


def main():
    provider = get_provider()
    amount = get_amount()

    if provider == 'adyen':
        payment_service = AdyenPaymentService()
    else:
        payment_service = StripePaymentService()
    
    payment_service.make_payment(amount)


if __name__ == "__main__":
    main()