import pandas as pd
import numpy as np
import pathlib
from datetime import date

def hhdata_excelimport(xlsxfile):
    df = pd.read_excel(xlsxfile, 0, 
                   # decimal = ",",
                   # encoding = "latin1",
                   #thousands = ".",
                   names = ["hhs", "produkt", "mn", "sk", "bez", "th", "dk", "anshhj", "sollhhj", "ansvj", "sollvj", "planvvj", "rgergvvj", "rgergvj", "rgakt", "plan1", "plan2", "plan3", "ve"],
                   dtype= {"hhs": str,
                           "produkt": str,
                           "bez": str,
                           "th": str,
                           "dk": str} 
                   )

    return df

def hhdata_clipboardimport():
    df = pd.read_clipboard(
                   # decimal = ",",
                   # encoding = "latin1",
                   #thousands = ".",
                   names = ["hhs", "produkt", "mn", "sk", "bez", "th", "dk", "anshhj", "sollhhj", "ansvj", "sollvj", "planvvj", "rgergvvj", "rgergvj", "rgakt", "plan1", "plan2", "plan3", "ve"],
                   dtype= {"hhs": str,
                           "produkt": str,
                           "bez": str,
                           "th": str,
                           "dk": str} 
                   )
    return df

def mn_excelimport(xlsxfile):
    df = pd.read_excel(xlsxfile, 1)
    return df

def prod_excelimport(xlsxfile):
    df = pd.read_excel(xlsxfile, 2)
    return df

def readgrunddatengde(xlsfile, gdenr):
    df = pd.read_excel(xlsfile, sheet_name="gde",)
    dfgde = df.loc[(df["gdenr"] == gdenr)]
    return dfgde

def readgrunddatenhh(xlsfile, gdenr, hhj):
    df = pd.read_excel(xlsfile, sheet_name="hhdaten",)
    dfhh = df.loc[(df["gdenr"] == gdenr) & (df["hhj"] == hhj)]
    return dfhh

def hhsatzungekentwicklung(xlsfile, gdenr, hhj):
       df = pd.read_excel(xlsfile, sheet_name="JAWerte")
       dfhh = df.loc[(df["gdenr"] == gdenr) & (df["hhj"] == hhj)]
       return dfhh

def readewstatistik_wohn(xlsfile, gdenr, jahr):
    df = pd.read_excel(xlsfile, sheet_name="ew_wohn")
       
    dfewdata = df.loc[(df["gdenr"] == gdenr) & (df["datum"] <= np.datetime64(date(year=jahr, month = 6, day = 30))) &  (df["datum"] >= np.datetime64(date(year=jahr-10, month=6, day=30)))]
    
    return dfewdata

#df = readewstatistik_wohn(xlsfile=str(pathlib.Path.cwd() / "hhdaten/grunddaten.xlsx"), gdenr=60, jahr=2022)
#print(df)





