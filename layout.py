from dash import html
import data
import config
from components.header import build_header
from components.kpis import build_kpis
from components.charts_layout import build_charts
from components.insight import build_insight


def get_layout():
    df = data.fetch_clients_packages()

    return html.Div(
        style={
            "background": config.COLORS["background"],
            "padding": "32px 40px",
            "minHeight": "100vh"
        },
        children=[
            build_header(),
            build_kpis(df),
            build_charts(df),
            build_insight(df)
        ]
    )