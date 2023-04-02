import docxtpl
import jinja2
import contextbuilder
import pathlib

def builddocx(template, context, filename):
    tpl = docxtpl.DocxTemplate(template)

    tpl.render(context)
    tpl.save(filename+'.docx')


# Haushaltssatzung

hhsatzung_tpl = pathlib.Path()
hhsatzung_context = contextbuilder.hhsatzung()

builddocx(hhsatzung_tpl, hhsatzung_context, "01_HH-Satzung" )

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
builddocx(hhvorb_vj_tpl, hhvorb_vj_context, "04_VorberichtVVJ")

# Vorbericht Überblick Ergebnishaushalt

hhvorb_ueberg_tpl = pathlib.Path()
hhvorb_ueberg_context = contextbuilder.hh_vorb_ueberg()
builddocx(hhvorb_ueberg_tpl, hhvorb_ueberg_context, "05_Vorbericht_uebersicht_erghh")

# Vorbericht Erträge
hvorb_ueberg_tpl = pathlib.Path()
hhvorb_ueberg_context = contextbuilder.hh_vorb_ueberg()
builddocx(hhvorb_ueberg_tpl, hhvorb_ueberg_context, "06_Vorbericht_aenderungenErtraege")

# Vorbericht Aufwand
hvorb_ueberg_tpl = pathlib.Path()
hhvorb_ueberg_context = contextbuilder.hh_vorb_ueberg()
builddocx(hhvorb_ueberg_tpl, hhvorb_ueberg_context, "07_Vorbericht_aenderungenAufwand")


# Vorbericht Überblick Finanzen
hvorb_ueberg_tpl = pathlib.Path()
hhvorb_ueberg_context = contextbuilder.hh_vorb_ueberg()
builddocx(hhvorb_ueberg_tpl, hhvorb_ueberg_context, "08_Vorbericht_ueb_FinHH")

# Vorbericht Finanzhaushalt Investitionen

hvorb_ueberg_tpl = pathlib.Path()
hhvorb_ueberg_context = contextbuilder.hh_vorb_ueberg()
builddocx(hhvorb_ueberg_tpl, hhvorb_ueberg_context, "09_Vorbericht_Invest")

# Vorbericht Kredit und Bestände

hvorb_ueberg_tpl = pathlib.Path()
hhvorb_ueberg_context = contextbuilder.hh_vorb_ueberg()
builddocx(hhvorb_ueberg_tpl, hhvorb_ueberg_context, "10_Kredit_und_bestand")

# Vorbericht Pflichtanlagen

hvorb_ueberg_tpl = pathlib.Path()
hhvorb_ueberg_context = contextbuilder.hh_vorb_ueberg()
builddocx(hhvorb_ueberg_tpl, hhvorb_ueberg_context, "05_Vorberichtueberg")