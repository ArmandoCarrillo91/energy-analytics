from dash import html, dcc, Input, Output, State, callback
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
                    "maxWidth": "400px",
                },
                children=[
                    # Header
                    html.Div("⚡", style={"fontSize": "32px", "marginBottom": "8px"}),
                    html.H2(
                        "Energy Cycle Studio",
                        style={
                            "color": config.COLORS["primary"],
                            "fontSize": "20px",
                            "fontWeight": "700",
                            "marginBottom": "4px"
                        }
                    ),
                    html.P(
                        "Dashboard de Analytics",
                        style={
                            "color": config.COLORS["muted"],
                            "fontSize": "13px",
                            "marginBottom": "32px"
                        }
                    ),

                    # Email
                    html.Label(
                        "Email",
                        style={"fontSize": "12px", "color": config.COLORS["muted"], "marginBottom": "6px", "display": "block"}
                    ),
                    dcc.Input(
                        id="login-email",
                        type="email",
                        placeholder="juan@energy.com",
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
                            "boxSizing": "border-box"
                        }
                    ),

                    # Password
                    html.Label(
                        "Contraseña",
                        style={"fontSize": "12px", "color": config.COLORS["muted"], "marginBottom": "6px", "display": "block"}
                    ),
                    dcc.Input(
                        id="login-password",
                        type="password",
                        placeholder="••••••••",
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
                            "boxSizing": "border-box"
                        }
                    ),

                    # Botón
                    html.Button(
                        "Entrar",
                        id="login-button",
                        style={
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
                        }
                    ),

                    # Error message
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