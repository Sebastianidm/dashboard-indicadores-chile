from fastapi import FastAPI
import pandas as pd
from pathlib import Path
#Añadimos CORSMiddleware
from fastapi.middleware.cors import CORSMiddleware

#Creamos la instancia de la aplicacion.

app = FastAPI(
    title ="API de mi Proyecto de Datos",
    description="Una API para exponer datos económicos de Chile, construida con FastAPI",
    version="0.1.0"
)

#Codigo de CORS, En una lista agregamos los origenes permitidos
#En este caso "*", que significa todos.
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials=True,
    allow_methods=["*"], # PERMITE TODOS LOS METODOS (GET, POST, etc)
    allow_headers=["*"]
)


#PRIMER ENDPOINT
@app.get("/")
def read_root():
    return {"mensaje" : "¡Bienvenido a mi API de datos económicos!"}

#SEGUNDO ENDPOINT (CONSUMIENDO ARCHIVO CSV)
@app.get("/api/indicadores")
def get_indicadores():
    """
    Endpoint para obtener datos historicos del dolar, UF y Euro.
    Lee los datos desde el archivo CSV y los devuelve en formato JSON.
    """
    print("Petición recibida en /api/indicadores")
    
    try:
        script_dir = Path(__file__).parent
        file_path = script_dir / "indicadores_economicos.csv"
        print(f"Intentando leer el archivo desde: {file_path}")
        df_indicadores = pd.read_csv(file_path)
        # Reemplazamos los valores NaN (Not a Number) de Pandas por None,
        # que es el equivalente de 'null' para JSON.
        df_indicadores = df_indicadores.astype(object).where(df_indicadores.notna(), None)
       

        datos = df_indicadores.to_dict(orient="records")
        return datos

    except FileNotFoundError:
        return {"error": f"El archivo de datos ('{file_path}') no fue encontrado. Asegúrate de que el script extractor se haya ejecutado."}
    except Exception as e:
        return {"error": f"Ocurrió un error inesperado al procesar los datos: {str(e)}"}