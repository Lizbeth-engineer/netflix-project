# Netflix Data Analysis Dashboard

Esta es una aplicación interactiva desarrollada con **Streamlit** para el análisis exploratorio de datos del catálogo de Netflix.

## Descripción

Este proyecto es un **dashboard interactivo** que permite a los usuarios explorar y analizar datos del catálogo de Netflix a través de una interfaz web intuitiva. El análisis abarca desde la **carga y limpieza de datos** hasta la **creación de visualizaciones complejas** que revelan patrones en el contenido disponible.

---

## Características

- Carga dinámica del archivo CSV
- Análisis exploratorio de datos (EDA)
- Visualizaciones interactivas
- Exploración de variables como:
  - Tipo de contenido (películas/series)
  - País
  - Año de lanzamiento
  - Géneros

## Análisis Incluidos

### 1️._ **Carga y Revisión Inicial**
- Información sobre dimensiones del dataset
- Resumen de columnas disponibles
- Tipos de datos y estadísticas descriptivas

### 2️._ **Auditoría de Calidad de Datos**
- Detección de valores faltantes (cantidad y porcentaje)
- Identificación de registros duplicados
- Validación de rangos de años
- Conteo de valores únicos por columna

### 3️._ **Limpieza y Transformación**
- Conversión de fechas a formato datetime
- Separación de campos de duración (número + tipo)
- Reemplazo de valores faltantes
- Conversión de variables categóricas
- Extracción de año y mes de incorporación

### 4️._ **Ingeniería de Variables**
Se crean **8 nuevas variables** derivadas para análisis avanzado:
- `content_age`: Antigüedad del contenido
- `country_count`: Cantidad de países de producción
- `cast_count`: Número de actores
- `genre_count`: Cantidad de géneros
- `description_length`: Extensión de la descripción
- `has_director`: Presencia de director
- `is_movie`: Identificación de películas vs series

### 5️.- **Exploración y Visualización**
- Distribución de **películas vs series**
- **Evolución temporal** del catálogo
- **Top 10 países** con más contenido
- **Géneros más populares** (gráfico pie)
- Relación entre **año y tipo de contenido**

## Hallazgos Principales

Basado en el análisis del catálogo de Netflix se encontró que:

🎬 **63%** del contenido corresponde a películas  
🌎 **Estados Unidos** lidera con la mayor cantidad de títulos  
📈 Crecimiento significativo de contenido desde **2015**  
🎭 **Drama** y **Comedia** son los géneros más frecuentes  
⏱️ Duración promedio de películas: **~100 minutos**


## Tecnologías utilizadas

Tecnología      ----->        Uso 
----------------------------------------------------------
**Python 3**   ------>   Lenguaje principal
**Streamlit**  ------>   Framework para crear la aplicación web interactiva
**Pandas**     ------>   Manipulación y transformación de datos
**NumPy**      ------>   Operaciones numéricas
**Matplotlib** ------>   Creación de visualizaciones estáticas

## Estructura del proyecto

```
netflix-project/
│
├── app/
│ └── app.py
│
├── notebooks/
│ └── Netflix_Final_Datos.ipynb
│
├── data/
│ └── netflix.csv
│
├── assets/
│ └── Capturas_Datos_Netflix.pdf
│
└── README.md
```

## ¿Cómo Usar?

### Requisitos Previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Instalación

1. Clona el repositorio
```bash
git clone https://github.com/Lizbeth-engineer/netflix-project.git
cd netflix-project
```
2. Crea un entorno virtual
```
python -m venv venv
# En Windows:
venv\Scripts\activate
```
3. Instala manualmente las dependencias
```
pip install streamlit pandas numpy matplotlib
```

### Ejecución
Desde la raíz del proyecto:

```bash
streamlit run App/app.py
La aplicación se abrirá en http://localhost:8501
```
Carga el archivo CSV desde la carpeta Data/

---

## Notebook de Análisis
En Notebooks/Netflix_Final_Datos.ipynb encontrarás el análisis detallado paso a paso, incluyendo:

Exploración inicial
Transformaciones aplicadas
Visualizaciones de investigación
Interpretación de resultados

## Capturas

En la carpeta Assets/ encontrarás screenshots de la aplicación en funcionamiento.

---
## Autor

Mónica Lizbeth Z.V.

## Licencia
Este proyecto es de uso educativo.
