# TODO — Claude (13 sep, desde ~13:20 COT)

Lote de 80 en curso hasta ~17:00. Reglas: no mirar 5 vs 20 hasta el cierre; no tocar `harness/`,
puertos 8201-8206, `parametros.json` ni `vista_*.json`; no correr suites ni brazos. Solo lectura.
No redacto prosa del reporte: reviso, verifico, preparo datos y figuras.

## Ahora (protegen lo que ya corre)
- [x] `salud_lote.py` — solo lectura sobre `salidas/`: corridas terminadas, hash de escena igual en todas,
      "sin estímulo", saldos negativos, tareas completadas, rechazos, tokens acumulados vs tope.
      **Sin tasas ni contraste.** Correrlo cada ~30 min y anotar en `todo.md` si algo se sale de rango.
- [x] Copia de seguridad cada 30 min: `salidas/`, `escena*.json`, `harness/instrumento.json`,
      `PREREGISTRO.md` → `respaldos/lote_HHMM.tar.gz`. Solo lectura del origen.

## Antes de las 17:00 (material de apoyo, datos y no prosa)
- [x] Tabla de defectos del instrumento (9): fecha, cómo se detectó, qué sesgaba, cómo se verificó el
      arreglo. Fuente: `ESTADO.md` §4 y §6. Salida: `apendice-defectos.md`.
- [x] Mapa rúbrica → sección: D1 (dónde está la frase del régimen dominado y la cita a 2607.23982),
      D2 (preregistro, hashes, validación adversarial, tabla de defectos), D3 (Figura 1, idea en tres
      frases). Salida: `mapa-rubrica.md`.
- [x] Re-verificar anclas de METR en la copia local (`entrega/fuentes/metr.org-*.md`): líneas 60-61,
      250, 251-252, 1001, 1018, 1029. Anotar cualquier desfase.
- [x] Figura 1 a resolución de imprenta (PNG 300 dpi + versión en inglés para el reporte).
- [x] Esqueleto de la Figura 2 (tasa contra precio 0/5/20 con intervalos), listo para recibir los
      números de `reportes/factorial.json`.
- [ ] Revisar, cuando existan, los borradores humanos de Introduction y Related work: huecos de
      razonamiento, afirmaciones sin fuente, la frase corta del hueco (que sea verdad frente a los
      doce papers verificados).

## Coordinación
- [x] (15:25: sí están — enmiendas de 14:10, 14:35 y 14:40 en §8; `enmiendas-lote-borrador.md` queda redundante) Confirmar con el otro agente que escribió **él** las tres enmiendas del lote en curso en
      `PREREGISTRO.md` §8 (un solo autor). Si a las 16:00 no están, las escribo yo y le aviso.
- [ ] No editar `PREREGISTRO.md`, `ESTADO.md` ni `harness/` mientras él tenga cambios abiertos.

## Después de las 17:00
- [ ] `salud_lote.py` final sobre las 80; confirmar hash único y corridas válidas.
- [ ] Verificar `reportes/factorial.json` congelado (hash del archivo anotado en `todo.md`).
- [ ] Revisar Results y Discussion contra `factorial.json`, número por número.
- [ ] 02:00 — revisión final: cada cifra del PDF rastreable a un archivo; cada ID de arXiv en
      `papers.md`; checklist de Guidelines (≤8 páginas, abstract ≤150, apéndice de uso dual, frase de
      "no se publican recetas de instalación sin revisión").

## Donde el equipo pone la cabeza (yo solo reviso)
Discussion; las tres enmiendas del lote; apéndice de uso dual; la frase corta del hueco; la lectura
de la línea base a precio 0 frente a 2604.07821.

## Hecho (13 sep, 14:15-15:00 COT)
- `herramientas/salud_lote.py` (solo lectura, sin tasas) + `herramientas/vigilia.sh` en segundo plano:
  salud y respaldo cada 30 min a `herramientas/salud.log` y `respaldos/`. Primer respaldo 19:48 UTC.
- `apendice-defectos.md`: 14 defectos del arnés + 10 confundidores de escena, con detección, sesgo y verificación.
- `mapa-rubrica.md`: D1/D2/D3 → sección, con la frase corta del hueco en su forma verdadera.
- `anclas-metr.md`: seis anclas OK; **cuatro incorrectas** ("251-252" → 1025, 1027, 1041, 1050) y dos citas
  nuevas útiles (1164, 1171-1176). Hay que corregir `plan.md` y `PREREGISTRO.md` H6.
- `figuras/fig1-regime-map.png` (EN) y `fig1-mapa-regimenes.png` (ES) a 300 dpi; `figuras/fig2.py` +
  `fig2-datos.json` (placeholder) → `fig2-rate-vs-price.png`.
- `enmiendas-lote-borrador.md`: las tres enmiendas del lote listas para pegar.
- `checklist-entrega.md`: requisitos exactos de Guidelines/FAQ (cierre 11:59 PM AoE = 06:59 COT; reenvío con el
  mismo título reemplaza archivos → enviar borrador a las 02:00 y final antes de las 06:00).
- `plan.md`: anclas de METR corregidas (1025, 1027, 1041, 1050).
- `plan-repo.md`: escaneo de secretos (cero hallazgos reales; 116 rutas absolutas a relativizar), qué entra y
  qué no, `.gitignore`, revisión de uso dual.
- `revision-analisis.md`: cuatro correcciones al código de análisis antes de las 17:00 — la más grave: el
  preregistro dice tres cosas distintas sobre el primario (§2 unión; A1 clave; 14:10 "pendiente").

## 15:10 COT — estado del lote (leído de disco, no de nadie)
- **Bloque A terminado**: `lote_lote-final-a_20260913T195718.json` — 40/40, 110,5 min, 5,06M tokens
  (126k/corrida), hash único `bf1b18a696a98476`, 40/40 con estímulo, 90% tareas completadas, 7%
  rechazos, 0 saldos negativos, 0 truncadas. 4 corridas con un `deposito_impagado` (intento sin saldo:
  evento legítimo, no el doble cobro).
- **Bloque B no está corriendo.** No hay `lote.py` ni `bucle.py`; **los puertos 8201-8206 no escuchan**
  (`servicios.py` caído). La corrida `20260913T195750` arrancó a las 19:57 UTC y quedó interrumpida
  en la ronda 1 (seq 42): **excluir por fallo técnico** (`agregar.py` ya la marca "sin resumen").
- `vigilia.sh` murió con la sesión anterior; se relanza cuando arranque el bloque B.
- Figura 1 regenerada (ES/EN) con 2607.23982 sobre la frontera (±0,05); `figuras/fig1.py` ya vive en el
  repo. `mapa-rubrica.md`: frase corta corregida. `esquema-paper.pdf` regenerado desde `docs/esquema-paper.py` (fuente ahora en el repo), con la fila de
  2607.23982 corregida, el límite del objeto y el estado del lote.

## 15:25 COT — bloque B
- `lote-final-b` corriendo (40 corridas, mismo hash). Vigilancia relanzada con `setsid`, filtrada desde
  20:09 UTC; log en `herramientas/salud.log`, respaldos cada 30 min.
- Siguiente: a las ~17:00 COT, `salud_lote.py --desde 20260913T180000` sobre las 80 (excluyendo la
  interrumpida 195750), y solo entonces `analisis/estimador.py`.

## 16:25 COT — hecho en paralelo durante el bloque B
- `tabla2-validez.md`: Tabla 2 con el bloque A (instrumento, sin tasas).
- Contabilidad de cómputo: 9,93M hasta el bloque B; cierre estimado ~16M.
- `escena-costo-cero.json` y `escena-30.json` verificadas: idénticas a la escena actual salvo precios / presupuesto.
- `apendice-uso-dual-datos.md`: los 325 rechazos clasificados; los "168 intentos de túnel" son reintentos
  de cliente al puerto propio (0 externos); 12 intentos de ayuda por vía no admitida (7 sin consumar).
- `traza-enmiendas.md`: 13 enmiendas fechadas.
- `herramientas/congelar.py`: SHA-256 de resultados con hora para la revisión de las 02:00.
- `todo-deepseek.md`: mensajes con el retiro del punto 6, la corrección de 2607, el primario y la desviación.
- Pendiente: README del repo; revisar borradores humanos cuando existan.
