from dash import html
import config
import data


def build_insight(df):
    clients_without_package = data.count_clients_without_package(df)
    ticket_avg = data.avg_ticket(df)
    potential = round(clients_without_package * ticket_avg * 0.1)

    return html.Div(
        style={
            "background": "#1A1A1A",
            "borderRadius": "12px",
            "padding": "16px 24px",
            "display": "flex",
            "alignItems": "center",
            "gap": "12px",
            "marginTop": "0",
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
                children=[
                    html.Span(f"{clients_without_package:,} clients", style={"color": config.COLORS["primary"], "fontWeight": "500"}),
                    html.Span(" never purchased. At "),
                    html.Span(f"${ticket_avg:,.0f}", style={"color": config.COLORS["primary"], "fontWeight": "500"}),
                    html.Span(" avg ticket, recovering 10% represents ~"),
                    html.Span(f"${potential:,}", style={"color": config.COLORS["primary"], "fontWeight": "500"}),
                    html.Span(" in potential revenue."),
                ],
                style={
                    "color": "rgba(255,255,255,0.7)",
                    "margin": "0",
                    "fontSize": "12px",
                    "lineHeight": "1.5"
                }
            )
        ]
    )