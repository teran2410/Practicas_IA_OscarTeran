# Sistema Experto de Diagnóstico Médico Simple

Este proyecto implementa un sistema experto basado en reglas con encadenamiento hacia
adelante (*forward chaining*) utilizando Python y la librería `experta`. El objetivo del
sistema es realizar diagnósticos médicos sencillos a partir de un conjunto de síntomas
ingresados.

## Requisitos Previos

- **Python 3.x**
- **Git**

## Instalación

1. **Clonar el repositorio:**

```bash
git clone <URL_DE_TU_REPOSITORIO>
cd <NOMBRE_DE_LA_CARPETA>
```

2. **Crear y activar un entorno virtual (opcional pero recomendado):**

```bash
python3 -m venv venv
source venv/bin/activate  # En Linux/Mac
# venv\Scripts\activate   # En Windows
```

3. **Instalar las dependencias:**

```bash
pip install experta
```

## Ejecución del Proyecto

Para correr la suite completa de pruebas (Casos de prueba 1 al 5 y pruebas del sistema ampliado):

```bash
python3 main.py
```

## Estructura del Código

- **`sistema_experto.py`**: Contiene la definición de hechos (`Sintoma`, `Diagnostico`)
	y el motor de inferencia `SistemaExpertoDiagnostico` con todas las reglas de
	diagnóstico y la regla de respaldo.

Otros archivos:

- `main.py`: Runner con casos de prueba y ejemplos de uso.
- `ejercicio2.py`: Ejercicios y pruebas adicionales.
- `reflexion.md`: Reflexión sobre la práctica.