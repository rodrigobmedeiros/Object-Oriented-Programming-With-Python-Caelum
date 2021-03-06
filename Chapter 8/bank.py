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
    # Slot create a list of attributes for the objects, avoid that an user creates a new attribute dinamically.

    __slots__ = ['_creation_date', '_number', '_owner', '_balance', '_limit', '_log', 'id']

    # Count the number os instances created. In order to be a global counter, this attribute is defined at class level
    instance_count = 0

    def __init__(self, number, owner, balance, limit):

        print('Creating an account...')
        self._creation_date = CreationDate()
        self._number = number
        self._owner = owner
        self._balance = balance
        self._limit = limit
        self._log = Log()

        # Each object created increment the instance count
        Account.instance_count += 1

        # In this step we define the unique id of each instance
        self.id = Account.instance_count
        print('Creation Date: {}'.format(self._creation_date.today))
        print('Account created...')

    @property
    def number(self):

        return self._number

    @number.setter
    def number(self, number):

        self._number = number

    def withdraw(self, value):

        self._balance -= value
        self._log.log('withdraw: R${}'.format(value))

    def deposit(self, value):

        self._balance += value
        self._log.log('deposit: R${}'.format(value))

    def statement(self):

        print('Account Owner: {}'.format(self._owner.name))
        print('Account: {} Balance: {}'.format(self._number, self._balance))
        self._log.log('print statement')

    def transfer_to(self, account_to_transfer, value):

        self._balance -= value
        account_to_transfer.deposit(value)
        print('value: {} Transfer to: {}'.format(value, account_to_transfer.number))
        print('Account: {} Balance: {}'.format(self._number, self._balance))
        self._log.log('value: {} Transfer to: {}'.format(value, account_to_transfer.number))

    def print_log(self):

        for log in self._log.log_operation:

            print(log)

