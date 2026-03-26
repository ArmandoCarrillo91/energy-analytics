# Energy Analytics

Business intelligence dashboard for indoor cycling studios.

## Overview
Descriptive analytics platform built with Python, Dash, and Apache ECharts. Provides studio owners with real-time visibility into their business — clients, packages, classes, revenue, and retention.

## Stack
- **Python** — core language
- **Dash** — web framework
- **Apache ECharts** — data visualization
- **PostgreSQL** — database
- **SQLAlchemy** — database connection
- **pandas** — data transformation
- **Vercel** — deployment

## Project Structure
```
energy-analytics/
├── app.py          ← entry point
├── data.py         ← SQL queries
├── layout.py       ← visual components
├── assets/         ← CSS
├── .env            ← credentials (not committed)
├── requirements.txt
└── README.md
```

## Getting Started

1. Clone the repository
```bash
git clone https://github.com/ArmandoCarrillo91/energy-analytics.git
cd energy-analytics
```

2. Create and activate virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Create a `.env` file with your database credentials
```
DB_HOST=your_host
DB_PORT=5432
DB_NAME=your_database
DB_USER=your_user
DB_PASSWORD=your_password
```

4. Run the app
```bash
python3 app.py
```

5. Open your browser at `http://127.0.0.1:8050`

## Roadmap
- [x] Phase 1 — Clients & Packages EDA
- [x] Database connection
- [x] First chart — registered clients over time
- [ ] Phase 2 — Classes & Coaches EDA
- [ ] Full dashboard
- [ ] Vercel deployment