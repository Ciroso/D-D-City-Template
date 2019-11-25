import Filer as file
import Struttura


class Citta:
    def __init__(self):
        self.nome = ""
        self.strutture = []

    def generaCitta(self):
        self.nome = file.giveJustOne("NomiCitta.txt")
        self.generaStrutture()
        self.riepilogoCitta()

    def generaStrutture(self):
        tempCity = file.giveList("Strutture.txt")
        for i in range(len(tempCity)):
            self.strutture.append(Struttura.Struttura(tempCity[i]))

    def riepilogoCitta(self):
        print("Nome della citta :", self.nome, "\n")
        for i in range(len(self.strutture)):
            self.strutture[i].info()
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n")
