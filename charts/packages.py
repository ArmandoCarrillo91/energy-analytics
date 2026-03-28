import config

def build_packages_chart(df):
    periods = df["period"].astype(str).tolist()
    values = df["package_id"].tolist()
    moving_avg_raw = df["package_id"].rolling(window=3).mean()
    moving_avg = [round(x, 1) if x == x else None for x in moving_avg_raw]
    
    option = {
        "textStyle": config.CHART_BASE["textStyle"],
        "title": {
            "text": "Package Volume",
            "left": "center",
            "top": 10,
            "textStyle": {
                "color": config.COLORS["text"]
            }
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
            "data": ["Packages", "Moving Average"],
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
                "fontSize": 12,
                "fontFamily": "JetBrains Mono, monospace"
            }
        },
        "yAxis": {
            "type": "value",
            "name": "Packages",
            "nameLocation": "middle",
            "nameGap": 40,
            "nameRotate": 90,
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
                "name": "Packages",
                "data": values,
                "type": "bar",
                "label": {
                    "show": True,
                    "position": "top",
                    "color": config.COLORS["text"]
                },
                "itemStyle": {
                    "color": config.COLORS["primary"]
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
                    "width": 2
                }
            }
        ]
    }
    return option