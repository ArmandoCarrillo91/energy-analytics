import data

df = data.fetch_clients_packages()


print(data.count_unique_clients(df))
print(data.get_clients_per_month(df))