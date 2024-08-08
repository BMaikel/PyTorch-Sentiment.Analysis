# Email Spam or Not (Classification)📭

## Metodología

Se utilizó una técnica avanzada de procesamiento de lenguaje natural basada en un modelo preentrenado conocido como BERT. (Bidirectional Encoder Representations from Transformers)

- **Modelo Preentrenado:** Se empleó el modelo BERT base, es un modelo de aprendizaje automático diseñado para entender el lenguaje. BERT ha sido previamente entrenado en una gran cantidad de texto para captar el significado de las palabras en diferentes contextos.

- **Ajuste Fino del Modelo:** Adaptamos BERT a nuestra tarea de clasificación multiclase. Añadimos capas adicionales al modelo para ajustar sus predicciones a nuestro problema. Estas capas adicionales fueron entrenadas con nuestros datos, permitiendo que el modelo aprenda a clasificar correctamente las declaraciones en diferentes categorías de estados mentales.

## Arquitectura del Modelo base:
<img src="https://i.ibb.co/k6sKmkY/image.png" width=100%/>
