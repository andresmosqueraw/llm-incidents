#!/usr/bin/env bash
# Congelamiento: la secuencia completa, en orden, en un solo comando.
#
#   bash analisis/congelar.sh
#
# Se corre UNA vez, cuando el ultimo lote haya cerrado. Hace, en este orden:
#   1. trae salidas/ del arbol 2 al arbol 1, para que todo quede en un solo lugar
#   2. el analisis confirmatorio (la mirada, con las tres declaradas)
#   3. el analisis del 2x2 de abstencion
#   4. el analisis de la familia del incidente
#   5. la auditoria de integridad sobre todas las familias
#   6. las figuras vectoriales
#   7. la tabla de numeros congelados y los hashes de los archivos que la sostienen
#
# No calcula nada por su cuenta: solo encadena los guiones ya probados y deja el rastro de hashes.

set -u
RAIZ="$(cd "$(dirname "$0")/.." && pwd)"
ARBOL2="$(dirname "$RAIZ")/Sprint-2"
PY="$RAIZ/.venv-inspect/bin/python"
PYFIG="/tmp/venv-figuras/bin/python"
cd "$RAIZ" || exit 1

echo "=== 0. comprobacion: no hay lotes vivos ==="
if pgrep -f "[l]ote.py" >/dev/null; then
  echo "  HAY LOTES CORRIENDO: se detiene. El congelamiento espera a que cierren."
  pgrep -af "[l]ote.py" | sed 's/^/    /'
  exit 1
fi
echo "  ninguno: se puede congelar"

echo
echo "=== 1. traer los datos del arbol 2 ==="
traidas=0
if [ -d "$ARBOL2/salidas" ]; then
  for d in "$ARBOL2"/salidas/2026*/; do
    [ -d "$d" ] || continue
    nombre="$(basename "$d")"
    if [ ! -d "$RAIZ/salidas/$nombre" ]; then
      cp -r "$d" "$RAIZ/salidas/$nombre" && traidas=$((traidas+1))
    fi
  done
fi
echo "  corridas traidas del arbol 2: $traidas (las ya presentes no se tocan)"

echo
echo "=== 2. analisis confirmatorio (la mirada) ==="
"$PY" analisis/confirmatorio.py

echo
echo "=== 3. abstencion: 2x2 ==="
"$PY" analisis/abstencion.py

echo
echo "=== 4. familia del incidente ==="
"$PY" analisis/incidente.py

echo
echo "=== 5. auditoria de integridad ==="
"$PY" analisis/auditoria_aislamiento.py 2>&1 | tail -12

echo
echo "=== 6. figuras ==="
if [ -x "$PYFIG" ]; then
  "$PYFIG" analisis/figuras.py
else
  echo "  falta el entorno de figuras ($PYFIG): se omiten. Recrearlo con:"
  echo "    uv venv --python 3.12 /tmp/venv-figuras && uv pip install -p /tmp/venv-figuras/bin/python matplotlib"
fi

echo
echo "=== 7. tabla de numeros y hashes del congelamiento ==="
mkdir -p docs
"$PY" analisis/tabla-numeros.py > docs/NUMEROS-CONGELADOS.md
echo "  escrito docs/NUMEROS-CONGELADOS.md"
echo
echo "  hashes de los archivos que sostienen los numeros:"
for f in reportes/confirmatorio.json reportes/abstencion-2x2.json reportes/incidente.json; do
  if [ -f "$f" ]; then
    printf "    %-34s %s\n" "$f" "$(sha256sum "$f" | cut -c1-16)"
  fi
done
echo
echo "  figuras:"
ls -1 figuras/*.pdf 2>/dev/null | sed 's/^/    /'
echo
echo "CONGELADO. Los numeros estan en docs/NUMEROS-CONGELADOS.md y sus hashes arriba."
