import data_01_allgemein as allgemein
import data_02_hhsatzung as hhdaten
import data_03_ergebnis as erg
import pathlib
import docxtpl
import dataimport as di


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
    ikred_verzinst = dictbew["ikred_aufnahme"] - dicthhgd["ikred_zinslos"]
    conhhsatzung["ek_vvj"] = ekvvj
    conhhsatzung["ek_vj"] = ekvj
    conhhsatzung["ek_hhj"] = ekhhj
    conhhsatzung["ikred_verzinst"] = ikred_verzinst
    return conhhsatzung

def hh_vorbericht_01_Allgemeines(dfhhs, dfgdegrunddaten, dfewentwicklung, dfewaltersgliederung, dfewalteru20, dfflaeche, quelleewdaten, quelleflaeche, doc):
    
    """
    gde_bez:			#Gemeindebezeichnung: zusammenfassung der Felder Gemeindetyp und 
    hhj:				#Haushaltsjahr für das ein Vorbericht erstellt wird
    gde_typ:			#Ortsgemeinde, Stadt, Verbandsgemeinde
    bm_typ:				#Ortsbürgermeister, Stadtbürgermeister, Bürgermeister
    hhj-1:				#Vorjahr der Haushaltsplanung
    EW_akt:				#Aktuelle Einwohnerzahl
    img_einwohnerentwicklung:	#Graph der Einwohnerentwicklung der letzten 10 Jahre
    img_altersstruktur:		#Graph, Alterspyramide der Einwohner/Bürger
    img_struktur_altersgruppebis20: #Graph der Einwohnerentwicklung bis 20 Jahre
    quelleewdaten:			#Woher stammen die Einwohnerdaten
    flaeche:			#Gesamtfläche der Gemeinde in km²
    img_flaeche:			#Graph der Flächennutzung
    quelleflaeche:			#Woher stammen die Flächendaten
    """
    hhj = dfhhs["hhj"]

    ew_akt = dfewentwicklung.loc[(dfewentwicklung["gdenr"] == 60)&(dfewentwicklung["jahr"] == hhj-1)]

    flaeche = dfflaeche

    conhh_vorb_allg = {
    "gde_bez" : dfgdegrunddaten["gde_bez"], 		#Gemeindebezeichnung: zusammenfassung der Felder Gemeindetyp und 
    "hhj" : hhj,				                    #Haushaltsjahr für das ein Vorbericht erstellt wird
    "gde_typ" : dfgdegrunddaten["gde_typ"],			#Ortsgemeinde, Stadt, Verbandsgemeinde
    "bm_typ" : dfgdegrunddaten["bm_typ"],			#Ortsbürgermeister, Stadtbürgermeister, Bürgermeister
    "hhj-1" : hhj-1,        				        #Vorjahr der Haushaltsplanung
    "EW_akt" : ew_akt,         		                #Aktuelle Einwohnerzahl
    "img_einwohnerentwicklung" : docxtpl.inline_image(doc, pathlib.Path.cwd() / "hhdaten/plots/bev-entw.png"),               #Graph der Einwohnerentwicklung der letzten 10 Jahre
    "img_altersstruktur" : docxtpl.inline_image(doc, pathlib.Path.cwd() / "hhdaten/plots/bev-entw.png"),               #Graph, Alterspyramide der Einwohner/Bürger
    "img_struktur_altersgruppebis20" : docxtpl.inline_image(doc, pathlib.Path.cwd() / "hhdaten/plots/bev-entw.png"),             #Graph der Einwohnerentwicklung bis 20 Jahre
    "quelleewdaten" : quelleewdaten,                 #Woher stammen die Einwohnerdaten
    "flaeche" : flaeche,			                #Gesamtfläche der Gemeinde in km²
    "img_flaeche" : docxtpl.inline_image(doc, pathlib.Path.cwd() / "hhdaten/plots/bev-entw.png"),			                        #Graph der Flächennutzung
    "quelleflaeche" : quelleflaeche                 #Woher stammen die Flächendaten

    }
    return conhh_vorb_allg

def hh_vorbericht_05_UebersichtErgHH(df):
    ergdict = erg.gesamtplan_erg(df)
    return ergdict

if __name__ == "__main__":
    #print test hhsatzungcontext
    #print(hhsatzung(gde=60 , hhj=2023, xlsgrunddaten=str(pathlib.Path.cwd() / "hhdaten/grunddaten.xlsx"),xlsbewegung=str(pathlib.Path.cwd() / "hhdaten/bewegungsdaten.xlsx") ))

    #print test vorbericht-allgemein
    print(hh_vorbericht_05_UebersichtErgHH(di.hhdata_excelimport(xlsxfile= str(pathlib.Path.cwd() / "hhdaten/bewegungsdaten.xlsx"))))
    print("test")
