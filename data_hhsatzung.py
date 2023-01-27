
import pandas as pd
import numpy as np



df = pd.read_excel("HHDaten.xlsx", 0, 
                   # decimal = ",",
                   # encoding = "latin1",
                   #thousands = ".",
                   names = ["hhs", "produkt", "mn", "sk", "bez", "th", "dk", "anshhj", "sollhhj", "ansvj", "sollvj", "rgergvvj", "rgergvj", "rgakt", "plan1", "plan2", "plan3", "ve"],
                   dtype= {"hhs": str,
                           "produkt": str,
                           "bez": str,
                           "th": str,
                           "dk": str} 
                   )

#df.head()
#dfert = df.loc[df["sk"]<500000]
#dfert.head()

       

ertrag_gesamt = df.loc[(df["sk"]<500000)]["anshhj"].sum()
aufwand_gesamt = df.loc[(df["sk"]<600000) & (df["sk"]>500000)]["anshhj"].sum()
erg_saldo = ertrag_gesamt - aufwand_gesamt

saldo_vj = df.loc[(df["sk"]<500000)]["ansvj"].sum() - df.loc[(df["sk"]<600000) & (df["sk"]>500000)]["ansvj"].sum()

lfd_ez = df.loc[(df["sk"]<670000) & (df["sk"]>600000)]["anshhj"].sum()
lfd_az = df.loc[(df["sk"]<770000) & (df["sk"]>700000)]["anshhj"].sum()
lfd_saldo = lfd_ez - lfd_az

fin_ez = df.loc[(df["sk"]<680000) & (df["sk"]>670000)]["anshhj"].sum()
fin_az = df.loc[(df["sk"]<780000) & (df["sk"]>770000)]["anshhj"].sum()
fin_saldo = fin_ez - fin_az

ord_ez = lfd_ez + fin_ez
ord_az = lfd_az + fin_az
ord_saldo = ord_ez - ord_az

inv_ez = df.loc[(df["sk"]<690000) & (df["sk"]>680000)]["anshhj"].sum()
inv_az = df.loc[(df["sk"]<790000) & (df["sk"]>780000)]["anshhj"].sum()
inv_saldo = inv_ez - inv_az

ft_ez = df.loc[(df["sk"]<700000) & (df["sk"]>690000)]["anshhj"].sum()
ft_az = df.loc[(df["sk"]<800000) & (df["sk"]>790000)]["anshhj"].sum()
ft_saldo = ft_ez - ft_az

ikred_aufnahme = df.loc[(df["sk"]<693000) & (df["sk"]>692000)]["anshhj"].sum()
ve_gesamt = df["ve"].sum()

ve_kredfin = ve_gesamt - gde.ve_zinslos