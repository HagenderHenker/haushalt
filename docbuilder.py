import docxtpl
import jinja2
import contextbuilder
import pathlib



def builddocx(template, context, filename, gde, hhj):

    def ec(number):
        eurofied = "{:,.2f}".format(number).replace(",", "x").replace(".", ",").replace("x", ".")
        return eurofied

    def ecp(number):
        euro = "{:,}".format(number).replace(",", ".")
        return euro


    env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath="."), 
                             trim_blocks=True,
                             lstrip_blocks=True)
    env.filters["ec"] = ec
    #env.filters["ecp"] = ec
    env.filters["ecp"] = ecp

    gdepfad = pathlib.Path.cwd() /f"Ausgabe/{gde}"
    hhpfad = pathlib.Path.cwd() /f"Ausgabe/{gde}/{hhj}"


    tpl = docxtpl.DocxTemplate(template)
    tpl.render(context, env)

    if not pathlib.Path(gdepfad).exists():
        pathlib.Path.mkdir(gdepfad)
    
    if not pathlib.Path(hhpfad).exists:
        pathlib.Path.mkdir(hhpfad)

    tpl.save(pathlib.Path(f"{hhpfad}/{filename}.docx"))

"""
# Haushaltssatzung

hhsatzung_tpl = pathlib.Path()
hhsatzung_context = contextbuilder.hhsatzung()

builddocx(hhsatzung_tpl, hhsatzung_context, "01_HH-Satzung" )
"""
"""
# Vorbericht Allgemeines

hhvorb_allg_tpl = pathlib.Path()
hhvorb_allg_context = contextbuilder.hh_vorb_allg()
builddocx(hhvorb_allg_tpl, hhvorb_allg_context, "02_VorberichtAllgemein")

# Vorbericht VVJ

hhvorb_vvj_tpl = pathlib.Path()
hhvorb_vvj_context = contextbuilder.hh_vorb_vvj()
builddocx(hhvorb_vvj_tpl, hhvorb_vvj_context, "03_VorberichtVVJ")

# Vorbericht VJ

hhvorb_vj_tpl = pathlib.Path()
hhvorb_vj_context = contextbuilder.hh_vorb_vj()
builddocx(hhvorb_vj_tpl, hhvorb_vj_context, "04_VorberichtVJ")

# Vorbericht Überblick Ergebnishaushalt

vorbericht_uebersicht_erghh_tpl = pathlib.Path()
vorbericht_uebersicht_erghh_context = contextbuilder.vorbericht_uebersicht_erghh()
builddocx(vorbericht_uebersicht_erghh_tpl, vorbericht_uebersicht_erghh_context, "05_Vorbericht_uebersicht_erghh")

# Vorbericht Erträge
vorbericht_aenderungenErtraege_tpl = pathlib.Path()
vorbericht_aenderungenErtraege_context = contextbuilder.vorbericht_aenderungenErtraege()
builddocx(vorbericht_aenderungenErtraege_tpl, vorbericht_aenderungenErtraege_context, "06_Vorbericht_aenderungenErtraege")

# Vorbericht Aufwand
vorbericht_aenderungenAufwand_tpl = pathlib.Path()
vorbericht_aenderungenAufwand_context = contextbuilder.vorbericht_aenderungenAufwand()
builddocx(vorbericht_aenderungenAufwand_tpl, vorbericht_aenderungenAufwand_context, "07_Vorbericht_aenderungenAufwand")


# Vorbericht Überblick Finanzen
vorbericht_ueb_FinHH_tpl = pathlib.Path()
vorbericht_ueb_FinHH_context = contextbuilder.vorbericht_ueb_FinHH()
builddocx(vorbericht_ueb_FinHH_tpl, vorbericht_ueb_FinHH_context, "08_Vorbericht_ueb_FinHH")

# Vorbericht Finanzhaushalt Investitionen

hvorb_ueberg_tpl = pathlib.Path()
hhvorb_ueberg_context = contextbuilder.vorbericht_Invest()
builddocx(hhvorb_ueberg_tpl, hhvorb_ueberg_context, "09_Vorbericht_Invest")

# Vorbericht Kredit und Bestände

hvorb_ueberg_tpl = pathlib.Path()
hhvorb_ueberg_context = contextbuilder.kredit_und_bestand()
builddocx(hhvorb_ueberg_tpl, hhvorb_ueberg_context, "10_Kredit_und_bestand")

# Vorbericht Pflichtanlagen

hvorb_ueberg_tpl = pathlib.Path()
hhvorb_ueberg_context = contextbuilder.Vorbericht_Pflichtanlagen()
builddocx(hhvorb_ueberg_tpl, hhvorb_ueberg_context, "11_Vorbericht_Pflichtanlagen")
"""