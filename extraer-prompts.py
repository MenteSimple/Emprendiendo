#!/usr/bin/env python3
"""Genera el `prompt.txt` de cada herramienta a partir de su `README.md`.

Por qué existe. Cada herramienta necesita dos cosas: un documento que explique
cuándo se usa y qué esperar, y el prompt solo, para quien lo quiera copiar sin
leer nada. Tener el prompt escrito en dos archivos es garantía de que se
desincronizan: basta una corrección aplicada en uno y no en el otro.

Entonces el README.md manda —el prompt vive dentro de su primer bloque de
código— y el prompt.txt se genera. Si hay que corregir el prompt, se corrige
el README y se vuelve a correr esto.

    python3 extraer-prompts.py            # regenera todos
    python3 extraer-prompts.py --revisar  # solo avisa si alguno quedó viejo
"""

import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
BLOQUE = re.compile(r"^```[a-z]*\n(.*?)^```", re.S | re.M)
CABECERA = (
    "# Generado desde README.md por extraer-prompts.py — no editar a mano.\n"
    "# Si hay que cambiar el prompt, se cambia el README y se vuelve a generar.\n\n"
)


def prompts() -> list[tuple[Path, str]]:
    salida = []
    for readme in sorted(RAIZ.glob("*/*/README.md")):
        m = BLOQUE.search(readme.read_text(encoding="utf8"))
        if not m:
            print(f"⚠️  sin bloque de código: {readme.relative_to(RAIZ)}")
            continue
        salida.append((readme.parent / "prompt.txt", CABECERA + m.group(1).strip() + "\n"))
    return salida


def main() -> int:
    revisar = "--revisar" in sys.argv
    desactualizados = 0
    for destino, contenido in prompts():
        actual = destino.read_text(encoding="utf8") if destino.exists() else None
        if actual == contenido:
            print(f"·  al día      {destino.relative_to(RAIZ)}")
            continue
        desactualizados += 1
        if revisar:
            print(f"⚠️  desactualizado  {destino.relative_to(RAIZ)}")
        else:
            destino.write_text(contenido, encoding="utf8")
            palabras = len(contenido.split())
            print(f"✅ generado    {destino.relative_to(RAIZ)}  ({palabras} palabras)")
    if revisar and desactualizados:
        print(f"\n⛔ {desactualizados} prompt(s) sin regenerar. Corre `python3 extraer-prompts.py`.")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
