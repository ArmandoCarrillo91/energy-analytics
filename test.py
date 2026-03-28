import charts.clients as clients
import data

df = data.fetch_clients_packages()        # 1. trae datos crudos
df_packages = data.get_packages_per_month(df)  # 2. transforma

print(data.total_revenue(df))
print(data.revenue_this_month(df))
print(data.avg_ticket(df))