class CreditCardPayment:
    def __init__(self, amount, card_number):
        self.amount = amount
        self.card_number = card_number

    def process_payment(self):
        print(f"Processing credit card payment of {self.amount} using card number {self.card_number}")


class PayPalPayment:
    def __init__(self, amount, paypal_account):
        self.amount = amount
        self.paypal_account = paypal_account

    def process_payment(self):
        print(f"Processing PayPal payment of {self.amount} from account {self.paypal_account}.")


class CryptoPayment:
    def __init__(self, amount, wallet_address):
        self.amount = amount
        self.wallet_address = wallet_address

    def process_payment(self):
        print(f"Processing cryptocurrency payment of {self.amount} from account {self.wallet_address}.")


def process_payment(payment):
    payment.process_payment()


credit_card = CreditCardPayment(100, "1234-5678-9101-1121")
paypal = PayPalPayment(200, "user@example.com")
crypto = CryptoPayment(0.05, "abc123xyz456crypto")

for payment_method in [credit_card, paypal, crypto]:
    process_payment(payment_method)
