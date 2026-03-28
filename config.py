STUDIO_NAME = "Energy"

COLORS = {
    "background": "#FFFAFA",  # main background — off white
    "card":       "#FAFAFA",  # chart and card background
    "border":     "#E0E0E0",  # subtle borders
    "primary":    "#FFBF00",  # amber — main color
    "secondary":  "#363636",  # dark gray — secondary elements
    "danger":     "#F87171",  # red — negative metrics
    "text":       "#2E3133",  # main text — dark
    "muted":      "#7A7A7A",  # secondary text — gray
    "trend_line":   "#AAAAAA",  # moving average line — subtle gray
    "trend_point":  "#888888",  # moving average points — medium gray
}

CHART_BASE = {
    "backgroundColor": COLORS["background"],
    "textStyle": {
        "color": COLORS["text"],
        "fontFamily": "JetBrains Mono, monospace"
    }
}