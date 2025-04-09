# base 
class Protesis:
    def descripcion(self):
        return "Prótesis básica"

    def daño(self):
        return 0

# Ayudante 
class MejoraProtesis(Protesis):
    def __init__(self, protesis):
        self._protesis = protesis

    def descripcion(self):
        return self._protesis.descripcion()

    def daño(self):
        return self._protesis.daño()

# Decoradores de prótesis

class ShurikenCargado(MejoraProtesis):
    def descripcion(self):
        return self._protesis.descripcion() + " + Shuriken cargado"
    def daño(self):
        return self._protesis.daño() + 25

class HachaCargada(MejoraProtesis):
    def descripcion(self):
        return self._protesis.descripcion() + " + Hacha cargada"
    def daño(self):
        return self._protesis.daño() + 40

class LanzaCargada(MejoraProtesis):
    def descripcion(self):
        return self._protesis.descripcion() + " + Lanza cargada"
    def daño(self):
        return self._protesis.daño() + 35

class Sabimaru(MejoraProtesis):
    def descripcion(self):
        return self._protesis.descripcion() + " + Sabimaru (veneno)"
    def daño(self):
        return self._protesis.daño() + 10

class AbanicoDeHierro(MejoraProtesis):
    def descripcion(self):
        return self._protesis.descripcion() + " + Abanico de hierro"
    def daño(self):
        return self._protesis.daño() + 0

class BarrenosDeShinobi(MejoraProtesis):
    def descripcion(self):
        return self._protesis.descripcion() + " + Barrenos de shinobi"
    def daño(self):
        return self._protesis.daño() + 7

class ConductoLlamenante(MejoraProtesis):
    def descripcion(self):
        return self._protesis.descripcion() + " + Conducto llameante"
    def daño(self):
        return self._protesis.daño() + 26

class CuervoDeNiebla(MejoraProtesis):
    def descripcion(self):
        return self._protesis.descripcion() + " + Cuervo de niebla"
    def daño(self):
        return self._protesis.daño() + 0

class SecuestroDivino(MejoraProtesis):
    def descripcion(self):
        return self._protesis.descripcion() + " + Secuestro divino"
    def daño(self):
        return self._protesis.daño() + 15

class Silbato(MejoraProtesis):
    def descripcion(self):
        return self._protesis.descripcion() + " + Silbato"
    def daño(self):
        return self._protesis.daño() + 3


if __name__ == "__main__":
    protesis = Protesis()   
    protesis = ShurikenCargado(protesis)
    # protesis = HachaCargada(protesis)
    # protesis = LanzaCargada(protesis)
    # protesis = Sabimaru(protesis)
    # protesis = AbanicoDeHierro(protesis)
    # protesis = BarrenosDeShinobi(protesis)
    # protesis = ConductoLlamenante(protesis)
    # protesis = CuervoDeNiebla(protesis)
    # protesis = SecuestroDivino(protesis)
    # protesis = Silbato(protesis)

    print("Prótesis equipada:", protesis.descripcion())
    print("Daño total:", protesis.daño())
