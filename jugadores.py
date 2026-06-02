class Jugador:

    def __init__(self, nombre, edad, altura, dorsal):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.dorsal = dorsal

 
        self.esta_lesionado = False

    def correr(self):

        if self.esta_lesionado:
            return f"{self.nombre} no puede correr porque está lesionado."

        return f"{self.nombre} está corriendo en la cancha."

    def mostrar_rol(self):
        return "Soy un jugador de fútbol."
    
    def lesionado(self):

        if self.esta_lesionado:
            return f"{self.nombre} se encuentra lesionado."

        return f"{self.nombre} está en buen estado físico."

    def lesionar(self):
        self.esta_lesionado = True
        return f"{self.nombre} sufrió una lesión."

    def recuperar(self):
        self.esta_lesionado = False
        return f"{self.nombre} se recuperó de su lesión."
    


    #   CLASES HIJAS, PARTE 2


class Portero(Jugador):

    def __init__(self, nombre, edad, altura, dorsal,
                 atajadas, penales):

        super().__init__(nombre, edad, altura, dorsal)

        self.atajadas = atajadas
        self.penales = penales

    def atajar(self):
        return f"{self.nombre} realizó una atajada."

    def sacar_balon(self):
        return f"{self.nombre} realizó un saque largo."

    def mostrar_rol(self):
        return "Soy portero y defiendo el arco."


class Defensa(Jugador):

    def __init__(self, nombre, edad, altura, dorsal,
                 balones_recuperados, despejes):

        super().__init__(nombre, edad, altura, dorsal)

        self.balones_recuperados = balones_recuperados
        self.despejes = despejes

    def marcar(self):
        return f"{self.nombre} está marcando al rival."

    def barrerse(self):
        return f"{self.nombre} realizó una barrida."

    def mostrar_rol(self):
        return "Soy defensa "

class Mediocampista(Jugador):

    def __init__(self, nombre, edad, altura, dorsal,
                 asistencias, posesion):

        super().__init__(nombre, edad, altura, dorsal)

        self.asistencias = asistencias
        self.posesion = posesion

    def dar_pase_largo(self):
        return f"{self.nombre} dio un pase largo."

    def dar_pase_corto(self):
        return f"{self.nombre} dio pase corto."

    def mostrar_rol(self):
        return "Soy mediocampista."


class Delantero(Jugador):

    def __init__(self, nombre, edad, altura, dorsal,
                 goles, velocidad):

        super().__init__(nombre, edad, altura, dorsal)

        self.goles = goles
        self.velocidad = velocidad

    def patear_al_arco(self):
        return f"{self.nombre} pateó al arco."

    def celebrar_gol(self):
        return f"{self.nombre} celebró un gol."

    def mostrar_rol(self):
        return "Soy delantero."