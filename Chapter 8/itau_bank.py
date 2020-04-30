import bank

client_1 = bank.Client('Rodrigo', 'Bernardo', '111484867-04')
client_2 = bank.Client('Renata', 'Teixeira', '120132167-00')

account_1 = bank.Account('123-4', client_1, 250.0, 1500.0)
account_2 = bank.Account('124-0', client_2, 500.0, 2500.0)


account_1.balance = 10500
print(bank.Account.get_total_accounts())


