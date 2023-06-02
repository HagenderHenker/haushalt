import matplotlib.pyplot as plt
import seaborn as sns

import data_09_statistik as stat
import pandas as pd 
import numpy as np

def hebesatzentwicklung(df):
    ''' 
    Entwicklung der Hebesätze
    this function creates a lineplot of the development of the taxrates (Realsteuerhebesätze)
    for Grundsteuer A, Grundsteuer B and Gewerbesteuer
    It takes a Dataframe created in "data_09_statistik.py" from the /hhdaten/grunddaten.xlsx
    '''

    