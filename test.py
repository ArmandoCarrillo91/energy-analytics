import data

df = data.get_clients_packages()
print(df.head())
print(data.total_clients(df))