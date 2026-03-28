import dash
from dotenv import load_dotenv
from cache import cache
import layout

load_dotenv()

app = dash.Dash(
    __name__,
    title="Energy",
    external_stylesheets=[
        "https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap"
    ]
)

cache.init_app(app.server, config={   # ← init_app en vez de Cache()
    'CACHE_TYPE': 'SimpleCache',
    'CACHE_DEFAULT_TIMEOUT': 1300
})

app.layout = layout.get_layout()

if __name__ == "__main__":
    app.run(debug=True)