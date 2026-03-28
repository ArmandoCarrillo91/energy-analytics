import config
from dash import html
from dash_echarts import DashECharts

def build_forecast_chart(df):
    weeks = df["week"].tolist()
    expiring = df["expiring"].tolist()
    remaining = df["remaining"].tolist()

    total_active = df["remaining"].iloc[0]  # primer valor = total activos hoy
    week1_expiring = df["expiring"].iloc[0]  # cuántos vencen esta semana
    halfway = df[df["remaining"] <= total_active / 2].iloc[0]["week"]  # semana donde pierdes la mitad
    narrative = f"You have {total_active} active clients today. Each bar shows how many expire that week — after {halfway}, you'll have lost more than half. The line tracks what's left. Use this to prioritize who to call first."

    option = {
        "textStyle": config.CHART_BASE["textStyle"],
        "title": {
            "text": "Active Client Forecast",
            "left": "center",
            "top": 10,
            "textStyle": {"color": config.COLORS["text"]}
        },
        "tooltip": {
            "trigger": "axis",
            "backgroundColor": config.COLORS["card"],
            "borderColor": config.COLORS["border"],
            "textStyle": {
                "color": config.COLORS["text"],
                "fontFamily": "JetBrains Mono, monospace",
                "fontSize": 11
            }
        },
        "legend": {
            "data": ["Expiring", "Still Active"],
            "textStyle": {
                "color": config.COLORS["muted"],
                "fontSize": 11,
                "fontFamily": "JetBrains Mono, monospace"
            },
            "bottom": 0,
            "left": "left",
            "itemWidth": 12,
            "itemHeight": 8
        },
        "xAxis": {
            "type": "category",
            "data": weeks,
            "name": "Week",
            "nameLocation": "middle",
            "nameGap": 30,
            "axisLabel": {
                "color": config.COLORS["text"],
                "fontFamily": "JetBrains Mono, monospace",
                "fontSize": 9,
                "rotate": 15
            },
            "nameTextStyle": config.CHART_AXIS["nameTextStyle"]
        },
        "yAxis": {
            "type": "value",
            "name": "Clients",
            "nameLocation": "middle",
            "nameGap": config.CHART_AXIS["nameGap"],
            "nameRotate": 90,
            "nameTextStyle": config.CHART_AXIS["nameTextStyle"],
            "axisLabel": {
                "color": config.COLORS["text"],
                "fontFamily": "JetBrains Mono, monospace"
            },
            "splitLine": {
                "lineStyle": {
                    "type": "dashed",
                    "color": config.COLORS["border"]
                }
            }
        },
        "series": [
            {
                "name": "Expiring",
                "type": "bar",
                "data": expiring,
                "label": {
                    "show": True,
                    "position": "top",
                    "color": config.COLORS["text"],
                    "fontSize": 10
                },
                "itemStyle": {"color": config.COLORS["primary"]}
            },
            {
                "name": "Still Active",
                "type": "line",
                "smooth": True,
                "showSymbol": True,
                "data": remaining,
                "label": {"show": False},
                "lineStyle": {
                    "color": config.COLORS["trend_line"],
                    "width": 2,
                    "type": "dashed"
                },
                "itemStyle": {"color": config.COLORS["trend_point"]}
            }
        ]
    }
    return html.Div(
        style={
            "borderRadius": "12px",
            "border": f"1px solid {config.COLORS['border']}",
            "overflow": "hidden",
            "background": config.COLORS["card"]
        },
        children=[
            DashECharts(
                option=option,
                style={"height": "400px", "width": "100%"}
            ),
            html.P(narrative, style={
                "color": config.COLORS["muted"],
                "fontSize": "11px",
                "fontStyle": "italic",
                "padding": "8px 16px 12px",
                "lineHeight": "1.5"
            })
        ]
    )