from dash import html
import config
import data
from datetime import datetime, timedelta


def build_active_clients_section(df):
    active = data.count_active_clients(df)
    total_classes, avg_classes = data.get_active_classes_stats(df)
    df_forecast = data.get_expiration_forecast(df)
    expiring_this_week = int(df_forecast["expiring"].iloc[0]) if len(df_forecast) > 0 else 0
    pct_expiring = round(expiring_this_week / active * 100) if active > 0 else 0
    next_week = (datetime.now() + timedelta(days=7)).strftime("%b %d")

    kpi_active = html.Div(
        style={
            "background": "#FFFFFF",
            "padding": "24px 20px",
            "borderRadius": "12px",
            "border": f"1px solid {config.COLORS['border']}",
            "display": "flex",
            "flexDirection": "column",
            "justifyContent": "center",
            "alignItems": "center",
            "gap": "4px",
            "textAlign": "center"
        },
        children=[
            html.P("ACTIVE CLIENTS TODAY", style={
                "color": config.COLORS["muted"],
                "margin": "0",
                "fontSize": "10px",
                "letterSpacing": "0.1em"
            }),
            html.H2(f"{active:,}", style={
                "color": config.COLORS["text"],
                "margin": "0",
                "fontSize": "48px",
                "fontWeight": "500",
                "lineHeight": "1"
            }),
            html.P("classes remaining + not expired", style={
                "color": config.COLORS["muted"],
                "margin": "0",
                "fontSize": "11px"
            })
        ]
    )

    kpi_classes = html.Div(
        style={
            "background": "#FFFFFF",
            "padding": "24px 28px",
            "borderRadius": "12px",
            "border": f"1px solid {config.COLORS['border']}",
            "display": "flex",
            "flexDirection": "column",
            "justifyContent": "center"
        },
        children=[
            html.P("CLASSES REMAINING", style={
                "color": config.COLORS["muted"],
                "margin": "0 0 12px 0",
                "fontSize": "10px",
                "letterSpacing": "0.1em"
            }),
            html.Div(
                style={"display": "flex", "alignItems": "flex-end", "gap": "16px", "marginBottom": "12px", "justifyContent": "center"},
                children=[
                    html.Div(children=[
                        html.H3(f"{total_classes:,}", style={
                            "color": config.COLORS["text"],
                            "margin": "0",
                            "fontSize": "36px",
                            "fontWeight": "500"
                        }),
                        html.P("total classes left", style={
                            "color": config.COLORS["muted"],
                            "margin": "0",
                            "fontSize": "10px"
                        })
                    ]),
                    html.P("/", style={
                        "color": config.COLORS["muted"],
                        "fontSize": "11px",
                        "margin": "0 0 8px 0"
                    }),
                    html.Div(children=[
                        html.H3(f"{avg_classes}", style={
                            "color": config.COLORS["text"],
                            "margin": "0",
                            "fontSize": "36px",
                            "fontWeight": "500"
                        }),
                        html.P("avg per client", style={
                            "color": config.COLORS["muted"],
                            "margin": "0",
                            "fontSize": "10px"
                        })
                    ])
                ]
            ),
            html.Div(
                style={"borderTop": f"0.5px solid {config.COLORS['border']}", "paddingTop": "10px"},
                children=[
                    html.P(
                        f"At current pace, the average active client has enough classes for ~{round(avg_classes / 3)} more weeks.",
                        style={
                            "color": config.COLORS["muted"],
                            "margin": "0",
                            "fontSize": "11px",
                            "fontStyle": "italic",
                            "lineHeight": "1.5"
                        }
                    )
                ]
            )
        ]
    )

    kpi_expiring = html.Div(
        style={
            "background": "#FFFDF5",
            "padding": "24px 28px",
            "borderRadius": "12px",
            "border": f"2px solid {config.COLORS['primary']}",
            "display": "flex",
            "flexDirection": "column",
            "justifyContent": "center"
        },
        children=[
            html.P("EXPIRING THIS WEEK", style={
                "color": config.COLORS["primary"],
                "margin": "0 0 12px 0",
                "fontSize": "10px",
                "letterSpacing": "0.1em"
            }),
            html.Div(
                style={"display": "flex", "alignItems": "flex-end", "gap": "16px", "marginBottom": "12px", "justifyContent": "center"},
                children=[
                    html.Div(children=[
                        html.H3(f"{expiring_this_week}", style={
                            "color": config.COLORS["primary"],
                            "margin": "0",
                            "fontSize": "36px",
                            "fontWeight": "500"
                        }),
                        html.P("clients expiring", style={
                            "color": config.COLORS["muted"],
                            "margin": "0",
                            "fontSize": "10px"
                        })
                    ]),
                    html.P("/", style={
                        "color": config.COLORS["muted"],
                        "fontSize": "11px",
                        "margin": "0 0 8px 0"
                    }),
                    html.Div(children=[
                        html.H3(f"{pct_expiring}%", style={
                            "color": config.COLORS["text"],
                            "margin": "0",
                            "fontSize": "36px",
                            "fontWeight": "500"
                        }),
                        html.P("of active base", style={
                            "color": config.COLORS["muted"],
                            "margin": "0",
                            "fontSize": "10px"
                        })
                    ])
                ]
            ),
            html.Div(
                style={"borderTop": f"0.5px solid {config.COLORS['border']}", "paddingTop": "10px"},
                children=[
                    html.P(
                        f"These are your most urgent renewals. Reach out before {next_week}.",
                        style={
                            "color": config.COLORS["muted"],
                            "margin": "0",
                            "fontSize": "11px",
                            "fontStyle": "italic",
                            "lineHeight": "1.5"
                        }
                    )
                ]
            )
        ]
    )

    return html.Div(
        style={
            "display": "grid",
            "gridTemplateColumns": "1fr 2fr 2fr",
            "gap": "16px",
            "marginBottom": "16px"
        },
        children=[kpi_active, kpi_classes, kpi_expiring]
    )