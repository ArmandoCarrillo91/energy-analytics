import config

def build_clients_chart(df):
    
    moving_avg_raw = df["client_id"].rolling(window=3).mean()
    moving_avg = [round(x, 1) if x == x else None for x in moving_avg_raw]

    periods = df["period"].astype(str).tolist()
    values = df["client_id"].tolist()
    option = {
        "title": {
            "text": "New Clients Over Time",
            "left": "center",
            "textStyle": {
                "color": config.COLORS["text"]
            }
        },
        "xAxis": {
            "type": "category",
            "data": periods,
            "name": "Period",
            "axisLabel": {
                "color": config.COLORS["text"]
            }
        },
        "yAxis": {
            "type": "value",
            "name": "Clients",
            "axisLabel": {
                "color": config.COLORS["text"]
            }

        },
        "series": [{
            "data": values,
            "type": "line",
            "smooth": True,
            "label": {
                "show": True,
                "position": "top",
                "color": config.COLORS["text"]
            },
            "lineStyle": {
                "color": config.COLORS["primary"]
            }
        },
        {
            "name": "Moving Average",
            "type": "line",
            "smooth": True,
            "data": moving_avg,
            "label": {"show": False},
            "lineStyle": {
                "color": config.COLORS["secondary"],
                "type": "dashed"
            }
        }
        ]
    }
    return option