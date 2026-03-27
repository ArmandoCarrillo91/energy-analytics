import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from pandas import read_sql

load_dotenv()

engine = create_engine(f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}")

def get_clients_packages():
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
            INNER JOIN client_packages_package_lnk cpp on p.id = cpp.client_package_id
            INNER JOIN packages pack on cpp.package_id = pack.id
        """
    df = read_sql(sql, engine)
    return df
    
def total_clients(df):
    return df["client_id"].nunique()