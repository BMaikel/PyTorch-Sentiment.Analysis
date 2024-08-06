# PyTorch-Sentiment.Analysis
Proyecto de procesamiento de lenguaje natural con PyTorch, centrado en análisis de estados mentales a partir de datos etiquetados.

## Descripción del Dataset
Este conjunto de datos es una colección curada de estados mentales etiquetados a partir de declaraciones de múltiples fuentes. Incluye datos de diversas plataformas como Reddit y Twitter, limpiados y organizados para ser utilizados en el desarrollo de chatbots y análisis de sentimientos.

El dataset contiene declaraciones etiquetadas con uno de los siguientes estados mentales:

- Normal
- Depression
- Suicidal
- Anxiety
- Stress
- Bi-Polar
- Personality Disorder

## Metodología

Se utilizó una técnica avanzada de procesamiento de lenguaje natural basada en un modelo preentrenado conocido como BERT. (Bidirectional Encoder Representations from Transformers)

- **Modelo Preentrenado:** Se empleó el modelo BERT base, es un modelo de aprendizaje automático diseñado para entender el lenguaje. BERT ha sido previamente entrenado en una gran cantidad de texto para captar el significado de las palabras en diferentes contextos.

- **Ajuste Fino del Modelo:** Adaptamos BERT a nuestra tarea de clasificación multiclase. Añadimos capas adicionales al modelo para ajustar sus predicciones a nuestro problema. Estas capas adicionales fueron entrenadas con nuestros datos, permitiendo que el modelo aprenda a clasificar correctamente las declaraciones en diferentes categorías de estados mentales.

## Arquitectura del Modelo base:
<img src="https://i.ibb.co/k6sKmkY/image.png" width=100%/>
