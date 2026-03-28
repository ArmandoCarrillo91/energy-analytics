import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from pandas import read_sql

load_dotenv()

engine = create_engine(f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}")

def fetch_clients_packages():
    sql = """
            SELECT
                c.id as client_id
                ,c.name as client_name
                ,c.created_at as c_created_at
                ,p.id as package_id
                ,p.package_name
                ,p.price as package_sold
                ,p.created_at as p_created_at
                ,p.remaining_classes
                ,p.expiration_date
                ,p.total_classes
                ,pack.name 
                ,pack.price
                ,pack.number_of_classes
            FROM clients c
            LEFT JOIN client_packages_client_lnk cpcl ON c.id = cpcl.client_id 
            LEFT JOIN client_packages p on cpcl.client_package_id = p.id 
            LEFT JOIN client_packages_package_lnk cpp on p.id = cpp.client_package_id
            LEFT JOIN packages pack on cpp.package_id = pack.id
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