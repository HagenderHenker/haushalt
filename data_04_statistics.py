"""
Provide the statistics Data needed for the document
"""


class EW:
    def __init__(self, quelleflaeche):
        self.EW_akt = 				                #Aktuelle Einwohnerzahl
        img_einwohnerentwicklung:	        #Graph der Einwohnerentwicklung der letzten 10 Jahre
        img_altersstruktur:		            #Graph, Alterspyramide der Einwohner/Bürger
        img_struktur_altersgruppebis20:     #Graph der Einwohnerentwicklung bis 20 Jahre
        quelleewdaten:			            #Woher stammen die Einwohnerdaten
        flaeche:			                #Gesamtfläche der Gemeinde in km²
        img_flaeche:			            #Graph der Flächennutzung
        self.quelleflaeche	= quelleflaeche		            #Woher stammen die Flächendaten

    def getewdata(self):
        pass

    def addewdata(self):
        pass
