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

## Las diez reglas, y de dónde salió cada una

Salen de correr la herramienta 01 contra Copilot, Gemini y Claude el 19 de agosto de 2026. Ninguna es teórica.

**1 · Pida contexto antes de producir.** Sin insumo propio, la herramienta no arranca. Es lo que separa una que ayuda de una que reemplaza. Funcionó en los tres motores.

**2 · Prohíba las pausas, salvo una.** Todos los pasos en una sola respuesta. Si hay una pausa legítima —falta un archivo, falta un dato que solo la persona tiene—, declárela como la única, con la frase exacta que debe decir. Cada pregunta a mitad de camino es una oportunidad de que la persona conteste cualquier cosa con tal de avanzar. *Origen:* Claude se frenó en el Paso 4 de la 01 y hubo que responderle «escoge tú».

**3 · Nunca ponga la orden en forma de pregunta.** «Escoge tres de las anteriores» se lee como consulta. «Escoge TÚ tres, no me preguntes cuáles, decide y sigue» no. *Origen:* la frase exacta que frenó a Claude en el Paso 4 —la misma de la regla 2—: era una orden escrita como pregunta, y por eso se leyó como pregunta.

**4 · Verifique con algo que no se pueda inventar.** No pida una frase, pida un dato que solo exista si el trabajo se hizo: el texto de una celda que no aparezca en el prompt, un valor calculado, un conteo real. Y ofrezca la salida honesta: «si no pudiste, escribe NO PUDE y no inventes». Si se le da la frase con la que debe certificar algo, la escribe sin hacer nada: una plantilla de verificación es un formulario en blanco. *Origen:* Gemini 3.5 Flash-Lite, que no ejecuta código y no generó ningún archivo, escribió igual «Leído del archivo · contadores 15/34/14 · fórmulas intactas».

**5 · Obligue a declarar el camino.** Una línea fija al final: qué ruta tomó, qué hizo, qué no pudo. No evita el fallo, lo vuelve visible. Un fallo declarado se corrige; uno silencioso se entrega. *Origen:* Copilot no pudo abrir la plantilla y fabricó un `.xlsx` nuevo —con las hojas correctas y sin fórmulas ni listas—, y solo se supo porque lo mencionó de pasada.

**6 · No ofrezca una alternativa sin haberla probado sola.** Dos caminos que parecen equivalentes y no lo son son peores que uno solo. Si la vía B depende en secreto de la A, va a fallar justo cuando la A no está. *Origen:* se agregó «bájala de esta URL» como alternativa a adjuntar el archivo. Ninguno de los tres motores pudo: adjuntar el archivo es lo que activa el entorno de código, así que la segunda vía dependía de la primera. Costó tres corridas fallidas.

**7 · Lea lo que su propio material dice adentro.** Si la herramienta entrega un archivo o una plantilla, eso suele traer instrucciones propias. Un prompt que las contradice pierde: el modelo le hará caso al material, y con razón. *Origen:* el prompt decía «20 filas, Origen X» y el panel de la plantilla decía que las de SCAMPER van también en esa hoja con meta 34. Gemini le hizo caso a la plantilla —con razón— y marcó mal la columna.

**8 · Repita los números y pida el conteo final.** Un modelo al que se le piden 15 devuelve 15 o 20. Si la cantidad importa, dígala dos veces y exija el conteo real al cerrar.

**9 · Marque lo generado.** Lo que produjo la máquina va señalado, y esa marca no se puede confundir con la del trabajo de la persona. Sirve para lo único que importa después: ver qué sobrevivió, si lo propio o lo generado.

**10 · Las reglas van al prompt; las explicaciones, al documento.** El modelo necesita la regla. El porqué lo lee una persona. Un prompt con ensayos adentro crece sin mejorar y se vuelve imposible de pegar desde un celular.

## Cómo se prueba

⛔ **No en la misma conversación donde lo escribió.** Sale contaminado: usted sabe lo que quiso decir. Ábralo en una ventana nueva, como si fuera alguien más.

Tres corridas, con casos distintos:

| Corrida | Quién simula | Qué comprueba |
|---|---|---|
| **La clara** | responde bien a todo | conteos, formato, que no se frene |
| **La torcida** | responde mal a propósito: varios grupos, «no sé», sin trabajo previo | que las defensas disparen |
| **La incompleta** | no adjunta lo que hace falta | que se detenga y lo pida en vez de fabricarlo |

Y pruebe en más de un asistente. Los modelos ligeros —las versiones «lite» y «flash»— no ejecutan código y no van a devolver archivos por más que afirmen que sí.

## Lo que no se puede resolver escribiendo mejor

Dos cosas, y conviene saberlas antes de intentarlo:

**No puede impedir que desobedezca.** Puede hacer que lo confiese. Diseñe para que el fallo sea visible, no para que sea imposible.

**No sabe nada de su ciudad ni de sus clientes.** Todo lo que diga sobre el mundo real es una conjetura plausible, y varias van a ser falsas con seguridad y buen tono. Pídale que marque lo que está suponiendo — y desconfíe si no marca nada.
