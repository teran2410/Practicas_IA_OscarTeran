from experta import KnowledgeEngine, Fact, Rule, NOT

# Parte 1: Definición de Hechos

class Sintoma(Fact):
    """
    Representa un síntoma o conjunto de síntomas presentes o ausentes en el paciente.
    Se define pasando atributos booleanos o descriptivos, por ejemplo:
    Sintoma(fiebre=True, tos=True)
    """
    pass

class Diagnostico(Fact):
    """
    Representa el diagnóstico o enfermedad identificada por el sistema experto.
    Almacena el nombre del diagnóstico en su atributo principal.
    Por ejemplo: Diagnostico(enfermedad="Gripe")
    """
    pass


# Parte 2: Motor de Inferencia y Reglas de Diagnóstico

class SistemaExpertoDiagnostico(KnowledgeEngine):

    @Rule(Sintoma(fiebre=True, tos=True, dolor_garganta=True))
    def regla_gripe(self):
        self.declare(Diagnostico(enfermedad="Gripe"))
        print("[DIAGNÓSTICO]: Gripe")
        print("[RECOMENDACIÓN]: Descanse y manténgase hidratado.\n")

    @Rule(Sintoma(fiebre=True, dolor_cabeza=True, nauseas=True))
    def regla_migrana(self):
        self.declare(Diagnostico(enfermedad="Migraña"))
        print("[DIAGNÓSTICO]: Migraña")
        print("[RECOMENDACIÓN]: Descanse en una habitación oscura y silenciosa.\n")

    @Rule(Sintoma(estornudos=True, congestion_nasal=True, picazon_ojos=True))
    def regla_alergia(self):
        self.declare(Diagnostico(enfermedad="Alergia"))
        print("[DIAGNÓSTICO]: Alergia")
        print("[RECOMENDACIÓN]: Evite alérgenos conocidos y considere antihistamínicos.\n")

    @Rule(Sintoma(dolor_estomago=True, diarrea=True, vomitos=True))
    def regla_gastroenteritis(self):
        self.declare(Diagnostico(enfermedad="Gastroenteritis"))
        print("[DIAGNÓSTICO]: Gastroenteritis")
        print("[RECOMENDACIÓN]: Reponga líquidos con suero oral y lleve una dieta blanda.\n")

    # Reglas ampliadas (Ejercicio 1)

    @Rule(Sintoma(fiebre=True, tos_seca=True, perdida_olfato=True))
    def regla_covid19(self):
        self.declare(Diagnostico(enfermedad="COVID-19"))
        print("[DIAGNÓSTICO]: COVID-19")
        print("[RECOMENDACIÓN]: Aíslese, hágase una prueba confirmatoria y vigile su oxigenación.\n")

    @Rule(Sintoma(congestion_nasal=True, estornudos=True, tos_leve=True))
    def regla_resfriado_comun(self):
        self.declare(Diagnostico(enfermedad="Resfriado común"))
        print("[DIAGNÓSTICO]: Resfriado común")
        print("[RECOMENDACIÓN]: Tome abundantes líquidos y descanse.\n")

    @Rule(Sintoma(tos_persistente=True, produccion_flema=True, dificultad_respiratoria=True))
    def regla_bronquitis(self):
        self.declare(Diagnostico(enfermedad="Bronquitis"))
        print("[DIAGNÓSTICO]: Bronquitis")
        print("[RECOMENDACIÓN]: Acuda al médico para valoración pulmonar y tratamiento específico\n")

    @Rule(Sintoma(fiebre=True, dolor_cabeza=True, erupcion_cutanea=True))
    def regla_dengue(self):
        self.declare(Diagnostico(enfermedad="Dengue"))
        print("[DIAGNÓSTICO]: Dengue")
        print("[RECOMENDACIÓN]: Manténgase muy bien hidratado, no se auto-medique aspirina/ibuprofeno y consulte urgencias.\n")

    # Regla de respaldo
    @Rule(NOT(Diagnostico()))
    def regla_respaldo(self):
        print("[DIAGNÓSTICO]: No se pudo determinar un diagnóstico preciso con los síntomas dados.")
        print("[RECOMENDACIÓN]: Le recomendamos consultar a un médico profesional para una evaluación formal.\n")