# Emprendiendo — instrucciones del repositorio

Herramientas de IA para emprender: prompts en español que se usan **después** de que la persona hizo el trabajo. Proyecto personal de Andrés Saldarriaga Navarro, publicado en `github.com/MenteSimple/Emprendiendo` bajo CC BY-SA 4.0.

## Lo que este repositorio no es

⛔ **No es material de ninguna universidad.** Nada acá puede nombrar una institución, usar sus marcas, ni suponer que quien lee está matriculado en algo. Los criterios salen del método propio del autor, pero el vocabulario del aula se cuela solo —«la entrega», «la sesión», «su equipo del curso»—. Antes de publicar cualquier herramienta:

```bash
grep -rniE "uniandes|universidad|facultad|admi|nrc|bloque ne[óo]n|brightspace|syllabus|la entrega|la sesi[óo]n" --include='*.md' --include='*.txt' .
```

Y para los `.xlsx`, mirar también adentro: el texto de las celdas no aparece en un `grep` normal.

## Estructura

Una carpeta por herramienta. `README.md` es la **fuente única**; `prompt.txt` se genera de su primer bloque de código.

```
<etapa>/NN-nombre-herramienta/
├── README.md      qué es, cuándo se usa, el prompt, qué revisar
├── prompt.txt     generado — NO editar a mano
└── <archivos>     lo que esa herramienta necesite
```

```bash
python3 extraer-prompts.py            # regenera
python3 extraer-prompts.py --revisar  # avisa si alguno quedó viejo, sale con 1
```

⛔ **Nunca editar `prompt.txt` directamente.** Se corrige el README y se regenera.

## El principio

**Divergir con la máquina, converger uno mismo.** En la fase de generar, la IA amplía sin límite y hay que usarla a fondo. En la fase de decidir, no decide: pide el trabajo ya hecho, busca el punto débil y devuelve la pregunta.

## Las nueve reglas, y de dónde salió cada una

Todas salen de correr la herramienta 01 contra Copilot, Gemini y Claude el 19 de agosto de 2026. Ninguna es teórica.

**1 · Puerta de entrada.** El prompt pide contexto propio antes de producir nada. Las de divergencia preguntan para quién, dónde y en qué sector; las de convergencia piden el trabajo hecho con sus razones. Funcionó en los tres motores.

**2 · Una sola pausa permitida, y declarada.** Los pasos van de corrido en una sola respuesta. Cada pregunta a mitad de camino es una oportunidad de que la persona conteste cualquier cosa con tal de avanzar. *Origen:* Claude se frenó en el Paso 4 porque «Escoge 3 de las anteriores» se leyó como pregunta al usuario; hubo que responder «escoge tú».

**3 · Verificar con un dato que el modelo no pueda inventar.** Si se le da la frase exacta con la que debe certificar algo, la escribe sin hacer nada: una plantilla de verificación es un formulario en blanco. Hay que pedirle un dato que solo exista si de verdad hizo el trabajo — el texto de una celda que no aparezca en el prompt, por ejemplo. *Origen:* Gemini 3.5 Flash-Lite, que no ejecuta código y no generó ningún archivo, escribió igual «Leído del archivo · contadores 15/34/14 · fórmulas intactas».

**4 · Que declare qué hizo.** No se puede impedir que un modelo desobedezca, pero sí obligarlo a confesarlo con una línea fija. Un fallo declarado se corrige; uno silencioso se entrega. *Origen:* Copilot no pudo abrir la plantilla y fabricó un `.xlsx` nuevo —con las hojas correctas y sin fórmulas ni listas—, y solo se supo porque lo mencionó de pasada.

**5 · No ofrecer una alternativa que no se haya probado sola.** Dos caminos que parecen equivalentes y no lo son son peores que uno. *Origen:* se agregó «bájala de esta URL» como alternativa a adjuntar el archivo. Ninguno de los tres motores pudo: adjuntar el archivo es lo que activa el entorno de código, así que la segunda vía dependía de la primera. Le costó tres corridas fallidas.

**6 · Leer primero lo que el material propio ya dice adentro.** Si la herramienta entrega un archivo, ese archivo suele traer instrucciones, y el prompt no puede contradecirlas. *Origen:* el prompt decía «20 filas, Origen X» y el panel de la plantilla decía que las de SCAMPER van también en esa hoja con meta 34. Gemini le hizo caso a la plantilla —con razón— y marcó mal la columna.

**7 · Las reglas operativas al prompt; el porqué al README.** El modelo necesita la regla; la explicación la lee una persona. Un prompt que lleva ensayos adentro crece sin mejorar y se vuelve incómodo de pegar en un celular.

**8 · Los conteos son piso, no meta.** Un modelo que pide 15 devuelve 15 o 20. Si el número importa, hay que decirlo dos veces y pedir el conteo real al final.

**9 · Marcar lo generado.** Todo lo que produjo la máquina va señalado como tal, y esa marca no se puede confundir con la del trabajo de la persona. Sirve para lo único que importa después: ver qué sobrevivió al filtro, si lo propio o lo generado.

## Cómo se prueba, antes de publicar

⛔ **No probar en la misma conversación donde se escribió el prompt.** El resultado sale contaminado: quien escribió el prompt sabe lo que quería decir. Se corre en **contexto aislado** —una ventana nueva, o un subagente que solo recibe el texto del prompt— simulando ser un chat común.

Mínimo dos corridas por herramienta, con casos distintos:

1. **El caso claro.** Alguien que responde bien a todo. Verifica conteos, formato y que no se frene.
2. **El caso torcido.** Alguien que responde mal a propósito —varios grupos a la vez, «no sé», o sin haber hecho el trabajo previo—. Verifica que las defensas disparen.

Y si la herramienta entrega archivo, una tercera: **sin adjuntar nada**, para comprobar que se detiene y lo pide en vez de fabricarlo.

## Qué revisar en cada corrida

- ¿Respetó los conteos exactos?
- ¿Se frenó a preguntar algo fuera de la única pausa permitida?
- ¿Declaró la ruta o el camino que tomó?
- ¿La verificación se apoya en un dato real o repitió la plantilla?
- ¿Marcó como conjetura lo que no puede saber?
- ¿El formato de salida se puede pegar donde tiene que ir?

## El modelo importa

Las versiones ligeras —Flash-Lite y equivalentes— **no ejecutan código**: no devuelven archivos por más que afirmen que sí. Documentarlo en el README de cualquier herramienta que dependa de un archivo.

## Convenciones de escritura

- Español de Colombia, tratamiento de **usted** con quien lee.
- Sin saltos de línea duros: un párrafo es una sola línea.
- Nada codificado solo por color; el estado lo lleva un símbolo con silueta propia.
- Los archivos del repo **no llevan frontmatter**: se leen en GitHub, no en Obsidian.
- Commits en español, explicando el porqué y no solo el qué.

## Agent skills

### Issue tracker

Los issues, specs y mapas de `/wayfinder` viven en GitHub Issues de `MenteSimple/Emprendiendo`, con el CLI `gh`. El repositorio es **público**: todo ticket nace publicado, así que el `grep` institucional aplica antes de escribirlo, no antes de publicarlo. Ver `docs/agents/issue-tracker.md`.

### Triage labels

Las cinco etiquetas canónicas, sin renombrar. Ver `docs/agents/triage-labels.md`.

### Domain docs

Contexto único: `CONTEXT.md` y `docs/adr/` en la raíz, creados solo cuando haya algo que escribir. Ver `docs/agents/domain.md`.
