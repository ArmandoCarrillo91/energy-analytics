import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from pandas import read_sql
import pandas as pd
from datetime import datetime
from cache import cache

load_dotenv()

engine = create_engine(f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}")

@cache.memoize(timeout=86400)
def fetch_clients_packages():
    sql = """
            SELECT * FROM mv_clients_packages
        """
    df = read_sql(sql, engine)
    return df
    
def count_unique_clients(df):
    return df["client_id"].nunique()

def get_clients_per_month(df):
    df_work = df.copy()
    df_work["c_created_at"] = df_work["c_created_at"].dt.tz_localize(None)
    df_work["period"] = df_work["c_created_at"].dt.to_period("M")
    result = df_work.groupby("period")["client_id"].nunique().reset_index()
    return result

def get_packages_per_month(df):
    df_work = df.copy()
    df_work = df_work[df_work["package_id"].notna()]
    df_work["p_created_at"] = df_work["p_created_at"].dt.tz_localize(None)
    df_work["period"] = df_work["p_created_at"].dt.to_period("M")
    result = df_work.groupby("period")["package_id"].nunique().reset_index()
    return result

def count_clients_with_packages(df):
    df_work = df[df["package_id"].notna()]
    return df_work["client_id"].nunique()

def count_clients_without_package(df):
    df_work = df[df["package_id"].isna()]
    return df_work["client_id"].nunique()

def count_total_packages(df):
    df_work = df[df["package_id"].notna()]
    return df["package_id"].nunique()

def count_gifted_packages(df):
    df_work = df[
        (df["package_sold"] == 0) | (df["package_sold"].isna())
    ]
    return df_work["package_id"].nunique()

def count_sold_packages(df):
    df_work = df[df["package_sold"] > 0]
    return df_work["package_id"].nunique()  

def total_revenue(df):
    return df["package_sold"].sum()

def revenue_this_month(df):
    df_work = df[df["package_sold"].notna()].copy()
    df_work["p_created_at"] = df_work["p_created_at"].dt.tz_localize(None)
    current_month = df_work["p_created_at"].dt.to_period("M").max()
    df_work = df_work[df_work["p_created_at"].dt.to_period("M") == current_month]
    return df_work["package_sold"].sum()

def avg_ticket(df):
    df_work = df[df["package_sold"] > 0]
    return round(df_work["package_sold"].mean(), 2)

def get_revenue_per_month(df):
    df_work = df[df["package_sold"].notna()].copy()
    df_work["p_created_at"] = df_work["p_created_at"].dt.tz_localize(None)
    df_work["period"] = df_work["p_created_at"].dt.to_period("M")
    result = df_work.groupby("period")["package_sold"].sum().reset_index()
    return result

def get_expiration_forecast(df):
    df_work = df[df["package_id"].notna()].copy()
    df_work["expiration_date"] = pd.to_datetime(
        df_work["expiration_date"]
    ).dt.tz_localize(None)

    today = datetime.now()

    df_active = df_work[
        (df_work["expiration_date"] > today) &
        (df_work["remaining_classes"] > 0)
    ].copy()

    df_active["week"] = df_active["expiration_date"].dt.to_period("W")

    result = df_active.groupby("week")["client_id"].nunique().reset_index()
    result.columns = ["week", "expiring"]
    result["week"] = result["week"].apply(
        lambda p: p.end_time.strftime("%b %d")
        )

    total = result["expiring"].sum()
    result["remaining"] = total - result["expiring"].cumsum() + result["expiring"]

    return result

def count_active_clients(df):
    from datetime import datetime
    import pandas as pd
    df_work = df[df["package_id"].notna()].copy()
    df_work["expiration_date"] = pd.to_datetime(
        df_work["expiration_date"]
    ).dt.tz_localize(None)
    today = datetime.now()
    active = df_work[
        (df_work["remaining_classes"] > 0) &
        (df_work["expiration_date"] > today)
    ]
    return active["client_id"].nunique()

def get_active_classes_stats(df):
    from datetime import datetime
    import pandas as pd
    df_work = df[df["package_id"].notna()].copy()
    df_work["expiration_date"] = pd.to_datetime(
        df_work["expiration_date"]
    ).dt.tz_localize(None)
    today = datetime.now()
    active = df_work[
        (df_work["remaining_classes"] > 0) &
        (df_work["expiration_date"] > today)
    ]
    total_classes = int(active["remaining_classes"].sum())
    avg_classes = round(active["remaining_classes"].mean())
    return total_classes, avg_classes