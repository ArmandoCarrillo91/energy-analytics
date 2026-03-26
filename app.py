import dash
from dotenv import load_dotenv
import layout

load_dotenv()

app = dash.Dash(__name__)
app.layout = layout.get_layout()

if __name__ == "__main__":
    app.run(debug=True)