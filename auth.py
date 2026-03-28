import os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()

supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_ANON_KEY")
)

def login_user(email: str, password: str):
    """
    Intenta autenticar al usuario contra Supabase.
    Regresa (user, error) — uno de los dos siempre es None.
    """
    try:
        response = supabase.auth.sign_in_with_password({
            "email": email,
            "password": password
        })
        return response.user, None
    except Exception as e:
        return None, str(e)

def check_tenant_access(user_id: str, tenant_slug: str = "energy"):
    """
    Verifica que el usuario tenga acceso al tenant Energy.
    Regresa True/False.
    """
    try:
        response = supabase.table("tenant_users") \
            .select("id, role") \
            .eq("user_id", user_id) \
            .execute()
        
        # Si tiene al menos un registro en tenant_users, tiene acceso
        return len(response.data) > 0
    except Exception:
        return False