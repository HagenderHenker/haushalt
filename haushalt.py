import dataimport as di 
import contextbuilder as ctx
import docbuilder
import pathlib
import enviromentvar as env

gde = env.gde
hhj = env.hhj
grunddaten = env.grunddaten
bewegungsdaten = env.bewDat

hhstpl = env.hhstpl
quelleewdaten = env.quelleewdaten
quelleflaechendaten = env.quelleflaechendaten

if __name__ == "__main__":

    # create the dataframes for all further purposes from dataimport
    print("Creating Dataframes")
    dfbew = di.hhdata_excelimport(xlsxfile=bewegungsdaten)
    print("... Bewegungsdaten")
    dferl = di.erl_excelimport(xlsxfile=bewegungsdaten)
    print("... Erläuterungen")
    dfgde = di.readgrunddatengde(xlsfile=grunddaten, gdenr=gde)
    print("... Gemeindegrunddaten")
    dfhhs = di.readgrunddatenhh(xlsfile=grunddaten, gdenr=gde, hhj=hhj)
    print("... Haushaltssatzungsdaten")
    dfewentw = di.readewstatistik_wohn(xlsfile=grunddaten, gdenr=gde, jahr=hhj-1)
    print("... Einwohnerstatistik")
    dfewalter = di.readewdatenaltersstruktur(xlsfile=grunddaten, gdenr=gde, jahr=hhj-1)
    print("... Einwohnerstatistik Altersstruktur")
    dfewu20 = di.readewdaten_u20(xlsfile=grunddaten, gdenr=gde, jahr=hhj-1)
    print("... Einwohnerstatistik Altersstruktur unter 20jährige")
    dfeweinschulung = di.readewdaten_u20(xlsfile=grunddaten, gdenr=gde, jahr=hhj-1)
    print("... Einwohnerstatistik Einschulung")
    dfflaeche = di.readflaechenstatistik(xlsfile=grunddaten, gdenr=gde, jahr=hhj-1)
    print("... Flächenstatistik")

    # build "Haushaltssatzung"
    """
    contexthhsatzung = ctx.hhsatzung(gde = gde, hhj = hhj, xlsgrunddaten = grunddaten, xlsbewegung = bewegungsdaten)
    print("Daten für 'Haushaltssatzung' sind zusammengestellt")
    
    docbuilder.builddocx(template=hhstpl, context=contexthhsatzung, filename="00-Haushaltssatzung", gde=gde, hhj=hhj)
    print("Haushaltssatzung erstellt in Ordner")
    """
    # build "02_Vorbericht" 1. Abschnitt: Allgemeines

    vorb1tpl = docbuilder.create_tpl_instance(

                                                )
    print("... Templateinstanz Vorbericht 01 Allgemeines erzeugt")

    contextvorb1 = ctx.hh_vorbericht_01_Allgemeines(
                                                    dfhhs=dfhhs,dfgdegrunddaten = dfgde, 
                                                    dfewentwicklung=dfewentw, 
                                                    dfewaltersgliederung=dfewalter, 
                                                    dfewalteru20= dfewu20, 
                                                    dfflaeche=dfflaeche, 
                                                    quelleewdaten=quelleewdaten, quelleflaeche=quelleflaechendaten,
                                                    doc =  vorb1tpl
                                                  )
    print("Daten für Vorbericht 01 Allgemeines sind zusammengestellt")

    docbuilder.builddocx(template=hhstpl, context=contexthhsatzung, filename="00-Haushaltssatzung", gde=gde, hhj=hhj)
    print("Haushaltssatzung erstellt in Ordner")

    # build "03_Vorbericht" Information about closed year



    # build "04_Vorbericht" Information about last year




    # build "05_Vorbericht" Gesamtergebnisplan





    # build "06_Vorbericht" Erträge im Ergebnishaushalt




    #build "07_Vorbericht" Aufwendungen im Ergebnishaushalt