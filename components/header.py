from dash import html
import config

def build_header():
    return html.Div(
        style={
            "background": config.COLORS["card"],
            "borderRadius": "12px",
            "border": f"1px solid {config.COLORS['border']}",
            "padding": "20px 28px",
            "display": "flex",
            "justifyContent": "space-between",
            "alignItems": "center",
            "marginBottom": "24px"
        },
        children=[
            html.Div(
                style={"display": "flex", "flexDirection": "column", "gap": "4px"},
                children=[
                    html.Div(
                        style={"display": "flex", "alignItems": "center", "gap": "10px"},
                        children=[
                            html.Div(style={
                                "width": "8px",
                                "height": "8px",
                                "borderRadius": "50%",
                                "background": config.COLORS["primary"]
                            }),
                            html.Span("ENERGY CYCLE STUDIO", style={
                                "fontSize": "11px",
                                "color": config.COLORS["muted"],
                                "letterSpacing": "0.1em"
                            })
                        ]
                    ),
                    html.H1("Pulso", style={
                        "color": config.COLORS["text"],
                        "fontSize": "28px",
                        "fontWeight": "500",
                        "margin": "0",
                        "lineHeight": "1"
                    }),
                    html.P("Vista ejecutiva del negocio", style={
                        "color": config.COLORS["muted"],
                        "fontSize": "12px",
                        "margin": "0"
                    })
                ]
            ),
            html.Div(
                style={"display": "flex", "flexDirection": "column", "alignItems": "flex-end", "gap": "2px"},
                children=[
                    html.Span("PERIOD", style={
                        "fontSize": "10px",
                        "color": config.COLORS["muted"],
                        "letterSpacing": "0.08em"
                    }),
                    html.Span("Mar 2026", style={
                        "fontSize": "14px",
                        "fontWeight": "500",
                        "color": config.COLORS["text"]
                    })
                ]
            )
        ]
    )