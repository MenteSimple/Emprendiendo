# Emprendiendo — instrucciones del repositorio

Herramientas de IA para emprender: prompts en español que se usan **después** de que la persona hizo el trabajo. Proyecto personal de Andrés Saldarriaga Navarro, publicado en `github.com/MenteSimple/Emprendiendo` bajo CC BY-SA 4.0.

**Divergir con la máquina, converger uno mismo.** En la fase de generar, la IA amplía sin límite y hay que usarla a fondo. En la fase de decidir, no decide: pide el trabajo ya hecho, busca el punto débil y devuelve la pregunta.

## Dónde vive cada cosa

| Cuando toca | Ir a |
|---|---|
| Retomar en frío: en qué va cada herramienta y qué sigue | `ESTADO.md` |
| Escribir una herramienta nueva, reescribir una vieja o corregir un prompt que falló | subagente `redactor` |
| Correr un prompt en limpio: la clara, la torcida, la incompleta | subagente `probador-aislado` |
| Decidir si algo se puede publicar o mezclar a `main` | subagente `auditor` |
| Las reglas de los prompts, y el porqué de cada una | `COMO-ESCRIBIR-ESTAS-HERRAMIENTAS.md` — **fuente única** |

Escribir o corregir un prompt sin pasar por `redactor` no exime de ninguna regla: se leen en `COMO-ESCRIBIR-ESTAS-HERRAMIENTAS.md` y se aplican una por una.

## El grep institucional

⛔ **Ninguna institución nombrada, ninguna marca ajena, ningún supuesto de que quien lee está matriculado en algo.** Los criterios salen del método propio del autor y esto le escribe a emprendedores. El vocabulario del aula se cuela solo —«la entrega», «la sesión», «su equipo del curso»—, así que antes de escribir un ticket, publicar una herramienta o mezclar a `main` hay que correr **el grep institucional**:

```bash
grep -rniE "uniandes|universidad|facultad|\badmi\b|\bnrc\b|bloque ne[óo]n|brightspace|syllabus|la entrega|la sesi[óo]n|estudiante|alumn[oa]|profesor|docente|\bcursos?\b|semestre|r[úu]brica|calificaci[óo]n|matriculad|c[áa]tedra" --include='*.md' --include='*.txt' .
```

Los `.xlsx` no los ve un `grep`: hay que abrir cada hoja con `~/.venvs/skills/bin/python` y openpyxl —el `python3` de Homebrew no tiene las dependencias— y revisar el texto de las celdas contra la misma lista, paneles de instrucciones y encabezados incluidos.

## Los prompt.txt se generan

Una carpeta por herramienta. Su `README.md` es la **fuente única**: `prompt.txt` sale del primer bloque de código. Para cambiar un prompt se corrige el README y se regenera.

```bash
python3 extraer-prompts.py            # regenera
python3 extraer-prompts.py --revisar  # sin salida y código 0 = todos sincronizados
```

⛔ Nunca editar un `prompt.txt` a mano.

## Probar, siempre en limpio

La corrida la hace `probador-aislado`, que recibe el texto del prompt y nada más: ni los README, ni las reglas, ni la intención de quien lo escribió. ⛔ En la misma conversación donde se escribió el prompt el resultado sale contaminado, porque quien lo escribió sabe lo que quiso decir.

Las versiones ligeras —Flash-Lite y equivalentes— **no ejecutan código** y no devuelven archivos por más que afirmen que sí. Documentarlo en el README de cualquier herramienta que dependa de un archivo.

## Convenciones de escritura

- Español de Colombia, tratamiento de **usted** con quien lee.
- Sin saltos de línea duros: un párrafo es una sola línea.
- Nada codificado solo por color; el estado lo lleva un símbolo con silueta propia.
- Los archivos del repo **no llevan frontmatter**: se leen en GitHub, no en Obsidian.
- Commits en español, explicando el porqué y no solo el qué.

## Agent skills

### Issue tracker

Los issues, specs y mapas de `/wayfinder` viven en GitHub Issues de `MenteSimple/Emprendiendo`, con el CLI `gh`. El repositorio es **público**: todo ticket nace publicado, así que el grep institucional aplica antes de escribirlo, no antes de publicarlo. Ver `docs/agents/issue-tracker.md`.

### Triage labels

Las cinco etiquetas canónicas, sin renombrar. Ver `docs/agents/triage-labels.md`.

### Domain docs

Contexto único: `CONTEXT.md` y `docs/adr/` en la raíz, creados solo cuando haya algo que escribir. Ver `docs/agents/domain.md`.
