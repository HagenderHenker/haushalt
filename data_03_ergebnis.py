import dataimport as di  
import pandas as pd
import pathlib


def gesamtplan_erg(xlsfile, hhj, gde):
    df = di.hhdata_excelimport(xlsxfile=xlsfile)
    
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

print(gesamtplan_erg(xlsfile=str(pathlib.Path.cwd() / "haushalt/hhdaten/bewegungsdaten.xlsx"), hhj=2023, gde=60))