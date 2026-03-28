import dash
from dotenv import load_dotenv
import layout

load_dotenv()

app = dash.Dash(
    __name__,
    title="Energy",
    external_stylesheets=[
                "https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap"
        ]
    )
app.layout = layout.get_layout()

if __name__ == "__main__":
    app.run(debug=True)