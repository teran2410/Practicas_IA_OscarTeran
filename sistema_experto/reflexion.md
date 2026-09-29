# Ejercicio 2

## ¿Cuántos diagnósticos se generan?
Se generan dos diagnósticos (por ejemplo, Gripe y Alergia en el Caso 5).

### ¿En qué orden se ejecutan las reglas activadas?
Primero se activó la regla de gripe porque los 3 sintomas primeros fueron de gripe y luego el de Alergia porque los últimos 3 son de alergia.

### ¿El resultado depende del orden en que se definieron las reglas?
Si todas las reglas tienen la misma prioridad, el orden de ejecución puede depender del orden de declaración o del patrón de coincidencia de hechos.
Como fue el caso 5.

# Preguntas de reflexión

### ¿Qué limitaciones observaste en este enfoque durante la práctica?
El sistema exige coincidencia exacta de los hechos, por una que falte la regla no se activará.
Pienso que a medida que crezca la base de conocimiento pudiera haber conflictos por reglas similares o contradictorios.

### ¿Cómo podría manejarse la incertidumbre en los síntomas?
En base a lo investigado sobre sistemas expertos yo sugeriría Redes Bayesianas o coeficientes de probabilidad (por ejemplo, asignando a un síntoma un valor de presencia entre 0.0 y 1.0).

### En el Ejercicio 2, ¿qué implicaciones tiene para un sistema experto real que se activen varias reglas a la vez?
Podría generar confusiones para el personal médico, en un sistema experto de este rubro un error podría significar una vida humana.