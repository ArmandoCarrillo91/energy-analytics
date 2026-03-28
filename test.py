import charts.clients as clients
import data

df = data.fetch_clients_packages()        # 1. trae datos crudos
df_packages = data.get_packages_per_month(df)  # 2. transforma

df_revenue = data.get_revenue_per_month(df)
print(df_revenue)