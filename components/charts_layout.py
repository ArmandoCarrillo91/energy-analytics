from dash import html
from dash_echarts import DashECharts
import config
import data
import charts.clients as clients
import charts.packages as packages
import charts.revenue as revenue
from components.insight import build_insight
import charts.forecast as forecast
from components.active_clients import build_active_clients_section

def build_charts(df):
    df_monthly = data.get_clients_per_month(df)
    df_packages = data.get_packages_per_month(df)
    df_revenue = data.get_revenue_per_month(df)
    df_forecast = data.get_expiration_forecast(df)

    chart_clients = clients.build_clients_chart(df_monthly)
    chart_packages = packages.build_packages_chart(df_packages)
    chart_revenue = revenue.build_revenue_chart(df_revenue)
    chart_forecast = forecast.build_forecast_chart(df_forecast)

    return html.Div(
        style={"display": "flex", "flexDirection": "column", "gap": "16px"},
        children=[
            html.Div(
                style={"display": "grid", "gridTemplateColumns": "1fr 1fr", "gap": "16px"},
                children=[chart_clients, chart_packages]
            ),
            build_insight(df),
            build_active_clients_section(df),
            html.Div(
                style={"display": "grid", "gridTemplateColumns": "1fr 1fr", "gap": "16px"},
                children=[chart_revenue, chart_forecast]
            )
        ]
    )