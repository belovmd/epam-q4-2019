#!/usr/bin/env python3.7

"""Classes.

12 lines: Classes from https://wiki.python.org/moin/SimplePrograms .

"""


class BankAccount():
    """
    Bank account.

    Attributes
    ----------
    object : object
    Initial balance.

    Methods
    -------
    deposit(amount)
        Add amount to account deposit.
    withdraw(amount)
        Withdraw amount to account deposit.
    overdrawn()
        Return true if balance less than 0.

    """

    def __init__(self, initial_balance=0):
        """Create bacnk account with initial balance."""
        self.balance = initial_balance

    def deposit(self, amount):
        """Add amount to account deposit."""
        self.balance += amount

    def withdraw(self, amount):
        """Withdraw amount to account deposit."""
        self.balance -= amount

    def overdrawn(self):
        """Return true if balance less than 0."""
        return self.balance < 0


MY_ACCOUNT = BankAccount(15)
MY_ACCOUNT.withdraw(50)
print(MY_ACCOUNT.balance, MY_ACCOUNT.overdrawn())
