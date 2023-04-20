import pandas as pd
import numpy as np 
import dataimport as di
import pathlib

class Gemeinde:
    """
    The "Gemeinde" class is used to store the repeatedly used key data for the municipal authority
    for which the budget is drawn up
    """
    def __init__(self, gde_nr, gde_name, gde_typ, bm_name, bm_typ):
        self.gde_nr = gde_nr
        self.gde_name = gde_name
        self.gde_typ = gde_typ
        self.bm_name = bm_name
        self.bm_typ = bm_typ
        self.gde_bez = f"{self.gde_typ} {self.gde_name}"

class Haushalt:
    """
    Repeatedly used data for the budget itself. 
    """

    def __init__(self, hhj, planodernachtrag, beschluss_vorjahr,beschluss_vorvorjahr ,vvj_abgeschlossen):
        self.hhj = hhj
        self.vj = hhj - 1
        self.vvj = hhj - 2
        self.hhj1 = hhj + 1
        self.hhj2 = hhj + 2
        self.hhj3 = hhj + 3
        self.beschluss_vorjahr = beschluss_vorjahr
        self.beschluss_vorvorjahr = beschluss_vorvorjahr
        self.vvj_abgeschlossen = vvj_abgeschlossen
        self.planodernachtrag = planodernachtrag


def readgrunddaten(xlsfile):
    gde = pd.read_excel(xlsfile, sheet_name="gde",)
    
    print(gde.head())
    return gde

xls = str(pathlib.Path.cwd() / "hhdaten/grunddaten.xlsx")
print(xls)
gde = readgrunddaten(xls)


        


