# Energy Analytics

Dashboard de analytics para Energy Cycle Studio — Colima, México.

## ¿Qué es esto?
Plataforma de análisis descriptivo construida en Python con Dash y Apache ECharts. Permite a Juan, dueño de Energy, monitorear el estado de su negocio en tiempo real.

## Stack
- **Python** — lenguaje principal
- **Dash** — framework web
- **Apache ECharts** — visualizaciones
- **PostgreSQL** — base de datos
- **SQLAlchemy** — conexión a BD
- **pandas** — transformación de datos
- **Vercel** — deploy

## Estructura
```
energy-analytics/
├── app.py          ← entry point
├── data.py         ← queries SQL
├── layout.py       ← componentes visuales
├── assets/         ← CSS
├── .env            ← credenciales (no se sube)
├── requirements.txt
└── README.md
```

## Cómo correr el proyecto

1. Clona el repo
```bash
git clone https://github.com/ArmandoCarrillo91/energy-analytics.git
cd energy-analytics
```

2. Crea el ambiente virtual
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Crea tu archivo `.env` con las credenciales
```
DB_HOST=tu_host
DB_PORT=5432
DB_NAME=tu_database
DB_USER=tu_usuario
DB_PASSWORD=tu_password
```

4. Corre el proyecto
```bash
python3 app.py
```

5. Abre tu browser en `http://127.0.0.1:8050`

## Estado del proyecto
- [x] Fase 1 — EDA Clientes y Paquetes
- [x] Conexión a BD
- [x] Primer chart — clientes por mes
- [ ] Fase 2 — EDA Clases y Coaches
- [ ] Dashboard completo
- [ ] Deploy en Vercel