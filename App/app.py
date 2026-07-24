import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from datetime import datetime

st.set_page_config(page_title="Netflix Analysis")

st.title("Análisis del catálogo de Netflix 🛠️")
st.write(
    """
    Aplicación basada en el notebook de análisis del catálogo de Netflix.
    
    Incluye:
    - carga de datos
    - revisión inicial
    - auditoría
    - limpieza
    - creación de variables
    - exploración
    """
)

st.header("1. Carga de datos")

archivo = st.file_uploader(
    "Selecciona tu archivo CSV",
    type=["csv"]
)

if archivo is not None:

    dfn = pd.read_csv(archivo)

    st.success("Datos cargados correctamente")

    st.write("Filas:", dfn.shape[0])
    st.write("Columnas:", dfn.shape[1])

    st.subheader("Vista inicial")
    st.dataframe(dfn.head())

    st.header("Revisión inicial de los datos")
    st.write(
        """
        Antes de realizar cambios se revisan:

        - nombres de columnas,
        - tipos de datos,
        - valores faltantes,
        - resumen general.
        """
    )

    st.subheader("Columnas disponibles")

    columnas = pd.DataFrame(
        { "Columnas": dfn.columns.tolist() }
    )

    st.dataframe(columnas)

    st.subheader("Resumen numérico")

    st.dataframe(dfn.describe())


    st.subheader("Valores faltantes")

    ntn = dfn.isnull().sum()

    ntn_pct = (ntn / len(dfn) * 100 ).round(1)

    info = pd.DataFrame(
        {
            "Conteo_Nulos": ntn,
            "Porcentaje": ntn_pct,
            "Conteo_NoNulos": dfn.notnull().sum(),
            "Tipo_datos": dfn.dtypes
        }
    )

    info = info.sort_values(
        by="Conteo_Nulos",
        ascending=False
    ).T

    st.dataframe(info)


    st.header("Exploración inicial del contenido")

    st.subheader("Valores posibles de type")

    tab_tp = pd.DataFrame(
        { "Valores posibles": dfn["type"].unique() }
    )

    st.dataframe(tab_tp)

    st.subheader("Años en existencia")

    años = pd.DataFrame(
        { "Años": dfn["release_year"].unique() }
    )

    st.dataframe(años)

    st.subheader("Cantidades existentes por año")

    cantidad_años = (
        dfn["release_year"]
        .value_counts()
        .to_frame()
        .T
    )

    st.dataframe(cantidad_años)

    st.subheader("Contenido por país")

    contenido_pais = (
        dfn["country"]
        .value_counts()
        .to_frame()
    )

    st.dataframe(contenido_pais)

    st.subheader("Cantidad de categorías")

    categorias = (
        dfn["listed_in"]
        .value_counts()
        .to_frame()
        .T
    )

    st.dataframe(categorias)

    st.subheader("Cantidad de clasificaciones")

    clasificaciones = (
        dfn["rating"]
        .value_counts()
        .to_frame()
        .T
    )

    st.dataframe(clasificaciones)


    st.header("Auditoría de calidad")

    st.write(
        """
        En esta sección se revisa:

        - cantidad de películas y series,
        - duplicados,
        - formatos de duración,
        - años inválidos,
        - valores únicos por columna,
        - cantidad de directores.
        """
    )

    st.subheader("Cantidad de películas y series")

    conteo = dfn["type"].value_counts()

    conteo_pct = (
        dfn["type"]
        .value_counts(normalize=True)
        * 100
    )

    info_tipo = pd.DataFrame(
        {
            "Cantidad": conteo,
            "Porcentaje (%)": conteo_pct.round(2)
        }
    ).T

    st.dataframe(info_tipo)

    st.subheader("Cantidad de duplicados")

    duplicados = dfn.duplicated().sum()

    st.write(duplicados)

    st.subheader("Ejemplos de duración")

    st.dataframe( dfn["duration"].head(10) )

    st.subheader("Títulos repetidos")

    Ttl_dup = dfn.duplicated().sum()

    st.write(Ttl_dup)

    st.subheader("Años inválidos")

    año = pd.DataFrame(
        {
            "Cantidad": [
                (dfn["release_year"] < 1900).sum()
            ]
        }
    )

    st.dataframe(año)

    st.subheader("Valores diferentes por columna")

    valores_columna = (
        dfn.nunique()
        .to_frame()
        .T
    )

    st.dataframe(valores_columna)

    st.subheader("Cantidad de directores")

    directores = dfn["director"].nunique()

    st.write(directores)

    st.subheader("Auditoría general")

    auditoria = pd.DataFrame(
        {
            "faltantes": ntn,
            "porcentaje": ntn_pct,
            "tipo": dfn.dtypes
        }
    )

    auditoria = auditoria.sort_values(
        "porcentaje",
        ascending=False
    )
    st.dataframe(auditoria)

    st.header("Limpieza de datos")

    st.write(
        """
        En esta etapa se realizan las transformaciones necesarias:

        - conversión de fechas,
        - separación de duración,
        - reemplazo de valores faltantes,
        - creación de año y mes de incorporación,
        - conversión de columnas repetidas a categorías.
        """
    )

    # Crear copia del dataset

    dfn_copia = dfn.copy()

    # Reemplazar valores faltantes

    st.subheader("Reemplazo de valores faltantes")

    dfn_copia["director"] = (
        dfn_copia["director"]
        .fillna("Desconocido")
    )

    dfn_copia["cast"] = (
        dfn_copia["cast"]
        .fillna("Desconocido")
    )

    dfn_copia["country"] = (
        dfn_copia["country"]
        .fillna("Desconocido")
    )

    st.dataframe(
        dfn_copia[
            [
                "director",
                "cast",
                "country"
            ]
        ].head()
    )

    # Conversión de fechas

    st.subheader("Conversión de fechas")

    dfn_copia["date_added"] = pd.to_datetime(
        dfn_copia["date_added"],
        errors="coerce"
    )

    st.dataframe(
        dfn_copia[
            [ "date_added" ]
        ].head()
    )

    # Extracción de número de duración

    st.subheader("Separación de duración")

    dfn_copia["duration_num"] = (
        dfn_copia["duration"]
        .str.extract(r"(\d+)")
        .astype(float)
    )

    dfn_copia["duration_type"] = (
        dfn_copia["duration"]
        .str.extract(r"([a-zA-Z]+)")
    )

    st.dataframe(
        dfn_copia[
            [
                "duration",
                "duration_num",
                "duration_type"
            ]
        ].head()
    )

    # Conversión a categorías

    st.subheader("Conversión de columnas a categorías")

    dfn_copia["type"] = (
        dfn_copia["type"]
        .astype("category")
    )

    dfn_copia["rating"] = (
        dfn_copia["rating"]
        .astype("category")
    )

    dfn_copia["country"] = (
        dfn_copia["country"]
        .astype("category")
    )

    st.dataframe(
        dfn_copia[
            [
                "type",
                "rating",
                "country"
            ]
        ].head()
    )

    # Extracción de años y meses

    st.subheader("Extracción de años")

    dfn_copia["year_added"] = (
        dfn_copia["date_added"]
        .dt.year
    )

    st.dataframe(
        dfn_copia[
            [ "year_added" ]
        ].head()
    )

    st.subheader("Extracción de meses")

    dfn_copia["month_added"] = (
        dfn_copia["date_added"]
        .dt.month
    )

    st.dataframe(
        dfn_copia[
            [ "month_added" ]
        ].head()
    )

    # Verificación de limpieza

    st.header("Verificación de limpieza")

    st.subheader("Valores nulos después de limpieza")

    nulos_final = (
        dfn_copia
        .isnull()
        .sum()
        .to_frame()
    )

    st.dataframe(nulos_final)

    st.subheader("Tipos de datos")

    tipos_final = (
        dfn_copia
        .dtypes
        .to_frame()
    )

    st.dataframe(tipos_final)

    st.subheader("Comparación antes y después")

    antes_despues = pd.DataFrame(
        {
            "Antes": dfn.isnull().sum(),
            "Después": dfn_copia.isnull().sum()
        }
    )

    st.dataframe(antes_despues)

    st.subheader("Dataset limpio")

    st.dataframe( dfn_copia.head() )

    st.header("Creación de variables")

    st.write(
        """
        Se crean nuevas columnas para facilitar el análisis:

        - edad del contenido,
        - cantidad de países,
        - cantidad de actores,
        - cantidad de géneros,
        - longitud de descripción,
        - existencia de director,
        - identificación de películas.
        """
    )

    # tiempo desde la creación del contenido

    dfn_copia["content_age"] = (
        datetime.now().year -
        dfn_copia["release_year"]
    )

    # cantidad de países

    dfn_copia["country_count"] = (
        dfn_copia["country"]
        .str.split(",")
        .str.len()
    )

    # cantidad de actores

    dfn_copia["cast_count"] = (
        dfn_copia["cast"]
        .str.split(",")
        .str.len()
    )

    # cantidad de géneros

    dfn_copia["genre_count"] = (
        dfn_copia["listed_in"]
        .str.split(",")
        .str.len()
    )

    # longitud de la descripción

    dfn_copia["description_length"] = (
        dfn_copia["description"]
        .str.len()
    )

    # existe director

    dfn_copia["has_director"] = (
        dfn_copia["director"] != "Desconocido"
    )

    # es película

    dfn_copia["is_movie"] = (
        dfn_copia["duration_type"] == "min"
    )

    st.dataframe(
        dfn_copia[
            [
                "title",
                "content_age",
                "country_count",
                "cast_count",
                "genre_count",
                "description_length",
                "has_director",
                "is_movie"
            ]
        ].head()
    )
    
    #########################################

    st.header("Análisis de exploración de datos")

    st.write(
        """
        En esta parte se crean gráficas para identificar patrones
        dentro del catálogo de Netflix.

        Las visualizaciones permiten observar:

        - cantidad de películas vs series,
        - crecimiento del catálogo por año,
        - distribución de duración de películas.
        """
    )

    # ¿Cuántas películas vs series hay?

    st.subheader("Cantidad de películas vs series")

    fig, ax = plt.subplots(figsize=(8, 4))

    dfn_copia["type"].value_counts().plot(
        kind="bar",
        ax=ax
    )

    ax.set_title( "Cantidad de películas vs series" )

    ax.set_xlabel( "Tipo" )

    ax.set_ylabel( "Cantidad" )

    st.pyplot(fig)

    # ¿Cuánto se agregó cada año?

    st.subheader("Contenido agregado por año")

    fig, ax = plt.subplots(figsize=(8, 4))

    (
        dfn_copia["year_added"]
        .value_counts()
        .sort_index()
        .plot(
            ax=ax
        )
    )

    ax.set_title( "Contenido agregado por año" )

    ax.set_xlabel( "Año" )

    ax.set_ylabel( "Cantidad" )
    st.pyplot(fig)

    # ¿Cuánto duran las películas?

    st.subheader("Duración de películas")

    fig, ax = plt.subplots(figsize=(8, 4))

    dfn_copia[
        dfn_copia["duration_type"] == "min"
    ]["duration_num"].hist( ax=ax )

    ax.set_title( "Duración de películas" )

    ax.set_xlabel( "Minutos" )

    ax.set_ylabel( "Cantidad de películas" )

    st.pyplot(fig)
  
    ####################################

    st.header("Países con más contenido")

    paises_tabla = (
        dfn_copia["country"]
        .value_counts()
        .head(10)
        .to_frame()
        .T
    )

    st.dataframe( paises_tabla )

    # Gráfica

    st.subheader( "Top 10 países con más contenido" )

    paises = (
        dfn_copia["country"]
        .value_counts()
        .head(10)
    )

    fig, ax = plt.subplots(figsize=(8, 4))

    paises.plot(
        kind="bar",
        ax=ax
    )

    ax.set_title( "Top 10 países con más contenido" )

    ax.set_xlabel( "País" )

    ax.set_ylabel( "Cantidad" )

    plt.xticks( rotation=45 )

    plt.tight_layout()

    st.pyplot(fig)

    # Géneros más comunes

    st.header("Géneros más comunes")

    st.write(
        """
        Se separan los géneros para poder contar cada categoría
        individualmente.
        """
    )

    dfn_copia["listed_in"] = (
        dfn_copia["listed_in"]
        .str.split(", ")
    )

    df_exploded = dfn_copia.explode( "listed_in" )

    top_genres = (
        df_exploded["listed_in"]
        .value_counts()
        .head(10)
    )

    st.dataframe( top_genres.to_frame() )

    # Gráfica pastel géneros

    fig, ax = plt.subplots(figsize=(6, 6))

    top_genres.plot(
        kind="pie",
        autopct="%1.1f%%",
        ax=ax
    )

    ax.set_title( "Top 10 géneros más comunes" )

    ax.set_ylabel(
        ""
    )

    plt.tight_layout()

    st.pyplot(fig)

    # Contenido por año y tipo

    st.header("Contenido por año y tipo")

    tabla = pd.crosstab(
        dfn_copia["year_added"],
        dfn_copia["type"]
    )

    st.dataframe( tabla )

    fig, ax = plt.subplots(figsize=(8, 4))

    tabla.plot(
        kind="bar",
        ax=ax
    )

    ax.set_title( "Contenido por año y tipo" )

    ax.set_xlabel( "Año" )

    ax.set_ylabel( "Cantidad" )

    plt.xticks( rotation=45 )

    plt.tight_layout()

    st.pyplot(fig)

    # Conclusiones

    st.header("Conclusiones")

    st.write(
        """
        Después de todo el proceso realizado se puede observar que:

        - Los datos necesitaban limpieza antes de utilizarlos.
        - Fue importante separar y convertir formatos.
        - La creación de nuevas variables ayudó a comprender mejor
          el dataset.
        - Las visualizaciones permitieron encontrar patrones dentro
          del catálogo.

        En general, este ejercicio muestra que trabajar con datos
        no solamente consiste en analizarlos, sino también en
        prepararlos correctamente desde el inicio.
        """
    )
