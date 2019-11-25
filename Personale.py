import random
import Filer

class Personale:

    def __init__(self):
        self.razza = self.selezionaRazza()
        self.sesso = self.selezionaSesso()
        self.nome = self.selezionaNome(self.razza, self.sesso)
        self.eta = self.selezionaEta()

    def aggiungiPersonale(self):
        return self

    def selezionaNome(self, razza, sesso):
        tempSesso = sesso
        tempRazza = razza

        while tempSesso == "Indefinito":
            tempSesso = self.selezionaSesso()
            self.selezionaNome(tempRazza, tempSesso)
        while tempRazza == "Razza sconosciuta":
            tempRazza = self.selezionaRazza()
            self.selezionaNome(tempRazza, tempSesso)

        if razza == "Mezzorco":
            return Filer.giveJustOne("Nomi"+"Orco"+".txt")
        elif razza == "Orco":
            return Filer.giveJustOne("Nomi"+"Orco"+".txt")
        elif tempRazza == "Mezzelfo":
            return Filer.giveJustOne("Nomi" + "Elfo" + tempSesso + ".txt")
        elif tempRazza != "Orco" and tempRazza != "Mezzorco":
            return Filer.giveJustOne("Nomi"+tempRazza+tempSesso+".txt")
        self.selezionaNome(tempRazza, tempSesso)

    def selezionaEta(self):
        a = random.randint(0, 120)
        if a < 20:
            return "Adolescente"
        elif a < 40:
            return "Giovane"
        elif a < 60:
            return "Adulto"
        elif a < 80:
            return "Anziano"
        elif a < 100:
            return "Decrepito"
        else:
            return "Indefinita"

    def selezionaSesso(self):
        s = random.randint(0, 100)
        if s < 50:
            return "Maschio"
        elif s > 50:
            return "Femmina"
        else:
            return "Indefinito"

    def selezionaRazza(self):
        raz = random.randint(0, 110)
        if raz < 13:
            return "Nano"
        elif raz < 26:
            return "Elfo"
        elif raz < 39:
            return "Gnomo"
        elif raz < 52:
            return "Mezzelfo"
        elif raz < 65:
            return "Mezzorco"
        elif raz < 78:
            return "Halfling"
        elif raz < 91:
            return "Umano"
        else:
            return "Razza sconosciuta"

    def info(self):
        print("\t", "Nome:", self.nome, "\t", self.razza, self.sesso, self.eta)
