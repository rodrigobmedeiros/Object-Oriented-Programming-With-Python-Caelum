import bank


client_1 = bank.Client('Rodrigo', 'Bernardo', '111484867-04')

account_1 = bank.Account('123-4', client_1, 250.0, 1500.0)

print(account_1._Account__balance)

