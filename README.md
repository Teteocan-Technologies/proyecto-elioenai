# Limpiador de CSV 🧹

Script en Python para limpiar archivos CSV automáticamente.

## Requisitos
- Python 3.6+
- Instalar dependencias:
    ```bash
    pip install pandas numpy
    ```

## Uso básico
1. Coloca tu archivo CSV en la misma carpeta que el script.
2. Ejecuta:
    ```bash
    python limpiador_csv.py
    ```
3. Ingresa el nombre del archivo cuando lo solicite (ej: `social_media_users.csv`).

## Funcionalidades
- Elimina filas/columnas vacías
- Maneja valores faltantes:
  - Numéricos: reemplaza con la mediana
  - Texto: reemplaza con "Desconocido"
- Estandariza texto (minúsculas, sin espacios extras)
- Elimina duplicados
- Guarda archivo limpio con marca de tiempo (ej: `social_media_users_limpio_20250506_1423.csv`)
- Muestra resumen antes/después de la limpieza

## Ejemplo de salida
```bash
=== Script de Limpieza de CSV ===
Ingrese el nombre del archivo CSV a limpiar: social_media_users.csv

Datos originales (10000 filas, 7 columnas):
    Platform      Owner  ... Verified Account Date Joined
0   WhatsApp       Meta  ...              Yes  2019-03-03
1     WeChat    Tencent  ...              Yes  2023-09-21

Datos limpios (muestra):
    platform      owner  ... verified account date joined
0   whatsapp       meta  ...              yes  2019-03-03
1     wechat    tencent  ...              yes  2023-09-21

✓ Datos limpios guardados en social_media_users_limpio_20250506_1423.csv
✓ Filas procesadas: 9985
✓ Columnas finales: ['platform', 'owner', ...]
