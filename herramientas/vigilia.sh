#!/usr/bin/env bash
# Cada 30 min: salud del lote (solo lectura) al log + copia de seguridad. Termina cuando muere lote.py.
cd /home/daw/Sprint
while pgrep -f "harness/lote.py" >/dev/null; do
  { echo "=== $(date -u +%H:%M) UTC — bloque B ==="; python3 herramientas/salud_lote.py --desde 20260913T200900 --hash bf1b18a696a98476; } >> herramientas/salud.log 2>&1
  herramientas/respaldo.sh >> herramientas/salud.log 2>&1
  sleep 1800
done
{ echo "=== $(date -u +%H:%M) UTC — lote.py terminó (bloque B) ==="; python3 herramientas/salud_lote.py --desde 20260913T200900 --hash bf1b18a696a98476; } >> herramientas/salud.log 2>&1
herramientas/respaldo.sh >> herramientas/salud.log 2>&1
