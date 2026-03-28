import charts.clients as clients
import data

df = data.fetch_clients_packages()        # 1. trae datos crudos
df_packages = data.get_packages_per_month(df)  # 2. transforma
print(data.count_clients_without_package(df))
print(data.count_total_packages(df))
print(data.count_gifted_packages(df))
print(data.count_sold_packages(df))