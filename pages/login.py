from dash import html, dcc
import config

def build_login_layout():
    return html.Div(
        style={
            "background": config.COLORS["background"],
            "minHeight": "100vh",
            "display": "flex",
            "alignItems": "center",
            "justifyContent": "center",
            "fontFamily": "JetBrains Mono, monospace"
        },
        children=[
            html.Div(
                style={
                    "background": config.COLORS["card"],
                    "border": f"1px solid {config.COLORS['border']}",
                    "borderRadius": "12px",
                    "padding": "48px 40px",
                    "width": "100%",
                    "maxWidth": "420px",
                },
                children=[
                    html.Div("⚡", style={"fontSize": "32px", "marginBottom": "8px"}),
                    html.H2("Energy Cycle Studio", style={
                        "color": config.COLORS["primary"],
                        "fontSize": "20px",
                        "fontWeight": "700",
                        "marginBottom": "4px"
                    }),
                    html.P("Dashboard de Analytics", style={
                        "color": config.COLORS["muted"],
                        "fontSize": "13px",
                        "marginBottom": "32px"
                    }),
                    html.Label("Email", style={"fontSize": "12px", "color": config.COLORS["muted"], "marginBottom": "6px", "display": "block"}),
                    dcc.Input(
                        id="login-email",
                        type="email",
                        placeholder="correo@ejemplo.com",
                        n_submit=0,
                        debounce=False,
                        style={
                            "width": "100%",
                            "padding": "10px 14px",
                            "borderRadius": "8px",
                            "border": f"1px solid {config.COLORS['border']}",
                            "background": config.COLORS["background"],
                            "color": config.COLORS["text"],
                            "fontFamily": "JetBrains Mono, monospace",
                            "fontSize": "14px",
                            "marginBottom": "16px",
                        }
                    ),
                    html.Label("Contraseña", style={"fontSize": "12px", "color": config.COLORS["muted"], "marginBottom": "6px", "display": "block"}),
                    dcc.Input(
                        id="login-password",
                        type="password",
                        placeholder="••••••••",
                        n_submit=0,
                        debounce=False,
                        style={
                            "width": "100%",
                            "padding": "10px 14px",
                            "borderRadius": "8px",
                            "border": f"1px solid {config.COLORS['border']}",
                            "background": config.COLORS["background"],
                            "color": config.COLORS["text"],
                            "fontFamily": "JetBrains Mono, monospace",
                            "fontSize": "14px",
                            "marginBottom": "24px",
                        }
                    ),
                    html.Button("Entrar", id="login-button", style={
                        "width": "100%",
                        "padding": "12px",
                        "background": config.COLORS["primary"],
                        "color": "#000",
                        "border": "none",
                        "borderRadius": "8px",
                        "fontFamily": "JetBrains Mono, monospace",
                        "fontSize": "14px",
                        "fontWeight": "700",
                        "cursor": "pointer",
                        "marginBottom": "16px"
                    }),
                    html.Div(id="login-error", style={
                        "color": config.COLORS["danger"],
                        "fontSize": "13px",
                        "textAlign": "center",
                        "minHeight": "20px"
                    }),
                ]
            )
        ]
    )