# Estado del repositorio

Actualizado: **19 de agosto de 2026, 11:42 p. m.**

## Dónde va cada herramienta

| # | Herramienta | Escrita | Probada | Publicada |
|---|---|---|---|---|
| 01 | Generador de ideas | ✅ | ✅ Copilot · Gemini · Claude | ✅ |
| 02 | Descarte y filtros | ✅ **sin probar** | ⛔ | ✅ el código, no la validación |
| 03 | ¿Problema o solución? | ⚠️ borrador viejo | ⛔ | ⚠️ versión previa a los aprendizajes |
| 04 | Afilador del reto | ⚠️ borrador viejo | ⛔ | ⚠️ versión previa a los aprendizajes |

## Lo que hay que hacer, en orden

**1 · Probar la 02.** Está escrita con las reglas de `COMO-ESCRIBIR-ESTAS-HERRAMIENTAS.md` —falta confirmar la de la orden en imperativo, que no estaba en la lista de `CLAUDE.md` cuando se escribió— y con su plantilla `plantilla-descarte.xlsx`, pero **no se ha corrido ni una vez**. Faltan las tres corridas en contexto aislado que hace `probador-aislado`: el caso claro, el torcido —descartes sin motivo, sobrevivientes con «un tipo de persona» en el corte 2— y el de sin adjuntar archivo. Sin eso no se le puede dar a nadie.

**2 · Sacar «el estudiante» de la 01.** El grep institucional ampliado encontró seis usos en `descubrir/01-generador-de-ideas/README.md` —líneas 133, 138, 140, 147, 154 y 199, con su espejo en `prompt.txt`— donde «el estudiante» es quien usa la herramienta. Es la violación exacta que prohíbe la regla ⛔, y el patrón viejo no la veía: salió de casualidad porque `admi` hace match con «admitirlo». Los de la línea 49 y los de la 04 son distintos —ahí «estudiantes» es un ejemplo de segmento de clientes— y se quedan. Corregir el README desincroniza el `prompt.txt`, así que hay que regenerar y volver a correr la 01: es la única probada que hay, y el cambio la deja sin validar.

**3 · Rehacer la 03 y la 04.** Las que están publicadas son borradores del principio de la sesión, escritos bajo un principio que después resultó equivocado —«interroga, no produce»— y sin ninguna de las diez reglas. Hay que reescribirlas desde cero conservando lo que sigue siendo válido: las tres categorías de enunciado en la 03, y la plantilla «A ___ le cuesta ___ porque ___» con sus ejemplos en la 04.

Decisión ya tomada sobre archivos: la 03 **no** lleva plantilla —es un enunciado y una respuesta en un minuto— y la 04 tampoco, pero devuelve la frase en un formato fijo.

**4 · Volver a auditar antes de publicar.** El grep institucional de `CLAUDE.md`, y para los `.xlsx` mirar también el texto de las celdas.

## Lo que quedó decidido y no hay que volver a discutir

- El repositorio es un proyecto personal, no material institucional. Nada puede remitir a ninguna universidad.
- `README.md` de cada herramienta es la fuente; `prompt.txt` se genera con `extraer-prompts.py`.
- Las reglas operativas van al prompt; las explicaciones, al README.
- Se prueba en contexto aislado, nunca en la conversación donde se escribió.
- Verificar siempre con un dato que el modelo no pueda inventar.

## La 02, en detalle, por si se retoma en frío

Su plantilla tiene tres hojas —`Descartadas`, `Sobrevivientes`, `Finalistas`— y una columna `Revisión` en cada una que **solo llena la herramienta**. El equipo llena el resto, incluidos los motivos de cada descarte: sin motivos escritos el prompt se detiene y los pide, porque el filtro es el razonamiento y no la lista.

Los rótulos testigo están en `Descartadas!F11:F13` — «Descartes revisados», «Motivos escritos», «Sin motivo»— y **no aparecen en el prompt**, verificado. Sirven para comprobar que el modelo abrió el archivo de verdad.

Riesgo conocido y no probado: el prompt le prohíbe tocar cualquier columna que no sea `Revisión`. No sé si lo respeta. Es lo primero que hay que mirar en la corrida de prueba.
