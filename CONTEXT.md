# Vocabulario

Las palabras con las que se habla de este repositorio. Si un término no está acá, todavía no está resuelto.

## Etapa

Cada uno de los cuatro tramos del método: **Descubrir · Proponer · Construir · Validar**. Una etapa es una carpeta del repositorio y agrupa varias herramientas.

⛔ No es «fase». Y la tercera es **Construir**, no «Modelar».

## Herramienta

Un prompt que produce un resultado dentro de una etapa. Vive en una subcarpeta numerada —`descubrir/02-descarte-y-filtros/`— y su `README.md` es la fuente única.

**Una herramienta no es una Skill.** Es texto que se pega en cualquier asistente, desde un celular, sin instalar nada. Esa portabilidad es una decisión, no una limitación: una Skill correría solo en Claude Code y dejaría por fuera a la mayoría de quien usa esto.

## Paso

Cada tramo numerado dentro del prompt de una herramienta. Los pasos van de corrido en una sola respuesta, salvo la única pausa declarada.

## Insumo

Lo que una herramienta exige antes de producir nada, y que siempre es trabajo que la persona ya hizo. Sin insumo la herramienta se detiene y lo pide: no lo rellena.

## Resultado

Lo que una herramienta deja al terminar, y que suele ser el insumo de la siguiente.

⛔ Nunca **«la entrega»**: esa palabra es vocabulario de aula y está prohibida por el `grep` institucional.

## Divergir · Converger

Los dos movimientos del método. En **divergencia** la máquina amplía sin límite. En **convergencia** pide el trabajo hecho, produce alternativas marcadas y **tiene prohibido escoger**.

## Descartar

Sacar una idea de la mesa dejando escrito el motivo. El descarte es **sustractivo**: lo que sigue vivo no es «lo elegido», es lo que nadie botó y por eso sigue siendo viable.

⛔ No hay número mínimo ni máximo de sobrevivientes. Un número objetivo convertiría el descarte en una selección, que es otra cosa.

## Origen · `P` `S` `X`

La marca de procedencia de cada idea: `P` si salió de un problema que la persona observó, `S` si salió de SCAMPER, `X` si la sugirió una IA. Viaja con la idea de una herramienta a la siguiente, y es lo único que después permite saber qué sobrevivió al descarte: lo propio o lo generado.

## `★`

Las tres ideas que la persona más ganas tiene de contarle a alguien, marcadas al terminar de generar.

⛔ **No es una preselección y no alimenta el descarte.** Es entusiasmo anterior a cualquier filtro, y usarla para filtrar sería editarse mientras se genera.

## Corte · Filtro

No son lo mismo y confundirlos desordena toda la etapa.

Un **corte** elimina: es binario, no admite «más o menos», y se aplica a **todas** las ideas. Son tres — es un problema o una solución, hay alguien concreto con quien hablar, cabe en el plazo.

Un **filtro** compara: tiene matices y se aplica solo a **las pocas** que sobrevivieron. Son cuatro — deseabilidad, factibilidad, viabilidad, encaje con el equipo.

⛔ Aplicarle los cuatro filtros a treinta ideas no lo hace nadie, y aplicarles los cortes binarios a tres es llegar tarde.

## Hoja de descarte

El archivo que produce el generador de ideas al terminar: una fila por idea, con `Origen`, las columnas de los tres cortes, el motivo escrito y la preferencia de cada persona. **Las columnas las llena el equipo**; la máquina la prepara y después la audita.

No hay número de sobrevivientes: mínimo uno, máximo ninguno.

## Ejecutor de la tarea

Quien realiza la tarea que la hipótesis nombra. Es la misma persona que el «quién» con el que se mira una idea al principio, vista después de saber qué está tratando de lograr.

⛔ No es «el cliente» ni «el usuario»: es quien **ejecuta la tarea**, que puede no ser quien paga.

## Hipótesis JTBD

Lo que el equipo sale a validar. Son **dos frases**, y entre las dos cubren las cuatro fuerzas:

> **«Cuando [detonante], [ejecutor] quiere [tarea funcional], para poder [resultado deseado], sin [ansiedad principal].»**
>
> **«Hoy lo resuelve [apaño], y le falla porque [causa].»**

La primera está escrita desde la persona; la segunda desde afuera. **Esa asimetría es a propósito** y no se corrige.

## Las cuatro fuerzas

Lo que mueve o frena un cambio: **empuje** —la frustración con lo de hoy—, **atracción** —lo que promete lo nuevo—, **ansiedad** —lo que da miedo del cambio— y **hábito** —lo que ya se hace y funciona a medias—. Se cambia cuando empuje + atracción > ansiedad + hábito.

Cada hueco de la hipótesis alimenta una: *causa* → empuje · *resultado* → atracción · *ansiedad* → ansiedad · *apaño* → hábito.

## Competencia real

Lo que la persona usa hoy para salir del paso, **incluido el apaño casero y no hacer nada**. Es el `apaño` de la segunda frase, y es lo que casi todos los equipos se saltan.
