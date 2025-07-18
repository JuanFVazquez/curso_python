import tkinter as tk

class CalculadoraIOS(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora estilo iOS")
        self.configure(bg="black")
        self.resizable(False, False)

        self.expresion = ""
        self.inicial = True  # Para controlar si está en el estado inicial
        self.crear_widgets()

    def crear_widgets(self):
        self.display = tk.Entry(
            self,
            font=("Helvetica", 40, "bold"),
            bd=0,
            bg="black",
            fg="white",
            justify="right"
        )
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="we")
        self.display.insert(0, "0")

        botones = [
            ('C', 1, 0), ('/', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
            ('0', 5, 0), (',', 5, 1), ('=', 5, 2),
        ]

        for (texto, fila, columna) in botones:
            self.crear_boton(texto, fila, columna)

        # Botón igual ocupa 2 columnas para mejor diseño
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        igual = tk.Button(
            self,
            text='=',
            font=("Helvetica", 24, "bold"),
            bg="#ff9500",
            fg="green",
            width=9,
            height=2,
            bd=0,
            command=lambda: self.pulsar_boton('=')
        )
        igual.grid(row=5, column=2, columnspan=2, padx=5, pady=5, sticky="nsew")

    def crear_boton(self, texto, fila, columna):
        if texto == 'C':
            bg_color = "#a5a5a5"  # Gris claro para el botón de borrar
            fg_color = "black"
        elif texto in ('+', '-', '*', '/', '='):
            bg_color = "#ff9500"
            fg_color = "blue"
        elif texto.isdigit() or texto == ',':
            bg_color = "#d4d4d2"
            fg_color = "black"
        else:
            bg_color = "#505050"
            fg_color = "green"

        boton = tk.Button(
            self,
            text=texto,
            font=("Helvetica", 24, "bold"),
            bg=bg_color,
            fg=fg_color,
            width=4,
            height=2,
            bd=0,
            command=lambda: self.pulsar_boton(texto)
        )
        boton.grid(row=fila, column=columna, padx=5, pady=5, sticky="nsew")

    def pulsar_boton(self, texto):
        if texto == 'C':
            self.expresion = ""
            self.inicial = True
            self.display.delete(0, tk.END)
            self.display.insert(0, "0")
            return

        if texto == '=':
            try:
                expresion_eval = self.expresion.replace(',', '.')
                resultado = eval(expresion_eval)
                resultado = str(resultado).replace('.', ',')
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, resultado)
                self.expresion = resultado.replace(',', '.')
                self.inicial = True
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
                self.expresion = ""
                self.inicial = True
        else:
            if self.inicial:
                self.display.delete(0, tk.END)
                self.expresion = ""
                self.inicial = False

            self.expresion += texto.replace(',', '.')
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.expresion.replace('.', ','))

if __name__ == "__main__":
    app = CalculadoraIOS()
    app.mainloop()
