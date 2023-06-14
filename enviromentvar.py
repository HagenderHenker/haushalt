import pathlib

'''
***************** A C H T U N G *****************
ATTENTION ATTENTION ATTENTION ATTENTION ATTENTION 
*************************************************

Es ist wichtig, dass für die einzulesenden Dateien

bewegungsdaten.xlsx

und

grunddaten.xlsx

keine Veränderungen an der Struktur vorgenommen werden.
Daten MÜSSEN in der vorgegebenen Struktur eingegeben werden!

'''
# Gemeinde
gde = 60

# Haushaltsjahr
hhj = 2023


# Datei für die Bewegungsdaten des Haushaltsplans
bewDat = str(pathlib.Path.cwd() / "hhdaten/bewegungsdaten.xlsx")

# Datei für die Grunddaten des Haushaltsplans
grunddaten = str(pathlib.Path.cwd() / "hhdaten/grunddaten.xlsx")

# Templates Haushaltssatzung und Vorbericht
hhstpl = str(pathlib.Path.cwd() / "wordtemplates/hhs.docx")
vorb01tpl = str(pathlib.Path.cwd() / "wordtemplates/02_Vorbericht_Allgemeines.docx")


# Quelle für die Flächenstatistik
quelleflaechendaten = "Statistisches Landesamt RLP, 2021"

# Quelle der Einwohnerstatistik
quelleewdaten = "Komwisberichte"


