from dash import html
from dash_echarts import DashECharts
import data

COLORS = {
    "background": "#FAF9F6",
    "accent": "#F5A623",
    "text": "#0A0A0A",
    "muted": "#888888",
    "green": "#1A9E5C",
    "red": "#D94F4F",
    "border": "#E5E2DC",
    "card": "#FFFFFF",
}

def get_layout():
    df = data.get_clientes_por_mes()
    df["mes"] = df["mes"].dt.strftime("%b %Y")

    option = {
        "backgroundColor": COLORS["background"],
        "xAxis": {
            "type": "category",
            "data": df["mes"].tolist(),
            "axisLabel": {"color": COLORS["muted"]}
        },
        "yAxis": {
            "type": "value",
            "axisLabel": {"color": COLORS["muted"]}
        },
        "series": [{
            "data": df["nuevos"].tolist(),
            "type": "line",
            "smooth": True,
            "lineStyle": {"color": COLORS["accent"], "width": 2},
            "itemStyle": {"color": COLORS["accent"]}
        }]
    }

    return html.Div(
        style={"background": COLORS["background"], "height": "100vh", "padding": "20px"},
        children=[
            html.H3("Clientes registrados por mes",
                    style={"color": COLORS["text"], "fontFamily": "monospace"}),
            DashECharts(option=option, style={"height": "400px"})
        ]
    )