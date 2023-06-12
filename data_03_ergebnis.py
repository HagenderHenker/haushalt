import dataimport as di  
import pandas as pd
import pathlib


def gesamtplan_erg(df):
        
    # Summenermittlung für den Gesamtplan
    dic = {
    "e_p_steuern"	: df.loc[(df["sk"]<410000)]["anshhj"].sum(),
    "e_v_steuern"	: df.loc[(df["sk"]<410000)]["ansvj"].sum(),
    "e_re_steuern" : df.loc[(df["sk"]<410000)]["rgergvvj"].sum(),
    "e_p_tranfer"	: df.loc[(df["sk"]<420000) & (df["sk"]>410000)]["anshhj"].sum(),
    "e_v_tranfer"	: df.loc[(df["sk"]<420000) & (df["sk"]>410000)]["ansvj"].sum(),
    "e_re_tranfer" : df.loc[(df["sk"]<420000) & (df["sk"]>410000)]["rgergvvj"].sum(),
    "e_p_sozE" : df.loc[(df["sk"]<430000) & (df["sk"]>420000)]["anshhj"].sum(),
    "e_v_sozE"  : df.loc[(df["sk"]<430000) & (df["sk"]>420000)]["ansvj"].sum(),
    "e_re_sozE" : df.loc[(df["sk"]<430000) & (df["sk"]>420000)]["rgergvvj"].sum(),
    "e_p_oerLeist" : df.loc[(df["sk"]<440000) & (df["sk"]>430000)]["anshhj"].sum(),
    "e_v_oerLeist" : df.loc[(df["sk"]<440000) & (df["sk"]>430000)]["ansvj"].sum(),	
    "e_re_oerLeist" : df.loc[(df["sk"]<440000) & (df["sk"]>430000)]["rgergvvj"].sum(),
    "e_p_prLeist"	: df.loc[(df["sk"]<420000) & (df["sk"]>410000)]["anshhj"].sum(),
    "e_v_prLeist"	: df.loc[(df["sk"]<420000) & (df["sk"]>410000)]["ansvj"].sum(),
    "e_re_prLeist" : df.loc[(df["sk"]<420000) & (df["sk"]>410000)]["rgergvvj"].sum(),
    "e_p_koste"	: df.loc[(df["sk"]<420000) & (df["sk"]>410000)]["anshhj"].sum(),
    "e_v_koste"	: df.loc[(df["sk"]<420000) & (df["sk"]>410000)]["ansvj"].sum(),
    "e_re_koste": df.loc[(df["sk"]<420000) & (df["sk"]>410000)]["rgergvvj"].sum(),
    "e_p_sonstE"	: df.loc[(df["sk"]<420000) & (df["sk"]>410000)]["anshhj"].sum(),
    "e_v_sonstE" : df.loc[(df["sk"]<420000) & (df["sk"]>410000)]["ansvj"].sum(),
    "e_re_sonstE" : df.loc[(df["sk"]<420000) & (df["sk"]>410000)]["rgergvvj"].sum(),
    "e_p_summeE" : df.loc[(df["sk"]<470000)]["anshhj"].sum(),
    "e_v_summeE" : df.loc[(df["sk"]<470000)]["ansvj"].sum(),
    "e_re_summeE" : df.loc[(df["sk"]<470000)]["rgergvvj"].sum(),
    "e_p_pers" : df.loc[(df["sk"]<520000) & (df["sk"]>500000)]["anshhj"].sum(),
    "e_v_pers" : df.loc[(df["sk"]<520000) & (df["sk"]>500000)]["ansvj"].sum(),
    "e_re_pers" : df.loc[(df["sk"]<520000) & (df["sk"]>500000)]["rgergvvj"].sum(),
    "e_p_msd" : df.loc[(df["sk"]<530000) & (df["sk"]>520000)]["anshhj"].sum(),
    "e_v_msd" : df.loc[(df["sk"]<530000) & (df["sk"]>520000)]["ansvj"].sum(),
    "e_re_msd" : df.loc[(df["sk"]<530000) & (df["sk"]>520000)]["rgergvvj"].sum(),
    "e_p_afa" : df.loc[(df["sk"]<540000) & (df["sk"]>530000)]["anshhj"].sum(),	
    "e_v_afa" : df.loc[(df["sk"]<540000) & (df["sk"]>530000)]["ansvj"].sum(),
    "e_re_afa" : df.loc[(df["sk"]<540000) & (df["sk"]>530000)]["rgergvvj"].sum(),
    "e_p_umla" : df.loc[(df["sk"]<550000) & (df["sk"]>540000)]["anshhj"].sum(),
    "e_v_umla" : df.loc[(df["sk"]<550000) & (df["sk"]>540000)]["ansvj"].sum(),
    "e_re_umla" : df.loc[(df["sk"]<550000) & (df["sk"]>540000)]["rgergvvj"].sum(),
    "e_p_sozA" :df.loc[(df["sk"]<560000) & (df["sk"]>550000)]["anshhj"].sum(),
    "e_v_sozA" : df.loc[(df["sk"]<560000) & (df["sk"]>550000)]["ansvj"].sum(),
    "e_re_sozA" : df.loc[(df["sk"]<560000) & (df["sk"]>550000)]["rgergvvj"].sum(),
    "e_p_sonstA" : df.loc[(df["sk"]<570000) & (df["sk"]>560000)]["anshhj"].sum(),	
    "e_v_sonstA" : df.loc[(df["sk"]<570000) & (df["sk"]>560000)]["ansvj"].sum(),	
    "e_re_sonstA" : df.loc[(df["sk"]<570000) & (df["sk"]>560000)]["rgergvvj"].sum(),
    "e_p_summeA" : df.loc[(df["sk"]<570000) & (df["sk"]>500000)]["anshhj"].sum(),
    "e_v_summeA" : df.loc[(df["sk"]<570000) & (df["sk"]>500000)]["ansvj"].sum(),
    "e_re_summeA" : df.loc[(df["sk"]<570000) & (df["sk"]>500000)]["rgergvvj"].sum(),
    "e_p_saldolfd" : df.loc[(df["sk"]<470000) & (df["sk"]>400000)]["anshhj"].sum() - df.loc[(df["sk"]<570000) & (df["sk"]>500000)]["anshhj"].sum(),	
    "e_v_saldolfd" : df.loc[(df["sk"]<470000) & (df["sk"]>400000)]["ansvj"].sum() - df.loc[(df["sk"]<570000) & (df["sk"]>500000)]["ansvj"].sum(),	
    "e_re_saldolfd" : df.loc[(df["sk"]<470000) & (df["sk"]>400000)]["rgergvvj"].sum() - df.loc[(df["sk"]<570000) & (df["sk"]>500000)]["rgergvvj"].sum(),
    "e_p_finE" : df.loc[(df["sk"]<480000) & (df["sk"]>470000)]["anshhj"].sum(),
    "e_v_finE" : df.loc[(df["sk"]<480000) & (df["sk"]>470000)]["ansvj"].sum(),
    "e_re_finE" : df.loc[(df["sk"]<480000) & (df["sk"]>470000)]["rgergvvj"].sum(),
    "e_p_finA" : df.loc[(df["sk"]<580000) & (df["sk"]>570000)]["anshhj"].sum(),
    "e_v_finA" : df.loc[(df["sk"]<580000) & (df["sk"]>570000)]["ansvj"].sum(),
    "e_re_finA" : df.loc[(df["sk"]<580000) & (df["sk"]>570000)]["rgergvvj"].sum(),
    "e_p_finSaldo" : df.loc[(df["sk"]<480000) & (df["sk"]>470000)]["anshhj"].sum() - df.loc[(df["sk"]<580000) & (df["sk"]>570000)]["anshhj"].sum(),	
    "e_v_finSaldo" : df.loc[(df["sk"]<480000) & (df["sk"]>470000)]["ansvj"].sum() - df.loc[(df["sk"]<580000) & (df["sk"]>570000)]["ansvj"].sum(),	
    "e_re_finSaldo" : df.loc[(df["sk"]<480000) & (df["sk"]>470000)]["rgergvvj"].sum() - df.loc[(df["sk"]<580000) & (df["sk"]>570000)]["rgergvvj"].sum(),	
    "e_p_ordErg" : df.loc[(df["sk"]<480000) & (df["sk"]>400000)]["anshhj"].sum() - df.loc[(df["sk"]<580000) & (df["sk"]>500000)]["anshhj"].sum(),	
    "e_v_ordErg" : df.loc[(df["sk"]<480000) & (df["sk"]>400000)]["ansvj"].sum() - df.loc[(df["sk"]<580000) & (df["sk"]>500000)]["ansvj"].sum(),
    "e_re_ordErg" : df.loc[(df["sk"]<480000) & (df["sk"]>400000)]["rgergvvj"].sum() - df.loc[(df["sk"]<580000) & (df["sk"]>500000)]["rgergvvj"].sum(),
    "e_p_je" : df.loc[(df["sk"]<500000) & (df["sk"]>400000)]["anshhj"].sum() - df.loc[(df["sk"]<600000) & (df["sk"]>500000)]["anshhj"].sum(),
    "e_v_je" : df.loc[(df["sk"]<500000) & (df["sk"]>400000)]["ansvj"].sum() - df.loc[(df["sk"]<600000) & (df["sk"]>500000)]["ansvj"].sum(),
    "e_re_je" : df.loc[(df["sk"]<500000) & (df["sk"]>400000)]["rgergvvj"].sum() - df.loc[(df["sk"]<600000) & (df["sk"]>500000)]["rgergvvj"].sum(),
    }

    return(dic)

def get_hhst_dict(df, dferl, minsk, maxsk):
    """
    Gibt ein dictionary nach Sachkonten gefiltert zurück  
    df = Dataframe mit den Haushaltsstellendaten
    dferl = Dataframe mit Erläuterungen
    minsk = kleinster Sachkontowert
    maxsk = größter Sachkontowert

    Return: gefilterter Dataframe wird in eine dict-liste umgewandelt
    """
    teildf = df.loc[df["sk"] < 410000]   
    #print(dferl)
    dferl["sk"] = dferl["sk"].fillna(0).astype("int")
    #print(dferl)
    dfnew = pd.merge(teildf, dferl, how = "left", left_on= ["produkt", "sk"], right_on=["produkt", "sk"])
    dfnew = dfnew.drop(["hh", "mn_y", "erlNr", "erlTyp", "nicht uebertragbar"], axis=1)
    #print(dfnew)
    st = dfnew[["hhs","sk", "produkt", "bez", "anshhj", "ansvj", "rgergvvj", "erl"]].to_dict('records')
    return st



def get_steuern(df, dferl):
   """
   Gibt ein dictionary zurück 
   """
   teildf = df.loc[df["sk"] < 410000]   
   #print(dferl)
   dferl["sk"] = dferl["sk"].fillna(0).astype("int")
   #print(dferl)
   dfnew = pd.merge(teildf, dferl, how = "left", left_on= ["produkt", "sk"], right_on=["produkt", "sk"])
   dfnew = dfnew.drop(["hh", "mn_y", "erlNr", "erlTyp", "nicht uebertragbar"], axis=1)
   #print(dfnew)
   st = dfnew[["hhs","sk", "produkt", "bez", "anshhj", "ansvj", "rgergvvj", "erl"]].to_dict('records')
   return st

def get_umlagen(df, dferl):
   teildf = df.loc[(df["sk"]<420000) & (df["sk"]>410000)]
   #print(dferl)
   dferl["sk"] = dferl["sk"].fillna(0).astype("int")
   #print(dferl)
   dfnew = pd.merge(teildf, dferl, how = "left", left_on= ["produkt", "sk"], right_on=["produkt", "sk"])
   dfnew = dfnew.drop(["hh", "mn_y", "erlNr", "erlTyp", "nicht uebertragbar"], axis=1)
   #print(dfnew)
   st = dfnew[["hhs","sk", "produkt", "bez", "anshhj", "ansvj", "rgergvvj", "erl"]].to_dict('records')
   return st

def get_sozE(df, dferl):
   teildf = df.loc[(df["sk"]<430000) & (df["sk"]>420000)]
   #print(dferl)
   dferl["sk"] = dferl["sk"].fillna(0).astype("int")
   #print(dferl)
   dfnew = pd.merge(teildf, dferl, how = "left", left_on= ["produkt", "sk"], right_on=["produkt", "sk"])
   dfnew = dfnew.drop(["hh", "mn_y", "erlNr", "erlTyp", "nicht uebertragbar"], axis=1)
   #print(dfnew)
   st = dfnew[["hhs","sk", "produkt", "bez", "anshhj", "ansvj", "rgergvvj", "erl"]].to_dict('records')
   return st

def get_oerE(df, dferl):
   teildf = df.loc[(df["sk"]<440000) & (df["sk"]>430000)]
      #print(dferl)
   dferl["sk"] = dferl["sk"].fillna(0).astype("int")
   #print(dferl)
   dfnew = pd.merge(teildf, dferl, how = "left", left_on= ["produkt", "sk"], right_on=["produkt", "sk"])
   dfnew = dfnew.drop(["hh", "mn_y", "erlNr", "erlTyp", "nicht uebertragbar"], axis=1)
   #print(dfnew)
   st = dfnew[["hhs","sk", "produkt", "bez", "anshhj", "ansvj", "rgergvvj", "erl"]].to_dict('records')
   return st

def get_prE(df, dferl):
   teildf = df.loc[(df["sk"]<442000) & (df["sk"]>440000)]
      #print(dferl)
   dferl["sk"] = dferl["sk"].fillna(0).astype("int")
   #print(dferl)
   dfnew = pd.merge(teildf, dferl, how = "left", left_on= ["produkt", "sk"], right_on=["produkt", "sk"])
   dfnew = dfnew.drop(["hh", "mn_y", "erlNr", "erlTyp", "nicht uebertragbar"], axis=1)
   #print(dfnew)
   st = dfnew[["hhs","sk", "produkt", "bez", "anshhj", "ansvj", "rgergvvj", "erl"]].to_dict('records')
   return st

def get_kostE(df, dferl):
   teildf = df.loc[(df["sk"]<450000) & (df["sk"]>442000)]
      #print(dferl)
   dferl["sk"] = dferl["sk"].fillna(0).astype("int")
   #print(dferl)
   dfnew = pd.merge(teildf, dferl, how = "left", left_on= ["produkt", "sk"], right_on=["produkt", "sk"])
   dfnew = dfnew.drop(["hh", "mn_y", "erlNr", "erlTyp", "nicht uebertragbar"], axis=1)
   #print(dfnew)
   st = dfnew[["hhs","sk", "produkt", "bez", "anshhj", "ansvj", "rgergvvj", "erl"]].to_dict('records')
   return st

def get_sonstE(df, dferl):
   teildf = df.loc[(df["sk"]<470000) & (df["sk"]>460000)]
      #print(dferl)
   dferl["sk"] = dferl["sk"].fillna(0).astype("int")
   #print(dferl)
   dfnew = pd.merge(teildf, dferl, how = "left", left_on= ["produkt", "sk"], right_on=["produkt", "sk"])
   dfnew = dfnew.drop(["hh", "mn_y", "erlNr", "erlTyp", "nicht uebertragbar"], axis=1)
   #print(dfnew)
   st = dfnew[["hhs","sk", "produkt", "bez", "anshhj", "ansvj", "rgergvvj", "erl"]].to_dict('records')
   return st

def get_finE(df, dferl):
   teildf = df.loc[(df["sk"]<480000) & (df["sk"]>470000)]
      #print(dferl)
   dferl["sk"] = dferl["sk"].fillna(0).astype("int")
   #print(dferl)
   dfnew = pd.merge(teildf, dferl, how = "left", left_on= ["produkt", "sk"], right_on=["produkt", "sk"])
   dfnew = dfnew.drop(["hh", "mn_y", "erlNr", "erlTyp", "nicht uebertragbar"], axis=1)
   #print(dfnew)
   st = dfnew[["hhs","sk", "produkt", "bez", "anshhj", "ansvj", "rgergvvj", "erl"]].to_dict('records')
   return st

def get_persA(df, dferl):
   teildf = df.loc[(df["sk"]<520000) & (df["sk"]>500000)]
      #print(dferl)
   dferl["sk"] = dferl["sk"].fillna(0).astype("int")
   #print(dferl)
   dfnew = pd.merge(teildf, dferl, how = "left", left_on= ["produkt", "sk"], right_on=["produkt", "sk"])
   dfnew = dfnew.drop(["hh", "mn_y", "erlNr", "erlTyp", "nicht uebertragbar"], axis=1)
   #print(dfnew)
   st = dfnew[["hhs","sk", "produkt", "bez", "anshhj", "ansvj", "rgergvvj", "erl"]].to_dict('records')
   return st

def get_msdA(df, dferl):
   teildf = df.loc[(df["sk"]<530000) & (df["sk"]>520000)]
      #print(dferl)
   dferl["sk"] = dferl["sk"].fillna(0).astype("int")
   #print(dferl)
   dfnew = pd.merge(teildf, dferl, how = "left", left_on= ["produkt", "sk"], right_on=["produkt", "sk"])
   dfnew = dfnew.drop(["hh", "mn_y", "erlNr", "erlTyp", "nicht uebertragbar"], axis=1)
   #print(dfnew)
   st = dfnew[["hhs","sk", "produkt", "bez", "anshhj", "ansvj", "rgergvvj", "erl"]].to_dict('records')
   return st

def get_AfA(df, dferl):
   teildf = df.loc[(df["sk"]<540000) & (df["sk"]>530000)]
      #print(dferl)
   dferl["sk"] = dferl["sk"].fillna(0).astype("int")
   #print(dferl)
   dfnew = pd.merge(teildf, dferl, how = "left", left_on= ["produkt", "sk"], right_on=["produkt", "sk"])
   dfnew = dfnew.drop(["hh", "mn_y", "erlNr", "erlTyp", "nicht uebertragbar"], axis=1)
   #print(dfnew)
   st = dfnew[["hhs","sk", "produkt", "bez", "anshhj", "ansvj", "rgergvvj", "erl"]].to_dict('records')
   return st

def get_UmlA(df, dferl):
   teildf = df.loc[(df["sk"]<550000) & (df["sk"]>540000)]
   #print(dferl)
   dferl["sk"] = dferl["sk"].fillna(0).astype("int")
   #print(dferl)
   dfnew = pd.merge(teildf, dferl, how = "left", left_on= ["produkt", "sk"], right_on=["produkt", "sk"])
   dfnew = dfnew.drop(["hh", "mn_y", "erlNr", "erlTyp", "nicht uebertragbar"], axis=1)
   #print(dfnew)
   st = dfnew[["hhs","sk", "produkt", "bez", "anshhj", "ansvj", "rgergvvj", "erl"]].to_dict('records')
   return st

def get_sozA(df, dferl):
   teildf = df.loc[(df["sk"]<560000) & (df["sk"]>550000)]
   #print(dferl)
   dferl["sk"] = dferl["sk"].fillna(0).astype("int")
   #print(dferl)
   dfnew = pd.merge(teildf, dferl, how = "left", left_on= ["produkt", "sk"], right_on=["produkt", "sk"])
   dfnew = dfnew.drop(["hh", "mn_y", "erlNr", "erlTyp", "nicht uebertragbar"], axis=1)
   #print(dfnew)
   st = dfnew[["hhs","sk", "produkt", "bez", "anshhj", "ansvj", "rgergvvj", "erl"]].to_dict('records')
   return st

def get_sonstA(df, dferl):
   teildf = df.loc[(df["sk"]<570000) & (df["sk"]>560000)]
      #print(dferl)
   dferl["sk"] = dferl["sk"].fillna(0).astype("int")
   #print(dferl)
   dfnew = pd.merge(teildf, dferl, how = "left", left_on= ["produkt", "sk"], right_on=["produkt", "sk"])
   dfnew = dfnew.drop(["hh", "mn_y", "erlNr", "erlTyp", "nicht uebertragbar"], axis=1)
   #print(dfnew)
   st = dfnew[["hhs","sk", "produkt", "bez", "anshhj", "ansvj", "rgergvvj", "erl"]].to_dict('records')
   return st

def get_finA(df, dferl):
   teildf = df.loc[(df["sk"]<580000) & (df["sk"]>570000)]
      #print(dferl)
   dferl["sk"] = dferl["sk"].fillna(0).astype("int")
   #print(dferl)
   dfnew = pd.merge(teildf, dferl, how = "left", left_on= ["produkt", "sk"], right_on=["produkt", "sk"])
   dfnew = dfnew.drop(["hh", "mn_y", "erlNr", "erlTyp", "nicht uebertragbar"], axis=1)
   #print(dfnew)
   st = dfnew[["hhs","sk", "produkt", "bez", "anshhj", "ansvj", "rgergvvj", "erl"]].to_dict('records')
   return st

def get_ilvE(df, dferl):
   teildf = df.loc[(df["sk"]<490000) & (df["sk"]>480000)]
      #print(dferl)
   dferl["sk"] = dferl["sk"].fillna(0).astype("int")
   #print(dferl)
   dfnew = pd.merge(teildf, dferl, how = "left", left_on= ["produkt", "sk"], right_on=["produkt", "sk"])
   dfnew = dfnew.drop(["hh", "mn_y", "erlNr", "erlTyp", "nicht uebertragbar"], axis=1)
   #print(dfnew)
   st = dfnew[["hhs","sk", "produkt", "bez", "anshhj", "ansvj", "rgergvvj", "erl"]].to_dict('records')
   return st

def get_ilfA(df, dferl):
   teildf = df.loc[(df["sk"]<590000) & (df["sk"]>580000)]
      #print(dferl)
   dferl["sk"] = dferl["sk"].fillna(0).astype("int")
   #print(dferl)
   dfnew = pd.merge(teildf, dferl, how = "left", left_on= ["produkt", "sk"], right_on=["produkt", "sk"])
   dfnew = dfnew.drop(["hh", "mn_y", "erlNr", "erlTyp", "nicht uebertragbar"], axis=1)
   #print(dfnew)
   st = dfnew[["hhs","sk", "produkt", "bez", "anshhj", "ansvj", "rgergvvj", "erl"]].to_dict('records')
   return st

if __name__ == "__main__":
   print(gesamtplan_erg(xlsfile=str(pathlib.Path.cwd() / "haushalt/hhdaten/bewegungsdaten.xlsx"), hhj=2023, gde=60))