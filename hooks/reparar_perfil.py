"""Repair the known GET /api/me response-property regression in a profile module."""
import argparse
from pathlib import Path

BROKEN = "const user = payload.profile;"
FIXED = "const user = payload.user;"


def reparar_perfil(archivo):
    archivo = Path(archivo)
    contenido = archivo.read_text(encoding="utf-8")
    if contenido.count(BROKEN) != 1:
        raise ValueError(
            f"Se esperaba exactamente una referencia rota a payload.profile en {archivo}"
        )
    with archivo.open("w", encoding="utf-8", newline="") as destino:
        destino.write(contenido.replace(BROKEN, FIXED, 1))
    return archivo


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archivo", type=Path, help="Ruta al archivo src/profile.js")
    args = parser.parse_args()
    corregido = reparar_perfil(args.archivo)
    print(f"Hook: contrato de GET /api/me corregido en {corregido}")


if __name__ == "__main__":
    main()
