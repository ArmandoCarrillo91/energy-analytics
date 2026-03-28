from dash import html
from dash_echarts import DashECharts
import data
import config
import charts.clients as clients

def get_layout():
    df = data.fetch_clients_packages()
    df_monthly = data.get_clients_per_month(df)
    total = data.count_unique_clients(df)
    kpi_total_clients = html.Div(
        style={
            "background": config.COLORS["card"],
            "padding": "16px 20px",
            "borderRadius": "12px",
            "border": f"1px solid {config.COLORS['border']}",
            "minWidth": "160px",
            "textAlign": "center"
        },
        children=[
            html.P("Total Clients", style={
                "color": config.COLORS["muted"],
                "margin": "0",
                "fontSize": "12px",
                "fontFamily": "'JetBrains Mono', monospace",
                "letterSpacing": "0.1em",
                "textTransform": "uppercase"
            }),
            html.H2(f"{total:,}", style={
                "color": config.COLORS["text"],
                "margin": "0",
                "fontSize": "48px",
                "fontWeight": "700",
                "fontFamily": "'JetBrains Mono', monospace",
                "letterSpacing": "-1px"
            })
        ],
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
            style={
                "height": "400px",
                "width": "100%",
            }
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
                style={"marginBottom": "32px"},
                children=[
                    html.H1("Pulso", style={
                        "color": config.COLORS["text"],
                        "fontSize": "32px",
                        "fontWeight": "700",
                        "fontFamily": "'JetBrains Mono', monospace",
                        "margin": "0"
                    }),
                    html.P("Vista ejecutiva del negocio", style={
                        "color": config.COLORS["muted"],
                        "fontSize": "14px",
                        "fontFamily": "'JetBrains Mono', monospace",
                        "margin": "0"
                    })
                ]
            ),
            # KPIs
            html.Div(
                style={
                    "display": "grid",
                    "gridTemplateColumns": "repeat(auto-fill, minmax(200px, 1fr))",
                    "gap": "16px",
                    "marginBottom": "24px"
                },
                children=[kpi_total_clients]
            ),
            # Charts
            html.Div(
                style={
                    "display": "grid",
                    "gridTemplateColumns": "repeat(auto-fill, minmax(500px, 1fr))",
                    "gap": "16px"
                },
                children=[chart_clients]
            )
        ]
)