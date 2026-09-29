from sistema_experto import SistemaExpertoDiagnostico, Sintoma

def ejecutar_caso(nombre_caso, **sintomas):
    print(f"=== {nombre_caso} ===")
    print(f"Síntomas reportados: {sintomas}")
    engine = SistemaExpertoDiagnostico()
    engine.reset()
    engine.declare(Sintoma(**sintomas))
    engine.run()

if __name__ == "__main__":
    print("--- PARTE 3: CASOS DE PRUEBA ORIGINALES ---\n")
    
    # Caso 1: Gripe
    ejecutar_caso("Caso 1", fiebre=True, tos=True, dolor_garganta=True)
    
    # Caso 2: Alergia
    ejecutar_caso("Caso 2", estornudos=True, congestion_nasal=True, picazon_ojos=True)
    
    # Caso 3: Gastroenteritis
    ejecutar_caso("Caso 3", dolor_estomago=True, diarrea=True, vomitos=True)
    
    # Caso 4: Síntomas sin coincidencia (Regla de respaldo)
    ejecutar_caso("Caso 4", cansancio=True, mareo=True)
    
    # Caso 5: (Gripe + Alergia)
    ejecutar_caso("Caso 5", fiebre=True, tos=True, dolor_garganta=True, 
                            estornudos=True, congestion_nasal=True, picazon_ojos=True)

    print("\n--- EJERCICIO 1: PRUEBAS DE ENFERMEDADES NUEVAS ---\n")
    ejecutar_caso("Prueba COVID-19", fiebre=True, tos_seca=True, perdida_olfato=True)
    ejecutar_caso("Prueba Resfriado común", congestion_nasal=True, estornudos=True, tos_leve=True)
    ejecutar_caso("Prueba Bronquitis", tos_persistente=True, produccion_flema=True, dificultad_respiratoria=True)
    ejecutar_caso("Prueba Dengue", fiebre=True, dolor_cabeza=True, erupcion_cutanea=True)