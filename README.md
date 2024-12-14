# Traductor en Tiempo Real con Voz

Este proyecto es una **aplicación de traducción en tiempo real** construida utilizando **Python** y las bibliotecas **Tkinter**, **googletrans**, **pyttsx3** y **speech_recognition**. Permite traducir texto de un idioma a otro, además de incluir funcionalidad de entrada por voz y salida de voz para una experiencia más interactiva.

## Funcionalidades

1. **Traducción de texto**: 
   Los usuarios pueden ingresar un texto en un idioma y seleccionar el idioma de origen y destino. La aplicación utilizará Google Translate para realizar la traducción.

2. **Reconocimiento de voz**: 
   La aplicación puede escuchar lo que se dice a través del micrófono y convertir el audio en texto para ser traducido.

3. **Lectura en voz alta**: 
   Después de realizar la traducción, la aplicación puede leer el texto traducido en el idioma destino utilizando **pyttsx3**, lo que proporciona una experiencia accesible.

4. **Interfaz gráfica de usuario**:
   La aplicación tiene una interfaz intuitiva y amigable creada con **Tkinter**, donde los usuarios pueden interactuar fácilmente con los controles de texto, botones y menús desplegables.

## Requisitos

1. **Python 3.x**
2. Las siguientes bibliotecas de Python:
   - `tkinter`
   - `googletrans`
   - `pyttsx3`
   - `speech_recognition`
3. Un micrófono para la funcionalidad de reconocimiento de voz.

## Instalación

Para comenzar a utilizar el traductor, necesitas instalar las bibliotecas necesarias. Puedes hacerlo ejecutando el siguiente comando:

```bash
pip install googletrans==4.0.0-rc1 pyttsx3 speechrecognition
