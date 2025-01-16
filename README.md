# Proyecto de Análisis de Hosts

Este proyecto genera y analiza datos de hosts utilizando Python, pandas, matplotlib y seaborn. El objetivo es crear un conjunto de datos de hosts con atributos como sistema operativo, entorno y país, y luego visualizar estos datos mediante gráficos.

## Estructura del Proyecto

- `hosts.csv`: Archivo CSV generado que contiene los datos de los hosts.
- `host_analysis.ipynb.`: Script de Python que genera los datos de los hosts, los guarda en un archivo CSV y crea varios gráficos para analizar los datos.

## Requisitos

- Python 3.x
- pandas
- matplotlib
- seaborn

Puedes instalar las bibliotecas necesarias utilizando pip:

```sh pip install pandas matplotlib seaborn ```


## Uso
- Generar y Guardar Datos
El script hosts_analysis.py genera un DataFrame con 1500 registros de hosts y lo guarda en un archivo CSV llamado hosts.csv.

- Visualización de Datos
El script también crea varios gráficos para analizar los datos de los hosts, incluyendo:

  - Gráfico de barras de entornos por país.
  - Gráfico de barras horizontales de tipos de sistemas operativos por país.
  - Gráfico de pastel de porcentajes de sistemas operativos.
  - Gráfico de barras horizontales del número total de hosts por país.
  - Gráfico de barras de hosts por entorno agrupados por país.

## Ejecución del Script
Para ejecutar el script y generar los datos y gráficos, sigue estos pasos:

- Clona este repositorio o descarga los archivos.
- Navega al directorio donde se encuentra el archivo host_analysis.ipynb
- Abre el notebook con Jupyter Notebook o JupyterLab y ejecuta todas las celdas.

## Ejemplo de Salida
El script generará un archivo CSV llamado hosts.csv y mostrará varios gráficos como se describe en la sección de visualización de datos.

**Proyecto creado por:** Emily Capetillo López  
**Fecha de Creación:** Enero 2025

---

# Juego de Adivina el Número

Este proyecto es un **juego interactivo de adivinanza desarrollado en Python**. El juego incluye **dos versiones** con características distintas para adaptarse a diferentes necesidades y contextos.

## Versiones del Proyecto

### **Versión 1: Consola**
- **Interfaz**: Funciona completamente en la consola.
- **Características**:
  - Menús interactivos para seleccionar opciones del juego.
  - Validación de entradas y submenús para niveles de dificultad.
  - Almacenamiento de resultados en un archivo Excel (`Resultados.xlsx`).
  - Generación de gráficos de estadísticas usando `matplotlib`.
- **Ventajas**:
  - Simplicidad en la ejecución, no requiere instalación de librerías gráficas adicionales.
  - Ideal para aprender y trabajar en un entorno de línea de comandos.

### **Versión 2: Interfaz Gráfica (GUI)**
- **Interfaz**: Implementada con **PyQt5** para proporcionar una experiencia visual más interactiva.
- **Características**:
  - Menús y diálogos gráficos para seleccionar opciones y capturar datos.
  - Validación de entradas directamente en la interfaz.
  - Almacenamiento y visualización de estadísticas en tiempo real con gráficos dinámicos.
- **Ventajas**:
  - Experiencia de usuario mejorada gracias a la interfaz gráfica.
  - Más intuitivo para usuarios no técnicos.
  - Ventanas emergentes para resultados y mensajes clave.
- **Requisitos**: Instalación de **PyQt5**.

## Características Generales

- **Opciones de Juego**:
  1. **Modo Solitario**: El número a adivinar es generado aleatoriamente por el sistema.
  2. **Modo 2 Jugadores**: Un jugador selecciona el número, y el segundo intenta adivinarlo.
  3. **Estadísticas**: Visualización de resultados de partidas almacenados en un archivo Excel.
  4. **Salir**: Finaliza el programa.

- **Niveles de Dificultad**:
  1. Fácil: 20 intentos.
  2. Medio: 12 intentos.
  3. Difícil: 5 intentos.
  4. Sugerido: Ajusta la dificultad según el número a adivinar.

- **Estadísticas**:
  - Los resultados (ganó/perdió) se guardan en un archivo Excel (`Resultados.xlsx`).
  - Gráficos de barras que muestran el desempeño de los jugadores (partidas ganadas y perdidas).

## Tecnologías Utilizadas

- **Python**: Lenguaje principal del proyecto.
- **Librerías**:
  - `random`: Generación de números aleatorios.
  - `openpyxl`: Manejo de archivos Excel.
  - `matplotlib`: Visualización de datos (estadísticas).
  - **Versión 2**: Adicionalmente, utiliza `PyQt5` para la interfaz gráfica.

## Cómo Ejecutar el Proyecto

### **Versión 1: Consola**
1. **Instalar Dependencias**:
   - Asegúrate de tener Python 3.x instalado.
   - Instala las librerías necesarias ejecutando:
     ```bash
     pip install openpyxl matplotlib
     ```

2. **Ejecutar el Programa**:
   - Ejecuta el archivo principal con:
     ```bash
     python adivina_el_numero_v1.py
     ```

### **Versión 2: Interfaz Gráfica (GUI)**
1. **Instalar Dependencias**:
   - Asegúrate de tener Python 3.x instalado.
   - Instala las librerías necesarias ejecutando:
     ```bash
     pip install openpyxl matplotlib PyQt5
     ```

2. **Ejecutar el Programa**:
   - Ejecuta el archivo principal con:
     ```bash
     python adivina_el_numero_v2.py
     ```

**Proyecto creado por:** Emily Capetillo López  
**Fecha de Creación:** Noviembre 2024 

---

## Contacto  

Para dudas o sugerencias, puedes contactarme a través de GitHub o por correo electrónico [emi.capetillo@gmail.com](mailto:emi.capetillo@gmail.com)


