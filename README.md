# Proyecto de Análisis de Hosts

Este proyecto genera y analiza datos de hosts utilizando Python, pandas, matplotlib y seaborn. El objetivo es crear un conjunto de datos de hosts con atributos como sistema operativo, entorno y país, y luego visualizar estos datos mediante gráficos.

## Estructura del Proyecto

- `hosts.csv`: Archivo CSV generado que contiene los datos de los hosts.
- `hosts_analysis.py`: Script de Python que genera los datos de los hosts, los guarda en un archivo CSV y crea varios gráficos para analizar los datos.

## Requisitos

- Python 3.x
- pandas
- matplotlib
- seaborn

Puedes instalar las bibliotecas necesarias utilizando pip:

```sh
pip install pandas matplotlib seaborn

## Uso
Generar y Guardar Datos
El script hosts_analysis.py genera un DataFrame con 1500 registros de hosts y lo guarda en un archivo CSV llamado hosts.csv.

Visualización de Datos
El script también crea varios gráficos para analizar los datos de los hosts, incluyendo:

Gráfico de barras de entornos por país.
Gráfico de barras horizontales de tipos de sistemas operativos por país.
Gráfico de pastel de porcentajes de sistemas operativos.
Gráfico de barras horizontales del número total de hosts por país.
Gráfico de barras de hosts por entorno agrupados por país.
Ejecución del Script
Para ejecutar el script y generar los datos y gráficos, sigue estos pasos:

Clona este repositorio o descarga los archivos.
Navega al directorio donde se encuentra el archivo hosts_analysis.py.
Ejecuta el script con el siguiente comando:
python hosts_analysis.py
Ejemplo de Salida
El script generará un archivo CSV llamado hosts.csv y mostrará varios gráficos como se describe en la sección de visualización de datos.
