import tkinter as tk
from googletrans import Translator, LANGUAGES
import pyttsx3
import speech_recognition as sr

def traducir_texto():
    texto_original = entrada_texto.get("1.0", tk.END).strip()
    idioma_origen = idiomas[opcion_origen.get()]
    idioma_destino = idiomas[opcion_destino.get()]

    if texto_original:
        try:
            traduccion = traductor.translate(texto_original, src=idioma_origen, dest=idioma_destino)
            salida_texto.delete("1.0", tk.END)
            salida_texto.insert(tk.END, traduccion.text)
            reproducir_audio(traduccion.text, idioma_destino)
        except Exception as e:
            salida_texto.delete("1.0", tk.END)
            salida_texto.insert(tk.END, f"Error en la traducción: {str(e)}")

def escuchar_voz():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        salida_texto.delete("1.0", tk.END)
        salida_texto.insert(tk.END, "Escuchando...")
        try:
            audio = recognizer.listen(source, timeout=5)
            texto = recognizer.recognize_google(audio)
            entrada_texto.delete("1.0", tk.END)
            entrada_texto.insert(tk.END, texto)
        except Exception as e:
            salida_texto.delete("1.0", tk.END)
            salida_texto.insert(tk.END, f"Error al reconocer la voz: {str(e)}")

def reproducir_audio(texto, idioma_destino):
    engine = pyttsx3.init()
    voces = engine.getProperty('voices')
    for voz in voces:
        if idioma_destino in voz.languages:
            engine.setProperty('voice', voz.id)
            break
    engine.say(texto)
    engine.runAndWait()

ventana = tk.Tk()
ventana.title("Traductor en Tiempo Real")
ventana.geometry("700x500")
ventana.resizable(False, False)
ventana.configure(bg="#2E3440")

traductor = Translator()
idiomas = {v.title(): k for k, v in LANGUAGES.items()}

label_origen = tk.Label(ventana, text="Texto Original:", bg="#2E3440", fg="#ECEFF4", font=("Arial", 12))
label_origen.pack(pady=5)
entrada_texto = tk.Text(ventana, height=5, width=70, font=("Arial", 12), bg="#4C566A", fg="#ECEFF4")
entrada_texto.pack(pady=5)

opcion_origen = tk.StringVar(ventana)
opcion_origen.set("English")
opcion_destino = tk.StringVar(ventana)
opcion_destino.set("Spanish")

menu_origen = tk.OptionMenu(ventana, opcion_origen, *idiomas.keys())
menu_origen.config(width=20, font=("Arial", 10), bg="#434C5E", fg="#ECEFF4")
menu_destino = tk.OptionMenu(ventana, opcion_destino, *idiomas.keys())
menu_destino.config(width=20, font=("Arial", 10), bg="#434C5E", fg="#ECEFF4")

label_idiomas = tk.Label(ventana, text="Selecciona Idiomas:", bg="#2E3440", fg="#ECEFF4", font=("Arial", 12))
label_idiomas.pack(pady=5)
menu_origen.pack(pady=5)
menu_destino.pack(pady=5)

boton_traducir = tk.Button(ventana, text="Traducir", command=traducir_texto, bg="#A3BE8C", fg="#2E3440", font=("Arial", 12), width=15)
boton_traducir.pack(pady=10)

boton_voz = tk.Button(ventana, text="Escuchar Voz", command=escuchar_voz, bg="#88C0D0", fg="#2E3440", font=("Arial", 12), width=15)
boton_voz.pack(pady=10)

label_traduccion = tk.Label(ventana, text="Texto Traducido:", bg="#2E3440", fg="#ECEFF4", font=("Arial", 12))
label_traduccion.pack(pady=5)
salida_texto = tk.Text(ventana, height=5, width=70, font=("Arial", 12), bg="#4C566A", fg="#ECEFF4", state="normal")
salida_texto.pack(pady=5)

ventana.mainloop()
