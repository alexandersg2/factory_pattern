from abc import ABC, abstractmethod


class PaymentProcessor(ABC):

    @abstractmethod
    def make_payment(self, amount: float):
        ...


class StripePaymentProcessor(PaymentProcessor):

    def make_payment(self, amount: float):
        print(f"Made a Stripe payment of {amount}")


class AdyenPaymentProcessor(PaymentProcessor):

    def make_payment(self, amount: float):
        print("Did some Adyen specific stuff")
        print(f"Made an Adyen payment of {amount}")


class PaymentService(ABC):

    @abstractmethod
    def create_payment_processor(self):
        ...

    def make_payment(self, amount: float):
        self.verify_config()
        payment_processor = self.create_payment_processor()
        payment_processor.make_payment(amount)
    
    def verify_config(self):
        print("Verified payment config")


class StripePaymentService(PaymentService):

    def create_payment_processor(self):
        # You could do some specific Stripe setup stuff here
        return StripePaymentProcessor()


class AdyenPaymentService(PaymentService):

    def create_payment_processor(self):
        return AdyenPaymentProcessor()


PAYMENT_SERVICE_MAP = {
    "adyen": AdyenPaymentService,
    "stripe": StripePaymentService,
}


def get_provider():
    provider_list = " or ".join(PAYMENT_SERVICE_MAP.keys())
    while True:
        provider = input(f"Use {provider_list}? ").lower()
        if provider in PAYMENT_SERVICE_MAP.keys():
            return provider


def get_amount():
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

    payment_service = PAYMENT_SERVICE_MAP.get(provider)()
    payment_service.make_payment(amount)


if __name__ == "__main__":
    main()
