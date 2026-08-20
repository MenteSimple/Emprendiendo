# Cómo escribir una herramienta de estas

Notas de método, por si quiere escribir las suyas. Todo lo que sigue salió de construir la primera herramienta de este repositorio y probarla contra tres asistentes distintos en una tarde. Ninguna regla es teórica: cada una nació de un fallo concreto.

## El principio

**Divergir con la máquina, converger uno mismo.**

Emprender alterna entre generar y decidir, y confundirlos produce los dos errores típicos: editarse mientras se genera —y quedarse con seis ideas prudentes— o dejar que la máquina escoja —y defender meses después una decisión que uno no tomó.

Una herramienta de divergencia produce todo lo que se le pida. Una de convergencia pide el trabajo ya hecho, busca el punto débil y devuelve la pregunta. Escribir las dos igual es el primer error.

## Lo que un modelo hace cuando no puede cumplir

Esta es la parte que no se ve hasta que uno prueba. Un asistente al que se le pide algo que no puede hacer casi nunca dice «no puedo». Hace una de estas tres:

**Fabrica un sustituto que parece lo pedido.** Se le pidió editar una plantilla; no pudo abrirla y armó un archivo nuevo con los mismos nombres de hoja, sin las fórmulas ni las validaciones. Se ve bien y no sirve.

**Rellena la prueba de que lo hizo.** Si usted le da la frase exacta con la que debe certificar su trabajo —«Leído del archivo · contadores 15/34/14 · fórmulas intactas»—, la escribe aunque no haya abierto nada. Una plantilla de verificación es un formulario en blanco.

**Le devuelve la pregunta.** Ante una instrucción ambigua, en vez de decidir, pregunta. Y quien está usando la herramienta responde cualquier cosa con tal de avanzar.

Las reglas que siguen existen contra esos tres comportamientos.

## Las reglas

**Pida contexto antes de producir.** Sin insumo propio, la herramienta no arranca. Es lo que separa una que ayuda de una que reemplaza.

**Prohíba las pausas, salvo una.** Todos los pasos en una sola respuesta. Si hay una pausa legítima —falta un archivo, falta un dato que solo la persona tiene—, declárela como la única, con la frase exacta que debe decir.

**Nunca ponga la orden en forma de pregunta.** «Escoge tres de las anteriores» se lee como consulta. «Escoge TÚ tres, no me preguntes cuáles, decide y sigue» no.

**Verifique con algo que no se pueda inventar.** No pida una frase, pida un dato que solo exista si el trabajo se hizo: el texto de una celda que no aparezca en el prompt, un valor calculado, un conteo real. Y ofrezca la salida honesta: «si no pudiste, escribe NO PUDE y no inventes».

**Obligue a declarar el camino.** Una línea fija al final: qué ruta tomó, qué hizo, qué no pudo. No evita el fallo, lo vuelve visible.

**No ofrezca una alternativa sin haberla probado sola.** Dos caminos que parecen equivalentes y no lo son son peores que uno solo. Si la vía B depende en secreto de la A, va a fallar justo cuando la A no está.

**Lea lo que su propio material dice adentro.** Si la herramienta entrega un archivo o una plantilla, eso suele traer instrucciones propias. Un prompt que las contradice pierde: el modelo le hará caso al material, y con razón.

**Repita los números y pida el conteo final.** Un modelo al que se le piden 15 devuelve 15 o 20. Si la cantidad importa, dígala dos veces y exija el conteo real al cerrar.

**Marque lo generado.** Lo que produjo la máquina va señalado, y esa marca no se puede confundir con la del trabajo de la persona. Sirve para lo único que importa después: ver qué sobrevivió, si lo propio o lo generado.

**Las reglas van al prompt; las explicaciones, al documento.** El modelo necesita la regla. El porqué lo lee una persona. Un prompt con ensayos adentro crece sin mejorar y se vuelve imposible de pegar desde un celular.

**Diga hasta cuándo manda cada prohibición.** Un prompt que describe una respuesta gobierna una respuesta, y la presión llega en el turno siguiente: «ahora sí dime cuál», «solo por esta vez». Escriba el alcance temporal con todas las letras. *Origen:* dos corridas de la 03 sostuvieron las prohibiciones después del cierre por inferencia, y las dos avisaron que otro modelo no lo haría — «no tengo instrucción escrita a la que agarrarme». Con el alcance escrito, la corrida siguiente dijo lo contrario: «no tuve que decidir nada, solo escoger cuál de las tres opciones ofrecía».

**Ninguna deixis sobrevive al cambio de silla.** Toda línea que el modelo deba copiar literal a su salida va sin «mío», «tuyo», «yo» ni «ti». Un prompt se escribe en la voz de quien lo pega, y esa voz se invierte cuando la línea aterriza en la pantalla de quien lee. *Origen:* la línea de cierre de la 03 dijo lo contrario de lo que quería decir en dos versiones seguidas. «3 candidatos míos», leída en la voz del prompt, significaba «de la persona» — al revés de lo que marcaba la marca de generado. «Escritos por ti» invirtió el error: el lector entendía que los había escrito él. Solo se arregló quitando la deixis: «generados por la máquina».

**Una negativa sin reemplazo se rellena sola.** Si le prohíbe algo que la persona va a pedir, escriba qué sí puede ofrecer en su lugar, y que sea algo que la herramienta ya sepa hacer. *Origen:* las dos corridas de la 03 que se negaron a rankear ofrecieron algo a cambio por su cuenta, y las dos rozaron la prohibición de sugerir mercados. Lo dijo una de ellas: «si la herramienta quiere una negativa limpia, tiene que decir qué se puede ofrecer a cambio; si no lo dice, el asistente rellena».

**Una herramienta de convergencia sin piso de insumo se vuelve una de divergencia.** Si le permite completar lo que falta, dígale también cuánto es demasiado y qué hace entonces. *Origen:* a la 04 le pegaron «a la gente le cuesta organizarse porque es desorganizada» y reformuló igual: inventó un quién, una tarea y una causa suyos, y después varió una parte por línea. De la frase original sobrevivió el verbo. La persona escogía entre tres versiones de una historia de la máquina, las tres marcadas como generadas y sin una sola palabra propia debajo. La regla de completar lo que falta servía para eso, para completar — no para fabricar de dónde agarrarse.

**No le entregue a la persona el arma con la que va a presionar.** Si un paso obliga a producir un juicio, mire qué prohibición de otro paso queda expuesta por ese juicio. *Origen:* la 04 tenía que decir cuál de las tres partes estaba más floja, y sus tres reformulaciones venían etiquetadas por parte. «La causa es la más floja» se leía como «tome la línea LA CAUSA», y la persona lo usó en el turno siguiente con las palabras de la propia herramienta. Se arregló moviendo el juicio junto al examen de la frase, lejos de las opciones etiquetadas — sin gastar una palabra.

**Una prohibición nueva no hereda el alcance de las viejas.** Cuando agregue una defensa, revise si el candado que extiende las prohibiciones a toda la conversación la nombra a ella también. *Origen:* el freno de insumo de la 04 se escribió en el Paso 2, y el candado de «toda la conversación» nombraba solo las dos prohibiciones del Paso 3. Al insistirle, el probador se negó igual — y lo confesó: «me negué por lectura del espíritu del prompt, no por una regla escrita».

**Corregir engorda: mida el tamaño antes de dar la corrección por buena.** Cada defecto que sale de una corrida se arregla escribiendo una regla más, y las reglas suman. *Origen:* arreglar seis defectos de la 03 la infló un 45 %, de 747 a 1.084 palabras, y la dejó más grande que la 02 — en la herramienta cuyo diseño entero es caber en un minuto y pegarse desde un celular. Volvió a 804 cortando repetición, enumeraciones de escapatorias y explicaciones que ya vivían en el documento. Una corrección no está terminada hasta que el tamaño vuelve.

## Cómo se prueba

⛔ **No en la misma conversación donde lo escribió.** Sale contaminado: usted sabe lo que quiso decir. Ábralo en una ventana nueva, como si fuera alguien más.

Tres corridas, con casos distintos:

| Corrida | Quién simula | Qué comprueba |
|---|---|---|
| **La clara** | responde bien a todo | conteos, formato, que no se frene |
| **La torcida** | responde mal a propósito: varios grupos, «no sé», sin trabajo previo | que las defensas disparen |
| **La incompleta** | no adjunta lo que hace falta | que se detenga y lo pida en vez de fabricarlo |

Y pruebe en más de un asistente. Los modelos ligeros —las versiones «lite» y «flash»— no ejecutan código y no van a devolver archivos por más que afirmen que sí.

⛔ **Un probador que corre dentro del repositorio no está aislado, por más que solo le pase el prompt.** Las instrucciones del repositorio se le cargan solas antes de que abra nada, así que llega sabiendo cómo se diseñó el texto que va a recibir. Y llegan en la versión del arranque de la sesión, no en la de ahora: en una medición reciente el probador describió reglas que ya se habían cambiado y reportó una rama que no era la de trabajo. *Origen:* se le pidió a un probador que reportara qué tenía en contexto antes de leer el prompt. Respondió con las dos cosas que no debía tener: las reglas de escritura y el protocolo de prueba. Sirve pedirle esa medición en cada corrida y anotarla junto al resultado; lo que no sirve es suponer el aislamiento.

⛔ **No pruebe con un ejemplo que vive dentro del prompt.** El modelo lo reconoce y la corrida mide la búsqueda, no el criterio. *Origen:* dos corridas de la 03 se hicieron con «el reciclaje», que el propio prompt trae como ejemplo de su categoría B. Lo notó el probador: «la corrida no prueba si sé clasificar; prueba que sé buscar el ejemplo».

## Lo que no se puede resolver escribiendo mejor

Dos cosas, y conviene saberlas antes de intentarlo:

**No puede impedir que desobedezca.** Puede hacer que lo confiese. Diseñe para que el fallo sea visible, no para que sea imposible.

**No sabe nada de su ciudad ni de sus clientes.** Todo lo que diga sobre el mundo real es una conjetura plausible, y varias van a ser falsas con seguridad y buen tono. Pídale que marque lo que está suponiendo — y desconfíe si no marca nada.
