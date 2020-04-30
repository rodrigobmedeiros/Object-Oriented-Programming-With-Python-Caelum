import bank


client_1 = bank.Client('Rodrigo', 'Bernardo', '111484867-04')

account_1 = bank.Account('123-4', client_1, 250.0, 1500.0)

account_1.number = '999-9'

account_1._teste = 1000

print(account_1._teste)

