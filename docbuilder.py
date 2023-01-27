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

builddocx(hhsatzung_tpl, hhsatzung_context, "HH-Satzung" )