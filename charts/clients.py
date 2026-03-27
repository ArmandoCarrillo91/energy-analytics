import config

def build_clients_chart(df):
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
        }]
    }
    return option