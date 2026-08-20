# Estado del repositorio

Actualizado: **20 de agosto de 2026**

## Dónde va cada herramienta

| # | Herramienta | Escrita | Probada | Publicada |
|---|---|---|---|---|
| 01 | Generador de ideas | ✅ | ⚠️ el prompt cambió después de probarlo | ✅ |
| 02 | Descarte y filtros | ✅ terminada | ⚠️ corrida, pero sin registro en su README | ✅ |
| 03 | ¿Problema o solución? | ✅ reescrita | ✅ ocho corridas | ✅ |
| 04 | Afilador del reto | ✅ reescrita | ✅ | ✅ |

Las cuatro están escritas bajo las veinte reglas. Lo que queda no es escribir, es cerrar la validación.

## Lo que hay que hacer, en orden

**1 · Dejar por escrito cómo se probó la 02.** El ticket de pruebas está cerrado, pero su `README.md` no tiene sección de corridas, así que desde el repositorio no hay forma de saber qué se probó ni con qué caso. La 01 y la 03 sí lo tienen. Sin eso, la próxima persona que la retome no sabe si el fallo que vea es nuevo o conocido.

**2 · Dos huecos abiertos en la 02, los dos en la plantilla y no en el prompt.**

`Finalistas` no tiene fila donde escribir los nombres de los tres: los encabezados son `① ② ③` con formato de encabezado, así que nadie escribe ahí. El prompt lo tapa —«si la fila 1 no trae nombres, llámalos ①②③»— pero entonces la revisión solo puede decir «el ②», que es lo que se quería evitar.

`Sobrevivientes` tiene columna para el corte 2 y no para los cortes 1 y 3, así que esos dos hay que juzgarlos de la línea de la idea. Es una decisión de diseño, no un descuido: la alternativa es una columna por corte, y encarece lo que el equipo tiene que llenar antes de usarla. Hay que decidirla, no dejarla implícita.

**3 · Volver a correr la 01.** «El estudiante» ya salió: los seis usos donde así se le decía a quien usa la herramienta pasaron a «quien te escribe». Pero el cambio **dejó sin validar la única herramienta que estaba probada en tres motores**: el prompt que se corrió no es el que está publicado.

**4 · Correr las cuatro en más de un motor.** Todo lo de anoche se probó en uno solo. Necesita a una persona presente. Es el issue #15.

**5 · Auditar y mezclar a `main`.** El grep institucional, el texto dentro de los `.xlsx`, `extraer-prompts.py --revisar`, y las reglas una por una. Es el issue #16.

## Lo que quedó decidido y no hay que volver a discutir

- El repositorio es un proyecto personal, no material institucional. Nada puede remitir a ninguna universidad.
- `README.md` de cada herramienta es la fuente; `prompt.txt` se genera con `extraer-prompts.py`.
- Las reglas operativas van al prompt; las explicaciones, al README.
- Se prueba en contexto aislado, nunca en la conversación donde se escribió.
- Verificar siempre con un dato que el modelo no pueda inventar.

## La 02, en detalle, por si se retoma en frío

Su plantilla tiene tres hojas —`Descartadas`, `Sobrevivientes`, `Finalistas`— y una columna `Revisión` en cada una que **solo llena la herramienta**. `Descartadas` y `Sobrevivientes` llevan además una columna `Origen`, para que no se confunda lo que escribió el equipo con lo que agregó la máquina.

Los rótulos testigo están en la columna `F` de `Descartadas` —«Casillas con tinta», «Puño del equipo», «Ideas huérfanas»— y **no aparecen en el prompt**. Sirven para comprobar que el modelo abrió el archivo de verdad, y su README explica cómo comprobar en diez segundos que no tocó nada más.

**Dos versiones de esta herramienta se escribieron en paralelo el 20 de agosto**, en dos ramas, sin saber una de la otra. Sobrevivió la de `wayfinder/descubrir-02-03-04`, que llegó más lejos: quitó el desplegable que bloqueaba una columna, dejó una sola pausa declarada, exige una cita textual del material cuando la revisión no es `ok` a secas, y busca contradicciones entre hojas. De la otra rama quedó lo que no estaba allá y este archivo recoge arriba: los dos huecos de la plantilla.

Lo que se comprobó en corridas sobre la versión descartada, y que conviene volver a comprobar sobre esta: que respeta la columna `Revisión` sin tocar nada más, que no rellena celdas que el equipo dejó vacías, y que las `=COUNTA(...)` sobreviven como fórmulas —se ven vacías hasta que Excel recalcule, y eso no es un fallo del modelo.
