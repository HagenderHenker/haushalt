import dataimport as di 
import contextbuilder as ctx
import docbuilder
import pathlib

gde = 60
hhj = 2023
grunddaten = str(pathlib.Path.cwd() / "hhdaten/grunddaten.xlsx")

bewegungsdaten = str(pathlib.Path.cwd() / "hhdaten/bewegungsdaten.xlsx")




hhstpl = str(pathlib.Path.cwd() / "wordtemplates/hhs.docx")


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

    # build "Haushaltssatzung"

    contexthhsatzung = ctx.hhsatzung(gde = gde, hhj = hhj, xlsgrunddaten = grunddaten, xlsbewegung = bewegungsdaten)
    print("Data for 'Haushaltssatzung' is compiled")
    for k in contexthhsatzung:
        print(f"{k} - {contexthhsatzung[k]} -type: {type(contexthhsatzung[k])}" )
    
    """
    #test
    cont = {}
    cont["gde_bez"] = contexthhsatzung["gde_bez"]
    cont["hhj"] = contexthhsatzung["hhj"]
    print(cont)
    """

    docbuilder.builddocx(template=hhstpl, context=contexthhsatzung, filename="00-Haushaltssatzung", gde=gde, hhj=hhj)
    print("Haushaltssatzung erstellt in Ordner")
