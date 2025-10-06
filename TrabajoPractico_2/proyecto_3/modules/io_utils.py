# modules/io_utils.py
import re
from modules.graph import Graph
from typing import Tuple

def parse_line(line: str) -> Tuple[str, str, int]:
    s = line.strip()
    # quitar paréntesis exteriores
    if s.startswith("(") and s.endswith(")"):
        s = s[1:-1].strip()

    patterns = [
        r"""^\s*['"]?([A-Za-zÁÉÍÓÚáéíóúÑñ\s]+?)['"]?\s*[,;]\s*['"]?([A-Za-zÁÉÍÓÚáéíóúÑñ\s]+?)['"]?\s*[,;]\s*([0-9]+)\s*$""",
        r"""^\s*['"]?([A-Za-zÁÉÍÓÚáéíóúÑñ\s]+?)['"]?\s+['"]?([A-Za-zÁÉÍÓÚáéíóúÑñ\s]+?)['"]?\s+([0-9]+)\s*$"""
    ]

    for pat in patterns:
        m = re.match(pat, s)
        if m:
            a = m.group(1).strip()
            b = m.group(2).strip()
            w = int(m.group(3))
            return a, b, w

    # Si no cumple ningún patrón, devolver None (se interpretará como inválido)
    return None

def load_aldeas_from_file(path: str) -> Graph:
    g = Graph()
    with open(path, "r", encoding="utf-8") as f:
        for i, raw in enumerate(f, start=1):
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            parsed = parse_line(line)
            if parsed is None:
                print(f"⚠️  Línea {i} ignorada (formato inválido): '{line}'")
                continue
            try:
                u, v, w = parsed
                g.add_edge(u, v, w)
            except Exception as e:
                print(f"⚠️  Error en línea {i}: {e}. Línea omitida.")
                continue
    return g

