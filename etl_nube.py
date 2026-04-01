import os
import requests
from supabase import create_client

# 🔑 SEGURIDAD: Aquí le decimos a Python que busque las llaves en el sistema, no en el texto.
URL_SUPABASE = os.environ.get("SUPABASE_URL")
KEY_SUPABASE = os.environ.get("SUPABASE_KEY")

# Verificamos que las llaves existan para no dar un error feo
if not URL_SUPABASE or not KEY_SUPABASE:
    print("❌ Error: No se encontraron las credenciales en las variables de entorno.")
    exit()

supabase = create_client(URL_SUPABASE, KEY_SUPABASE)

def etl_proceso():
    print("🛰️ Extrayendo precios...")
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=usd"
    
    try:
        data = requests.get(url).json()

        # Transformación
        rows = [
            {"nombre": "Bitcoin", "precio_usd": data['bitcoin']['usd']},
            {"nombre": "Ethereum", "precio_usd": data['ethereum']['usd']},
            {"nombre": "Solana", "precio_usd": data['solana']['usd']}
        ]

        print("📤 Cargando datos a la nube...")
        # Carga a Supabase
        supabase.table("precios_crypto").insert(rows).execute()
        
        print("✅ ¡Pipeline completado con éxito!")
        
    except Exception as e:
        print(f"❌ Ocurrió un error: {e}")

if __name__ == "__main__":
    etl_proceso()