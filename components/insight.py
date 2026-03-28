from dash import html
import config
import data


def build_insight(df):
    clients_without_package = data.count_clients_without_package(df)
    ticket_avg = data.avg_ticket(df)
    potential = round(clients_without_package * ticket_avg * 0.1)

    return html.Div(
        style={
            "background": config.COLORS["card"],
            "borderRadius": "8px",
            "padding": "12px 20px",
            "display": "flex",
            "alignItems": "center",
            "gap": "8px",
            "marginTop": "12px",
            "border": f"0.5px solid {config.COLORS['border']}"
        },
        children=[
            html.Div(style={
                "width": "6px",
                "height": "6px",
                "borderRadius": "50%",
                "background": "#E24B4A",
                "flexShrink": "0"
            }),
            html.P(
                f"{clients_without_package:,} clients never purchased. At ${ticket_avg:,.0f} avg ticket, recovering 10% represents ~${potential:,} in potential revenue.",
                style={
                    "color": config.COLORS["muted"],
                    "margin": "0",
                    "fontSize": "11px"
                }
            )
        ]
    )