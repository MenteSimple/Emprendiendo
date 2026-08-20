#!/usr/bin/env python3
"""Genera `plantilla-descarte.xlsx`, la hoja de trabajo del filtro.

El equipo la llena con lo que YA decidió —incluidos los motivos de cada
descarte— y la herramienta de IA agrega la columna «Revisión» sin tocar lo
demás. Sin motivos escritos no hay nada que auditar, así que el archivo
mismo hace cumplir la puerta de entrada.

    python3 generar-plantilla.py

Las celdas de la columna F de `Descartadas` son rótulos que NO aparecen en el
prompt: sirven de testigo para comprobar que el modelo abrió el archivo de
verdad y no se limitó a repetir la frase de verificación.
"""

from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

SALIDA = Path(__file__).resolve().parent / "plantilla-descarte.xlsx"

AZUL, CREMA, BORDE_COLOR = "1F3A5F", "F1EEE7", "BFBFBF"
FILAS = 24

HOJAS = {
    "Descartadas": ["#", "La idea, en una línea", "El motivo que dimos", "Revisión"],
    "Sobrevivientes": ["#", "La idea, en una línea", "¿Con quién hablamos?", "¿Quién lo consigue?", "Revisión"],
    "Finalistas": ["Criterio", "① ", "② ", "③ ", "Revisión"],
}

CRITERIOS = [
    "Deseabilidad — ¿alguien lo quiere de verdad?",
    "Factibilidad — ¿se puede construir con lo que existe hoy?",
    "Viabilidad — ¿hay forma de que se sostenga?",
    "Encaje con el equipo — ¿lo podemos hacer NOSOTROS?",
]

# Rótulos testigo: no deben aparecer nunca en el prompt.
TESTIGOS = ["Descartes revisados", "Motivos escritos", "Sin motivo"]

AYUDA = {
    "Descartadas": (
        "Una fila por idea que botaron.\n\n"
        "• El motivo va con las palabras de ustedes, no en bonito. «Ya existe algo así» se escribe tal cual.\n"
        "• Sin motivo escrito la revisión no sirve: el filtro es el razonamiento, no la lista.\n"
        "• La columna Revisión la llena la herramienta. Déjenla vacía."
    ),
    "Sobrevivientes": (
        "Las que pasaron los tres cortes.\n\n"
        "• «¿Con quién hablamos?» se responde con un nombre o un lugar concreto. Un tipo de persona no cuenta.\n"
        "• «¿Quién lo consigue?» es alguien del equipo, con nombre.\n"
        "• La columna Revisión la llena la herramienta."
    ),
    "Finalistas": (
        "Los tres que quedaron, comparados.\n\n"
        "• Estos cuatro criterios no son binarios: tienen matices y de eso se trata la conversación.\n"
        "• El cuarto es el que más se deja en blanco y el que más pesa en un plazo corto.\n"
        "• «Nos parece interesante» no es encaje: encaje es qué sabe este equipo, a quién conoce y a qué tiene acceso."
    ),
}


def encabezar(hoja, titulos):
    for j, texto in enumerate(titulos, start=1):
        c = hoja.cell(row=1, column=j, value=texto)
        c.font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
        c.fill = PatternFill("solid", fgColor=AZUL)
        c.alignment = Alignment(horizontal="center", vertical="center")
    hoja.row_dimensions[1].height = 24
    hoja.freeze_panes = "A2"


def main() -> None:
    wb = Workbook()
    borde = Border(*[Side(style="thin", color=BORDE_COLOR)] * 4)

    for nombre, titulos in HOJAS.items():
        hoja = wb.active if nombre == "Descartadas" else wb.create_sheet()
        hoja.title = nombre
        encabezar(hoja, titulos)

        filas = len(CRITERIOS) if nombre == "Finalistas" else FILAS
        for i in range(filas):
            r = i + 2
            if nombre == "Finalistas":
                hoja.cell(row=r, column=1, value=CRITERIOS[i]).alignment = Alignment(wrap_text=True, vertical="top")
            else:
                hoja.cell(row=r, column=1, value=i + 1).alignment = Alignment(horizontal="center")
            for j in range(1, len(titulos) + 1):
                c = hoja.cell(row=r, column=j)
                c.border = borde
                if j > 1:
                    c.alignment = Alignment(wrap_text=True, vertical="top")
            hoja.row_dimensions[r].height = 30

        anchos = [5, 46, 34, 34, 40] if nombre == "Sobrevivientes" else [5, 46, 40, 44]
        if nombre == "Finalistas":
            anchos = [34, 28, 28, 28, 40]
        for j, w in enumerate(anchos[: len(titulos)], start=1):
            hoja.column_dimensions[get_column_letter(j)].width = w

        # panel de ayuda, a la derecha
        col = len(titulos) + 2
        letra = get_column_letter(col)
        hoja.column_dimensions[letra].width = 52
        p = hoja.cell(row=2, column=col, value=AYUDA[nombre])
        p.alignment = Alignment(wrap_text=True, vertical="top")
        p.fill = PatternFill("solid", fgColor=CREMA)
        hoja.merge_cells(start_row=2, start_column=col, end_row=9, end_column=col)

    # contadores y testigos, solo en Descartadas
    h = wb["Descartadas"]
    for i, (rotulo, formula) in enumerate(zip(
        TESTIGOS,
        [f"=COUNTA(D2:D{FILAS+1})", f"=COUNTA(C2:C{FILAS+1})",
         f"=COUNTA(B2:B{FILAS+1})-COUNTA(C2:C{FILAS+1})"],
    )):
        h.cell(row=11 + i, column=6, value=rotulo).font = Font(bold=True)
        h.cell(row=11 + i, column=7, value=formula)
    h.column_dimensions["G"].width = 12

    dv = DataValidation(type="list", formula1='"sí,no"', allow_blank=True, showDropDown=False)
    wb["Sobrevivientes"].add_data_validation(dv)
    dv.add(f"C2:C{FILAS+1}")

    wb.save(SALIDA)
    print(f"✅ {SALIDA.name} · hojas: {', '.join(HOJAS)} · testigos en F11:F13 de Descartadas")


if __name__ == "__main__":
    main()
