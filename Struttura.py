import random
import Personale


class Struttura:
    def __init__(self, tipologia):
        self.tipo = tipologia
        self.qualita = random.randint(0, 10)
        self.lavoratori = self.ufficioImpiego()
        self.prezzi = self.trovaPrezzi()

    def ufficioImpiego(self):
        lavoratori = []
        x = random.randint(0, 100)
        y = random.randint(0, 100)
        lavoratori.append(Personale.Personale())
        while x < y:
            lavoratori.append(Personale.Personale())
            x = y
            y = random.randint(0, 100)
        return lavoratori

    def trovaPrezzi(self):
        x = random.randint(0, 100)
        if x < 20:
            return "Molto economico - x 0.5"
        elif x < 40:
            return "Economico - x 0.75"
        elif x < 60:
            return "Bilanciato/equo - x 1"
        elif x < 80:
            return "Caro - x 1.25"
        elif x <= 100:
            return "Molto caro - x 1.5"

    def info(self):
        print(self.tipo, "\n Qualità :", self.qualita, "\n Prezzi :", self.prezzi, "\n Personale: ")
        for i in range(0, len(self.lavoratori)):
            self.lavoratori[i].info()

        print("\n")