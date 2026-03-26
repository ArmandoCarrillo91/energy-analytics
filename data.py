import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

def get_engine():
    return create_engine(
        f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
        f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    )

def run_query(sql):
    return pd.read_sql(sql, get_engine())

def get_clientes_por_mes():
    return run_query("""
        SELECT DATE_TRUNC('month', created_at) AS mes,
               COUNT(id) AS nuevos
        FROM clients
        GROUP BY 1
        ORDER BY 1
    """)

def get_total_clientes():
    return run_query("SELECT COUNT(id) as total FROM clients")