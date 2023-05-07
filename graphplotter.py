import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as gp
import dataimport as di
import pathlib
import datetime as dt
import matplotlib.pyplot as plt

def gr_populationdevelopment(xlsfile, gde, hhj):
    data = di.readewstatistik_wohn(xlsfile=xlsfile, gdenr=gde, jahr=hhj-1)
    data["gesamt"] =  data["maennl"] + data["weibl"]
    data["jahr"] = pd.to_datetime(data["datum"]).dt.year


    #print(data)
    dn = data[["jahr", "gesamt"]].loc[data["wohnstatus"] == "Einwohner mit Hauptwohnung"]
    dn = dn.set_index("jahr", drop=True)
    return dn

"""
def plot_gr_popdev(xlsfile, gde, hhj):
    data = gr_populationdevelopment(xlsfile=xlsfile, gde=gde, hhj=hhj)
    fig = px.line(data_frame=data             )
    fig.show()
"""

def plot_gr_popdev(xlsfile, gde, hhj):
    data = gr_populationdevelopment(xlsfile=xlsfile, gde=gde, hhj=hhj)
    
    plt.plot(data['gesamt'], color='blue', marker='o')
    plt.title('Bevölkerungsentwicklung', fontsize=14)
    plt.xlabel('Jahr', fontsize=12)
    plt.yticks(np.arange(3000, 5000, step = 1000))
    plt.ylabel('Anzahl Einwohner', fontsize=12)
    plt.grid(True)


    for year in np.sort(data.index):
        plt.annotate(str(data.loc[year]["gesamt"]), xy=(year, data.loc[year]["gesamt"]), xytext=(year, (data.loc[year]["gesamt"])-200))

   
    plt.savefig(str(pathlib.Path.cwd() / "hhdaten/plots/bev-entw.png"))

plot_gr_popdev(xlsfile=str(pathlib.Path.cwd() / "hhdaten/grunddaten.xlsx"), gde=60, hhj=2023)
