# Estado del repositorio

Actualizado: **20 de agosto de 2026**

## Dónde va cada herramienta

| # | Herramienta | Escrita | Probada | Publicada |
|---|---|---|---|---|
| 01 | Generador de ideas | ✅ | ✅ Copilot · Gemini · Claude | ✅ |
| 02 | Descarte y filtros | ✅ auditada y corregida | ✅ tres corridas en contexto aislado, 20 de agosto | ✅ |
| 03 | ¿Problema o solución? | ⚠️ borrador viejo | ⛔ | ⚠️ versión previa a los aprendizajes |
| 04 | Afilador del reto | ⚠️ borrador viejo | ⛔ | ⚠️ versión previa a los aprendizajes |

## Lo que hay que hacer, en orden

**1 · La 02 está lista, salvo por un detalle.** Las tres corridas en contexto aislado pasaron el 20 de agosto —el caso claro, el torcido y el de sin adjuntar archivo— y están contadas en su README. Queda vivo un defecto menor: el límite de «máximo dos frases» se pasó en 4 de las 26 revisiones escritas. Decidir si se corrige y se vuelve a correr, o si se publica así y queda anotado.

Falta también lo que necesita a una persona presente: correrla en varios motores. La 01 se probó en tres; esta, en uno solo.

**2 · Rehacer la 03 y la 04.** Las que están publicadas son borradores del principio de la sesión, escritos bajo un principio que después resultó equivocado —«interroga, no produce»— y sin ninguna de las nueve reglas. Hay que reescribirlas desde cero conservando lo que sigue siendo válido: las tres categorías de enunciado en la 03, y la plantilla «A ___ le cuesta ___ porque ___» con sus ejemplos en la 04.

Decisión ya tomada sobre archivos: la 03 **no** lleva plantilla —es un enunciado y una respuesta en un minuto— y la 04 tampoco, pero devuelve la frase en un formato fijo.

**3 · Volver a auditar antes de publicar.** El `grep` institucional de `CLAUDE.md`, y para los `.xlsx` mirar también el texto de las celdas.

## Lo que quedó decidido y no hay que volver a discutir

- El repositorio es un proyecto personal, no material institucional. Nada puede remitir a ninguna universidad.
- `README.md` de cada herramienta es la fuente; `prompt.txt` se genera con `extraer-prompts.py`.
- Las reglas operativas van al prompt; las explicaciones, al README.
- Se prueba en contexto aislado, nunca en la conversación donde se escribió.
- Verificar siempre con un dato que el modelo no pueda inventar.

## La 02, en detalle, por si se retoma en frío

Su plantilla tiene tres hojas —`Descartadas`, `Sobrevivientes`, `Finalistas`— y una columna `Revisión` en cada una que **solo llena la herramienta**. El equipo llena el resto, incluidos los motivos de cada descarte: sin motivos escritos el prompt se detiene y los pide, porque el filtro es el razonamiento y no la lista.

Los rótulos testigo están en `Descartadas!F11:F13` — «Descartes revisados», «Motivos escritos», «Sin motivo»— y **no aparecen en el prompt**, verificado. Sirven para comprobar que el modelo abrió el archivo de verdad.

**No estaba «solo sin probar».** La auditoría del 20 de agosto le encontró cinco defectos, ya corregidos, que habrían hecho fracasar la primera corrida y habrían hecho creer que el fallo era del modelo:

1. Una lista desplegable «sí,no» colgaba de `Sobrevivientes!C2:C25`, que es «¿Con quién hablamos?». Excel la aplica con bloqueo duro: no se podía escribir un nombre en la única columna donde el prompt exige un nombre.
2. La hoja solo tenía columna para el corte 2. Los cortes 1 y 3 había que adivinarlos de la línea de la idea.
3. `Finalistas` no tenía dónde escribir los nombres de los tres, así que la revisión solo podía decir «el ②».
4. El Paso 1 declaraba dos pausas y abría una tercera con «pregúntamelo si no te lo di» sobre el plazo.
5. Se ofrecía pegar las ideas en el chat como alternativa al archivo, sin haberla corrido nunca — la regla 5, otra vez.

Los tres riesgos que estaban sin probar, ya probados el 20 de agosto:

- **Respeta la columna `Revisión`.** Comparadas celda por celda las dos corridas con archivo contra su original: cero celdas modificadas afuera, en ninguna de las tres hojas, y ninguna celda vacía del equipo rellenada.
- **Juzga cada corte por su columna.** En el caso torcido marcó los cortes como no pasados por columna vacía, sin deducirlos de la línea de la idea.
- **Las `=COUNTA(...)` sobreviven como fórmulas**, no convertidas en números. Se ven vacías hasta que Excel recalcule, como estaba previsto.
