from dash import html
from dash_echarts import DashECharts
import config
import data
import charts.clients as clients
import charts.packages as packages


def build_charts(df):
    df_monthly = data.get_clients_per_month(df)
    df_packages = data.get_packages_per_month(df)

    chart_clients = html.Div(
        style={
            "borderRadius": "12px",
            "border": f"1px solid {config.COLORS['border']}",
            "overflow": "hidden",
            "background": config.COLORS["card"]
        },
        children=[
            DashECharts(
                option=clients.build_clients_chart(df_monthly),
                style={"height": "400px", "width": "100%"}
            )
        ]
    )

    chart_packages = html.Div(
        style={
            "borderRadius": "12px",
            "border": f"1px solid {config.COLORS['border']}",
            "overflow": "hidden",
            "background": config.COLORS["card"]
        },
        children=[
            DashECharts(
                option=packages.build_packages_chart(df_packages),
                style={"height": "400px", "width": "100%"}
            )
        ]
    )

    return html.Div(
        style={
            "display": "grid",
            "gridTemplateColumns": "repeat(auto-fill, minmax(500px, 1fr))",
            "gap": "16px"
        },
        children=[chart_clients, chart_packages]
    )