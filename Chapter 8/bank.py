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
        self.__creation_date = CreationDate()
        self.__number = number
        self.__owner = owner
        self.__balance = balance
        self.__limit = limit
        self.__log = Log()
        Account._total_accounts += 1
        print('Creation Date: {}'.format(self.__creation_date.today))
        print('Account created...')

    def __withdraw(self, value):

        self.__balance -= value
        self.__log.log('withdraw: R${}'.format(value))

    def __deposit(self, value):

        self.__balance += value
        self.__log.log('deposit: R${}'.format(value))

    def __statement(self):

        print('Account Owner: {}'.format(self.__owner.name))
        print('Account: {} Balance: {}'.format(self.__number, self.__balance))
        self.__log.log('print statement')

    def __transfer_to(self, account_to_transfer, value):

        self.__balance -= value
        account_to_transfer.deposit(value)
        print('value: {} Transfer to: {}'.format(value, account_to_transfer.number))
        print('Account: {} Balance: {}'.format(self.__number, self.__balance))
        self.__log.log('value: {} Transfer to: {}'.format(value, account_to_transfer.number))

    def print_log(self):

        for log in self.__log.log_operation:

            print(log)

    @property
    def __balance(self):

        return self.__balance

    @__balance.setter
    def __balance(self, value):

        if self.__balance < 0:

            print('Balance can not be negative')

        else:
            self.__balance = value

    @classmethod
    def __get_total_accounts(cls):

        return cls.__total_accounts

