# LLM Incidents — cooperación costosa entre agentes

**Pregunta de investigación.** ¿Cuánto de su propio presupuesto sacrifica un agente LLM para
responder una solicitud anónima que no le reporta nada, y paga menos cuando cuesta más?

Sprint de investigación en seguridad de IA (Apart Research / CeSIA). El diseño confirmatorio
está congelado en `docs/PREREGISTRO.md`; el estado operativo del día se sigue en
`docs/ESTADO.md` y `docs/PLAN-CIERRE.md`.

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
  ESTADO.md, PREREGISTRO.md, PLAN-IMPLEMENTACION.md, PROTOCOLO-JUEGO.md,
  papers.md, MEJORAS-ANTES-DEL-LOTE.md, EXPORTACION.md   Documentos vivos que sirve el dashboard
  PLAN-CIERRE.md, PREGUNTA-INVESTIGACION.md              Estado del cierre y pregunta original
  planificacion/    Planes de ejecución e implementación (plan.md, plan-repo.md, enmiendas...)
  investigacion/    Anclas, defectos conocidos, propuesta original, briefs de brazos exploratorios
  paquete-final/    Checklist de entrega, material para el reporte, esquema del paper
  notas/            Ideas y listas de tareas de trabajo
  apart-sprint/     Bases del sprint publicadas por los organizadores
```

Los siete documentos que lee `dashboard/servidor.py` (`DOCS` en ese archivo) están en `docs/` en
su raíz — si se renombran o mueven, actualizar esa lista.

## Reproducibilidad

`requirements.txt` se generó desde el entorno virtual del proyecto (`.venv`, gestionado con `uv`).
`plan-repo.md` (en `docs/planificacion/`) documenta qué debe entrar/salir del repo antes de
publicarlo y la revisión de uso dual pendiente.

## Seguridad

`.env` (claves de API) nunca se versiona — ver `.gitignore`. No hay claves en el histórico de git.
