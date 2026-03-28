from dash import html
import config
import data


def build_kpi_revenue(df):
    revenue = data.total_revenue(df)
    revenue_month = data.revenue_this_month(df)
    ticket_avg = data.avg_ticket(df)

    return html.Div(
        style={
            "background": config.COLORS["card"],
            "padding": "20px",
            "borderRadius": "12px",
            "border": f"2px solid {config.COLORS['primary']}",
        },
        children=[
            html.P("TOTAL REVENUE", style={
                "color": config.COLORS["muted"],
                "margin": "0 0 8px 0",
                "fontSize": "10px",
                "letterSpacing": "0.1em"
            }),
            html.H2(f"${revenue:,.0f}", style={
                "color": config.COLORS["text"],
                "margin": "0",
                "fontSize": "36px",
                "fontWeight": "500",
                "letterSpacing": "-1px",
                "lineHeight": "1"
            }),
            html.P("all time", style={
                "color": config.COLORS["muted"],
                "margin": "4px 0 14px 0",
                "fontSize": "11px"
            }),
            html.Div(
                style={
                    "borderTop": f"0.5px solid {config.COLORS['border']}",
                    "paddingTop": "12px",
                    "display": "grid",
                    "gridTemplateColumns": "1fr 1fr",
                    "gap": "8px"
                },
                children=[
                    html.Div(children=[
                        html.P("THIS MONTH", style={
                            "color": config.COLORS["muted"],
                            "margin": "0",
                            "fontSize": "10px",
                            "letterSpacing": "0.08em"
                        }),
                        html.P(f"${revenue_month:,.0f}", style={
                            "color": config.COLORS["text"],
                            "margin": "2px 0 0 0",
                            "fontSize": "16px",
                            "fontWeight": "500"
                        })
                    ]),
                    html.Div(children=[
                        html.P("AVG TICKET", style={
                            "color": config.COLORS["muted"],
                            "margin": "0",
                            "fontSize": "10px",
                            "letterSpacing": "0.08em"
                        }),
                        html.P(f"${ticket_avg:,.0f}", style={
                            "color": config.COLORS["text"],
                            "margin": "2px 0 0 0",
                            "fontSize": "16px",
                            "fontWeight": "500"
                        })
                    ])
                ]
            )
        ]
    )


def build_kpi_conversion(df):
    total = data.count_unique_clients(df)
    clients_with_packages = data.count_clients_with_packages(df)
    clients_without_package = data.count_clients_without_package(df)
    conversion_rate = round(clients_with_packages / total * 100)

    return html.Div(
        style={
            "background": config.COLORS["card"],
            "padding": "16px 20px",
            "borderRadius": "12px",
            "border": f"1px solid {config.COLORS['border']}",
            "display": "flex",
            "flexDirection": "column",
            "justifyContent": "space-between",
            "textAlign": "center"
        },
        children=[
            html.P(f"CONVERSION — {total:,} clients", style={
                "color": config.COLORS["muted"],
                "margin": "0 0 12px 0",
                "fontSize": "10px",
                "letterSpacing": "0.08em"
            }),
            html.Div(
                style={"display": "flex", "gap": "12px", "alignItems": "flex-end", "marginBottom": "8px", "justifyContent": "center"},
                children=[
                    html.Div(children=[
                        html.H3(f"{clients_with_packages:,}", style={
                            "color": config.COLORS["text"],
                            "margin": "0",
                            "fontSize": "24px",
                            "fontWeight": "500"
                        }),
                        html.P("purchased", style={
                            "color": config.COLORS["muted"],
                            "margin": "0",
                            "fontSize": "10px"
                        })
                    ]),
                    html.P("vs", style={
                        "color": config.COLORS["muted"],
                        "fontSize": "11px",
                        "margin": "0 0 4px 0"
                    }),
                    html.Div(children=[
                        html.H3(f"{clients_without_package:,}", style={
                            "color": "#E24B4A",
                            "margin": "0",
                            "fontSize": "24px",
                            "fontWeight": "500"
                        }),
                        html.P("never purchased", style={
                            "color": config.COLORS["muted"],
                            "margin": "0",
                            "fontSize": "10px"
                        })
                    ])
                ]
            ),
            html.Div(
                style={
                    "background": config.COLORS["background"],
                    "borderRadius": "4px",
                    "height": "6px",
                    "overflow": "hidden",
                    "border": f"0.5px solid {config.COLORS['border']}"
                },
                children=[
                    html.Div(style={
                        "background": config.COLORS["primary"],
                        "height": "100%",
                        "width": f"{conversion_rate}%"
                    })
                ]
            ),
            html.Div(
                style={"display": "flex", "justifyContent": "space-between", "marginTop": "4px"},
                children=[
                    html.P(f"{conversion_rate}% conversion rate", style={
                        "color": config.COLORS["muted"],
                        "margin": "0",
                        "fontSize": "10px"
                    }),
                    html.P(f"{100 - conversion_rate}% opportunity", style={
                        "color": "#E24B4A",
                        "margin": "0",
                        "fontSize": "10px"
                    })
                ]
            )
        ]
    )


def build_kpi_packages(df):
    total_packages = data.count_total_packages(df)
    gifted_packages = data.count_gifted_packages(df)
    sold_packages = data.count_sold_packages(df)
    packages_sold_rate = round(sold_packages / total_packages * 100)

    return html.Div(
        style={
            "background": config.COLORS["card"],
            "padding": "16px 20px",
            "borderRadius": "12px",
            "border": f"1px solid {config.COLORS['border']}",
            "display": "flex",
            "flexDirection": "column",
            "justifyContent": "space-between",
            "textAlign": "center"
        },
        children=[
            html.P(f"PACKAGES — {total_packages:,} total", style={
                "color": config.COLORS["muted"],
                "margin": "0 0 12px 0",
                "fontSize": "10px",
                "letterSpacing": "0.08em"
            }),
            html.Div(
                style={"display": "flex", "gap": "12px", "alignItems": "flex-end", "marginBottom": "8px", "justifyContent": "center"},
                children=[
                    html.Div(children=[
                        html.H3(f"{sold_packages:,}", style={
                            "color": config.COLORS["text"],
                            "margin": "0",
                            "fontSize": "24px",
                            "fontWeight": "500"
                        }),
                        html.P("sold", style={
                            "color": config.COLORS["muted"],
                            "margin": "0",
                            "fontSize": "10px"
                        })
                    ]),
                    html.P("vs", style={
                        "color": config.COLORS["muted"],
                        "fontSize": "11px",
                        "margin": "0 0 4px 0"
                    }),
                    html.Div(children=[
                        html.H3(f"{gifted_packages:,}", style={
                            "color": config.COLORS["muted"],
                            "margin": "0",
                            "fontSize": "24px",
                            "fontWeight": "500"
                        }),
                        html.P("gifted", style={
                            "color": config.COLORS["muted"],
                            "margin": "0",
                            "fontSize": "10px"
                        })
                    ])
                ]
            ),
            html.Div(
                style={
                    "background": config.COLORS["background"],
                    "borderRadius": "4px",
                    "height": "6px",
                    "overflow": "hidden",
                    "border": f"0.5px solid {config.COLORS['border']}"
                },
                children=[
                    html.Div(style={
                        "background": config.COLORS["primary"],
                        "height": "100%",
                        "width": f"{packages_sold_rate}%"
                    })
                ]
            ),
            html.Div(
                style={"display": "flex", "justifyContent": "space-between", "marginTop": "4px"},
                children=[
                    html.P(f"{packages_sold_rate}% packages with revenue", style={
                        "color": config.COLORS["muted"],
                        "margin": "0",
                        "fontSize": "10px"
                    }),
                    html.P(f"{100 - packages_sold_rate}% free", style={
                        "color": config.COLORS["muted"],
                        "margin": "0",
                        "fontSize": "10px"
                    })
                ]
            )
        ]
    )


def build_kpis(df):
    return html.Div(
        style={
            "display": "grid",
            "gridTemplateColumns": "1fr 2fr 2fr",
            "gap": "16px",
            "marginBottom": "24px"
        },
        children=[
            build_kpi_revenue(df),
            build_kpi_conversion(df),
            build_kpi_packages(df)
        ]
    )