from dash import html
from dash_echarts import DashECharts
import data
import config
import charts.clients as clients

def get_layout():
    df = data.fetch_clients_packages()
    df_monthly = data.get_clients_per_month(df)
    total = data.count_unique_clients(df)
    kpi_total_clients = html.Div(
        style={
            "background": config.COLORS["card"],
            "padding": "24px",
        },
        children=[
            html.H2(total),
            html.P("Total Clients")
        ]
    )

    chart_clients = DashECharts(
        option=clients.build_clients_chart(df_monthly),
        style={"height": "400px", "background": config.COLORS["card"]}
    )

    return html.Div(
        style={
            "background": config.COLORS["background"],
            "padding": "24px",
            "minHeight": "100vh"
        },
        children=[
        
            html.Div(
                style={
                    "display": "grid",
                    "gridTemplateColumns": "repeat(4, 1fr)",
                    "gap": "16px",
                    "marginBottom": "24px"
                },
                children=[
                    kpi_total_clients
                ]
            ),
            html.Div(
                style={
                    "display": "grid",
                    "gridTemplateColumns": "repeat(2, 1fr)",
                    "gap": "16px"
                },
                children=[chart_clients]
             )
        ]
    )