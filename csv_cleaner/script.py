import pandas as pd
import numpy as np
from datetime import datetime

def leer_csv(ruta_archivo):
    """Lee un archivo CSV y lo carga en un DataFrame de pandas."""
    try:
        return pd.read_csv(ruta_archivo)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {ruta_archivo}")
        return None
    except Exception as e:
        print(f"Error al leer el archivo: {str(e)}")
        return None

def limpiar_datos(df):
    """Realiza operaciones de limpieza básicas en un DataFrame."""
    if df is None or df.empty:
        print("DataFrame vacío o inválido")
        return df
    
    # Crear copia para no modificar el original
    df_limpio = df.copy()
    
    # 1. Eliminar filas/columnas completamente vacías
    df_limpio = df_limpio.dropna(how='all').dropna(axis=1, how='all')
    
    # 2. Manejo de valores faltantes (versión mejorada sin inplace)
    for col in df_limpio.columns:
        if np.issubdtype(df_limpio[col].dtype, np.number):
            df_limpio[col] = df_limpio[col].fillna(df_limpio[col].median())
        else:
            df_limpio[col] = df_limpio[col].fillna('Desconocido')
    
    # 3. Eliminar duplicados
    df_limpio = df_limpio.drop_duplicates()
    
    # 4. Estandarizar strings
    for col in df_limpio.select_dtypes(include=['object']).columns:
        df_limpio[col] = df_limpio[col].astype(str).str.strip().str.lower()
    
    return df_limpio

def guardar_csv(df, ruta_salida):
    """Guarda el DataFrame en un archivo CSV."""
    try:
        df.to_csv(ruta_salida, index=False)
        print(f"\n✓ Datos limpios guardados en {ruta_salida}")
        print(f"✓ Filas procesadas: {len(df)}")
        print(f"✓ Columnas finales: {list(df.columns)}")
    except Exception as e:
        print(f"Error al guardar el archivo: {str(e)}")

def generar_nombre_salida(ruta_entrada):
    """Genera un nombre para el archivo de salida."""
    fecha = datetime.now().strftime("%Y%m%d_%H%M")
    nombre_base = ruta_entrada.split('/')[-1].split('.')[0]
    return f"{nombre_base}_limpio_{fecha}.csv"

def main():
    print("=== Script de Limpieza de CSV ===")
    ruta_entrada = input("Ingrese el nombre del archivo CSV a limpiar: ")
    
    datos = leer_csv(ruta_entrada)
    if datos is None:
        return
    
    print(f"\nDatos originales ({len(datos)} filas, {len(datos.columns)} columnas):")
    print(datos.head())
    
    datos_limpios = limpiar_datos(datos)
    
    print("\nDatos limpios (muestra):")
    print(datos_limpios.head())
    
    ruta_salida = generar_nombre_salida(ruta_entrada)
    guardar_csv(datos_limpios, ruta_salida)

if __name__ == "__main__":
    main()