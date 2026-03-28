import config
from dash import html
from dash_echarts import DashECharts

def build_revenue_chart(df):
    
    periods = df["period"].astype(str).tolist()
    peak_idx = df["package_sold"].idxmax()
    peak_month = df.loc[peak_idx, "period"]
    peak_value = round(df["package_sold"].max() / 1000, 1)
    last_3_avg = round(df["package_sold"].tail(3).mean() / 1000, 1)
    prior_3_avg = round(df["package_sold"].iloc[-6:-3].mean() / 1000, 1)
    trend = round((last_3_avg - prior_3_avg) / prior_3_avg * 100)
    trend_word = "down" if trend < 0 else "up"
    narrative = f"Peak revenue hit ${peak_value}K in {peak_month}. The last 3 months averaged ${last_3_avg}K — {trend_word} {abs(trend)}% from peak. The trend line shows where revenue is heading."
    data = []
    for v in df["package_sold"].tolist():
        k = round(v / 1000, 1)
        real = round(v)
        data.append({
            "value": real,
            "label": {
                "formatter": f"${k}K"
            }
        })

    option = {
        "textStyle": config.CHART_BASE["textStyle"],
        "title": {
            "text": "Sales Performance",
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
            },
            "formatter": "{b}<br/>${c}"
        },
        "legend": {
            "data": ["Revenue"],
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
            "data": periods,
            "name": "Period",
            "nameLocation": "middle",
            "nameGap": 30,
            "axisLabel": {
                "color": config.COLORS["text"],
                "fontFamily": "JetBrains Mono, monospace"
            },
            "nameTextStyle": {
                "color": config.COLORS["muted"],
                "fontSize": 12
            }
        },
        "yAxis": {
            "type": "value",
            "name": "Revenue",
            "nameLocation": "middle",
            "nameTextStyle": {
                "color": config.COLORS["muted"],
                "fontSize": 12,
                "fontFamily": "JetBrains Mono, monospace"
            },
            "nameGap": 70,
            "nameTextStyle": config.CHART_AXIS["nameTextStyle"],
            "nameRotate": 90,
            "axisLabel": {
            "color": config.COLORS["text"],
            "fontFamily": "JetBrains Mono, monospace",
            "formatter": "${value}"
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
                "name": "Revenue",
                "type": "line",
                "data": data,
                "smooth": True,
                "label": {
                    "show": True,
                    "position": "top",
                    "color": config.COLORS["text"],
                    "fontSize": 10,
                    "formatter": "${c}K"
                },
                "itemStyle": {"color": config.COLORS["primary"]},
                "emphasis": {
                    "itemStyle": {
                        "color": "#FFD700"
                    },
                    "lineStyle": {
                        "width": 4
                    },
                    "symbolSize": 10
                },
                "showSymbol": True,
                "symbolSize": 6,
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