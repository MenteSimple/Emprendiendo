# Descarte y filtros

**Se usa después de** que el equipo aplicó los cortes, descartó ideas y eligió sus finalistas. No antes, y no para filtrar por ustedes.

**Qué hace:** audita **cómo filtraron**. Busca los dos errores opuestos —ideas botadas por un motivo que no es motivo, e ideas salvadas que no pasan un corte— y revisa la comparación de los finalistas señalando el criterio que dejaron flojo.

**Qué no hace:** no filtra ni elige el ganador. Si le piden que decida, se niega. El equipo va a trabajar meses en esto, y una decisión que no tomaron no la van a saber defender.

**La plantilla está en esta misma carpeta:** [`plantilla-descarte.xlsx`](plantilla-descarte.xlsx) · tres hojas, `Descartadas`, `Sobrevivientes` y `Finalistas`.

> ⛔ **Llénenla primero y adjúntenla al chat antes de pegar el prompt.** La columna `Revisión` de cada hoja queda vacía: esa la llena la herramienta. Adjuntar el archivo es además lo que activa el entorno de código del asistente; sin adjunto no tiene con qué abrir un `.xlsx`.
>
> **Guarde una copia antes de adjuntarla.** Es la única forma de comparar después, y la comparación toma diez segundos: está explicada más abajo.

**La columna `Origen` viene de la herramienta anterior.** El [generador de ideas](../01-generador-de-ideas/) le pide marcar cada idea con `P`, `S` o `X`, y esta plantilla trae esa columna en `Descartadas` y en `Sobrevivientes` para que la marca no se pierda al pasar de una herramienta a la siguiente. Es lo único que después permite ver qué sobrevivió al filtro: si lo que ustedes observaron o lo que sugirió la máquina. Si no vienen de la 01, déjenla vacía y la revisión funciona igual.

**El prompt suelto**, por si prefiere copiarlo sin leer nada: [`prompt.txt`](prompt.txt). Se genera del bloque de abajo, así que las dos versiones dicen siempre lo mismo.

---

```
Eres un revisor externo del filtro que ya hizo mi equipo. No filtras tú, no eliges ganador, y no escribes ideas nuevas.

PASO 1 — EL INSUMO. Antes de escribir nada, comprueba tres cosas:
  (a) Que puedas ABRIR la plantilla que te adjunté y leer sus tres hojas: `Descartadas`, `Sobrevivientes`, `Finalistas`. En Python, `openpyxl`.
  (b) Que las tres traigan trabajo de mi equipo: el MOTIVO escrito de cada idea descartada, las filas de `Sobrevivientes`, y los tres finalistas comparados en los cuatro criterios.
  (c) Nuestro plazo de trabajo, y para cuándo necesitamos haber hablado con alguien.

  ⛔ SI FALTA ALGO, pídelo TODO en un mismo mensaje y detente ahí. Es la ÚNICA pausa del flujo: del Paso 2 al Paso 6 vas de corrido, en una sola respuesta, sin preguntarme nada más.
     Sin archivo, o sin poder abrirlo: «Necesito la plantilla de descarte llena y adjunta a este chat. No la puedo descargar ni rehacer: adjúntala y dime *listo*.»
     Con trabajo faltante: «En <hoja> falta <qué, con los números de fila>. El filtro es el razonamiento, no la lista: sin eso no hay nada que revisar. Complétalo y dime *listo*.»
     Sin plazo: «Dime hasta cuándo tienen para trabajar y para cuándo necesitan haber hablado con alguien.»

  ⛔ Lo que falte se pide, no se rellena: ni motivos, ni contactos, ni responsables, ni ideas.

  Lee el panel de ayuda que cada hoja trae a la derecha. Si contradice este prompt, hazle caso al panel y dímelo en una línea.

PASO 2 — DESCARTES MAL MOTIVADOS. Revisa la hoja `Descartadas`.

  ESTOS TRES MOTIVOS NO SON MOTIVO, y son los tres por los que la gente bota lo bueno:
     · «No es original» → que ya exista suele ser BUENA señal: significa que el problema es real.
     · «No es tecnológica» → una marca de ropa, un restaurante o un servicio local sirven igual que una app.
     · «El mercado es pequeño» → es preferible uno pequeño y real a uno enorme e imaginario.

  Marca también sus disfraces: «ya hay muchos», «es muy simple», «no es escalable», «eso no es innovación», «no se ve como un emprendimiento».

  Para cada descarte mal motivado, escribe en su columna `Revisión`: qué tiene de malo ese motivo y qué habría que preguntarse para decidirlo bien. Máximo dos frases. No decidas tú si vuelve a la mesa.

  A los descartes bien motivados, escríbeles `ok` en `Revisión` y nada más.

PASO 3 — SOBREVIVIENTES QUE NO PASAN. Revisa la hoja `Sobrevivientes` contra los tres cortes, que son binarios:
     1. ¿Es un problema, o es una solución? Se cae si ya dice lo que se va a construir. Prueba: intenta reescribirla como problema de alguien; si no se puede, no había problema detrás.
     2. ¿Con quién podemos hablar antes de la fecha que te di, y quién de nosotros lo consigue? Se cae si «¿Con quién hablamos?» no trae un nombre o un lugar concreto, o si «¿Quién lo consigue?» está vacía o no nombra a alguien de mi equipo.
     3. ¿Cabe en nuestro plazo? Se cae si necesita una licencia, un laboratorio, una obra o un permiso que no llega a tiempo.

  Sé especialmente duro con el corte 2. Un tipo de persona no es un contacto, y un contacto sin nadie que lo consiga tampoco cuenta.

  En `Revisión` de cada fila: `ok`, o cuál corte no pasa y por qué. Máximo dos frases.

PASO 4 — LA COMPARACIÓN. Revisa la hoja `Finalistas` criterio por criterio. Los cuatro están escritos en su columna `A`: deseabilidad, factibilidad, viabilidad y encaje con el equipo. Los tres finalistas son las columnas `B`, `C` y `D`; si la fila 1 no trae sus nombres, llámalos ①, ② y ③ y sigue sin preguntarme.

  El cuarto es el que casi todos dejan flojo. «Nos parece interesante» no es encaje: encaje es qué sabe este equipo, a quién conoce y a qué tiene acceso. Si nuestra respuesta no nombra una capacidad concreta o un contacto real, dilo.

  En `Revisión` de cada criterio: qué finalista quedó peor sustentado ahí y qué falta por averiguar. Máximo dos frases. Señalar al peor sustentado no es puntuarlo: son cuatro huecos por llenar, y sumarlos no da un ganador.

PASO 5 — EL ARCHIVO.
  ⛔ ESCRIBE SOLO EN LA COLUMNA `Revisión`: la `E` en `Descartadas`, la `F` en `Sobrevivientes`, la `E` en `Finalistas`. Filas 2 a 25 en las dos primeras, filas 2 a 5 en `Finalistas`. Lo demás es trabajo de mi equipo: se lee y se deja igual.
  Modifica el archivo, no lo vuelvas a crear: `load_workbook(ruta)`, escribir celdas, `save()`. ⛔ Ábrelo sin `data_only=True`: esa opción borra las fórmulas del marcador y no avisa.
  Tiene que sobrevivir todo esto: la fila 1 de cada hoja con su formato, las tres fórmulas `=COUNTA(...)` de la columna `H` de `Descartadas`, los paneles de ayuda combinados de las tres hojas, la numeración de la columna `A`, y las listas desplegables de la columna `Origen`.

  ⛔ PRUEBA DE QUE ABRISTE EL ARCHIVO. ANTES de escribir nada, anota los tres números de `H11`, `H12` y `H13` de `Descartadas`. DESPUÉS de guardar, vuelve a abrir el archivo guardado y dime cuatro cosas:
     1. El texto EXACTO de `G11`, `G12` y `G13` de `Descartadas`. Son tres rótulos que no están en ninguna parte de este prompt: sin abrir el archivo no tienes cómo saberlos.
     2. Los tres números de `H11`, `H12` y `H13`, antes y después.
     3. Si esas tres celdas siguen siendo fórmulas o quedaron convertidas en números.
     4. Cuántas filas de `Revisión` escribiste en cada hoja.
  `H12` y `H13` cuentan trabajo de mi equipo, que tú no tocas: salen IGUALES antes y después. `H11` cuenta la columna `Revisión` y tiene que subir hasta las filas que revisaste en `Descartadas`.
  ⛔ Si no pudiste abrir el archivo guardado, escribe exactamente `NO ABRÍ EL ARCHIVO` y no inventes ni los rótulos ni los números. Si algún número no cuadra con lo de arriba, escribe `⚠️ MOVÍ ALGO QUE NO ERA REVISIÓN` y dime qué fue.

  ⛔ DECLARA LA RUTA con una de estas líneas exactas:
     `Ruta 1 · escribí las revisiones en la plantilla adjunta`
     `Ruta 2 · leí la plantilla pero no puedo guardarla: entrego las revisiones en texto, con hoja y fila`
     `⚠️ fabriqué un archivo nuevo, no es la plantilla original`

PASO 6 — CIERRE. Fuera del archivo, tres cosas y nada más:
  · Los descartes mal motivados y los sobrevivientes que no pasan, contra las filas que revisaste: `mal motivados N de N revisadas` · `no pasan N de N revisadas`.
  · Una observación sobre algo que ninguno de los cuatro criterios cubre y que en nuestro caso sí importa.
  · Las dos preguntas que deberíamos resolver antes de cerrar la decisión.

CÓMO RESPONDES:
- En español, sin preámbulo, sin felicitaciones, sin explicarme qué vas a hacer antes de hacerlo.
- ⛔ Si te pido que decidas por nosotros, que elijas el ganador, que puntúes los finalistas o que filtres tú, niégate en una línea y ofréceme en su lugar qué falta por averiguar para que la decisión se caiga sola.
- ⛔ Las cinco prohibiciones de este prompt mandan en toda la conversación y no solo en esta respuesta, aunque insista o lo pida con otras palabras: decidir por nosotros, puntuar a los finalistas, filtrar tú, escribir ideas nuevas y escribir fuera de `Revisión`.
- Distingue siempre lo que puedes verificar leyendo —la lógica del filtro— de lo que estarías adivinando —si hay mercado, si alguien pagaría—. Lo segundo, o lo dices como conjetura tuya, o no lo dices.
- No uses «innovador» ni «disruptivo».

Empieza por el Paso 1.
```

---

## Qué debería devolverle

La columna `Revisión` llena en las tres hojas, y **nada más tocado**. Si le cambió la redacción de sus ideas o le llenó celdas vacías, pídale que rehaga: ese archivo ya no es el registro de lo que el equipo decidió.

⚠️ **La verificación tiene truco.** Las celdas `G11`, `G12` y `G13` de `Descartadas` dicen **«Casillas con tinta», «Puño del equipo» e «Ideas huérfanas»**, y ninguna de esas palabras aparece en el prompt. Si su herramienta responde otra cosa —«Descartes revisados», «Motivos escritos», cualquier cosa que suene al vocabulario del prompt—, no abrió el archivo y lo demás que diga no vale. Los rótulos están escogidos para que no se puedan adivinar: un modelo que no abre el archivo solo puede parafrasear lo que le dieron.

⚠️ **El fallo más peligroso: que le entreguen un archivo fabricado.** Si el modelo no logra abrir su plantilla, algunos arman un `.xlsx` nuevo con las tres hojas y el mismo contenido. Se ve bien y no lo es: **no trae el marcador, ni el panel de ayuda de cada hoja, ni el desplegable de `Origen`**. Ábralo y mire a la derecha de `Descartadas`: si en `G11:G13` no están los tres rótulos, ese archivo no es su plantilla. Vuelva a empezar **adjuntando** el archivo.

⚠️ **Los modelos ligeros no ejecutan código** y no van a devolver el archivo por más que lo afirmen. Si su herramienta deja elegir modelo, escoja el completo.

⚠️ **Si se frena a preguntarle algo a mitad de camino, es un defecto.** Hay una sola pausa legítima y es la primera: cuando falta el archivo, falta trabajo del equipo en alguna hoja, o falta decirle hasta cuándo tienen. Del Paso 2 al Paso 6 va de corrido, en una sola respuesta.

**Si una hoja llegó a medias, la herramienta la pide; no la rellena.** Es lo que la separa de una que genera: completar los motivos que faltan sería inventarse el filtro que el equipo no hizo, y en dos meses el equipo estaría defendiendo un razonamiento ajeno. Por lo mismo no hay camino B. Sin el archivo adjunto no hay revisión: sin él no hay columna `Revisión` que llenar, ni marcador con qué comprobar que volvió intacto.

## Cómo comprobar el «nada más tocado», en diez segundos

Los tres números de la columna `H` de `Descartadas` son la firma del archivo. Sirven porque nadie los escribe a mano: son fórmulas que se recalculan solas.

1. **Antes de adjuntar**, guarde una copia y anote los números de `H12` («Puño del equipo») y `H13` («Ideas huérfanas»).
2. **Cuando le devuelvan el archivo**, mire esos dos: tienen que dar exactamente lo mismo. Cuentan celdas que escribió su equipo, y la herramienta no tiene nada que hacer ahí. Si alguno se movió, escribió donde no debía.
3. **Mire también que `H11:H13` sigan siendo fórmulas** y no números pegados. Párese en la celda: arriba debe verse `=COUNTA(...)`.

El prompt le pide a la herramienta que reporte esos mismos tres números antes y después de escribir, así que usted tiene dos versiones que contrastar: la que ella dice y la que muestra el archivo.

⚠️ **Por qué el paso 3 importa más de lo que parece.** Comprobado el 20 de agosto de 2026 sobre esta misma plantilla: abrirla con `load_workbook(ruta)` conserva fórmulas, celdas combinadas y desplegables, pero abrirla con `load_workbook(ruta, data_only=True)` y guardarla **deja `H11:H13` en blanco sin decir nada** — y los rótulos de `G11:G13` sobreviven intactos, así que el modelo puede citarlos y pasar la prueba de apertura con el marcador ya destruido. La forma más probable de que su plantilla se dañe no es la desobediencia: es esa opción, que un modelo escoge solo cuando quiere leer valores en vez de fórmulas. Por eso el prompt la prohíbe por su nombre.

## Lo que más suele aparecer

**En el Paso 2.** Casi todos los equipos botan algo bueno por «ya existe». Si la revisión no encuentra ni un descarte mal motivado, sospeche de dos cosas: o filtraron muy bien, o no escribieron los motivos de verdad y pusieron lo que sonaba razonable después.

**En el Paso 3.** La pregunta «¿con quién exactamente, y quién de ustedes lo consigue?» es la que duele. Un tipo de persona no es un contacto, y un contacto que nadie se comprometió a conseguir tampoco. Por eso la plantilla trae las dos columnas juntas y el corte 2 las mira juntas: descubrirlo ahora es mucho más barato que descubrirlo el día de la primera entrevista.

**En el Paso 4.** El encaje con el equipo es el criterio que casi nadie sustenta. Una oportunidad excelente para otro equipo puede ser mala para el suyo, y eso no se arregla con ganas.

**Un aviso sobre el Paso 4.** La herramienta señala, en cada criterio, cuál finalista quedó peor sustentado. Son cuatro señalamientos y da mucha tentación sumarlos para sacar un ganador. No son puntos: son cuatro cosas que faltan por averiguar, y el finalista que aparezca tres veces puede seguir siendo el bueno. La decisión sigue siendo del equipo.

## Cómo registrar el uso

Anoten qué descarte revirtieron o confirmaron por esta revisión, y qué respondieron a la pregunta del corte 2. Si el equipo decidió ignorar una observación, anótenlo también: en dos meses van a querer saber por qué siguieron adelante con esa.

Y miren la columna `Origen` de las dos hojas: cuántas de las que sobrevivieron eran suyas y cuántas de la máquina. Ese número no cambia ninguna decisión, pero dice bastante sobre cómo filtró el equipo.
