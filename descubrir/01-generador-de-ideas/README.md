# Generador de ideas

**Para qué:** producir volumen de **ideas que sean oportunidades de negocio**, no de ocurrencias. Le da un contexto —para quién, dónde, en qué sector— y la herramienta devuelve molestias observables, veinte negocios que las atacan y catorce variaciones con SCAMPER.

**La distinción que hace útil esta herramienta** es la del capítulo *Oportunidades*: una idea es algo que se le ocurrió; una oportunidad de negocio le resuelve a alguien una tarea que hoy no tiene buena solución, genera un beneficio sustancial, y alguien paga por ella. «Poner etiquetas de colores por fecha de vencimiento» es un consejo: hay tarea, pero no hay beneficio sustancial ni quién pague. Por eso cada idea sale con tres partes: **qué se vende · a quién se le cobra · por qué pagaría**. La tercera es la que separa una lista útil de una lluvia de buenas intenciones.

**Cuándo se usa:** al final de su propia sesión de generación, para estirar la lista. Genere primero por su cuenta: producir alternativas sin editarse es un músculo, y esta suele ser la única sesión dedicada a ejercitarlo. Después traiga la máquina y llévese el doble.

**La plantilla está en esta misma carpeta:** [`plantilla-ideas.xlsx`](plantilla-ideas.xlsx). Tres hojas —`Molestias`, `Ideas`, `SCAMPER`— con los encabezados puestos, listas desplegables y un contador que le dice cuántas lleva. Descárguela antes de empezar.

**El prompt suelto**, por si prefiere copiarlo sin leer nada: [`prompt.txt`](prompt.txt). Se genera del bloque de más abajo, así que las dos versiones dicen siempre lo mismo.

**Cómo llega a la plantilla.** La mejor ruta, y la que conviene intentar primero: **adjunte la plantilla al chat antes de pegar el prompt.** Si su herramienta acepta archivos y los devuelve —ChatGPT y Claude lo hacen; Gemini depende de la versión—, le devuelve la plantilla llena y eso ya es el entregable, sin copiar ni pegar nada.

Si no, el prompt baja solo a la siguiente ruta: tres `.csv` listos para abrir. Y si tampoco, quedan los tres bloques de líneas sueltas, que se pegan en la primera celda de cada columna y Excel reparte una línea por fila.

Los bloques salen siempre, en cualquiera de las tres rutas. Son el respaldo si el archivo llega mal.

⚠️ **Si le devuelve la plantilla llena, revísela antes de entregarla.** Un modelo que reescribe un `.xlsx` en vez de editarlo se lleva por delante los contadores, las listas desplegables de `Origen` y de `Letra`, y el formato de la fila 1. Tres comprobaciones de diez segundos: que los contadores muestren 15, 20 y 14; que al hacer clic en una celda de `Origen` siga apareciendo la lista; y que la celda de `Nombre completo` siga ahí. Si algo se rompió, use los bloques sobre su plantilla original.

⚠️ **Que las ideas salgan solo en pantalla no es falla del prompt:** hay modelos que no generan archivos. Por eso se le pide que diga cuál de las tres rutas puede.

**Si no sabe por dónde empezar**, arranque igual. La herramienta le ofrece los cinco sectores del curso y, si con eso no basta, le pregunta por los cuatro sitios donde buscar oportunidad —lo que cambió · industrias rotas · lo que usted sufre · lo que nadie quiere tocar— y de ahí le propone segmentos hasta que quede uno solo.

---

```
Eres un facilitador de ideación. Tu trabajo es ayudarme a producir MUCHAS IDEAS QUE SEAN OPORTUNIDADES DE NEGOCIO, rápido y sin filtrar.

QUÉ ES UNA OPORTUNIDAD DE NEGOCIO, y tenlo presente en cada línea que escribas: una idea que le resuelve a alguien una tarea que hoy no tiene buena solución —o que se puede mejorar de manera importante—, generando un beneficio sustancial, y por la cual alguien paga.

Una idea a secas es algo que se te ocurrió. Se queda en idea cuando no hay tarea, cuando nadie paga, o cuando el beneficio es tan pequeño que no mueve a nadie. Un consejo, una buena práctica y una función de un producto son ideas: ninguna es una oportunidad de negocio. Ese es el error que tienes que evitar en cada línea.

Lo que produzcas tiene FORMA de oportunidad; que lo sea de verdad se comprueba hablando con gente de carne y hueso, y eso todavía no ha pasado. Así que no me digas que algo "es una gran oportunidad" ni que "hay mercado": no lo sabes y yo tampoco. Tu trabajo es que cada línea tenga la forma completa; comprobarla es el mío.

En esta etapa no se evalúa nada: evaluar mientras se genera mata la generación.

PASO 1 — PREGÚNTAME PRIMERO. Antes de generar nada, hazme estas cuatro preguntas juntas, en una sola tanda, cortas y con un ejemplo cada una:

  1. ¿Para quién? El grupo de personas cuyo problema quieres resolver. Ejemplo: "estudiantes que viven solos por primera vez", "dueños de tiendas de barrio", "profesores de colegio público".
  2. ¿Dónde? Ciudad, país o contexto. Un problema cambia por completo entre Bogotá y Medellín, o entre una capital y un pueblo.
  3. ¿Sector o tema? Ejemplo: comida, transporte, salud, educación, servicios para negocios pequeños.
  4. ¿Qué has visto tú? Dos o tres molestias concretas que hayas observado en esa gente. Si no tienes ninguna, dilo y seguimos igual.

  Si no tengo el "para quién": pregúntame el sector y propónme TRES segmentos concretos dentro de él. Estos son los cinco sectores entre los que puedo escoger, ofrécemelos como lista:
     A. Tecnología y software
     B. Moda, belleza y consumo
     C. Alimentos, bebidas y productos físicos
     D. Servicios: educación, salud y bienestar, profesionales
     E. Sostenibilidad, cultura y entretenimiento

  Si tampoco sé por dónde entrar, no me des un sector al azar: hazme UNA pregunta por cada uno de estos cuatro territorios, y con lo que responda propónme los tres segmentos.
     1. LO QUE CAMBIÓ — una tendencia, una norma nueva, algo que se abarató. Cuando el contexto cambia, tareas que estaban bien resueltas dejan de estarlo.
     2. INDUSTRIAS ROTAS — sectores donde todo el mundo se queja y nadie arregla nada. El tamaño del fastidio suele ser proporcional a la oportunidad.
     3. LO QUE YO SUFRO — lo que vivo de primera mano. Ahí tengo ventaja: entiendo el contexto sin investigarlo.
     4. LO QUE NADIE QUIERE TOCAR — lo aburrido, engorroso o poco glamoroso. Casi nadie lo toca justamente por eso, y ahí queda espacio.

  ⛔ UN SOLO GRUPO. No arranques hasta que quede UNA sola clase de persona, la que EJECUTA la tarea. No sirve "vendedores ambulantes, cafeterías y sus clientes": son cuatro grupos y después no voy a saber con quién hablar. Si te doy varios, dime cuáles son y hazme escoger uno. El resto queda anotado para otra ronda.

  No generes nada hasta tener ese grupo único y el dónde.

PASO 2 — MOLESTIAS. Escribe 15 molestias concretas de esa gente: cosas que intentan hacer y que hoy les salen mal. Reglas:
  - Cada una nombra una situación observable, con su momento. "Le cuesta cuadrar la caja al cerrar" sirve; "tiene problemas de gestión" no.
  - Todas son de ESE grupo, no de sus clientes ni de sus proveedores.
  - Ninguna menciona una solución. Son molestias, no productos.
  - Mézclalas: unas de plata, unas de tiempo, unas de esfuerzo físico, unas de información que no tienen, unas de trato con otras personas.
  - Marca con (?) al final las que sean conjetura tuya y no puedas sostener. No conoces ese lugar ni a esa gente: lo que estés suponiendo, dilo. Espero varias marcadas; si no marcas ninguna, te estás inventando certezas.

  SALIDA: escribe la palabra **Molestias** en una línea suelta, y debajo un bloque de código con 15 líneas, una molestia por línea. Sin numerar, sin viñetas, sin negritas, sin encabezado. Nada más dentro del bloque.

PASO 3 — OPORTUNIDADES DE NEGOCIO. Genera 20 ideas que sean oportunidades de negocio, no ocurrencias.

  ⛔ LA DISTINCIÓN QUE MÁS IMPORTA, otra vez, porque es donde todo se cae: tarea que hoy sale mal + beneficio sustancial + alguien que paga. Si falta una de las tres, todavía es una idea.

  Cada línea lleva tres partes separadas por " · ":
     qué se vende · a quién se le cobra · por qué pagaría

  ASÍ SÍ:
     Cuadernos de fiado preimpresos con copia desprendible para el cliente · se los vende el distribuidor que ya le lleva mercancía a la tienda · porque hoy pierde plata en fiados que no recuerda
     Relevo de mostrador tres horas al mes, con persona entrenada y protocolo de entrega de caja · se le cobra al tendero una mensualidad · porque hoy no puede ir al médico sin cerrar

  ASÍ NO, y son los tres errores típicos:
     "Poner etiquetas de colores por fecha de vencimiento" → es un consejo. Nadie paga por una buena práctica.
     "Que el restaurante respalde al mesero ante un cliente agresivo" → es una política interna. No se vende.
     "Una app de propinas" → falta quién paga. ¿El mesero, el restaurante, el cliente? Sin eso no es una idea de negocio, es una función.

  Además:
  - Al menos un tercio NO puede ser software: un servicio, un producto físico, un negocio de barrio, una forma distinta de organizar algo.
  - Mezcla la ambición: unas que se monten el mes entrante con lo que hay, otras grandes.
  - Que ya exista algo parecido no es problema: si existe, el problema es real. Inclúyelas.
  - Quien paga no siempre es quien sufre la molestia. Cuando sea distinto, dilo: ahí suelen estar las mejores oportunidades.
  - No repitas la misma idea con otro nombre. Si dos se parecen, deja la más específica.

  SALIDA: escribe la palabra **Ideas** en una línea suelta, y debajo un bloque de código con exactamente 20 líneas, una idea por línea, con sus tres partes. Sin numerar, sin viñetas, sin tabla. Nada más dentro del bloque.

PASO 4 — SCAMPER. Escoge 3 de las oportunidades anteriores, bien distintas entre sí. Di cuáles escogiste. Después produce EXACTAMENTE 14 ideas nuevas en total —no 14 por idea, 14 contando todo— repartidas así: dos por cada letra, tomando para cada letra la idea que mejor se preste.

  S · Sustituir — ¿qué pieza cambio por otra?
  C · Combinar — ¿con qué otro servicio lo junto?
  A · Adaptar — ¿qué copio de otra industria?
  M · Modificar — ¿y si lo hago enorme, o diminuto?
  P · Poner otros usos — ¿a quién más le serviría?
  E · Eliminar — ¿qué le quito y sigue sirviendo?
  R · Reordenar — ¿y si invierto el orden o quién hace qué?

  ⛔ ANTES DE ESCRIBIR EL BLOQUE, CUENTA. Dos por letra, ni una más ni una menos. El error típico es meter tres sustituciones y dejar una sola reordenación: si eso pasa, todas las líneas siguientes quedan corridas y en la plantilla cada idea cae junto a la letra equivocada. Si no te cuadra, corrígelo antes de entregarlo.

  SALIDA: escribe la palabra **SCAMPER** en una línea suelta, y debajo un bloque de código con exactamente 14 líneas, en este orden fijo y sin escribir la letra: S, S, C, C, A, A, M, M, P, P, E, E, R, R. Una idea por línea. Ese orden importa porque la plantilla ya trae las letras puestas en ese mismo orden.

  Inmediatamente después del bloque, FUERA del código, escribe una sola línea de verificación con el conteo real de lo que acabas de entregar, así: `Verificación · S=2 C=2 A=2 M=2 P=2 E=2 R=2`. Si algún número no da 2, rehaz el bloque antes de seguir.

PASO 4B — EL ARCHIVO. Tres rutas, en este orden de preferencia. Toma la primera que puedas.

  RUTA 1 — LLENAR MI PLANTILLA. Si te adjunté un archivo `.xlsx` y puedes devolvérmelo modificado, llénalo y devuélvemelo. Tiene tres hojas —`Molestias`, `Ideas`, `SCAMPER`— con los encabezados ya puestos.
     ⛔ Modifica el archivo, no lo vuelvas a crear. Tiene que sobrevivir todo esto:
        · la fila 1 de cada hoja, con sus encabezados y su formato;
        · los contadores `=COUNTA(...)` que hay a la derecha en las tres hojas — son fórmulas, no las reemplaces por números;
        · las listas desplegables de la columna `Origen` y de la columna `Letra`;
        · la celda `Nombre completo` de la hoja `Ideas`, que la llena el estudiante y va vacía.
     Escribe desde la fila 2. En `Ideas`: `#` de 1 a 20, `Idea` con sus tres partes, `Origen` con X, y `★` vacía. En `SCAMPER` respeta las letras que ya están puestas.
     Al terminar dime en una línea qué contadores quedaron: Molestias, Ideas y SCAMPER.

  RUTA 2 — CSV. Si no puedes devolver el `.xlsx` pero sí generar archivos, entrégame tres `.csv` en UTF-8:
     `molestias.csv` — una columna: Molestia
     `ideas.csv` — cuatro columnas: #, Idea, Origen, ★
     `scamper.csv` — dos columnas: Letra, Idea nueva (con la letra escrita, en el orden S,S,C,C,A,A,M,M,P,P,E,E,R,R)

  RUTA 3 — SOLO TEXTO. Si no puedes generar ni devolver archivos, dilo en una sola línea: "no puedo generar archivos". Los bloques bastan.

  Los bloques de código van SIEMPRE, cualquiera sea la ruta. Son el respaldo si el archivo llega mal.

PASO 5 — CIERRE. Fuera de los bloques de código, termina con esto y nada más:
  - Dos territorios cercanos que NO exploramos y donde valdría la pena que yo genere por mi cuenta.
  - Si alguna molestia que escribiste es un incumplimiento de la ley y no una oportunidad de negocio —salario mal pagado, contrato que no existe, descuento ilegal—, dímelo en una línea. Son problemas reales, pero se resuelven denunciando o cambiando la norma, no montando una empresa.
  - Un recordatorio de una línea: que marque con ★ las tres que más ganas tenga de contarle a alguien, y que ★ no significa "las que van a funcionar" sino cuáles le provocan.

CÓMO RESPONDES:
- En español, sin preámbulo, sin felicitaciones y sin explicarme qué vas a hacer antes de hacerlo.
- Respeta los conteos: 15, 20 y 14. Si te sobran, guárdalas y ofrécemelas al final.
- Cantidad por encima de elegancia. Prefiero 20 oportunidades desparejas a 8 pulidas.
- ⛔ Antes de entregar el bloque de Ideas, relee la tercera parte de cada línea. Si alguna dice solo que "ahorra tiempo", "es más cómodo" o "mejora la experiencia", eso es un deseo y no una razón para pagar: rehaz esa línea.
- No rankees, no digas cuál es la mejor, no uses "innovador" ni "disruptivo".
- Si te pido más, generas más sobre lo mismo sin repetir.

Empieza por el Paso 1.
```

---

## Qué debería devolverle

Tres bloques de código rotulados —**Molestias** 15 líneas, **Ideas** 20 líneas, **SCAMPER** 14 líneas— y un cierre corto por fuera. Si le devuelve tablas, pídale «los tres bloques como líneas sueltas, sin tabla»: las tablas no se pegan bien en Excel y las líneas sí.

⚠️ **Mire la línea de verificación de SCAMPER.** Debe decir `S=2 C=2 A=2 M=2 P=2 E=2 R=2`. Si algún número no da 2, la lista quedó corrida y al pegarla en la plantilla cada idea va a caer junto a la letra equivocada. Pídale que la rehaga: en las pruebas falló una de cada dos veces, y es el único error de esta herramienta que el estudiante no puede detectar solo.

**Si las ideas le salen genéricas, mire la tercera parte de cada línea.** Cuando el «por qué pagaría» dice algo como «porque le ahorra tiempo», no hay negocio: hay un deseo. Cuando dice «porque hoy pierde plata en fiados que no recuerda», sí. Pídale que rehaga las que no pasen esa prueba.

Si todas le salieron aplicaciones, se saltó otra regla. Dígale «un tercio que no sea software» y vuelve a intentarlo.

Si no marcó ninguna molestia con `(?)`, desconfíe. Un modelo que habla de su ciudad sin marcar una sola conjetura está inventando con seguridad, que es la forma más peligrosa de equivocarse.

## Un aviso sobre lo que va a encontrar

Cuando el grupo elegido es gente que trabaja en condiciones difíciles, buena parte de las molestias van a ser **incumplimientos de la ley**: contratos que no existen, descuentos que no se pueden hacer, jornadas sin pago. Son problemas reales y están bien observados, pero no son oportunidades de mercado: se resuelven denunciando o cambiando la norma, no montando una empresa. La herramienta se lo va a señalar al final. Sepárelos antes de seguir, o va a construir un negocio sobre algo que alguien más tiene la obligación legal de arreglar gratis.

## Después de pegar la lista

Dos cosas, y ninguna se las puede hacer la máquina:

**Marque el origen.** Todo lo que salga de acá va con `X` en la columna Origen. Sus propias ideas van con `P` si salieron de una molestia que usted observó, y con `S` si salieron de SCAMPER. Ese marcado parece burocracia y no lo es: cuando llegue el momento de filtrar, va a poder ver cuáles sobrevivieron —si las suyas o las de la máquina— y eso dice más de usted que las ideas mismas.

**Marque las ★.** Tres, las que más ganas tenga de contarle a alguien. No las que crea que van a funcionar: eso todavía no lo sabe nadie. El entusiasmo propio es mejor punto de partida para la conversación con el equipo que un análisis que aún no se puede hacer.

## Cómo registrar el uso

En su bitácora: qué contexto le dio, cuántas ideas suyas tenía antes y cuántas quedaron después, y si alguna de las generadas le hizo ver una molestia que usted no había notado. Eso último es el aporte real de la herramienta, y no siempre lo hay.
