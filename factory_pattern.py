from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    """Base class for Payment Processors."""

    @abstractmethod
    def make_payment(self, amount: float):
        """Process a payment."""
        ...


class StripePaymentProcessor(PaymentProcessor):
    """Payment processor for making Stripe payments."""

    def make_payment(self, amount: float):
        """Process a Stripe payment."""

        # Do some Stripe specific payment stuff
        print(f"Made a Stripe payment of {amount}")


class AdyenPaymentProcessor(PaymentProcessor):
    """Payment processor for making Adyen payments."""

    def make_payment(self, amount: float):
        """Process a Adyen payment."""

        # Do some Adyen specific payment stuff
        print(f"Made an Adyen payment of {amount}")


class PaymentService(ABC):
    """An abstract service to handle the making of payments."""

    @abstractmethod
    def create_payment_processor(self):
        """Factory method to create a concrete PaymentProcessor."""
        ...

    def make_payment(self, amount: float):
        """Make a payment with the PaymentProcessor"""

        payment_processor = self.create_payment_processor()
        payment_processor.make_payment(amount)
    
    def verify_config(self):
        """
        Perform some business logic around verifying if the user has
        payments setup.
        """
        ...


class StripePaymentService(PaymentService):
    """
    A Stripe payment service that instantiates a StripePaymentProcessor
    to handle payments.
    """

    def create_payment_processor(self):
        return StripePaymentProcessor()


class AdyenPaymentService(PaymentService):
    """
    An Adyen payment service that instantiates an AdyenPaymentProcessor 
    to handle payments.
    """

    def create_payment_processor(self):
        return AdyenPaymentProcessor()


PAYMENT_SERVICE_MAP = {
        "adyen": AdyenPaymentService,
        "stripe": StripePaymentService,
    }


def get_provider():
    provider = None
    while True:
        provider = input("Use Stripe or Adyen? ").lower()
        if provider in PAYMENT_SERVICE_MAP.keys():
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

    payment_service = PAYMENT_SERVICE_MAP.get(provider)()
    payment_service.make_payment(amount)


if __name__ == "__main__":
    main()
