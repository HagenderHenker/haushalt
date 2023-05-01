import pandas as pd
import plotly.express as px
import plotly.graph_objects as gp
import dataimport as di
import pathlib
import datetime as dt


def gr_populationdevelopment(xlsfile, gde, hhj):
    data = di.readewstatistik_wohn(xlsfile=xlsfile, gdenr=gde, jahr=hhj-1)
    data["gesamt"] =  data["maennl"] + data["weibl"]
    data["jahr"] = pd.to_datetime(data["datum"]).dt.year


    #print(data)
    dn = data[["jahr", "gesamt"]].loc[data["wohnstatus"] == "Einwohner mit Hauptwohnung"]
    dn = dn.set_index("jahr", drop=True)
    return dn


df = gr_populationdevelopment(xlsfile=str(pathlib.Path.cwd() / "hhdaten/grunddaten.xlsx"), gde=60, hhj=2023)
print(df)