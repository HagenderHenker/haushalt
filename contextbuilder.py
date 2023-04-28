import data_01_allgemein as allgemein
import data_02_hhsatzung as hhdaten
import pathlib


def hhsatzung(gde, hhj, xlsgrunddaten, xlsbewegung):
    #dictgde = allgemein.gdegrunddaten(xlsfilegrunddaten=xlsgrunddaten, gde=gde)
    dictgde = allgemein.gdegrunddaten(xlsfilegrunddaten=xlsgrunddaten, gde=60)
    dictbew = hhdaten.hhsatzungbewegung(gde = gde, hhj = hhj, hhbewfile=xlsbewegung)
    dicthhgd = hhdaten.hhsatzunggrunddatenhh(xlsfile = xlsgrunddaten, gdenr=gde, hhj=hhj)
    #print(f"dictgde: {dictgde}")
    #print(f"dictbew: {dictbew}")
    #print(f"dicthhgd: {dicthhgd}")    
    conhhsatzung = dictgde | dictbew | dicthhgd
    ekvvj = hhdaten.hhsatzungekvvj(gdenr=gde, hhj=hhj, xlsfile=xlsgrunddaten)/100
    ekvj = ekvvj + dictbew["saldo_vj"]
    ekhhj = ekvj + dictbew["erg_saldo"]
    conhhsatzung["ek_vvj"] = ekvvj
    conhhsatzung["ek_vj"] = ekvj
    conhhsatzung["ek_hhj"] = ekhhj

    return conhhsatzung

def hh_vorb_allg():

    conhh_vorb_allg = {}
    return conhh_vorb_allg

"""
def freiefinanzspitze():
    confreiefinanzspitze= {}
    pass

def schuldenübersicht():
    conschuldenübersicht ={}
    pass



def hh_vorb_vvj():
    conhh_vorb_vvj = {}
    pass

def hh_vorb_vj():
    conhh_vorb_vj = {}
    pass

def vorbericht_uebersicht_erghh():
    conhh_vorb_ueberg = {
    
    }
    pass

def vorbericht_aenderungenErtraege():
    convorbericht_aenderungenErtraege = {

    }
    pass

def Vorbericht_aenderungenAufwand():
    conVorbericht_aenderungenAufwand = {

    }
    pass

def vorbericht_ueb_FinHH():
    conVorbericht_ueb_FinHH = {}
    pass

def vorbericht_Invest():
    conVorbericht_Invest = {}
    pass

def kredit_und_bestand():
    conKredit_und_bestand = {}
    pass
"""

if __name__ == "__main__":
    #print test hhsatzungcontext
    print(hhsatzung(gde=60 , hhj=2023, xlsgrunddaten=str(pathlib.Path.cwd() / "hhdaten/grunddaten.xlsx"),xlsbewegung=str(pathlib.Path.cwd() / "hhdaten/bewegungsdaten.xlsx") ))

    #print test vorbericht-allgemein
