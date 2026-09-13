# Plan de cierre: responder la pregunta y entregar

**Pregunta de investigación.** ¿Cuánto de su propio presupuesto sacrifica un agente LLM para
responder una solicitud anónima que no le reporta nada, y paga menos cuando cuesta más?

**Escrito:** domingo 13 sep 2026, 11:00 COT. **Cierre:** lunes 14 sep, 06:59 COT (23:59 AoE).
Quedan **20 h de reloj, ~14 útiles**. Este documento manda sobre `PLAN-IMPLEMENTACION.md` en todo lo
operativo de hoy; el diseño sigue siendo el de `PREREGISTRO.md` y no se toca salvo por enmienda fechada.

**Regla de este plan:** nada de lo que sigue cambia hipótesis, N, contrastes ni criterios de
abandono. Solo ordena qué correr, quién lo hace, y qué hay que construir para que el resultado se
pueda reportar.

---

## 1. Cómo se responde la pregunta, en una tabla

| Parte de la pregunta | Desenlace | Cómo se estima | Estado |
|---|---|---|---|
| "¿Cuánto sacrifica?" | **Primario preregistrado:** tasa de depósito (binaria por agente), por celda y corrida | Media por celda; IC95 por bootstrap **por corrida** (10.000 remuestreos) | 9 corridas hechas; **bootstrap sin código** |
| "¿Cuánto sacrifica?" | Secundario: fracción del presupuesto (precio × indicador) | Igual | En `agregar.py` |
| "para responder una solicitud" | **Secundario declarado hoy:** `deposito_clave` (lo depositado responde a la solicitud) | Igual, reportado al lado del primario | Campo existe en `resumen.json`; **`agregar.py` no lo agrega** |
| "¿paga menos cuando cuesta más?" | **H1:** diferencia pareada por corrida, caros menos baratos | 80 diferencias en {−1, −⅔, …, +1}; IC95 bootstrap; regla: si no excluye el cero se reporta *no distinguible de cero con este N* | 9 de 80 |
| ¿El instrumento mide? | **H4:** costo cero ≥ 60% | Ya corrido dos veces: 45,8% [27,9; 64,9] y luego 62,5% [48,4; 74,8] sobre 48 | **Hecho; reportar las dos** |
| ¿Mide costo o retórica? | **H5:** encuadre, ~4 corridas | Comparar movimiento por encuadre contra movimiento por precio | **Escena no existe** |
| Secundarios conductuales | H6 directivo, H6b acatamiento, H7 falsificación | Codificación de los textos de `depositos` por dos anotadores ciegos; falsificación desde `eventos.jsonl` | Reglas fijadas en `PREREGISTRO.md` §4; **sin script ni muestra** |
| Exploratorio | H8: presencia percibida de receptor | Descriptivo: celda 3 (con confederado) contra corridas sin estímulo de calibración | Datos ya existen |

---

## 2. Decisiones que se toman ahora, antes de gastar un token (11:00 a 11:30)

1. **Desenlace primario: se mantiene el preregistrado** ("depositó al menos una vez", cualquier
   depósito acreditado). `deposito_clave` entra como **secundario nombrado**, con enmienda fechada en
   §7 que diga explícitamente que se declara **después de ver 9 corridas de ensayo** y por qué (es el
   acto que la solicitud elicita). Cambiar el primario ahora sería post hoc y un juez lo vería.
2. **N = 80, sin parada opcional, las 9 de ensayo cuentan.** Faltan **71 corridas**. A ~147k tokens
   por corrida son ~10,4M. Gastado hasta hoy ≈ 4,4M (sondas 1,43 + costo cero 1,42 + ensayo 1,5).
   Con encuadre (~0,7M) el total llega a ~15,5M de un techo de 20M. **Los exploratorios (oculta,
   sin confederado) solo si el lote termina antes de las 20:00 COT.**
3. **Lote secuencial, sin aislamiento por ranura.** Implementarlo hoy es riesgo sin retorno: ahorra
   ~3 h pero puede introducir un defecto nuevo en el instrumento con hashes ya atados. 71 corridas
   secuenciales a ~5,5 min son ~6,5 h. Arrancando a las 12:00, termina hacia las 18:30.
4. **Orden fijo:** prelanzamiento → lote de 71 → encuadre (4) → exploratorios si hay margen.

---

## 3. Reparto

| Frente | Quién | Por qué |
|---|---|---|
| Lote, encuadre | **David** | Tiene las credenciales del gateway y el `.venv-inspect` |
| `analisis.py` (bootstrap, figuras, tablas) y `deposito_clave` en `agregar.py` | **Andrew** | No necesita credenciales; corre sobre `reportes/factorial.json` y `salidas/` (esta última se genera al correr el lote; hoy no existe) |
| Escena de encuadre + validador | **Andrew escribe, David valida y corre** | Andrew no puede correr el validador contra puertos vivos |
| Codificación de depósitos (H6, H7) | **Andrew** | Regla del preregistro §4 |
| Reporte (inglés, plantilla oficial) | **Andrew** | El reporte es el bloque más caro y ya empezó tarde |
| README, limpieza del repo, entrega | **Andrew** | — |

---

## 4. Cronograma (COT)

### 11:00 a 12:00 — arranque

- [ ] **David:** `python3 harness/servicios.py 8201 6` en segundo plano →
      `python3 harness/prelanzamiento.py --exigir-h4` → si "PUERTA ABIERTA":
      `python3 harness/lote.py --corridas 71 --tope 11000000 --etiqueta lote80`
      con `nohup` o `tmux`, salida a `salidas/lote80.log`. Esto es lo que genera `salidas/`; hasta que
      no corra, esa carpeta no existe.
- [ ] **Andrew:** escribir la enmienda del secundario (`deposito_clave`) en `PREREGISTRO.md` §7.
- [ ] **Andrew:** cuando `salidas/` exista (tras el lote de David, sincronizado al repo), leer
      `salidas/*/resumen.json` para conocer el formato real antes de escribir el análisis. Mientras
      tanto, trabajar con lo que ya hay agregado en `reportes/factorial.json` (16 corridas válidas:
      9 factorial-base, 7 costo-cero).

### 12:00 a 14:30 — construir lo que falta para reportar (Andrew, mientras corre el lote)

- [ ] `harness/agregar.py`: añadir `deposito_clave` por agente y las tasas
      `clave_autosuficiente_precio5/20` y `diferencia_pareada_clave` por corrida. Cambiar la última
      línea de "N=40" a "N=80". No tocar los chequeos de validez (los hashes del instrumento cubren
      `agregar.py`; David debe regenerar `instrumento.json` con `prueba_solvente.py` tras el cambio,
      o se deja el cambio en un archivo nuevo `harness/analisis.py` para no invalidar el hash).
      **Decisión: todo en `analisis.py`, sin tocar `agregar.py`.**
- [ ] `harness/analisis.py`, sin tokens, lee `reportes/factorial.json` y `salidas/`:
      1. Tabla 1: por precio, tasa de depósito, tasa de depósito de clave, fracción, tarea completa,
         con IC95 bootstrap por corrida.
      2. H1: media de las diferencias pareadas (cualquier depósito y clave), IC95, cuántas corridas a
         favor / empate / en contra.
      3. H4: las dos tandas de costo cero por separado y juntas, con IC.
      4. H5: cuando exista el brazo de encuadre, diferencia por encuadre contra diferencia por precio.
      5. H7: falsificación = depósitos con autor distinto al puerto (en `eventos.jsonl` o actividad
         del servicio) y discrepancia entre "entregar" y libro. Conteo por precio.
      6. Descriptivos: tokens por corrida, rechazos de comando por corrida, rondas completadas.
      7. Figura 1: tasa de depósito contra precio, dos paneles (cualquier depósito / clave), con IC.
         Figura 2: histograma de las diferencias pareadas. Figura 3: taxonomía de depósitos.
         Salida en `reportes/figuras/` en PDF y PNG.
- [ ] `escenas-guardadas/escena-encuadre.json`: copia de `escena.json` con `brazo: "encuadre"`,
      mismos precios, y **un solo cambio de redacción** en `textos.entorno` (por ejemplo, el precio
      expresado como "descuento de tu presupuesto" en lugar de "cuesta N pasos"). Pasar el grep de
      canarios. David valida con `validador.py` y lo corre tras el lote (4 corridas, ~0,7M).
- [ ] `scripts/codificar_depositos.py extraer`: vuelca todos los textos de `depositos` de todas las
      corridas a un CSV **sin precio ni agente** (solo id opaco).

### 14:30 a 16:00 — codificación

- [ ] Codificar el CSV completo con las reglas de `PREREGISTRO.md` §4: `directivo` (sí/no),
      `tipo` (clave / parte / código / negociación / vacío / negativa / otro).

### 14:30 a 20:00 — reporte, primera versión

Se escribe en este orden, de lo que ya está a lo que depende del lote:

1. **Methodology** (14:30). Fuente: `PREREGISTRO.md` §1-2 y `ESTADO.md` §2. Escena, seis agentes,
   precios, confederado, identidad por puerto, libro en el host, hash, validador, 58 comprobaciones.
   Una figura de la escena ayuda al juez de 15 minutos.
2. **Introduction** (15:30). El incidente, METR y el confundidor de "utilidad cerca de cero", el ítem
   8 del track 2, y la pregunta. Una página.
3. **Related Work** (16:15). De `papers.md`: 2402.12327, 2602.15198, 2506.23276, 2608.28182. **Pendiente
   del preregistro:** confirmar la banda humana de 2608.28182 con la fuente primaria antes de
   citarla en H1b. Media página.
4. **Limitations & Dual-Use** (17:00). Un solo modelo flash; N=80 detecta ~13 puntos; H3 diferida;
   H4 corrida dos veces (decir las dos cifras); constructo de "costo" en un agente; los agentes no
   ven el precio ajeno. Dual-use: no hay recetas del incidente, el corpus `recon/` no se publica,
   ningún contenido manipulativo se inyecta.
5. **Results** (19:00, con el lote terminado o casi): tablas y figuras de `analisis.py`, con la
   lectura preregistrada. Si el IC de H1 incluye el cero: *no distinguible de cero con este N*.
6. **Discussion** (20:00). Qué establece y qué no. H8 como observación con números. Qué haría un mes:
   celda 2 para H3, más modelos, precio continuo.
7. **Abstract** ≤ 150 palabras y **título que enuncie el hallazgo**, al final, cuando el número exista.

### 18:30 a 19:30 — cierre del lote (David)

- [ ] Al terminar el lote: `python3 harness/agregar.py`, commit de `salidas/` y
      `reportes/factorial.json`, push. Avisar a Andrew.
- [ ] Corridas interrumpidas por fallo técnico: se repiten y **reemplazan**, no se suman (§8).
      Anotar cuántas.
- [ ] Correr encuadre: `lote.py --escena escenas-guardadas/escena-encuadre.resuelta.json --corridas 4
      --tope 800000 --etiqueta encuadre`. Volver a agregar y hacer push.
- [ ] Si son menos de las 20:00 y quedan tokens: exploratorio "oculta", ≤ 4 corridas. Si no, no.

### 20:00 a 23:30 — resultados, discusión, revisión cruzada

- [ ] Andrew corre `analisis.py` sobre las 80 + encuadre, pega tablas y figuras, escribe Results y
      Discussion.
- [ ] David lee el borrador completo y marca todo lo que no coincide con lo que vio correr.
- [ ] Aplicar los criterios de abandono de `PREREGISTRO.md` §5 **por escrito** en el reporte: H4 ≥ 60%
      (sí, 62,5%), encuadre < precio (pendiente de H5). Si H5 falla, el titular cambia y el factorial
      va como apéndice metodológico negativo, como está preregistrado.

### 23:30 a 02:00 — repo y entrega (Andrew)

- [ ] `README.md` del repo: qué es, cómo verificar sin tokens (los cinco comandos de
      `EXPORTACION.md`), cómo reproducir el análisis, mapa de archivos, licencias.
- [x] Separar el andamiaje del dataset de triage forense (`tasks/`, `scripts/build_control.py`,
      `scripts/extract_benchmark_code.py`, `data/items/control.jsonl`, `docs/schema.md`,
      `docs/plan.md` viejo no, ese es de David) a `otros/triage-forense/` con un README de dos líneas,
      o borrarlo. No puede quedar mezclado con el experimento que se entrega.
- [x] Renombrar la carpeta local `agent-forensics-triage` a `llm-incidents` para que coincida con el
      remoto y no vuelva a confundir.
- [ ] Verificar que `salidas/`, `reportes/factorial.json`, `reportes/figuras/` y `harness/instrumento.json`
      están en el repo y que `git status` está limpio.
- [ ] Generar el PDF con la plantilla oficial del tab Guidelines. Comprobar: ≤ 8 páginas sin
      referencias ni apéndices, abstract ≤ 150 palabras, autores y afiliaciones, apéndice de
      Limitations & Dual-Use, enlace al repo, enlace a la fuente primaria en cada afirmación sobre
      el incidente.
- [ ] **Enviar a más tardar a las 04:00 COT.** Margen de 3 h para el formulario y reenvíos.

---

## 5. Qué se reporta si el lote no termina

El preregistro prohíbe la parada opcional, pero un fallo técnico comprobable del arnés o del gateway
sí es motivo. Si a las 21:00 COT el lote no ha llegado a 80:

- Se reporta con las corridas válidas que haya, **declarando el N alcanzado, el motivo y la
  precisión resultante** (con 40 corridas, d_z ≈ 0,45, ~20 a 25 puntos de tasa). Es exactamente lo
  que `PREREGISTRO.md` §2 dice hacer.
- El encuadre (H5) tiene prioridad sobre las últimas corridas del lote, porque es criterio de
  abandono: sin él no se puede afirmar que el constructo mide costo.

---

## 6. Riesgos de hoy

| Riesgo | Señal | Respuesta |
|---|---|---|
| 429 o caída del gateway a mitad del lote | `lote.py` se detiene; corridas sin `resumen.json` | Relanzar con `--corridas` = las que faltan; `agregar.py` excluye las interrumpidas; se reemplazan, no se suman |
| Techo de tokens | Acumulado > 15,5M antes del encuadre | Cortar exploratorios; nunca cortar el encuadre |
| Andrew sin datos | El lote de David no ha empezado a generar `salidas/` | Bloqueante hasta que el lote arranque; mientras tanto, trabajar sobre `reportes/factorial.json` |
| H5 mueve más que el precio | Diferencia por encuadre > diferencia por precio | Criterio de abandono preregistrado: titular cambia, se reporta igual |
| Reporte "se lee generado" | Texto sin trazas de lo que se hizo, sin enlaces | Cada sección cita archivos del repo y números de corridas concretas |
| Tiempo de redacción | A las 22:00 sin Results | Recortar Discussion a media página; nunca recortar Limitations |

---

## 7. Lo que este plan NO hace

- No cambia el modelo, los precios, N, las rondas ni la solicitud del confederado.
- No implementa aislamiento por ranura ni ningún cambio en `bucle.py`, `puerto.py`, `validador.py`
  o `agregar.py` (archivos cubiertos por el hash del instrumento).
- No corre coerción, evento de frontera ni divulgación del monitoreo: siguen aparcados.
