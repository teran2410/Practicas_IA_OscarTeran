from sistema_experto import SistemaExpertoDiagnostico, Sintoma

print("=== EJERCICIO 2: ANÁLISIS DE CONFLICTOS DE REGLAS ===")

# Declaramos síntomas que activan Gripe y Alergia simultáneamente
sintomas_conflicto = {
    # Síntomas de Gripe
    "fiebre": True,
    "tos": True,
    "dolor_garganta": True,
    # Síntomas de Alergia
    "estornudos": True,
    "congestion_nasal": True,
    "picazon_ojos": True
}

engine = SistemaExpertoDiagnostico()
engine.reset()
engine.declare(Sintoma(**sintomas_conflicto))

print("\nEjecutando el motor de inferencia...\n")
engine.run()