from bcchapi import Siete
import pandas as pd

#Muestra todas las filas y columnas
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)

print("Buscador de Series del Banco Central")


try:
    siete = Siete(file="credenciales.txt")
    print("Conexion exitosa, buscando series...")

    print("\nResultados para 'UF'")
    print(siete.buscar("UF"))
    
    print("\n--- Resultados para 'Euro' ---")
    print(siete.buscar("Euro"))
    
    print("\n--- Resultados para 'Dolar observado' ---")
    print(siete.buscar("Dolar observado"))

except Exception as e:
    print(f"Ocurrió un error: {e}")