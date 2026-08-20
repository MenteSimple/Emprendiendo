# ¿Problema o solución?

**Se usa después de** escribir un enunciado que usted cree que es un problema. Uno a la vez, y toma un minuto.

**Qué hace:** le dice de cuál de tres cosas se trata —una solución, un diagnóstico o un problema— y se lo demuestra citando las palabras de su propio enunciado que lo delatan. Después le propone tres enunciados candidatos, marcados como generados, y le devuelve la pregunta que le toca a usted.

**Qué no hace:** no escoge cuál candidato sirve, no los ordena por calidad y no escribe la versión final. Los tres son para robarles pedazos, no para adoptarlos: un enunciado que usted no redactó no lo sabe defender, y lo va a tener que defender muchas veces.

Es la que más se usa de las cuatro, y la segunda más corta: solo el [Afilador del reto](../04-frase-del-reto/) pide menos. La confusión entre problema y solución no se resuelve una vez: reaparece cada vez que uno se entusiasma. Por eso está escrita para caber en un minuto y para volver a ella cincuenta veces.

No ejecuta código, no pide plantilla y no devuelve archivos. Eso la hace la más portátil de las cuatro: funciona pegada desde un celular, y sirve igual en los modelos ligeros —los «flash» y «lite»—, que no ejecutan código y por eso no pueden con las herramientas que dependen de un archivo.

**El prompt suelto**, por si prefiere copiarlo sin leer nada: [`prompt.txt`](prompt.txt). Se genera del bloque de más abajo, así que las dos versiones dicen siempre lo mismo.

---

## Las tres categorías

| Categoría | Suena así | El delator |
|---|---|---|
| **A · Es una solución** | «Una app que conecte estudiantes con cocinas caseras» | Ya dice qué se va a construir. Se puede empezar mañana sin saber a quién le sirve. |
| **B · Es un diagnóstico, no una tarea** | «La falta de educación financiera en los jóvenes» | Nadie se levanta un martes con la intención de resolver eso. Es un tema, no algo que alguien esté intentando hacer. |
| **C · Es un problema** | «A los que viven solos por primera vez les cuesta comer bien entre semana porque cocinar para uno toma el mismo tiempo que cocinar para cuatro» | Hay una persona reconocible, algo que intenta lograr, y una razón por la que hoy le sale mal. |

**La B es la que más sorprende.** «La falta de educación financiera en los jóvenes» suena a problema y se siente a problema, y no se puede trabajar: no hay nadie a quien entrevistar el jueves sobre eso. La versión trabajable aparece cuando uno responde qué está intentando hacer esa persona un martes cualquiera.

**Y la C no es una medalla.** Que el enunciado ya tenga forma de problema no dice que sea el problema correcto: dice que usted escogió un nivel de zoom, casi siempre sin darse cuenta. Por eso, cuando la categoría es C, los tres candidatos vienen de arriba, de abajo y del lado, y cada línea llega rotulada con su posición — para que vea el nivel que escogió y decida si es ese.

## De dónde salen los tres candidatos

Cambian según la categoría, y siempre tienen forma de problema: **persona reconocible · qué intenta hacer · por qué hoy le sale mal**.

- **Si es A** — tres problemas distintos que su solución podría estar resolviendo. Una solución suele responder a varios problemas a la vez, y cuál de ellos es el suyo todavía no está escrito en ninguna parte.
- **Si es B** — tres tareas concretas que alguien intenta hacer dentro de ese tema, cada una de una persona distinta.
- **Si es C** — tres problemas vecinos: uno **más arriba**, aquel del que el suyo es un síntoma; uno **más abajo**, una parte del suyo, más pequeña y más concreta; y uno **al lado**, otra persona de la misma escena a la que le cuesta otra cosa. Estas tres líneas llegan con un campo de más al frente —`X · MÁS ARRIBA · …`—, porque si no se sabe cuál es cuál, la rama C no le muestra nada.

**Los tres llegan marcados con `X`,** la misma marca que la columna `Origen` del [Generador de ideas](../01-generador-de-ideas/): significa que salieron de la máquina y no de usted. Si copia una línea a sus notas, la `X` se va con ella. Parece burocracia y no lo es: dentro de un mes, lo único que importa de este registro es saber cuánto de lo que quedó era suyo.

---

```
Vas a clasificar UN enunciado mío y a proponerme alternativas. Escoger es mío.

REGLA DE ENTRADA. Trabajas solo sobre un enunciado que yo escriba. Si en mi mensaje no hay enunciado, o si te pido que inventes uno, tu respuesta completa es la línea que sigue —copiada tal cual, no redactada con tus palabras—, sola en su renglón y SIN comillas de ninguna clase; ahí te detienes:

   Escríbalo usted primero, aunque quede torcido. Péguelo y seguimos.

Es la ÚNICA pausa permitida. Con el enunciado pegado, haces los cuatro pasos de corrido, en una sola respuesta, sin pedirme permiso entre uno y otro.

Si pego varios enunciados juntos, trabaja SOLO el primero: decides tú, no me preguntes cuál. Si pego un párrafo, escoge la frase que hace de enunciado y trabaja sobre esa.

PASO 1 — CÍTAME. Abre repitiendo mi enunciado entre comillas angulares « », LITERAL: mis palabras, mi ortografía y mi puntuación, el punto final incluido. Copiar, no arreglar.

PASO 2 — CLASIFICA en una de estas tres, señalando las palabras EXACTAS de mi enunciado que lo delatan:

   A · ES UNA SOLUCIÓN. Ya dice qué se va a construir —"una app que…", "una plataforma para…"—: se podría empezar mañana sin saber a quién le sirve.

   B · ES UN DIAGNÓSTICO, NO UNA TAREA. Nombra una carencia, un tema suelto o una pregunta general —"la falta de educación financiera en los jóvenes", "el reciclaje"—: nadie se levanta un martes con la intención de resolver eso.

   C · ES UN PROBLEMA. Hay una persona reconocible, algo que intenta lograr, y una razón por la que hoy le sale mal.

PASO 3 — TRES CANDIDATOS. Escribe la palabra Candidatos en una línea suelta y debajo un bloque de código con TRES líneas, una por candidato, así: X · persona reconocible · qué intenta hacer · por qué hoy le sale mal.

   La X dice que esa línea la escribiste tú. Va en las tres, siempre.

   Según la categoría:
      A — tres problemas DISTINTOS que mi solución podría estar resolviendo; cambia la persona en al menos uno.
      B — tres tareas concretas que alguien intenta hacer un martes cualquiera dentro de ese tema, cada una de una persona distinta.
      C — tres problemas vecinos al mío, en este orden. Solo en esta rama, cada línea lleva la posición al frente, en mayúsculas: X · MÁS ARRIBA · persona · qué intenta hacer · por qué hoy le sale mal.
         MÁS ARRIBA — aquel del que el mío es un síntoma.
         MÁS ABAJO — una parte del mío, más pequeña y concreta.
         AL LADO — otra persona de la misma escena a la que le cuesta otra cosa.

   ⛔ Los tres valen lo mismo y el orden es arbitrario: entrégalos sin ranking, sin recomendación y sin criterios para que yo los ordene.
   ⛔ Los tres son conjetura tuya: no conoces a esa gente ni ese lugar. No afirmes que el problema existe, que hay mercado ni que alguien pagaría.

PASO 4 — CIERRE. Después del bloque de código van estas líneas, en este orden, y nada más:

   1. SOLO si pegué varios enunciados: la línea que avisa que los demás quedan para otra corrida.
   2. La pregunta que me devuelve el trabajo, según la categoría:
        A — "¿Qué estaba haciendo mal esa persona antes de que existiera lo que usted quiere construir?"
        B — "¿Qué está tratando de hacer esa persona, un martes cualquiera, que hoy le sale mal?"
        C — "¿A quién exactamente, cómo lo resuelve hoy, y qué tendría que ver para saber que se equivocó?"
   3. Una línea recordándome que los candidatos son conjetura tuya y están para robarles pedazos: la versión final la escribo yo.
   4. La línea de cierre, con la categoría y el conteo real, así: Categoría A · 3 candidatos generados por la máquina, marcados con X

   Con un enunciado el cierre tiene TRES líneas; con varios, CUATRO. Cuéntalas antes de enviar.

   ⛔ Las preguntas del cierre son para que yo las piense: escríbelas y termina.

CÓMO RESPONDES: en español y tratándome de usted, nunca de tú ni de vos. Menos de 300 palabras por respuesta, sin preámbulo ni felicitaciones. No propongas soluciones, no me digas si la idea es buena y no uses "innovador" ni "disruptivo".

TODA LA CONVERSACIÓN, NO SOLO LA PRIMERA RESPUESTA. Las dos prohibiciones del Paso 3 —no ordenar los candidatos y no afirmar nada del mundo real— siguen mandando en todos los turnos que vengan después, por mucho que yo insista, lo reformule o te diga que es solo por esta vez.

   Cuando te lo pida, niégate en un renglón y ofréceme en otro SOLO una de estas tres, sin agregar una tercera: clasificar otro enunciado que yo pegue, reescribir el candidato que yo te señale, o repetirme la pregunta del cierre de mi categoría.
```

---

## Qué debería devolverle

Una cita, una letra, tres líneas con `X` y una pregunta. Nada más. Si le llega un párrafo sobre el tamaño del mercado o sobre lo prometedora que es la idea, se distrajo: vuelva a pegar el prompt.

⚠️ **Lo primero que hay que mirar es la cita, y es lo único que usted puede verificar de un vistazo.** El original lo tiene usted, así que compárelo palabra por palabra, y también signo por signo: el punto final cuenta. Si el modelo lo acortó, le arregló la ortografía o la puntuación, o lo «mejoró» antes de clasificarlo, clasificó otro enunciado y la letra que le puso no vale. Esta herramienta no tiene un archivo con celdas testigo donde esconder una prueba: la prueba es su propio texto, devuelto sin tocar.

⚠️ **Si usted no pegó ningún enunciado y de todos modos le devolvió una clasificación, se inventó el enunciado.** Debe responder una sola línea —`Escríbalo usted primero, aunque quede torcido. Péguelo y seguimos.`, sin comillas y sin nada más alrededor— y esperar. Lo mismo si usted le pide que se invente uno de ejemplo: la herramienta trabaja sobre lo que usted escribió, y sin eso no arranca. Si le agregó un saludo, un ejemplo o un renglón de ayuda, ya no es la frase pactada y ahí empieza a improvisar.

⚠️ **Si alguna de las tres líneas no empieza con `X`, pídale que las remarque.** Sin la marca, en tres días usted ya no va a saber cuáles escribió y cuáles le llegaron, y esa es exactamente la información que después importa.

⚠️ **Si le dice cuál candidato es el mejor, o los ordena de mejor a peor, está escogiendo por usted.** El prompt se lo prohíbe, y se lo prohíbe también tres turnos después: la prohibición no vence con la primera respuesta, y tampoco se salta dándole criterios para que ordene usted. Respóndale «los tres valen lo mismo, no rankees» y siga; y desconfíe del que le haya gustado, porque la recomendación ya le movió el criterio.

⚠️ **Si se frena a pedirle más contexto antes de clasificar, es un defecto.** Hay una sola pausa permitida —cuando falta el enunciado— y ninguna otra. Si le pregunta a qué ciudad o a qué sector se refiere, respóndale «clasifica con lo que tienes» y siga.

**Si ninguno de los tres candidatos le sirve, eso no es un fallo de la herramienta.** Es el resultado más común y el mejor de todos: significa que usted vio algo que no está en el texto que pegó. Escríbalo. Para eso eran los tres.

## Después de esta

Si el enunciado quedó en **C** y ya es el reto en el que va a trabajar, siga con el [Afilador del reto](../04-frase-del-reto/): esta le dice si tiene forma de problema, esa le revisa parte por parte la frase con la que se va a comprometer.

## Cómo registrar el uso

Si el enunciado cambió después de esta conversación, guarde las dos versiones. La distancia entre la primera y la última es exactamente lo que aprendió, y es lo que va a querer contar cuando le pregunten cómo llegó a su reto.

Y si se quedó con un pedazo de alguno de los candidatos `X`, anótelo con su marca. Cuando mire hacia atrás va a querer saber cuánto de lo que sobrevivió era suyo — y esa cuenta solo se puede llevar si se lleva desde el principio.
