# Energy Cycle Studio · Analytics

Internal analytics platform for Energy Cycle Studio, Colima MX.  
Streamlit + PostgreSQL · runs locally · live data.

---

## Stack

- [Streamlit](https://streamlit.io/) — data app framework  
- [PostgreSQL](https://www.postgresql.org/) — production database via Strapi  
- [Plotly](https://plotly.com/python/) — interactive charts  
- [Pandas](https://pandas.pydata.org/) — data manipulation  

---

## Setup
```bash
git clone https://github.com/tu-usuario/energy-analytics.git
cd energy-analytics
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
streamlit run app.py
```

---

## Analysis pages

| Page | Question |
|------|----------|
| Weekly Occupancy | Which time slots fill on their own? |

---

## Notes

- `.env` is gitignored — never commit credentials  
- All data is read-only — no writes from this app