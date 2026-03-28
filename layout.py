from dash import html
from dash_echarts import DashECharts
import data
import config
import charts.clients as clients
import charts.packages as packages

def get_layout():

    df = data.fetch_clients_packages()
    df_monthly = data.get_clients_per_month(df)
    df_packages = data.get_packages_per_month(df)
    total = data.count_unique_clients(df)
    clients_with_packages = data.count_clients_with_packages(df)
    clients_without_package = data.count_clients_without_package(df)
    total_packages = data.count_total_packages(df)
    gifted_packages = data.count_gifted_packages(df)
    sold_packages = data.count_sold_packages(df)

    # Calculations for KPIs
    conversion_rate = round(clients_with_packages / total * 100)
    packages_sold_rate = round(sold_packages / total_packages * 100)

    kpi_universe = html.Div(
        style={
            "background": config.COLORS["card"],
            "padding": "16px 20px",
            "borderRadius": "12px",
            "border": f"1px solid {config.COLORS['border']}",
            "textAlign": "center",
            "display": "flex",
            "flexDirection": "column",
            "justifyContent": "center"
        },
        children=[
            html.P("Total Clients", style={
                "color": config.COLORS["muted"],
                "margin": "0",
                "fontSize": "10px",
                "letterSpacing": "0.08em"
            }),
            html.H2(f"{total:,}", style={
                "color": config.COLORS["text"],
                "margin": "6px 0",
                "fontSize": "40px",
                "fontWeight": "500",
                "letterSpacing": "-1px"
            }),
            html.P("registered", style={
                "color": config.COLORS["muted"],
                "margin": "0",
                "fontSize": "11px"
            })
        ]
    )

    kpi_conversion = html.Div(
        style={
            "background": config.COLORS["card"],
            "padding": "16px 20px",
            "borderRadius": "12px",
            "border": f"1px solid {config.COLORS['border']}",
            "textAlign": "center"
        },
        children=[
            html.P("Conversion", style={
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
            html.P(f"{conversion_rate}% conversion rate", style={
                "color": config.COLORS["muted"],
                "margin": "4px 0 0 0",
                "fontSize": "10px"
            })
        ]
    )

    kpi_packages = html.Div(
        style={
            "background": config.COLORS["card"],
            "padding": "16px 20px",
            "borderRadius": "12px",
            "border": f"1px solid {config.COLORS['border']}",
            "textAlign": "center"
        },
        children=[
            html.P(f"Packages — {total_packages:,} total", style={
                "color": config.COLORS["muted"],
                "textAlign": "center",
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
                            "fontSize": "10px",

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
            html.P(f"{packages_sold_rate}% packages with revenue", style={
                "color": config.COLORS["muted"],
                "margin": "4px 0 0 0",
                "fontSize": "10px"
            })
        ]
    )

    chart_clients = html.Div(
        style={
            "borderRadius": "12px",
            "border": f"1px solid {config.COLORS['border']}",
            "overflow": "hidden",
            "background": config.COLORS["card"]
        },
        children=[
            DashECharts(
                option=clients.build_clients_chart(df_monthly),
                style={"height": "400px", "width": "100%"}
            )
        ]
    )

    chart_packages = html.Div(
        style={
            "borderRadius": "12px",
            "border": f"1px solid {config.COLORS['border']}",
            "overflow": "hidden",
            "background": config.COLORS["card"]
        },
        children=[
            DashECharts(
                option=packages.build_packages_chart(df_packages),
                style={"height": "400px", "width": "100%"}
            )
        ]
    )

    return html.Div(
        style={
            "background": config.COLORS["background"],
            "padding": "32px 40px",
            "minHeight": "100vh"
        },
        children=[
            # Header
html.Div(
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
),
            # KPIs
            html.Div(
                style={
                    "display": "grid",
                    "gridTemplateColumns": "1fr 2fr 2fr",
                    "gap": "16px",
                    "marginBottom": "24px"
                },
                children=[kpi_universe, kpi_conversion, kpi_packages]
            ),
            # Charts
            html.Div(
                style={
                    "display": "grid",
                    "gridTemplateColumns": "repeat(auto-fill, minmax(500px, 1fr))",
                    "gap": "16px"
                },
                children=[chart_clients, chart_packages]
            )
        ]
    )