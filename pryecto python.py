"solitario klondike- 7 columnas de cartas (la primera cartas con 1 carta, la segunda con dos, etc.solo la ultima carta de cada columna esta visible)"
import dataclasses
import random 
from enum import Enum, Enumfrom dataclasses import dataclass
from typing import list, optional,
from typing import list, Optional,
tuple

class Palo(Enum):
    corazones = ("♥️" , "rojo")
    diamantes = ("♦️" , "rojo")
    tréboles = ("♣️" , " negro")
    espadas = ("♠️" , " negro")
    def __init__(self, simbolo,color):
        self.simbolo = simbolo
        self.color = color
        class Valor(Enum):
            AS= 1
            DOS= 2
            TRES= 3
            CUATRO= 4
            CINCO= 5
            SEIS= 6
            SIETE= 7 
            OCHO= 8
            NUEVE= 9
            DIEZ= 10
            JOTA= 11
            REINA= 12
            REY= 13
            def__str__(self):
            nombres =   {1: "A", 11: "J", 12: "Q", 13: "K"  }
            return nombres.get(self.value, str(self.value))
@dataclass
class Carta:
    plao: Palo
    valor: Valor
    visible: bool = False
    def __str__(self):
        if not self.visible:
            return "[?]"¨
        return f"[{self.valor}{self.plao.simbolo}]"
    def color(self)> str:
        return self.palo.color
    def puede_sobreponer(self, otra: "carta")> bool:
"Verificar si esta cartas puede colocarse sobre otra en el tablero"
return (self.color() != otra.color() and self.valor.value == otra.valor.value - 1)
def puede_colocar_en_fundacion(self, otra: "Carta") -> bool:
    "Verificar si esta carta puede colocarse en la fundación"
    if otra is None:
        return self.valor == Valor.AS
    return self.palo = otra.palo and self.valor.value == otra.valor.value + 1
class Mazo:
    def __init__(self):
        self.cartas = [Carta(palo, valor) for palo in Palo for valor in Valor]
        random.shuffle(self.cartas)
        self.cartas.append(Carta(palo, valor))
        random.shuffle(self.cartas)
    def repartir(self) -> [Carta]:
        if self.cartas:
            return self.cartas.pop()
        return None
    def vacío(self) -> bool:
        return len(self.cartas) == 0
    def __len__(self):
        return len(self.cartas)
    class solitario:
        def __init__ (self):
            self.mazo = Mazo()
            self.columnas = [[] for _ in range(7)]
            self.fundaciones = {palo: None for palo in Palo}
            self.pila_descartes = []
            self.repartir_cartas()
        def repartir_cartas(self):
            for i in range(7):
                for j in range(i + 1):
                    carta = self.mazo.repartir()
                    if carta:
                        carta.visible = (j == i)
                        self.columnas[i].append(carta)
        def mover_columna_a_columna(self, origen: int, destino: int) -> bool:
            if not self.columnas[origen]:
                return False
            carta_origen = self.columnas[origen][-1]
            if not self.columnas[destino]:
                if carta_origen.valor == Valor.REY:
                    self.columnas[destino].append(self.columnas[origen].pop())
                    return True
                return False
            carta_destino = self.columnas[destino][-1]
            if carta_origen.puede_sobreponer(carta_destino):
                self.columnas[destino].append(self.columnas[origen].pop())
                return True
            return False
        def mover_columna_a_fundacion(self, origen: int) -> bool:
            if not self.columnas[origen]:
                return False
            carta_origen = self.columnas[origen][-1]
            fundacion_destino = self.fundaciones[carta_origen.palo]
            if carta_origen.puede_colocar_en_fundacion(fundacion_destino):
                self.fundaciones[carta_origen.palo] = carta_origen
                self.columnas[origen].pop()
                return True
            return False
        def mover_descartes_a_columna(self, destino: int) -> bool:
            if not self.pila_descartes:
                return False
            carta_origen = self.pila_descartes[-1]
            if not self.columnas[destino]:
                if carta_origen.valor == Valor.REY:
                    self.columnas[destino].append(self.pila_descartes.pop())
                    return True
                return False
            carta_destino = self.columnas[destino][-1]
            if carta_origen.puede_sobreponer(carta_destino):
                self.columnas[destino].append(self.pila_descartes.pop())
                return True
            return False
        def mover_descartes_a_fundacion(self) -> bool:
            if not self.pila_descartes:
                return False
            carta_origen = self.pila_descartes[-1]
            fundacion_destino = self.fundaciones[carta_origen.palo]
            if carta_origen.puede_colocar_en_fundacion(fundacion_destino):
                self.fundaciones[carta_origen.palo] = carta_origen
                self.pila_descartes.pop()
                return True
            return False
        def robar_del_mazo(self):
            if self.mazo.vacío():
                self.mazo.cartas = self.pila_descartes[::-1]
                self.pila_descartes.clear()
            carta = self.mazo.repartir()
            if carta:
                carta.visible = True
                self.pila_descartes.append(carta)
        def mostrar_tablero(self):
            print("Fundaciones:")
            for palo, carta in self.fundaciones.items():
                print(f"{palo.name}: {carta if carta else '[ ]'}")
            print("\nColumnas:")
            for i, columna in enumerate(self.columnas):
                print(f"Columna {i + 1}: ", end="")
                for carta in columna:
                    print(carta, end=" ")
                print()
            print("\nPila de Descartes: ", end="")
            for carta in self.pila_descartes:
                print(carta, end=" ")
            print()
if __name__ == "__main__":    juego = solitario()
    juego.mostrar_tablero():
