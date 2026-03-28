import config

def build_clients_chart(df):
    
    moving_avg_raw = df["client_id"].rolling(window=3).mean()
    moving_avg = [round(x, 1) if x == x else None for x in moving_avg_raw]

    periods = df["period"].astype(str).tolist()
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
            "nameGap": 40,
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
            }
        }
        ]
    }
    return option