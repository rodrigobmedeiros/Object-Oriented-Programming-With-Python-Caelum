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
    """
    Class to define account's properties
    """
    def __init__(self, number, owner, balance, limit):

        print('Creating an account...')
        self.creation_date = CreationDate()
        self.number = number
        self.owner = owner
        self.balance = balance
        self.limit = limit
        self.log = Log()
        print('Creation Date: {}'.format(self.creation_date.today))
        print('Account created...')

    def withdraw(self, value):

        self.balance -= value
        self.log.log('withdraw: R${}'.format(value))

    def deposit(self, value):

        self.balance += value
        self.log.log('deposit: R${}'.format(value))

    def statement(self):

        print('Account Owner: {}'.format(self.owner.name))
        print('Account: {} Balance: {}'.format(self.number, self.balance))
        self.log.log('print statement')

    def transfer_to(self, account_to_transfer, value):

        self.balance -= value
        account_to_transfer.deposit(value)
        print('value: {} Transfer to: {}'.format(value, account_to_transfer.number))
        print('Account: {} Balance: {}'.format(self.number, self.balance))
        self.log.log('value: {} Transfer to: {}'.format(value, account_to_transfer.number))

    def print_log(self):

        for log in self.log.log_operation:

            print(log)

