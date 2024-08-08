# 📧 Clasificación de Correos y SMS: Spam o No Spam 📭

![](https://miro.medium.com/v2/resize:fit:1200/1*_igArwmR7Pj_Mu_KUGD1SQ.png)

## 1. 📝 Introducción
En la era digital, la comunicación electrónica se ha vuelto una herramienta esencial tanto para individuos como para organizaciones. Sin embargo, con el aumento en el uso de correos electrónicos y mensajes SMS, también ha crecido la problemática del spam: mensajes no solicitados y, a menudo, maliciosos que saturan nuestras bandejas de entrada. Estos mensajes no solo representan una molestia, sino que también pueden ser una amenaza a la seguridad y la privacidad.

## 2. 🚨 Problemática
La identificación precisa y oportuna de mensajes de spam es un desafío crítico en el ámbito de la seguridad digital. Un modelo ineficaz puede resultar en:

- ❌ Falsos positivos: Mensajes legítimos marcados como spam.
- ❌ Falsos negativos: Mensajes de spam que pasan desapercibidos.

Estos errores no solo afectan la experiencia del usuario, sino que también pueden tener consecuencias económicas y de seguridad significativas. Por ello, es esencial desarrollar un modelo de clasificación robusto que pueda diferenciar de manera efectiva entre mensajes legítimos y spam.

## 3. 🧠 Descripción del Proyecto
Este proyecto se centra en el desarrollo de un modelo de clasificación binaria utilizando BERT (📚 Bidirectional Encoder Representations from Transformers), un modelo de lenguaje preentrenado que ha demostrado un rendimiento excepcional en diversas tareas de procesamiento de lenguaje natural (NLP).

El modelo BERT ha sido ajustado específicamente para la tarea de clasificación de mensajes de correo electrónico y SMS, con el objetivo de distinguir entre:

- ✅ Mensajes legítimos (no spam)
- 🚫 Mensajes spam
El proceso de ajuste del modelo incluye la adaptación de BERT a este conjunto de datos específico, lo que permite al modelo capturar las sutilezas y patrones característicos de los mensajes spam en comparación con los mensajes legítimos.

## 4. 🗃️ Descripción del Conjunto de Datos
### 4.1 📊 Visión General
- Total de Entradas: 1,000
### 4.2 📋 Características:
- 📄 message_content: Contiene el texto del cuerpo del correo electrónico o mensaje SMS. Esta característica es la entrada principal para el modelo de clasificación.
- 🏷️ is_spam: Etiqueta binaria que indica si el mensaje es spam (1) o no (0). Esta es la variable objetivo para la tarea de clasificación.
