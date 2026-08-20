# Estado del repositorio

Actualizado: **20 de agosto de 2026**

## Dónde va cada herramienta

| # | Herramienta | Escrita | Probada | Publicada |
|---|---|---|---|---|
| 01 | Generador de ideas | ✅ | ✅ Copilot · Gemini · Claude | ✅ |
| 02 | Descarte y filtros | ✅ auditada y corregida, **sin probar** | ⛔ | ✅ el código, no la validación |
| 03 | ¿Problema o solución? | ⚠️ borrador viejo | ⛔ | ⚠️ versión previa a los aprendizajes |
| 04 | Afilador del reto | ⚠️ borrador viejo | ⛔ | ⚠️ versión previa a los aprendizajes |

## Lo que hay que hacer, en orden

**1 · Probar la 02.** Ya está auditada y corregida —ver abajo qué tenía—, y ahora sí lo único que falta son las tres corridas en contexto aislado que exige `CLAUDE.md`: el caso claro, el torcido —descartes sin motivo, sobrevivientes con «un tipo de persona» en el corte 2, columnas de corte vacías— y el de sin adjuntar archivo. Sin eso no se le puede dar a nadie.

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

Riesgos conocidos y todavía no probados, para mirar en la primera corrida:

- El prompt le prohíbe tocar cualquier columna que no sea `Revisión`. No sé si lo respeta. Es lo primero que hay que mirar.
- Si con las columnas nuevas el modelo de verdad juzga cada corte por la suya, o si sigue deduciendo de la línea de la idea cuando la columna está vacía.
- Al guardar con `openpyxl` los contadores `=COUNTA(...)` quedan sin valor en caché y se ven vacíos hasta que Excel recalcule. Ya está avisado en el README; hay que confirmar que sigan siendo fórmulas y no números.
