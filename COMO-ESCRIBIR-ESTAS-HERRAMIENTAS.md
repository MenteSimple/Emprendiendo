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

## Las reglas, y de dónde salió cada una

Ninguna es teórica: cada una salió de una corrida que falló. Las primeras, de correr la 01 contra Copilot, Gemini y Claude el 19 de agosto de 2026; las que llevan (02), de auditar y correr la herramienta de descarte el 20. Acá va la cita corta; la versión larga de cada incidente, con lo que dijo el modelo, vive en el README de la herramienta donde pasó.

**1 · Pida contexto antes de producir.** Sin insumo propio, la herramienta no arranca. Es lo que separa una que ayuda de una que reemplaza. Funcionó en los tres motores.

**2 · Prohíba las pausas, salvo una.** Todos los pasos en una sola respuesta. Si hay una pausa legítima —falta un archivo, falta un dato que solo la persona tiene—, declárela como la única, con la frase exacta que debe decir. Cada pregunta a mitad de camino es una oportunidad de que la persona conteste cualquier cosa con tal de avanzar. *Origen:* Claude se frenó en el Paso 4 de la 01 y hubo que responderle «escoge tú». *(02)* La misma herramienta de descarte declaraba dos pausas y abría una tercera diez líneas más arriba —«pregúntamelo si no te lo di», sobre el plazo—; se descubrió auditando, antes de publicarla. Cuando después se corrió con las dos pausas bien declaradas, el modelo juntó por su cuenta en una sola respuesta todo lo que faltaba, que es exactamente lo que la regla busca.

**3 · Nunca ponga la orden en forma de pregunta.** «Escoge tres de las anteriores» se lee como consulta. «Escoge TÚ tres, no me preguntes cuáles, decide y sigue» no. *Origen:* la frase exacta que frenó a Claude en el Paso 4 —la misma de la regla 2—: era una orden escrita como pregunta, y por eso se leyó como pregunta.

**4 · Verifique con algo que no se pueda inventar.** No pida una frase, pida un dato que solo exista si el trabajo se hizo: el texto de una celda que no aparezca en el prompt, un valor calculado, un conteo real. Y ofrezca la salida honesta: «si no pudiste, escribe NO PUDE y no inventes». Si se le da la frase con la que debe certificar algo, la escribe sin hacer nada: una plantilla de verificación es un formulario en blanco. *Origen:* Gemini 3.5 Flash-Lite, que no ejecuta código y no generó ningún archivo, escribió igual «Leído del archivo · contadores 15/34/14 · fórmulas intactas».

**5 · Obligue a declarar el camino.** Una línea fija al final: qué ruta tomó, qué hizo, qué no pudo. No evita el fallo, lo vuelve visible. Un fallo declarado se corrige; uno silencioso se entrega. *Origen:* Copilot no pudo abrir la plantilla y fabricó un `.xlsx` nuevo —con las hojas correctas y sin fórmulas ni listas—, y solo se supo porque lo mencionó de pasada.

**6 · No ofrezca una alternativa sin haberla probado sola.** Dos caminos que parecen equivalentes y no lo son son peores que uno solo. Si la vía B depende en secreto de la A, va a fallar justo cuando la A no está. *Origen:* se agregó «bájala de esta URL» como alternativa a adjuntar el archivo. Ninguno de los tres motores pudo: adjuntar el archivo es lo que activa el entorno de código, así que la segunda vía dependía de la primera. Costó tres corridas fallidas.

**7 · Lea lo que su propio material dice adentro.** Si la herramienta entrega un archivo o una plantilla, eso suele traer instrucciones propias. Un prompt que las contradice pierde: el modelo le hará caso al material, y con razón. *Origen:* el prompt decía «20 filas, Origen X» y el panel de la plantilla decía que las de SCAMPER van también en esa hoja con meta 34. Gemini le hizo caso a la plantilla —con razón— y marcó mal la columna. *(02)* La misma piedra en otra herramienta: la plantilla de descarte le colgaba una lista desplegable «sí,no» a la columna «¿Con quién hablamos?», que el prompt y el panel de esa misma hoja mandaban responder con un nombre. Excel la aplicaba con bloqueo duro, así que el equipo no podía escribir el nombre aunque quisiera. Dos herramientas distintas, el mismo error: la regla no vive de un solo caso.

**8 · Repita los números y pida el conteo final.** Un modelo al que se le piden 15 devuelve 15 o 20. Si la cantidad importa, dígala dos veces y exija el conteo real al cerrar.

**9 · Marque lo generado.** Lo que produjo la máquina va señalado, y esa marca no se puede confundir con la del trabajo de la persona. Sirve para lo único que importa después: ver qué sobrevivió, si lo propio o lo generado.

**10 · Las reglas van al prompt; las explicaciones, al documento.** El modelo necesita la regla. El porqué lo lee una persona. Un prompt con ensayos adentro crece sin mejorar y se vuelve imposible de pegar desde un celular.

**11 · Diga hasta cuándo manda cada prohibición.** Un prompt que describe una respuesta gobierna una respuesta, y la presión llega en el turno siguiente: «ahora sí dime cuál», «solo por esta vez». Escriba el alcance temporal con todas las letras. *Origen:* dos corridas de la 03 sostuvieron las prohibiciones después del cierre por inferencia, y las dos avisaron que otro modelo no lo haría — «no tengo instrucción escrita a la que agarrarme». Con el alcance escrito, la corrida siguiente dijo lo contrario: «no tuve que decidir nada, solo escoger cuál de las tres opciones ofrecía».

**12 · Ninguna deixis sobrevive al cambio de silla.** Toda línea que el modelo deba copiar literal a su salida va sin «mío», «tuyo», «yo» ni «ti». Un prompt se escribe en la voz de quien lo pega, y esa voz se invierte cuando la línea aterriza en la pantalla de quien lee. *Origen:* la línea de cierre de la 03 dijo lo contrario de lo que quería decir en dos versiones seguidas. «3 candidatos míos», leída en la voz del prompt, significaba «de la persona» — al revés de lo que marcaba la marca de generado. «Escritos por ti» invirtió el error: el lector entendía que los había escrito él. Solo se arregló quitando la deixis: «generados por la máquina».

**13 · Una negativa sin reemplazo se rellena sola.** Si le prohíbe algo que la persona va a pedir, escriba qué sí puede ofrecer en su lugar, y que sea algo que la herramienta ya sepa hacer. *Origen:* las dos corridas de la 03 que se negaron a rankear ofrecieron algo a cambio por su cuenta, y las dos rozaron la prohibición de sugerir mercados. Lo dijo una de ellas: «si la herramienta quiere una negativa limpia, tiene que decir qué se puede ofrecer a cambio; si no lo dice, el asistente rellena».

**14 · Que el trabajo ocurrió no prueba que el trabajo se hizo: pida una cita del material.** Un testigo demuestra que abrió el archivo; solo una cita demuestra que lo leyó. *Origen:* la 02 verificaba con tres rótulos escondidos, tres contadores y una comparación celda por celda, y la última corrida mostró que las cuatro se pasan limpio escribiendo «ok» en todas las filas sin leer una sola: «la verificación mide QUE escribí, no QUÉ escribí». Se arregló obligando a que todo lo que no sea un «ok» a secas cite entre comillas la celda que lo tumba — un «ok» mentiroso tendría que fabricar una cita verificable contra el archivo, que es mucho más caro que escribir dos letras.

**15 · Un conteo que sale de un número que el modelo declara es una encuesta, no una verificación.** Ánclelo a algo que exista en el material. *Origen:* el cierre de la 02 pedía «N de N revisadas», y quién decidía cuántas revisó era el propio modelo: escribiendo «ok» en las veinticuatro filas vacías reportaba «1 de 24», inflaba el contador de la plantilla y las tres defensas daban verde. Ahora los conteos se anclan a las filas con idea escrita, y una fila vacía se deja intacta.

**16 · Declarar que no tocó nada no obliga a comprobarlo.** Haga que aparte una copia del material antes de escribir y que la certificación salga de comparar los dos, no de sus notas. *Origen:* la 02 pedía reportar los contadores antes y después. Un modelo puede recalcular sus propios números tras guardar, verlos consistentes consigo mismos y certificar de buena fe sin haber comparado nunca contra el original.

**17 · Una herramienta de convergencia sin piso de insumo se vuelve una de divergencia.** Si le permite completar lo que falta, dígale también cuánto es demasiado y qué hace entonces. *Origen:* a la 04 le pegaron «a la gente le cuesta organizarse porque es desorganizada» y reformuló igual: inventó un quién, una tarea y una causa suyos, y después varió una parte por línea. De la frase original sobrevivió el verbo. La persona escogía entre tres versiones de una historia de la máquina, las tres marcadas como generadas y sin una sola palabra propia debajo. La regla de completar lo que falta servía para eso, para completar — no para fabricar de dónde agarrarse.

**18 · No le entregue a la persona el arma con la que va a presionar.** Si un paso obliga a producir un juicio, mire qué prohibición de otro paso queda expuesta por ese juicio. *Origen:* la 04 tenía que decir cuál de las tres partes estaba más floja, y sus tres reformulaciones venían etiquetadas por parte. «La causa es la más floja» se leía como «tome la línea LA CAUSA», y la persona lo usó en el turno siguiente con las palabras de la propia herramienta. Se arregló moviendo el juicio junto al examen de la frase, lejos de las opciones etiquetadas — sin gastar una palabra.

**19 · Una prohibición nueva no hereda el alcance de las viejas.** Cuando agregue una defensa, revise si el candado que extiende las prohibiciones a toda la conversación la nombra a ella también. *Origen:* el freno de insumo de la 04 se escribió en el Paso 2, y el candado de «toda la conversación» nombraba solo las dos prohibiciones del Paso 3. Al insistirle, el probador se negó igual — y lo confesó: «me negué por lectura del espíritu del prompt, no por una regla escrita».

**20 · Corregir engorda: mida el tamaño antes de dar la corrección por buena.** Cada defecto que sale de una corrida se arregla escribiendo una regla más, y las reglas suman. *Origen:* arreglar seis defectos de la 03 la infló un 45 %, de 747 a 1.084 palabras, y la dejó más grande que la 02 — en la herramienta cuyo diseño entero es caber en un minuto y pegarse desde un celular. Volvió a 804 cortando repetición, enumeraciones de escapatorias y explicaciones que ya vivían en el documento. Una corrección no está terminada hasta que el tamaño vuelve.

## Cómo se prueba

⛔ **No en la misma conversación donde lo escribió.** Sale contaminado: usted sabe lo que quiso decir. Ábralo en una ventana nueva, como si fuera alguien más.

Tres corridas, con casos distintos:

| Corrida | Quién simula | Qué comprueba |
|---|---|---|
| **La clara** | responde bien a todo | conteos, formato, que no se frene |
| **La torcida** | responde mal a propósito: varios grupos, «no sé», sin trabajo previo | que las defensas disparen |
| **La incompleta** | no adjunta lo que hace falta | que se detenga y lo pida en vez de fabricarlo |

### Qué revisar en cada corrida

- ¿Respetó los conteos exactos?
- ¿Se frenó a preguntar algo fuera de la única pausa permitida?
- ¿Declaró la ruta o el camino que tomó?
- ¿La verificación se apoya en un dato real o repitió la plantilla?
- ¿Marcó como conjetura lo que no puede saber?
- ¿El formato de salida se puede pegar donde tiene que ir?

Y pruebe en más de un asistente. Los modelos ligeros —las versiones «lite» y «flash»— no ejecutan código y no van a devolver archivos por más que afirmen que sí.

⛔ **Un probador que corre dentro del repositorio no está aislado, por más que solo le pase el prompt.** Las instrucciones del repositorio se le cargan solas antes de que abra nada, así que llega sabiendo cómo se diseñó el texto que va a recibir. Y llegan en la versión del arranque de la sesión, no en la de ahora: en una medición reciente el probador describió reglas que ya se habían cambiado y reportó una rama que no era la de trabajo. *Origen:* se le pidió a un probador que reportara qué tenía en contexto antes de leer el prompt. Respondió con las dos cosas que no debía tener: las reglas de escritura y el protocolo de prueba. Sirve pedirle esa medición en cada corrida y anotarla junto al resultado; lo que no sirve es suponer el aislamiento.

⛔ **Un insumo de prueba incompleto convierte la corrida de fondo en una corrida de puerta, y el resultado se lee como aprobado.** *Origen:* la corrida clara de la 02 se armó con la hoja de finalistas vacía. La puerta de entrada disparó con razón, el probador se detuvo, y la corrida nunca llegó al paso que había que medir — el de escribir en el archivo. Lo dijo él, no quien la diseñó: «si el propósito era medir el comportamiento de escritura, el fixture no lo permite». Revise que el caso de prueba pase las puertas que no está probando.

⛔ **No pruebe con un ejemplo que vive dentro del prompt.** El modelo lo reconoce y la corrida mide la búsqueda, no el criterio. *Origen:* dos corridas de la 03 se hicieron con «el reciclaje», que el propio prompt trae como ejemplo de su categoría B. Lo notó el probador: «la corrida no prueba si sé clasificar; prueba que sé buscar el ejemplo».

## Lo que no se puede resolver escribiendo mejor

Dos cosas, y conviene saberlas antes de intentarlo:

**No puede impedir que desobedezca.** Puede hacer que lo confiese. Diseñe para que el fallo sea visible, no para que sea imposible.

**No sabe nada de su ciudad ni de sus clientes.** Todo lo que diga sobre el mundo real es una conjetura plausible, y varias van a ser falsas con seguridad y buen tono. Pídale que marque lo que está suponiendo — y desconfíe si no marca nada.
