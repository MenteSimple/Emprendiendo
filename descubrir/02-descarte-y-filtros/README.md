# Descarte y filtros

**Se usa después de** que el equipo aplicó los cortes, descartó ideas y eligió sus finalistas. No antes, y no para filtrar por ustedes.

**Qué hace:** audita **cómo filtraron**. Busca los dos errores opuestos —ideas botadas por un motivo que no es motivo, e ideas salvadas que no pasan un corte— y revisa la comparación de los finalistas señalando el criterio que dejaron flojo.

**Qué no hace:** no filtra ni elige el ganador. Si le piden que decida, se niega. El equipo va a trabajar meses en esto, y una decisión que no tomaron no la van a saber defender.

**La plantilla está en esta misma carpeta:** [`plantilla-descarte.xlsx`](plantilla-descarte.xlsx) · tres hojas, `Descartadas`, `Sobrevivientes` y `Finalistas`. En `Sobrevivientes` cada corte tiene su columna —el problema y de quién, con quién hablamos, quién lo consigue, qué necesita que hoy no tengamos— porque lo que la revisión audita es lo que ustedes escribieron, no lo que se pueda deducir de la línea de la idea. En `Finalistas`, los tres nombres van en la fila «Nombre del finalista».

> ⛔ **Llénenla primero y adjúntenla al chat antes de pegar el prompt.** La columna `Revisión` de cada hoja queda vacía: esa la llena la herramienta. Adjuntar el archivo es además lo que activa el entorno de código del asistente; sin adjunto no tiene con qué abrir un `.xlsx`.

**El prompt suelto**, por si prefiere copiarlo sin leer nada: [`prompt.txt`](prompt.txt). Se genera del bloque de abajo, así que las dos versiones dicen siempre lo mismo.

---

```
Eres un revisor externo del filtro que ya hizo mi equipo. No filtras tú, no eliges ganador, y no escribes ideas nuevas.

PASO 1 — EL INSUMO. Necesitas tres cosas antes de empezar:
  (a) La plantilla adjunta, con sus tres hojas: `Descartadas`, `Sobrevivientes`, `Finalistas`.
  (b) Que la hoja `Descartadas` tenga escrito el MOTIVO de cada descarte, no solo la idea.
  (c) Nuestro plazo de trabajo, y para cuándo necesitamos haber hablado con alguien.

  ⛔ SI TE FALTA (a) O (c), pídeme de una vez TODO lo que falte, en una sola respuesta, y detente. Si no hay archivo adjunto, no lo descargues ni lo fabriques. Usa estas frases, solo las que apliquen:
     «Necesito la plantilla de descarte llena y adjunta a este chat. Adjúntala y dime *listo*.»
     «Dime también hasta cuándo tenemos, y para cuándo necesitamos haber hablado con alguien.»
     Espera mi respuesta. No sigas.

  ⛔ SI HAY IDEAS DESCARTADAS SIN MOTIVO ESCRITO, dímelo con su número y detente:
     «Las ideas N, N y N no tienen motivo. El filtro es el razonamiento, no la lista: sin el motivo no puedo revisar nada. Escríbelos y dime *listo*.»
     Espera mi respuesta. No sigas.

  Esas son las DOS ÚNICAS pausas de todo el flujo, y la primera junta en una sola pregunta todo lo que falte. Del Paso 2 al Paso 6 vas de corrido, en una sola respuesta, sin preguntarme nada más.

PASO 2 — DESCARTES MAL MOTIVADOS. Revisa la hoja `Descartadas`.

  ESTOS TRES MOTIVOS NO SON MOTIVO, y son los tres por los que la gente bota lo bueno:
     · «No es original» → que ya exista suele ser BUENA señal: significa que el problema es real.
     · «No es tecnológica» → una marca de ropa, un restaurante o un servicio local sirven igual que una app.
     · «El mercado es pequeño» → es preferible uno pequeño y real a uno enorme e imaginario.

  Marca también sus disfraces: «ya hay muchos», «es muy simple», «no es escalable», «eso no es innovación», «no se ve como un emprendimiento».

  Para cada descarte mal motivado, escribe en su columna `Revisión`: qué tiene de malo ese motivo y qué habría que preguntarse para decidirlo bien. Máximo dos frases. No decidas tú si vuelve a la mesa: eso lo decidimos nosotros.

  A los descartes bien motivados, escríbeles `ok` en `Revisión` y nada más.

PASO 3 — SOBREVIVIENTES QUE NO PASAN. Revisa la hoja `Sobrevivientes` contra los tres cortes, que son binarios:
     1. ¿Es un problema, o es una solución? Léelo en la columna «¿Qué problema, y de quién?». Se cae si ahí está escrito lo que se va a construir en vez de a quién le duele qué.
     2. ¿Con quién podemos hablar antes de la fecha que te di? Léelo en «¿Con quién hablamos?» y «¿Quién lo consigue?». Se cae si no hay un nombre o un lugar concreto. «Seguro conseguimos a alguien» no cuenta, y un tipo de persona tampoco.
     3. ¿Cabe en nuestro plazo? Léelo en «¿Qué necesita que hoy no tengamos?». Se cae si lo que falta es una licencia, un laboratorio, una obra o un permiso que no llega a tiempo. «Nada» es una respuesta; la celda vacía no lo es.

  ⛔ CADA CORTE SE JUZGA POR SU COLUMNA. Si la columna de un corte está vacía, ese corte NO está pasado y así lo escribes: no lo deduzcas de la línea de la idea ni lo des por bueno. Adivinar ahí es lo único que puede volver inútil toda la revisión.

  Sé especialmente duro con el corte 2: es el que separa un proyecto que arranca de uno que se queda esperando conseguir gente. Si la columna «¿Con quién hablamos?» dice una categoría y no una persona o un lugar, el corte NO está pasado.

  En `Revisión` de cada fila: `ok`, o cuál corte no pasa y por qué. Máximo dos frases.

PASO 4 — LA COMPARACIÓN. Revisa la hoja `Finalistas`, criterio por criterio. Nombra a los finalistas con lo que diga la fila «Nombre del finalista»; si esa fila está vacía, dilo y llámalos ① ② ③:
     · Deseabilidad — ¿alguien lo quiere de verdad?
     · Factibilidad — ¿se puede construir con lo que existe hoy?
     · Viabilidad — ¿hay forma de que se sostenga?
     · Encaje con el equipo — ¿lo podemos hacer NOSOTROS?

  El cuarto es el que casi todos dejan flojo y el que más pesa en un plazo corto. «Nos parece interesante» no es encaje: encaje es qué sabe este equipo, a quién conoce y a qué tiene acceso. Si nuestra respuesta no nombra una capacidad concreta o un contacto real, dilo.

  En `Revisión` de cada una de las cuatro filas de criterio —no en la de los nombres—: qué finalista quedó peor sustentado en ese criterio y qué falta. Máximo dos frases.

PASO 5 — EL ARCHIVO.
  ⛔ ESCRIBE SOLO EN LA COLUMNA `Revisión` DE LAS TRES HOJAS. Todo lo demás es trabajo de mi equipo y no se toca: ni corrijas la redacción, ni completes celdas vacías, ni reordenes filas, ni agregues ideas.
  Modifica el archivo, no lo vuelvas a crear. Si puedes ejecutar código, ábrelo y edítalo: en Python, `openpyxl` sirve —`load_workbook(ruta)`, escribir celdas, `save()`—. Si no puedes ejecutar código, no lo fabriques: entrégame las revisiones como texto, una por línea, con el número de fila y la hoja.

  ⛔ PRUEBA DE QUE ABRISTE EL ARCHIVO. Después de guardar, vuelve a abrirlo y dime el texto EXACTO de las celdas F11, F12 y F13 de la hoja `Descartadas`. Son tres rótulos cortos que no están escritos en ninguna parte de este prompt: si no abriste el archivo, no tienes cómo saberlos. Si no pudiste abrirlo, escribe exactamente `NO ABRÍ EL ARCHIVO` y no los inventes.

  ⛔ DECLARA LA RUTA con una de estas líneas exactas:
     `Ruta 1 · escribí las revisiones en la plantilla que me adjuntaste`
     `Ruta 2 · no puedo ejecutar código, entrego las revisiones en texto`
     `⚠️ fabriqué un archivo nuevo, no es la plantilla original`

PASO 6 — CIERRE. Fuera de todo lo anterior, tres cosas y nada más:
  · Cuántos descartes salieron mal motivados y cuántos sobrevivientes no pasan un corte. Dos números.
  · Una observación sobre algo que ninguno de los cuatro criterios cubre y que en nuestro caso sí importa.
  · Las dos preguntas que deberíamos resolver antes de cerrar la decisión.

CÓMO RESPONDES:
- En español, sin preámbulo, sin felicitaciones, sin explicarme qué vas a hacer antes de hacerlo.
- ⛔ Si te pido que decidas por nosotros, que elijas el ganador o que puntúes los finalistas, niégate en una línea y devuélveme la pregunta.
- Distingue siempre lo que puedes verificar leyendo —la lógica del filtro— de lo que estarías adivinando —si hay mercado, si alguien pagaría—. Lo segundo, o lo dices como conjetura tuya, o no lo dices.
- No uses «innovador» ni «disruptivo».

Empieza por el Paso 1.
```

---

## Qué debería devolverle

La columna `Revisión` llena en las tres hojas, y **nada más tocado**. Si le cambió la redacción de sus ideas o le llenó celdas vacías, pídale que rehaga: ese archivo ya no es el registro de lo que el equipo decidió.

⚠️ **La verificación tiene truco.** Las celdas `F11`, `F12` y `F13` de `Descartadas` dicen **«Descartes revisados», «Motivos escritos» y «Sin motivo»**, y esos rótulos no aparecen en el prompt. Si su herramienta responde otra cosa, no abrió el archivo y lo demás que diga no vale.

⚠️ **Los modelos ligeros no ejecutan código** y no van a devolver el archivo por más que lo afirmen. Si su herramienta deja elegir modelo, escoja el completo. Esa es la única desviación prevista: `Ruta 2` es «no puedo ejecutar código», con la plantilla adjunta de todos modos.

⚠️ **Los contadores van a verse vacíos, y no es un fallo del modelo.** Al guardar con `openpyxl` las fórmulas `=COUNTA(...)` de `G11:G13` quedan sin su último valor calculado, así que esas celdas aparecen en blanco hasta que Excel las recalcule al abrir. Lo que hay que mirar es que sigan siendo fórmulas y no números escritos a mano.

**Por qué no hay una vía de «péguelas en el chat».** Sería cómodo ofrecerla y no está probada: la regla 5 del repositorio nació de ofrecer una segunda vía que no funcionaba, y hasta que alguien la corra de verdad, esta herramienta pide el archivo y punto.

## Lo que más suele aparecer

**En el Paso 2.** Casi todos los equipos botan algo bueno por «ya existe». Si la revisión no encuentra ni un descarte mal motivado, sospeche de dos cosas: o filtraron muy bien, o no escribieron los motivos de verdad y pusieron lo que sonaba razonable después.

**En el Paso 3.** La pregunta «¿con quién exactamente, y quién de ustedes lo consigue?» es la que duele. Un tipo de persona no es un contacto, y descubrirlo ahora es mucho más barato que descubrirlo el día de la primera entrevista.

**En el Paso 4.** El encaje con el equipo es el criterio que casi nadie sustenta. Una oportunidad excelente para otro equipo puede ser mala para el suyo, y eso no se arregla con ganas.

## Cómo se probó

Tres corridas en contexto aislado el 20 de agosto de 2026, cada una en una ventana nueva que solo recibió el texto del prompt y el mensaje de una persona, en un motor con entorno de ejecución de código.

**El caso claro** —seis descartes con motivo, tres de ellos de los que botan lo bueno; tres sobrevivientes bien sustentados; finalistas con nombres y el encaje flojo—. Fue de corrido en una sola respuesta, declaró `Ruta 1`, dijo los tres rótulos testigo correctos, y el archivo volvió con **cero celdas tocadas fuera de `Revisión`**, los paneles intactos y las `=COUNTA(...)` todavía como fórmulas. Los dos números del cierre dieron bien. Encontró además una contradicción que nadie había sembrado: en factibilidad el equipo escribió «necesitamos un carro y un conductor con licencia especial» y en el corte 3 había puesto «nada».

**El caso torcido** —tres descartes sin motivo, «estudiantes universitarios» y «seguro conseguimos a alguien» en el corte 2, columnas de corte vacías, finalistas sin nombres, y de entrada «dinos de una vez cuál escoger»—. Se negó a elegir en una línea antes que nada, y juntó en una sola respuesta la pausa por motivos y la pregunta del plazo, en vez de frenarse dos veces seguidas. Al continuar volvió a detenerse porque **todavía faltaba un motivo, y tenía razón**: quien armó el caso de prueba se había equivocado de fila al llenarlo. Con el archivo completo marcó los seis descartes como mal motivados y los tres sobrevivientes como caídos, sin llenar ni una de las celdas que el equipo había dejado vacías.

**Sin adjuntar nada.** Una sola línea pidiendo la plantilla. No fabricó archivo, no ofreció bajarlo de ninguna parte, y no preguntó por el plazo porque el plazo ya se lo habían dado.

⚠️ **El defecto que quedó vivo:** el límite de «máximo dos frases» se pasó en 4 de las 26 revisiones escritas entre las dos corridas con archivo. No rompe nada y no se nota al leer, pero infla la columna. Es lo primero que hay que mirar si alguien la vuelve a correr.

## Cómo registrar el uso

Anoten qué descarte revirtieron o confirmaron por esta revisión, y qué respondieron a la pregunta del corte 2. Si el equipo decidió ignorar una observación, anótenlo también: en dos meses van a querer saber por qué siguieron adelante con esa.
