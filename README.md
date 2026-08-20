# Herramientas de IA para emprender

Prompts en español para las dos cosas que la IA hace bien en un proyecto de emprendimiento: **ampliar** cuando hay que generar, y **discutir** cuando hay que decidir.

## El principio: divergir con la máquina, converger usted

Emprender alterna entre dos movimientos, y confundirlos es de donde vienen casi todos los errores.

**Cuando toca divergir** —generar ideas, imaginar segmentos, listar formas de resolver algo— la IA es una ventaja enorme y no hay razón para no usarla a fondo. Produce volumen, no se cansa, y no tiene el pudor que a uno lo frena en la idea número doce. Úsela sin culpa. Las herramientas de esta etapa generan mucho, rápido y despareja.

**Cuando toca converger** —descartar, escoger, comprometerse— la máquina no decide. No porque no pueda dar una respuesta, sino porque va a dar una excelente respuesta con datos que no tiene, y usted va a trabajar meses sobre esa decisión. Ahí las herramientas cambian de papel: piden lo que usted ya decidió, buscan el punto débil y le devuelven la pregunta.

Confundir los dos movimientos es lo que produce las dos fallas típicas: editarse mientras se genera —y quedarse con seis ideas prudentes— o dejar que la máquina escoja —y defender en marzo una decisión que uno no tomó.

## Las reglas

1. **Contexto suyo, primero.** Ninguna arranca en el vacío. Las de divergencia preguntan para quién, dónde y en qué sector antes de generar una sola línea. Las de convergencia piden el trabajo que usted ya hizo, con sus razones.
2. **Genera sin límite, decide nunca.** En divergencia produce todo lo que se le pida. En convergencia tiene prohibido escoger por usted.
3. **Todo lo generado va marcado.** Lo que salió de la máquina se distingue de lo que salió de usted y de lo que salió de hablar con gente. Cuando llegue el momento de filtrar, va a querer saber cuál es cuál.
4. **Deja rastro.** Qué herramienta usó, qué le respondió que no esperaba, y qué hizo con eso. El uso de IA declarado se puede discutir; el escondido, no.

## Cómo se usan

Cada archivo tiene un bloque de código con el prompt completo. En GitHub, ese bloque trae un botón de copiar en la esquina superior derecha. Cópielo, péguelo en el chat de IA que use —ChatGPT, Claude, Gemini, el que sea— y responda lo que le pregunte.

No hace falta instalar nada ni abrir cuenta en ningún servicio nuevo. Están escritos para funcionar igual en cualquier modelo razonablemente reciente.

## Cómo está organizado

Una carpeta por herramienta. Al abrirla, GitHub muestra su `README.md`, que explica cuándo se usa, trae el prompt completo con botón de copiar y dice qué esperar de la respuesta. Al lado va el `prompt.txt` —el prompt solo, para quien lo quiera sin leer nada— y los archivos que esa herramienta necesite.

```
descubrir/
└── 01-generador-de-ideas/
    ├── README.md              qué es, cuándo se usa, el prompt, qué revisar
    ├── prompt.txt             el prompt solo
    └── plantilla-ideas.xlsx   el archivo donde se vacía el resultado
```

⚠️ **El `prompt.txt` se genera, no se edita.** Sale del primer bloque de código del `README.md`, que es la única fuente. Si hay que corregir un prompt, se corrige el README y se corre:

```bash
python3 extraer-prompts.py            # regenera todos
python3 extraer-prompts.py --revisar   # solo avisa si alguno quedó viejo
```

Es una precaución con motivo: un prompt escrito en dos archivos se desincroniza a la primera corrección, y entonces la mitad de la gente usa una versión y la otra mitad otra.

## Catálogo

### [Descubrir](descubrir/) — de la idea suelta al reto elegido

| Herramienta | Movimiento | Se usa… |
|---|---|---|
| [Generador de ideas](descubrir/01-generador-de-ideas/) | divergir | al final de su propia sesión de generación, para estirar la lista |
| [Descarte y filtros](descubrir/02-descarte-y-filtros/) | converger | después de que el equipo cortó y eligió finalistas |
| [¿Problema o solución?](descubrir/03-problema-o-solucion/) | converger | cada vez que escriba un enunciado que crea que es un problema |
| [Afilador del reto](descubrir/04-frase-del-reto/) | converger | después de escribir la frase del reto |

Proponer · Modelar · Validar — en construcción.

## Si quiere escribir la suya

Las diez reglas con las que están escritas estas herramientas —y el fallo del que salió cada una— están en **[cómo se escriben estas herramientas](COMO-ESCRIBIR-ESTAS-HERRAMIENTAS.md)**. Ninguna es teórica: cada una es una corrida que salió mal contra Copilot, Gemini o Claude, con lo que dijo el modelo. Sirven para cualquier prompt que tenga que producir algo verificable, no solo para estos.

## Lo que ninguna puede hacer

Ninguna sabe nada de su mercado, sus clientes ni su ciudad. Todo lo que digan sobre el mundo real es una conjetura plausible, y varias van a ser falsas con seguridad y con buen tono. **Sirven para producir alternativas y para revisar razonamientos, no para conseguir hechos.** Los hechos se consiguen hablando con gente, y eso no se delega.

## De quién es esto

Trabajo propio de **Andrés Saldarriaga Navarro**, publicado a título personal. No es material de ninguna institución: no lleva su nombre, ni sus marcas, ni sus ejemplos, ni depende de estar matriculado en nada. Se ofrece a quien quiera usarlo.

## Licencia

Contenido bajo [CC BY-SA 4.0](LICENSE). Puede usarlo, adaptarlo y redistribuirlo, incluso comercialmente, siempre que dé crédito y mantenga la misma licencia.
