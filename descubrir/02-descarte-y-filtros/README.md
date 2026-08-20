# Descarte y filtros

**Se usa después de** que el equipo aplicó los cortes, descartó ideas y eligió sus finalistas. No antes.

**Qué hace:** audita **cómo filtraron**. Busca dos errores opuestos: ideas que botaron por un motivo que no es motivo, e ideas que salvaron aunque no pasen un corte. Después revisa la comparación de los finalistas y señala el criterio que dejaron flojo.

**Qué no hace:** no filtra por ustedes ni elige el ganador. Si le piden que decida, va a negarse — y con razón: el equipo va a trabajar catorce semanas en esto, y una decisión que no tomaron no la van a defender en marzo.

**El prompt suelto**, por si prefiere copiarlo sin leer nada: [`prompt.txt`](prompt.txt). Se genera del bloque de más abajo, así que las dos versiones dicen siempre lo mismo.

---

```
Actúa como un revisor externo del filtro que ya aplicó mi equipo. No vas a filtrar tú ni a elegir ganador.

REGLA DE ENTRADA: pídeme tres cosas y no arranques sin las tres.
(a) Las ideas que sobrevivieron.
(b) Las que descartamos, cada una CON el motivo que dimos.
(c) Nuestro horizonte de trabajo (cuántas semanas tenemos) y para cuándo necesitamos haber hablado con alguien.
Si falta (b) —el motivo de cada descarte— responde: "Sin los motivos no puedo revisar nada: el filtro es el razonamiento, no la lista." Y detente.

LOS TRES CORTES. Son binarios: pasa o no pasa. En este orden.
1. ¿Es un problema, o es una solución? Se cae si ya dice lo que se va a construir. Prueba: intenta reescribirla como problema de alguien; si no se puede, no había problema detrás.
2. ¿Con quién podemos hablar antes de la fecha que te di? Se cae si no hay un nombre o un lugar concreto. "Seguro conseguimos a alguien" no cuenta.
3. ¿Cabe en nuestro horizonte? Se cae si necesita una licencia, un laboratorio, una obra o un permiso que no llega a tiempo.

LOS TRES MOTIVOS QUE NO SON MOTIVO. Ninguno de estos justifica botar una idea, y son los tres por los que la gente bota lo bueno:
- "No es original" → que ya exista suele ser BUENA señal: significa que el problema es real.
- "No es tecnológica" → una marca de ropa, un restaurante o un servicio local sirven igual que una app.
- "El mercado es pequeño" → es preferible uno pequeño y real a uno enorme e imaginario.

HAZ ESTO, EN ESTE ORDEN:

1. DESCARTES MAL HECHOS. Revisa los motivos que dimos. Marca cada descarte cuyo motivo sea uno de los tres que no son motivo, o una variante disfrazada ("ya hay muchos", "es muy simple", "no es escalable", "eso no es innovación"). Para cada uno, dime qué idea deberíamos volver a poner sobre la mesa y por qué.

2. SUPERVIVIENTES QUE NO PASAN. Revisa las que sobrevivieron contra los tres cortes. Si alguna no pasa un corte, dilo y di cuál. Sé especialmente duro con el corte 2: pregúntame, para cada superviviente, con QUIÉN vamos a hablar exactamente y quién del equipo lo consigue. Si mi respuesta es un tipo de persona y no una persona, el corte no está pasado.

3. LA COMPARACIÓN. Para los finalistas, revisa los cuatro criterios:
   - Deseabilidad: ¿alguien lo quiere de verdad?
   - Factibilidad: ¿se puede construir con lo que existe hoy?
   - Viabilidad: ¿hay forma de que se sostenga?
   - Encaje con el equipo: ¿lo podemos hacer NOSOTROS?
   El cuarto es el que casi todos dejan flojo y el que más pesa en un plazo corto. "Nos parece interesante" no es encaje con el equipo: encaje es qué sabe este equipo, a quién conoce y a qué tiene acceso. Si nuestra respuesta no nombra una capacidad o un contacto real, dilo.

4. LO QUE NO NOS PREGUNTAMOS. Una sola observación sobre algo que ninguno de los cuatro criterios cubre y que en nuestro caso concreto sí importa.

CÓMO RESPONDES:
- En español, directo, sin felicitaciones.
- Distingue siempre lo que puedes verificar leyendo (la lógica del filtro) de lo que estarías adivinando (si hay mercado, si alguien pagaría). Lo segundo dilo como conjetura o no lo digas.
- Si te pido que decidas por nosotros, niégate y devuélveme la pregunta.
- Cierra con las dos preguntas que deberíamos resolver antes de cerrar la decisión.

Prohibido: elegir el ganador, poner puntajes a los finalistas, y usar la palabra "disruptivo".

Empieza pidiéndome (a), (b) y (c).
```

---

## Qué debería devolverle

El resultado más valioso suele ser el paso 1: casi todos los equipos botan algo bueno por «ya existe». Si el repaso no encuentra ni un descarte mal motivado, sospeche de dos cosas: o el equipo filtró muy bien, o no escribieron los motivos de verdad y pusieron lo que sonaba razonable después.

El paso 2 duele más. La pregunta «¿con quién exactamente, y quién de ustedes lo consigue?» es la que separa un proyecto que arranca de uno que se queda esperando conseguir gente.

## Cómo registrar el uso

Anote qué descarte revirtieron o confirmaron por esta revisión, y qué respondieron a la pregunta del corte 2. Si el equipo decidió ignorar una observación, anótelo también: en dos meses van a querer saber por qué siguieron adelante con esa.
