import requests
import pandas as pd

def obtener_precios():
    print("🚀 Conectando con la API de CoinGecko...")
    
    # URL para obtener el precio de Bitcoin, Ethereum y Solana
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=usd"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        # Convertimos el JSON a una tabla (DataFrame)
        df = pd.DataFrame(data).T # La 'T' es para trasponer y que se vea mejor
        df.index.name = 'cripto'
        df.reset_index(inplace=True)
        
        print("✅ ¡Datos extraídos con éxito!")
        print(df)
        
        # Guardamos un respaldo rápido en un archivo CSV
        df.to_csv("precios_actuales.csv", index=False)
        print("\n💾 Archivo 'precios_actuales.csv' generado.")
        
    except Exception as e:
        print(f"❌ Error al extraer: {e}")

if __name__ == "__main__":
    obtener_precios()