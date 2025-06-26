# Importamos librerias necesarias.
from bcchapi import Siete
from datetime import datetime, timedelta
import pandas as pd

# Mostrar todas las columnas del Dataframe
pd.set_option('display.max_columns', None)

print("--- Iniciando script de extracción de datos ---")

#Conectamos a la API con nuestro archivo credenciales.
try:
    siete = Siete(file="credenciales.txt")
    print("Conexion establecida con exito.")
except Exception as e:
    print(f"Error al conectar con la API: {e}")
    exit()

#IMPORTANTE: Buscar los codigos y nombres de las series que queremos
# Dólar: F073.TCO.PRE.Z.D
# Euro: F086.EER.PRE.Z.D
# UF: F072.UFF.PRE.Z.D
print("\nBuscando codigos...")
series_a_consultar = {
    "F073.TCO.PRE.Z.D": "Dolar",
    "F073.UFF.PRE.Z.D": "UF",
    "F072.CLP.EUR.N.O.D": "Euro"
}

lista_series_ids = list(series_a_consultar.keys())
lista_nombres = list(series_a_consultar.values())



#Definir el rango de fechas (Ultimos 365 dias)
fecha_final = datetime.now()
fecha_inicial = fecha_final - timedelta(days=365)

#Formatear las fechas a 'YYYY-MM-DD' como lo requiere la API
fecha_final_str = fecha_final.strftime('%Y-%m-%d')
fecha_inicial_str = fecha_inicial.strftime('%Y-%m-%d')

print(f"Consultado datos desde {fecha_inicial_str} hasta {fecha_final_str}.")


#Obtener los datos usando el metodo cuadro()

try:
    print("\nObteniendo datos de Dólar, UF y Euro...")
    #el metodo cuadro nos devuelve un DATAFRAME de pandas directamente
    # Pedimos todas las series a la vez
    df_indicadores = siete.cuadro(
        series=lista_series_ids,
        nombres=lista_nombres,
        desde=fecha_inicial_str,
        hasta=fecha_final_str
    )
    print("¡Datos obtenidos correctamente!")

    ## La fecha viene como el índice del DataFrame. La convertimos en una columna.
    df_indicadores.reset_index(inplace=True)
    
    # Renombramos la columna del índice a 'Fecha'
    df_indicadores.rename(columns={'index': 'Fecha'}, inplace=True)
    
    # Convertimos la columna 'Fecha' a formato de solo fecha (sin hora)
    df_indicadores['Fecha'] = pd.to_datetime(df_indicadores['Fecha']).dt.date

    # En lugar de eliminar filas con CUALQUIER dato faltante (dropna), las dejaremos.
    # Es posible que en un feriado haya UF pero no Dólar, por ejemplo.
    # El Front-End se encargará de manejar los datos faltantes si es necesario.
    print("Procesamiento de fechas completado.")

    # Guardamos los datos en un archivo csv.
    nombre_archivo = "indicadores_economicos.csv"
    df_indicadores.to_csv(nombre_archivo, index=False, date_format='%Y-%m-%d')
    print(f"\n¡Datos guardados exitosamente en el archivo '{nombre_archivo}'!")
    
    print("\n--- Muestra de los datos guardados ---")
    print(df_indicadores.head())


except Exception as e:
    print(f"Ocurrió un error al obtener o guardar los datos de la serie: {e}")