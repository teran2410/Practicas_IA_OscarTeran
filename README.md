# Sistema Experto de Diagnóstico Médico Simple

Pequeño sistema experto basado en reglas (encadenamiento hacia adelante) para ilustrar
cómo usar la librería `experta` en Python para diagnosticar condiciones médicas
sencillas a partir de síntomas proporcionados.

## Contenido rápido
- Diagnóstico automático usando reglas.
- Casos de prueba incluidos para validar las reglas básicas.
- Código claro y comentado para fines educativos.

## Requisitos
- Python 3.8 o superior
- pip

Opcionalmente se recomienda trabajar dentro de un entorno virtual.

## Instalación
1. Clona el repositorio:

```bash
git clone <URL_DE_TU_REPOSITORIO>
cd <NOMBRE_DE_LA_CARPETA>
```

2. (Opcional) crea y activa un entorno virtual:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Instala la dependencia principal:

```bash
pip install experta
```

## Uso
Ejecuta el script principal que contiene los casos de prueba y ejemplos de ejecución:

```bash
python3 main.py
```

`main.py` ejecuta la suite de pruebas predefinida (Casos 1–5). Para usar el motor
de forma interactiva, importa `SistemaExpertoDiagnostico` desde `sistema_experto.py`
y crea un objeto con los hechos (síntomas) que quieras evaluar.

## Ejemplos rápidos
- Ejecutar la suite de pruebas:

```bash
python3 main.py
```

- Ejecutar un ejemplo desde intérprete o script:

```python
from sistema_experto import SistemaExpertoDiagnostico

engine = SistemaExpertoDiagnostico()
engine.reset()
engine.declare(Sintoma(nombre='fiebre'))
engine.run()
```

## Estructura del proyecto
- [sistema_experto.py](sistema%20experto/sistema_experto.py): Definición de hechos y motor de inferencia.
- [main.py](sistema%20experto/main.py): Runner con casos de prueba y ejemplos.
- [ejercicio2.py](sistema%20experto/ejercicio2.py): Ejercicios adicionales / pruebas.
- [README.md](sistema%20experto/README.md): Este documento.

## Pruebas y validación
`main.py` incluye una serie de casos de prueba que sirven para validar el comportamiento
de las reglas. Ejecuta `python3 main.py` y revisa la salida para verificar los diagnósticos.