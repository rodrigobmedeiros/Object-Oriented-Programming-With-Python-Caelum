"""
Module bank: represents class, methods, attributes that will be used by banks to open new accounts, creates customers
data base and so on.
"""
import datetime as dt


class Log(object):

    def __init__(self):

        self.log_operation = []

    def log(self, operation):

        self.log_operation.append(str(dt.datetime.today().date()) + ' - ' + operation)


class CreationDate(object):

    def __init__(self):

        self.today = dt.datetime.today().date()


class Client(object):
    """
    Class to define the clients
    """
    def __init__(self, name, surname, cpf):

        self.name = name
        self.surname = surname
        self.cpf = cpf


class Account(object):

    _total_accounts = 0
    """
    Class to define account's properties
    """
    def __init__(self, number, owner, balance, limit):

        print('Creating an account...')
        self.creation_date = CreationDate()
        self.number = number
        self.owner = owner
        self._balance = balance
        self.limit = limit
        self.log = Log()
        Account._total_accounts += 1
        print('Creation Date: {}'.format(self.creation_date.today))
        print('Account created...')

    def withdraw(self, value):

        self._balance -= value
        self.log.log('withdraw: R${}'.format(value))

    def deposit(self, value):

        self._balance += value
        self.log.log('deposit: R${}'.format(value))

    def statement(self):

        print('Account Owner: {}'.format(self.owner.name))
        print('Account: {} Balance: {}'.format(self.number, self._balance))
        self.log.log('print statement')

    def transfer_to(self, account_to_transfer, value):

        self._balance -= value
        account_to_transfer.deposit(value)
        print('value: {} Transfer to: {}'.format(value, account_to_transfer.number))
        print('Account: {} Balance: {}'.format(self.number, self._balance))
        self.log.log('value: {} Transfer to: {}'.format(value, account_to_transfer.number))

    def print_log(self):

        for log in self.log.log_operation:

            print(log)

    @property
    def balance(self):

        return self._balance

    @balance.setter
    def balance(self, value):

        if self._balance < 0:

            print('Balance can not be negative')

        else:
            self._balance = value

    @classmethod
    def get_total_accounts(cls):

        return cls._total_accounts

    @staticmethod
    def teste(x, y):

        return x + y

