# Práctica: Clasificación con Árbol de Decisión (Wine Dataset)

## Opiniones de los resultados
Los resultados fueron bastante buenos. Con un árbol pequeño y fácil de leer obtuvimos una precisión sólida, y al dejar que el árbol creciera más, el porcentaje de aciertos mejoró y se notó. Lo interesante de este modelo es que transforma datos de laboratorio en reglas lógicas muy claras ("si pasa esto, entonces es este tipo de vino"), lo cual facilita entender cómo toma decisiones.

## ¿El dataset cumple con los requerimientos para un árbol de decisiones?
**Sí, cumple adecuadamente.**

### Justificación:
* **Estructura de los datos:** Cuenta con características numéricas continuas (como el nivel de alcohol, los flavonoides y la intensidad del color) que permiten definir cortes exactos para las ramas del árbol.
* **Variable objetivo definida:** Las clases de vino están perfectamente separadas en tres categorías (0, 1 y 2), lo que evita confusiones al momento de clasificar.

### Características fundamentales y posibles adiciones:
* **Las más importantes:** La intensidad del color (`color_intensity`) y los flavonoides resultaron ser claves en los primeros niveles porque separan los grupos principales con mucha claridad.
* **Características extra:** Se podrían añadir variables relacionadas con el contenido total de polifenoles o la acidez total para ver si el árbol logra refinar aún más sus divisiones.