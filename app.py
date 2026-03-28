import dash
from dash import Input, Output, State, html
from dotenv import load_dotenv
from cache import cache
import layout
import auth

load_dotenv()

app = dash.Dash(
    __name__,
    title="Energy",
    suppress_callback_exceptions=True,  # ← necesario para multi-página
    external_stylesheets=[
        "https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap"
    ]
)

cache.init_app(app.server, config={
    'CACHE_TYPE': 'SimpleCache',
    'CACHE_DEFAULT_TIMEOUT': 1300
})

# Layout raíz — decide qué mostrar según sesión
from dash import dcc
app.layout = html.Div([
    dcc.Location(id="url", refresh=False),
    dcc.Store(id="session-store", storage_type="session"),
    html.Div(id="login-error", style={"display": "none"}),  # ← siempre presente
    html.Div(id="page-content")
])

# Callback: login
@app.callback(
    Output("session-store", "data"),
    Output("login-error", "children"),
    Input("login-button", "n_clicks"),
    State("login-email", "value"),
    State("login-password", "value"),
    prevent_initial_call=True
)
def handle_login(n_clicks, email, password):
    if not email or not password:
        return None, "Ingresa tu email y contraseña"
    
    user, error = auth.login_user(email, password)
    
    if error:
        return None, "Credenciales incorrectas"
    
    has_access = auth.check_tenant_access(str(user.id))
    
    if not has_access:
        return None, "No tienes acceso a este dashboard"
    
    # Guardamos el user_id en la sesión del browser
    return {"user_id": str(user.id), "email": user.email}, ""

# Callback: routing — decide qué página mostrar
@app.callback(
    Output("page-content", "children"),
    Input("session-store", "data")
)
def route(session):
    from pages.login import build_login_layout
    
    if not session or "user_id" not in session:
        return build_login_layout()
    
    return layout.get_layout()

if __name__ == "__main__":
    app.run(debug=True)