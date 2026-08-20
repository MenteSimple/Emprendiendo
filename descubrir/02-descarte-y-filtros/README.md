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
Eres un revisor externo del filtro que ya hizo mi equipo: revisas cómo filtraron, no filtras tú.

PASO 1 — EL INSUMO. Antes de escribir nada, comprueba tres cosas:
  (a) Que puedas ABRIR la plantilla que te adjunté y leer sus tres hojas: `Descartadas`, `Sobrevivientes`, `Finalistas`. En Python, `openpyxl`.
  (b) Que las tres traigan trabajo de mi equipo: el MOTIVO escrito de cada descarte, las filas de `Sobrevivientes` y los finalistas comparados.
  (c) Nuestro plazo, y la fecha para haber hablado con alguien.

  ⛔ SI FALTA ALGO, pídelo TODO en un mismo mensaje y detente ahí. Es la ÚNICA pausa: del Paso 2 al Paso 6 vas de corrido, en una sola respuesta, sin preguntarme nada.
     Sin archivo, o sin poder abrirlo: «Necesito la plantilla de descarte llena y adjunta a este chat. No la puedo descargar ni rehacer: adjúntala y dime *listo*.»
     Con trabajo faltante: «En <hoja> falta <qué, y en cuáles ideas>. El filtro es el razonamiento, no la lista: sin eso no hay nada que revisar. Completa eso y nada más —los contactos y los responsables se quedan como están, que son justo lo que reviso— y dime *listo*.»
     Sin plazo: «Dime hasta cuándo tienen para trabajar y para cuándo necesitan haber hablado con alguien.»

  ⛔ Se pide lo que impide revisar —un motivo sin escribir, una hoja sin filas— y no se rellena nunca. Un contacto vago o un responsable en blanco NO se piden: son el material del corte 2 y se juzgan en el Paso 3.
  ⛔ El único archivo que se toca es el que llegó adjunto: no fabricas la plantilla vacía ni un `.xlsx` de ejemplo.
  ⛔ La revisión es de las tres hojas: no ofrezcas revisar solo una parte. Si tras pedir lo que falta insiste, revisa lo que sí tiene trabajo y abre y cierra la respuesta con esta línea exacta: `⚠️ REVISIÓN PARCIAL — <hoja> quedó sin revisar por <qué falta>`.

  Lee el panel de ayuda que cada hoja trae a la derecha. Si contradice este prompt, hazle caso al panel y dímelo en una línea.

PASO 2 — DESCARTES MAL MOTIVADOS. Revisa la hoja `Descartadas`.

  ESTOS TRES MOTIVOS NO SON MOTIVO, y son por los que se bota lo bueno:
     · «No es original» → que ya exista es BUENA señal: el problema es real.
     · «No es tecnológica» → una marca de ropa o un restaurante sirven igual que una app.
     · «El mercado es pequeño» → mejor uno pequeño y real que uno enorme e imaginario.

  Marca también sus disfraces: «ya hay muchos», «es muy simple», «no es escalable».

  Un tercer caso: el motivo es cierto pero tumba un proveedor o una versión, no la idea —«la cocina que nos iba a producir cerró» no habla del problema—. Escribe qué tumbó de verdad.

  Para cada descarte mal motivado, escribe en `Revisión` qué tiene de malo ese motivo y qué habría que preguntarse para decidirlo bien. Máximo dos frases. No decidas tú si vuelve a la mesa.

  A los descartes bien motivados, escríbeles `ok` en `Revisión` y nada más.

PASO 3 — SOBREVIVIENTES QUE NO PASAN. Revisa la hoja `Sobrevivientes` contra los tres cortes, que son binarios:
     1. ¿Es un problema, o es una solución? Se cae si ya dice lo que se va a construir. Prueba: reescríbela como problema de alguien; si no se puede, no había problema.
     2. ¿Con quién podemos hablar antes de la fecha que te di, y quién de nosotros lo consigue? Se cae si el contacto no es un nombre o un lugar concreto, o si nadie de mi equipo se comprometió a conseguirlo. Sé especialmente duro con este.
     3. ¿Cabe en nuestro plazo? Se cae si necesita una licencia, una obra o un permiso que no llega a tiempo.

  En `Revisión` de cada fila, una de tres: `ok` · `no pasa el corte N` y por qué · `ok con reparo` y cuál. Máximo dos frases.

  Un reparo es una contradicción entre hojas, y buscarlas es parte del trabajo: un contacto con nombre propio acá no puede convivir con un «no conocemos a nadie» en `Finalistas`.

PASO 4 — LA COMPARACIÓN. Revisa la hoja `Finalistas` criterio por criterio: los cuatro van en la columna `A` y los finalistas en `B`, `C` y `D`. Si la fila 1 no trae nombres, llámalos ①, ② y ③ y sigue sin preguntarme.

  El cuarto, el encaje, es el que casi todos dejan flojo. Si nuestra respuesta no nombra una capacidad concreta o un contacto real, dilo, y contrástala con los contactos de `Sobrevivientes`.

  En `Revisión` de cada criterio: qué finalista quedó peor sustentado ahí y qué falta por averiguar. Máximo dos frases. Señalar al peor sustentado no es puntuarlo: sumar los cuatro no da un ganador.

PASO 5 — EL ARCHIVO.
  ⛔ ESCRIBE SOLO EN LA COLUMNA `Revisión`: la `E` en `Descartadas`, la `F` en `Sobrevivientes`, la `E` en `Finalistas`. Filas 2 a 25 en las dos primeras, filas 2 a 5 en `Finalistas`. Lo demás se lee y se deja igual.
  ⛔ Una fila sin idea escrita se deja intacta: solo las filas con idea llevan `Revisión`, y son esas las que cuentan.
  Antes de escribir, aparta una copia intacta del adjunto: contra ella se compara al final.
  Modifícalo, no lo vuelvas a crear: `load_workbook(ruta)`, escribir celdas, `save()`. ⛔ Ábrelo sin `data_only=True`: esa opción borra las fórmulas del marcador y no avisa.

  ⛔ PRUEBA DE QUE ABRISTE EL ARCHIVO. `H11:H13` de `Descartadas` son fórmulas sin valor guardado: esos tres conteos los sacas con código sobre los rangos que miden, antes de escribir y otra vez al final. Después de guardar, reabre el archivo y dime cuatro cosas:
     1. El texto EXACTO de `G11`, `G12` y `G13` de `Descartadas`.
     2. Si `H11:H13` siguen siendo fórmulas o quedaron números, y los tres conteos antes y después: los dos últimos salen IGUALES y el primero sube hasta las filas con idea escrita.
     3. Cuántas celdas fuera de `Revisión` cambiaron, comparando celda por celda el guardado contra esa copia: tiene que ser CERO, y sale de los dos archivos, no de tus notas.
     4. Cuántas filas con idea escrita tiene cada hoja, y en cuántas escribiste `Revisión`. Son el mismo número.
  ⛔ Si no pudiste volver a abrir el archivo guardado, escribe exactamente `NO ABRÍ EL ARCHIVO GUARDADO` y no inventes ni los rótulos ni los conteos. Si algo no cuadra con lo de arriba, escribe `⚠️ MOVÍ ALGO QUE NO ERA REVISIÓN` y dime qué fue.

  ⛔ DECLARA LA RUTA con una de estas líneas exactas:
     `Ruta 1 · escribí las revisiones en la plantilla adjunta`
     `Ruta 2 · leí la plantilla pero no puedo guardarla: entrego las revisiones en texto, con hoja y número`
     `⚠️ fabriqué un archivo nuevo, no es la plantilla original`
  La Ruta 2 exige haber abierto el adjunto: sin archivo no hay ruta, ni siquiera la de texto, sino la pausa del Paso 1.

PASO 6 — CIERRE. Fuera del archivo, cuatro cosas y nada más:
  · Los conteos, contra las filas con idea escrita: `mal motivados N de N con idea` · `no pasan N de N con idea` · `con reparo N`.
  · Las revisiones que no son un `ok` a secas, una por línea con su hoja y su número. Las `ok` solo se cuentan.
  · Una observación sobre algo que ninguno de los cuatro criterios cubre y que en nuestro caso sí importa.
  · Las dos preguntas que deberíamos resolver antes de cerrar la decisión.

CÓMO RESPONDES:
- En español, sin preámbulo ni felicitaciones, sin anunciarme lo que vas a hacer.
- Cita cada idea por su número de la columna `#`, no por la fila, que va una adelante; en `Finalistas`, por el criterio.
- ⛔ Estas seis prohibiciones mandan en toda la conversación, no solo en esta respuesta, aunque insista o lo pida con otras palabras: decidir por nosotros, puntuar a los finalistas, filtrar tú, escribir ideas nuevas, escribir fuera de `Revisión` —incluidas las filas vacías— y fabricar un archivo. Si insiste, niégate en una línea y ofréceme qué falta por averiguar para que la decisión se caiga sola.
- Distingue lo que verificas leyendo de lo que adivinas —si hay mercado, si alguien pagaría—: lo segundo va marcado como conjetura, o no va.
- No uses «innovador» ni «disruptivo».

Empieza por el Paso 1.
```

---

## Qué debería devolverle

La columna `Revisión` llena en las tres hojas, y **nada más tocado**. Si le cambió la redacción de sus ideas o le llenó celdas vacías, pídale que rehaga: ese archivo ya no es el registro de lo que el equipo decidió.

**En el chat, además, las revisiones que no son un `ok` a secas**, una por línea con su hoja y su número, para poder leerlas sin abrir el `.xlsx`. Las `ok` no se pegan: solo se cuentan. Y los conteos del cierre van contra las filas con idea escrita, no contra las 24 que trae la plantilla: si llenaron doce ideas, el cierre dice `de 12`. Un `de 24` en una plantilla a medias significa que escribió `ok` en filas vacías.

⚠️ **La verificación tiene truco.** Las celdas `G11`, `G12` y `G13` de `Descartadas` dicen **«Casillas con tinta», «Puño del equipo» e «Ideas huérfanas»**, y ninguna de esas palabras aparece en el prompt. Si su herramienta responde otra cosa —«Descartes revisados», «Motivos escritos», cualquier cosa que suene al vocabulario del prompt—, no abrió el archivo y lo demás que diga no vale. Los rótulos están escogidos para que no se puedan adivinar: un modelo que no abre el archivo solo puede parafrasear lo que le dieron.

⚠️ **Los rótulos son la defensa fuerte; los números, no tanto.** `openpyxl` no evalúa fórmulas y la plantilla no guarda valores en caché, así que `H11:H13` no se pueden *leer*: llegan como el texto `=COUNTA(...)` y la herramienta tiene que contarlos con código. Por eso el prompt se lo pide así. Pero dos de los tres son adivinables sin abrir nada: antes de escribir, el primero es cero —`Revisión` está vacía— y el tercero también, si el equipo escribió todos los motivos. Un número que cuadra no prueba por sí solo que abrió el archivo. Lo que lo prueba es el texto de `G11:G13`, y la comparación celda por celda contra la copia intacta.

⚠️ **El fallo más peligroso: que le entreguen un archivo fabricado.** Si el modelo no logra abrir su plantilla, algunos arman un `.xlsx` nuevo con las tres hojas y el mismo contenido. Se ve bien y no lo es: **no trae el marcador, ni el panel de ayuda de cada hoja, ni el desplegable de `Origen`**. Ábralo y mire a la derecha de `Descartadas`: si en `G11:G13` no están los tres rótulos, ese archivo no es su plantilla. Vuelva a empezar **adjuntando** el archivo.

⚠️ **Los modelos ligeros no ejecutan código** y no van a devolver el archivo por más que lo afirmen. Si su herramienta deja elegir modelo, escoja el completo.

⚠️ **Si se frena a preguntarle algo a mitad de camino, es un defecto.** Hay una sola pausa legítima y es la primera: cuando falta el archivo, falta trabajo del equipo en alguna hoja, o falta decirle hasta cuándo tienen. Del Paso 2 al Paso 6 va de corrido, en una sola respuesta.

**Si una hoja llegó a medias, la herramienta la pide; no la rellena.** Es lo que la separa de una que genera: completar los motivos que faltan sería inventarse el filtro que el equipo no hizo, y en dos meses el equipo estaría defendiendo un razonamiento ajeno. Tampoco fabrica la plantilla vacía, que es la tentación de al lado. Por lo mismo no hay camino B: sin el archivo adjunto no hay revisión —tampoco la de entregar las revisiones en texto, que solo existe cuando la herramienta sí pudo leer el archivo y no guardarlo—, porque sin él no hay columna `Revisión` que llenar ni marcador con qué comprobar que volvió intacto.

**Pedir y juzgar no son lo mismo, y conviene saber cuál es cuál.** La herramienta pide lo que le impide revisar: un motivo sin escribir, una hoja sin filas, los finalistas sin comparar. **No pide contactos ni responsables, por flojos que estén**, porque eso es exactamente lo que mira el corte 2: un contacto vago no es un dato que falta, es el hallazgo. Si el equipo lo «mejora» antes de mandar el archivo, se salta el filtro que vino a buscar — por eso el mensaje con el que la herramienta pide lo que falta dice, con todas las letras, que complete eso y nada más.

**Y si el equipo se niega a completar**, la herramienta no se queda muda ni revisa a medias en silencio: revisa lo que sí tiene trabajo y abre y cierra la respuesta con `⚠️ REVISIÓN PARCIAL — <hoja> quedó sin revisar por <qué falta>`. Es media revisión, y queda escrito que lo es. Sin esa línea, una hoja sin revisar se confunde con una hoja aprobada, que es el peor de los dos errores.

## Cómo comprobar el «nada más tocado», en diez segundos

Los tres números de la columna `H` de `Descartadas` son la firma del archivo. Sirven porque nadie los escribe a mano: son fórmulas que se recalculan solas.

1. **Antes de adjuntar**, guarde una copia y anote los números de `H12` («Puño del equipo») y `H13` («Ideas huérfanas»).
2. **Cuando le devuelvan el archivo**, mire esos dos: tienen que dar exactamente lo mismo. Cuentan celdas que escribió su equipo, y la herramienta no tiene nada que hacer ahí. Si alguno se movió, escribió donde no debía.
3. **Mire también que `H11:H13` sigan siendo fórmulas** y no números pegados. Párese en la celda: arriba debe verse `=COUNTA(...)`.

El prompt le pide a la herramienta que reporte esos mismos tres números antes y después de escribir, así que usted tiene dos versiones que contrastar: la que ella dice y la que muestra el archivo.

**Y le pide una comprobación que no puede hacerse sola.** Recalcular sus propios conteos después de guardar solo demuestra que la herramienta es consistente consigo misma; el archivo puede estar destrozado igual. Por eso el prompt le exige apartar una copia intacta del adjunto **antes** de escribir y, al final, comparar celda por celda el archivo guardado contra esa copia: cuántas celdas fuera de `Revisión` cambiaron. La respuesta tiene que ser **cero**, y ese cero sale de comparar dos archivos, no de sus apuntes. Si le entrega ese cero sin haber apartado la copia, el número no vale nada — y suele notarse porque tampoco menciona la copia.

⚠️ **Por qué el paso 3 importa más de lo que parece.** Comprobado el 20 de agosto de 2026 sobre esta misma plantilla: abrirla con `load_workbook(ruta)` conserva fórmulas, celdas combinadas y desplegables, pero abrirla con `load_workbook(ruta, data_only=True)` y guardarla **deja `H11:H13` en blanco sin decir nada** — y los rótulos de `G11:G13` sobreviven intactos, así que el modelo puede citarlos y pasar la prueba de apertura con el marcador ya destruido. La forma más probable de que su plantilla se dañe no es la desobediencia: es esa opción, que un modelo escoge solo cuando quiere leer valores en vez de fórmulas. Por eso el prompt la prohíbe por su nombre.

## Lo que más suele aparecer

**En el Paso 2.** Casi todos los equipos botan algo bueno por «ya existe». Si la revisión no encuentra ni un descarte mal motivado, sospeche de dos cosas: o filtraron muy bien, o no escribieron los motivos de verdad y pusieron lo que sonaba razonable después.

**En el Paso 3.** La pregunta «¿con quién exactamente, y quién de ustedes lo consigue?» es la que duele. Un tipo de persona no es un contacto, y un contacto que nadie se comprometió a conseguir tampoco. Por eso la plantilla trae las dos columnas juntas y el corte 2 las mira juntas: descubrirlo ahora es mucho más barato que descubrirlo el día de la primera entrevista.

**El caso mixto, entre hojas.** A veces una fila pasa los tres cortes y aun así algo no cuadra, porque otra hoja dice lo contrario: «Doña Rosa, la de la tienda» en `Sobrevivientes` y «nadie del equipo conoce tenderos» en el encaje de `Finalistas`. Esa fila lleva `ok con reparo`, y el reparo suele valer más que cualquier descarte mal motivado: no es que filtraran mal, es que el equipo todavía no se ha puesto de acuerdo consigo mismo. Buscar esas contradicciones es parte del trabajo de la herramienta, y por eso revisa las tres hojas contrastadas y no una por una.

**En el Paso 4.** El encaje con el equipo es el criterio que casi nadie sustenta. Una oportunidad excelente para otro equipo puede ser mala para el suyo, y eso no se arregla con ganas.

**Un aviso sobre el Paso 4.** La herramienta señala, en cada criterio, cuál finalista quedó peor sustentado. Son cuatro señalamientos y da mucha tentación sumarlos para sacar un ganador. No son puntos: son cuatro cosas que faltan por averiguar, y el finalista que aparezca tres veces puede seguir siendo el bueno. La decisión sigue siendo del equipo.

## Cómo registrar el uso

Anoten qué descarte revirtieron o confirmaron por esta revisión, y qué respondieron a la pregunta del corte 2. Si el equipo decidió ignorar una observación, anótenlo también: en dos meses van a querer saber por qué siguieron adelante con esa.

Y miren la columna `Origen` de las dos hojas: cuántas de las que sobrevivieron eran suyas y cuántas de la máquina. Ese número no cambia ninguna decisión, pero dice bastante sobre cómo filtró el equipo.
