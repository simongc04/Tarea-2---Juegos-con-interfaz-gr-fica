from tkinter import *
import random

def jugar_piedra_papel_tijera():
    def jugar():
        eleccion_jugador = var_jugador.get()
        eleccion_maquina = random.choice(["Piedra", "Papel", "Tijera"])

        if eleccion_jugador == eleccion_maquina:
            resultado = "¡Empate!"
        elif (eleccion_jugador == "Piedra" and eleccion_maquina == "Tijera") or \
             (eleccion_jugador == "Papel" and eleccion_maquina == "Piedra") or \
             (eleccion_jugador == "Tijera" and eleccion_maquina == "Papel"):
            resultado = "Ganaste"
        else:
            resultado = "Perdist!"

        etiqueta_resultado.config(text=f"Elegiste: {eleccion_jugador}\neligio: {eleccion_maquina}\nResultado: {resultado}")

    ventana_juego = Toplevel()
    ventana_juego.title("Piedra, Papel o Tijera")
    var_jugador = StringVar(value="Piedra")

    Label(ventana_juego, text="Elige Piedra, Papel o Tijera:").pack()
    Radiobutton(ventana_juego, text="Piedra", variable=var_jugador, value="Piedra").pack()
    Radiobutton(ventana_juego, text="Papel", variable=var_jugador, value="Papel").pack()
    Radiobutton(ventana_juego, text="Tijera", variable=var_jugador, value="Tijera").pack()

    Button(ventana_juego, text="Jugar", command=jugar).pack()
    etiqueta_resultado = Label(ventana_juego, text="")
    etiqueta_resultado.pack()

def jugar_palabras_en_ingles():
    pass

def jugar_adivina_el_numero():
    numero_secreto = random.randint(0, 200)
    intentos = 0

    def intentar():
        nonlocal intentos
        intento = int(entry_intento.get())
        intentos += 1

        if intentos <= 3:
            if intento < numero_secreto:
                etiqueta_resultado.config(text="El número es mayor.")
            elif intento > numero_secreto:
                etiqueta_resultado.config(text="El número es menor.")
            else:
                etiqueta_resultado.config(text="¡Felicidades! Adivinaste el número.")
                boton_intentar.config(state=DISABLED)

        if intentos == 3 and intento != numero_secreto:
            etiqueta_resultado.config(text=f"Perdiste. El número era: {numero_secreto}.")
            boton_intentar.config(state=DISABLED)

    ventana_juego = Toplevel()
    ventana_juego.title("Adivina el Número")

    Label(ventana_juego, text="Adivina el número (entre 0 y 200):").pack()
    entry_intento = Entry(ventana_juego)
    entry_intento.pack()

    boton_intentar = Button(ventana_juego, text="Intentar", command=intentar)
    boton_intentar.pack()

    etiqueta_resultado = Label(ventana_juego, text="")
    etiqueta_resultado.pack()

ventana = Tk()
ventana.geometry("550x550")
ventana.title("Menús")
ventana.config(bg="pink")


boton_piedra = Button(ventana, text="Jugar Piedra, Papel o Tijera", command=jugar_piedra_papel_tijera)
boton_piedra.place(x=200, y=100)

boton_ingles = Button(ventana, text="Jugar Palabras en Inglés", command=jugar_palabras_en_ingles)
boton_ingles.place(x=200, y=200)

boton_numero = Button(ventana, text="Jugar Adivina el Número", command=jugar_adivina_el_numero)
boton_numero.place(x=200, y=300)

ventana.mainloop()
















