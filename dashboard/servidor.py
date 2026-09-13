"""Servidor del dashboard de sondas. Solo lectura, sin dependencias.

    python3 servidor.py [puerto]        ->  http://127.0.0.1:8890

Rutas:
    /                     la página
    /api/corpus           reportes/corpus.jsonl como arreglo JSON
    /api/reporte/<arch>   un reporte individual (solo archivos dentro de reportes/)
    /api/estado           los documentos .md del proyecto, para el panel de estado
"""

from __future__ import annotations

import json
import os
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import unquote

BASE = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(BASE)
REPORTES = os.path.join(RAIZ, "reportes")
DOCS = ["ESTADO.md", "PREREGISTRO.md", "PLAN-IMPLEMENTACION.md", "PROTOCOLO-JUEGO.md", "papers.md"]


def _leer_corpus() -> list[dict]:
    ruta = os.path.join(REPORTES, "corpus.jsonl")
    if not os.path.exists(ruta):
        return []
    filas = []
    with open(ruta, encoding="utf-8") as fh:
        for linea in fh:
            linea = linea.strip()
            if linea:
                try:
                    filas.append(json.loads(linea))
                except json.JSONDecodeError:
                    pass
    return filas


class Manejador(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def log_message(self, *a):  # silencio
        pass

    def _json(self, datos, codigo=200):
        cuerpo = json.dumps(datos, ensure_ascii=False).encode("utf-8")
        self.send_response(codigo)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(cuerpo)))
        self.end_headers()
        self.wfile.write(cuerpo)

    def _html(self, texto):
        cuerpo = texto.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(cuerpo)))
        self.end_headers()
        self.wfile.write(cuerpo)

    def do_GET(self):  # noqa: N802
        ruta = unquote(self.path.split("?")[0])
        if ruta in ("/", "/index.html"):
            with open(os.path.join(BASE, "index.html"), encoding="utf-8") as fh:
                self._html(fh.read())
        elif ruta == "/api/corpus":
            self._json(_leer_corpus())
        elif ruta == "/api/reglas":
            p = os.path.join(REPORTES, "reglas.json")
            if os.path.exists(p):
                with open(p, encoding="utf-8") as fh:
                    self._json(json.load(fh))
            else:
                self._json({"error": "corre antes: python3 harness/reglas.py"}, 404)
        elif ruta.startswith("/api/reporte/"):
            nombre = os.path.basename(ruta[len("/api/reporte/"):])
            destino = os.path.join(REPORTES, nombre)
            if not destino.endswith(".json") or not os.path.exists(destino) or REPORTES not in destino:
                self._json({"error": "reporte no encontrado"}, 404)
            else:
                with open(destino, encoding="utf-8") as fh:
                    self._json(json.load(fh))
        elif ruta == "/api/estado":
            salida = {}
            for doc in DOCS:
                p = os.path.join(RAIZ, doc)
                if os.path.exists(p):
                    with open(p, encoding="utf-8") as fh:
                        salida[doc] = fh.read()
            self._json(salida)
        else:
            self._json({"error": "ruta desconocida"}, 404)


def main() -> None:
    puerto = int(sys.argv[1]) if len(sys.argv) > 1 else 8890
    if not os.path.isdir(REPORTES):
        print(f"AVISO: no existe {REPORTES}. Corre antes: python harness/corpus.py")
    srv = ThreadingHTTPServer(("127.0.0.1", puerto), Manejador)
    print(f"dashboard en http://127.0.0.1:{puerto}  (Ctrl-C para parar)", flush=True)
    srv.serve_forever()


if __name__ == "__main__":
    main()
