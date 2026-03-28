import config
from dash import html
from dash_echarts import DashECharts

def build_clients_chart(df):
    
    moving_avg_raw = df["client_id"].rolling(window=3).mean()
    moving_avg = [round(x, 1) if x == x else None for x in moving_avg_raw]

    periods = df["period"].astype(str).tolist()
    peak_idx = df["client_id"].idxmax()
    peak_month = df.loc[peak_idx, "period"]
    peak_value = df["client_id"].max()
    last_3_avg = round(df["client_id"].tail(3).mean())
    prior_3_avg = round(df["client_id"].iloc[-6:-3].mean())
    trend = round((last_3_avg - prior_3_avg) / prior_3_avg * 100)
    trend_word = "down" if trend < 0 else "up"
    narrative = f"Peak growth was {peak_value} new clients in {peak_month}. The last 3 months averaged {last_3_avg} — {trend_word} {abs(trend)}% vs prior period. The gray line shows the 3-month trend."
    values = df["client_id"].tolist()
    option = {
        "textStyle": config.CHART_BASE["textStyle"],
        "title": {
            "text": "Client Growth",
            "top": 15,
            "left": "center",
            "textStyle": {
                "color": config.COLORS["text"],
                "fontFamily": "JetBrains Mono, monospace"
            }
        },
        "legend": {
            "data": ["New Clients", "Moving Average"],
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
        "xAxis": {
            "type": "category",
            "data": periods,
            "name": "Period",
            "axisLabel": {
                "color": config.COLORS["text"],
                "fontFamily": "JetBrains Mono, monospace"
            },
            "nameTextStyle": {
                "color": config.COLORS["muted"],
                "fontSize": 12,
                "fontFamily": "JetBrains Mono, monospace"

            },
            "nameLocation": "middle",
            "nameGap": 30
        },
        "yAxis": {
            "type": "value",
            "name": "Clients",
            "axisLabel": {
                "color": config.COLORS["text"],
                "fontFamily": "JetBrains Mono, monospace"
            },
            "nameLocation": "middle",
            "nameGap": config.CHART_AXIS["nameGap"],
            "nameTextStyle": config.CHART_AXIS["nameTextStyle"],
            "nameRotate": 90,
            "splitLine": {
            "lineStyle": {
                "type": "dashed",
                "color": config.COLORS["border"]
                }
            }
        },
        "series": [{
            "name": "New Clients",
            "data": values,
            "type": "bar",
            "smooth": True,
            "label": {
                "show": True,
                "position": "top",
                "color": config.COLORS["text"],
                "fontFamily": "JetBrains Mono, monospace"
            },
            "itemStyle": {
                "color": config.COLORS["primary"],
                "fontFamily": "JetBrains Mono, monospace"
            },
            "emphasis": {
                "itemStyle": {
                    "color": "#FFD700"  # brighter amber on hover
                }
            }
        },
        {
            "name": "Moving Average",
            "type": "line",
            "smooth": True,
            "showSymbol": False,
            "data": moving_avg,
            "label": {"show": False},
            "lineStyle": {
                "color": config.COLORS["trend_line"],
                "fontFamily": "JetBrains Mono, monospace",
                "width": 2
                # "type": "dashed"
            },
            "emphasis": {
                "lineStyle": {
                    "width": 4  # thicker line on hover
                }
            }
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