import bank


client_1 = bank.Client('Rodrigo', 'Bernardo', '111484867-04')

account_1 = bank.Account('123-4', client_1, 250.0, 1500.0)

client_2 = bank.Client('Renata', 'Teixeira', '120132167-00')

account_2 = bank.Account('123-4', client_2, 250.0, 1500.0)
account_3 = bank.Account('123-4', client_2, 250.0, 1500.0)
account_4 = bank.Account('123-4', client_2, 250.0, 1500.0)
account_5 = bank.Account('123-4', client_2, 250.0, 1500.0)
account_6 = bank.Account('123-4', client_2, 250.0, 1500.0)


print(account_1.id)
print(account_2.id)
print(account_3.id)
print(account_4.id)
print(account_5.id)
print(account_6.id)

