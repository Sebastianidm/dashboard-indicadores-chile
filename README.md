# Dashboard de Indicadores Económicos de Chile

![Captura de Pantalla del Dashboard](https://github.com/user-attachments/assets/13960c38-1bea-43d3-b9c0-d5b96d8b8690)

Aplicación web Full-Stack que extrae, procesa y visualiza indicadores económicos clave de Chile (Dólar, UF, Euro) en un dashboard interactivo. El proyecto demuestra un ciclo de vida de datos completo, desde la fuente hasta la visualización.

**Enlace a la aplicación en vivo:** [Enlace se añadirá cuando se despliegue en Azure]

## Características Principales
- **Visualización Interactiva:** Gráfico de líneas que permite al usuario cambiar dinámicamente entre diferentes indicadores.
- **Datos en Tiempo Real:** Extracción de datos directamente desde la API oficial del Banco Central de Chile.
- **Diseño Responsive:** Interfaz adaptable que asegura una experiencia de usuario óptima en dispositivos de escritorio, tablets y móviles.
- **API Propia:** Un Back-End construido con FastAPI sirve los datos procesados a la interfaz de usuario.

## Pila Tecnológica (Stack)
* **Back-End:** Python, FastAPI, Uvicorn
* **Front-End:** HTML5, CSS3, JavaScript (ES6+)
* **Análisis y Extracción de Datos:** Pandas, bcchapi
* **Visualización:** Chart.js

## Cómo Ejecutarlo Localmente

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/tu-usuario/dashboard-indicadores-chile.git](https://github.com/tu-usuario/dashboard-indicadores-chile.git)
    cd dashboard-indicadores-chile
    ```

2.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Crear archivo de credenciales:**
    Crea un archivo llamado `credenciales.txt` en la raíz del proyecto. Basándote en `credenciales.txt.example`, añade tu usuario y contraseña de la API del Banco Central en dos líneas separadas.

4.  **Ejecutar el script de extracción:**
    ```bash
    python extractor_dolar.py
    ```

5.  **Lanzar el servidor Back-End:**
    ```bash
    uvicorn main:app --reload
    ```

6.  **Abrir el Front-End:**
    Abre el archivo `index.html` en tu navegador.

## Autor
* **Sebastian Díaz M** - [https://www.linkedin.com/in/sebasti%C3%A1n-d%C3%ADaz-miranda-82a707168/]
