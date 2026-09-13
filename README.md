# LLM Incidents — cooperación costosa entre agentes

**Pregunta de investigación.** ¿Cuánto de su propio presupuesto sacrifica un agente LLM para
responder una solicitud anónima que no le reporta nada, y paga menos cuando cuesta más?

Sprint de investigación en seguridad de IA (Apart Research / CeSIA). El diseño confirmatorio
está congelado en `docs/PREREGISTRO.md`; el estado operativo del día y el plan de cierre están en
`docs/ESTADO-Y-PLAN.md`.

Modelo único: `glm-5.3-flash` vía gateway opencode-go (se declara así en abstract y límites).

## Cómo correr algo

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # completar las API keys de los proveedores usados

python3 harness/validador.py      # valida una escena antes de gastar tokens
python3 harness/lote.py           # corre un lote de corridas
python3 dashboard/servidor.py     # http://127.0.0.1:8890, panel de solo lectura
```

Las escenas activas (`escena*.json`, `escena*.resuelta.json`) viven en la **raíz** a propósito:
`harness/` y `analisis/` las leen por ruta relativa fija. Las escenas ya cerradas/archivadas están
en `escenas-guardadas/`.

## Estructura

```
harness/          Arnés del juego: bucle de rondas, puerto de mensajes, validador, lote, análisis
analisis/          Estimadores, codificación ciega, descriptivos (leen salidas/ y reportes/)
scripts/           Utilidades de un solo uso (codificación de depósitos, etc.)
dashboard/         Panel de solo lectura sobre corridas, agregados y documentos (servidor.py)
herramientas/      Scripts operativos (salud del lote, respaldo)
data/raw/          Insumos externos (artefactos públicos del incidente, exploitgym)
figuras/           Figuras del reporte y sus scripts generadores
salidas/           Salida cruda de cada corrida del harness (resumen.json, eventos.jsonl, ...)
reportes/          Agregados y reportes derivados de salidas/
escenas-guardadas/ Escenas archivadas (no las que usa el lote activo)
otros/             Andamiaje de una pregunta de investigación anterior, archivado (ver su README)
docs/
  PREREGISTRO.md        Hipótesis, N, criterios de abandono — congelado antes de correr, no se toca
  PROTOCOLO-JUEGO.md    Formalización de teoría de juegos del protocolo de créditos
  papers.md             Literatura, verificada identificador por identificador contra arXiv
  ESTADO-Y-PLAN.md      Pregunta + estado vigente + plan de cierre de hoy + plan de implementación
  investigacion.md      Propuesta original, verificación (anclas de METR + defectos), brief de familias mixtas
  planificacion.md      Qué entra al repo al publicarlo + enmiendas (lote en curso y brazos futuros)
  paquete-final.md      Checklist de entrega + material para el reporte (con el mapa de rúbrica)
  esquema-paper.pdf     Esqueleto del paper (mapa de regímenes, para revisión de mentor)
  notas.md              La tesis del reporte (ideas.md) + coordinación maestro/Claude/DeepSeek (todo.md)
  historia.md           Documentos ya superados (investigación inicial, manifiesto de un paquete anterior)
  apart-sprint.md       Bases del sprint publicadas por los organizadores
```

Los cuatro documentos que lee `dashboard/servidor.py` (`DOCS` en ese archivo: `PREREGISTRO.md`,
`PROTOCOLO-JUEGO.md`, `papers.md`, `ESTADO-Y-PLAN.md`) están en `docs/` en su raíz — si se renombran
o mueven, actualizar esa lista.

## Reproducibilidad

`requirements.txt` se generó desde el entorno virtual del proyecto (`.venv`, gestionado con `uv`).
`docs/planificacion.md` §A documenta qué debe entrar/salir del repo antes de publicarlo y la
revisión de uso dual pendiente.

## Estado y verificación (de `EXPORTACION.md`, fusionado aquí)

- **Instrumento**: `harness/prueba_solvente.py` — decenas de comprobaciones sin gastar tokens.
  Cubre que la tarea se puede ganar, que el umbral muerde, que un depósito impagable se rechaza,
  que la lista blanca de comandos aguanta intentos de inyección, y que un depósito por HTTP se
  cobra y entra en la vista.
- **Escena**: `harness/validador.py` — invariantes condicionales al brazo + grep de canarios sobre
  todas las superficies de texto. Emite `escena.resuelta.json`, lo que consume el bucle.
- **Validez de corridas**: `harness/agregar.py` no confía en el resumen de la corrida: lo contrasta
  con el libro de presupuesto y el registro de actividad del servicio, y excluye por evidencia
  (saldo negativo, depósito no contado, truncamiento, corrida sin estímulo).
- **Verificar sin gastar un token**:
  ```bash
  python3 harness/validador.py
  python3 harness/prelanzamiento.py
  python3 harness/agregar.py
  ```
- **Honestidad sobre el estado**: cada defecto del arnés lo encontró correr, no la revisión — están
  documentados uno por uno en `docs/investigacion.md` §B, con la evidencia que los delata.

## Seguridad

`.env` (claves de API) nunca se versiona — ver `.gitignore`. No hay claves en el histórico de git.
