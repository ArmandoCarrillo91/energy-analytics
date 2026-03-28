from dash import html, dcc

def build_login_layout():
    return html.Div(className="login-root", children=[
        html.Div(className="login-container", children=[

            # Logo
            html.Div(className="login-logo", children=[
                html.Img(
                    src="/assets/logo-aa.svg",
                    style={"display": "block", "margin": "0 auto 24px", "width": "72px", "height": "72px"}
                ),
                html.Div("armandoanalytics", className="login-logo-text")
            ]),

            # Email
            html.Div(className="login-field-email", children=[
                html.Label("Email", className="login-label"),
                dcc.Input(
                    id="login-email",
                    type="email",
                    placeholder="correo@empresa.com",
                    n_submit=0,
                    debounce=False,
                    className="login-input"
                ),
            ]),

            # Password
            html.Div(children=[
                html.Label("Password", className="login-label"),
                dcc.Input(
                    id="login-password",
                    type="password",
                    placeholder="••••••••",
                    n_submit=0,
                    debounce=False,
                    className="login-input"
                ),
            ]),

            # Error
            html.Div(id="login-error", className="login-error"),

            # Botón
            html.Button("Sign in", id="login-button", className="login-button"),

            # Footer
            html.Div(
                "Internal system · Access by invitation only.",
                className="login-footer"
            )
        ])
    ])