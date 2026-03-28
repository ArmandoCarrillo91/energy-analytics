import config

def build_revenue_chart(df):
    
    periods = df["period"].astype(str).tolist()
    data = []
    for v in df["package_sold"].tolist():
        real = round(v)
        k = round(v / 1000, 1)
        formatted = f"{real:,}"
        data.append({
            "value": real,
            "label": {
                "formatter": f"${k}K"
            },
            "tooltip": {
                "formatter": f"${formatted}"
            }
        })

    option = {
        "textStyle": config.CHART_BASE["textStyle"],
        "title": {
            "text": "Monthly Revenue",
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
            "nameGap": 60,
            "nameRotate": 90,
            "axisLabel": {
            "color": config.COLORS["text"],
            "fontFamily": "JetBrains Mono, monospace",
            "formatter": "${value}K"
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
                "label": {
                    "show": True,
                    "position": "top",
                    "color": config.COLORS["text"],
                    "fontSize": 10,
                    "formatter": "${c}K"
                },
                "itemStyle": {"color": config.COLORS["primary"]}
            }
        ]
    }
    return option