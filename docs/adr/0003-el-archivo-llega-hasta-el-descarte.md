# 0003 · El archivo llega hasta el descarte, y de ahí en adelante es texto

**Estado:** aceptada · 22 de agosto de 2026

## Contexto

Las herramientas de este repositorio son prompts que se pegan en cualquier asistente, desde un celular, sin instalar nada. Pero las que entregan un archivo rompen esa promesa: **los modelos ligeros no ejecutan código** y no devuelven archivos por más que afirmen que sí. Está probado y documentado.

Al rediseñar la etapa apareció la pregunta de si las herramientas siguientes —hipótesis y guía de entrevistas— también deberían trabajar sobre un archivo.

## Decisión

**El archivo llega hasta el descarte y no más allá.** El generador de ideas produce la hoja, el descarte la recibe y la devuelve, y de ahí en adelante todo es texto que se pega y se copia.

## Por qué

Porque el archivo se gana el puesto cuando hay muchas filas y columnas que marcar —treinta ideas por tres cortes es una tabla, y una tabla pide una hoja de cálculo—. La hipótesis son dos frases y la guía de entrevistas es una lista de preguntas: prosa, en un sitio donde una hoja de cálculo estorba.

Y cada archivo nuevo vuelve a excluir a quien usa un modelo ligero. Con este corte, de cuatro herramientas solo dos dependen de un archivo.

## Consecuencias

- Las herramientas de hipótesis y de entrevistas funcionan en cualquier asistente y desde un celular.
- Las dos que sí dependen de archivo tienen que documentar en su README que necesitan un modelo con ejecución de código.
- Si más adelante la captura de hallazgos de campo necesita una plantilla, esa decisión se toma aparte: es tabular y podría ganarse su propio archivo.
