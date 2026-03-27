import charts.clients as clients
import data

df = data.fetch_clients_packages()
df_monthly = data.get_clients_per_month(df)
option = clients.build_clients_chart(df_monthly)
print(option)