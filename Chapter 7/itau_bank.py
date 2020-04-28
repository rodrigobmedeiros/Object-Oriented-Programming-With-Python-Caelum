import bank

client_1 = bank.Client('Rodrigo', 'Bernardo', '111484867-04')
client_2 = bank.Client('Renata', 'Teixeira', '120132167-00')

account_1 = bank.Account('123-4', client_1, 250.0, 1500.0)
account_2 = bank.Account('124-0', client_2, 500.0, 2500.0)

account_1.withdraw(1000)
account_1.deposit(1500)
account_1.transfer_to(account_2, 500)

account_1.print_log()

