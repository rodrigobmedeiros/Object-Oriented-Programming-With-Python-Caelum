# File to create employee classes


class Employee(object):

    def __init__(self, name, cpf, salary):

        self._name = name
        self._cpf = cpf
        self._salary = salary

    def get_bonus(self):

        return self._salary * 0.1

    @property
    def name(self):

        return self._name

    @name.setter
    def name(self, correct_name):

        self._name = correct_name


class Manager(Employee):

    def __init__(self, name, cpf, salary, password, qtd_employee):

        super().__init__(name, cpf, salary)
        self._password = password
        self._qtd_employee = qtd_employee

    def authenticate(self, password):

        if self._password == password:

            print('Access Cleared')

        else:

            print('Access Denied')

    def get_bonus(self):

        return self._salary * 0.15

