import config

def build_revenue_chart(df):
    
    periods = df["period"].astype(str).tolist()
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
                "itemStyle": {"color": config.COLORS["primary"]}
            }
        ]
    }
    return option