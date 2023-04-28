import contextbuilder
import pathlib 

gde = 60
hhj = 2023
grunddaten = str(pathlib.Path.cwd() / "hhdaten/grunddaten.xlsx")
bewegungsdaten = str(pathlib.Path.cwd() / "hhdaten/bewegungsdaten.xlsx")


if __name__ == "__main__":

    #
    contexthhsatzung = contextbuilder.hhsatzung(gde = gde, hhj = hhj, xlsgrunddaten = grunddaten, xlsbewegung = bewegungsdaten)
    print(contexthhsatzung)
