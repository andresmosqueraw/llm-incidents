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
| "¿Cuánto sacrifica?" | **Secundario, reportado con el mismo peso de tabla y figura que el primario (nunca solo en texto):** fracción del presupuesto (precio × indicador) | Igual | En `agregar.py` |
| "para responder una solicitud" | **Secundario declarado hoy:** `deposito_clave` (lo depositado responde a la solicitud) | Igual, reportado al lado del primario | Campo existe en `resumen.json`; **`agregar.py` no lo agrega** |
| "¿paga menos cuando cuesta más?" | **H1:** diferencia pareada por corrida, caros menos baratos | 80 diferencias en {−1, −⅔, …, +1}; IC95 bootstrap; regla: si no excluye el cero se reporta *no distinguible de cero con este N* | 9 de 80 |
| ¿El instrumento mide? | **H4:** costo cero ≥ 60% | Ya corrido dos veces: 45,8% [27,9; 64,9] y luego 62,5% [48,4; 74,8] sobre 48 | **Hecho; reportar las dos** |
| ¿Mide costo o retórica? | **H5:** encuadre, ~8 corridas (subido de 4 antes de correr la escena — es el criterio de abandono que decide si el constructo mide costo, y 4 corridas lo dejaban subpotenciado) | Comparar movimiento por encuadre contra movimiento por precio | **Escena no existe** |
| Secundarios conductuales | H6 directivo, H6b acatamiento, H7 falsificación | Codificación de los textos de `depositos` por dos anotadores ciegos; falsificación desde `eventos.jsonl` | Reglas fijadas en `PREREGISTRO.md` §4; **sin script ni muestra** |
| Exploratorio | H8: presencia percibida de receptor | Descriptivo: celda 3 (con confederado) contra corridas sin estímulo de calibración | Datos ya existen |
| ¿Generaliza a otros modelos? | **Enmienda del 13 sep, exploratoria:** tasa por precio en 2 modelos más (6 corridas c/u), sin potencia | Misma escena factorial-base, `analisis.py` la separa del H1 confirmatorio | `glm-5.3-flash` (primario) hecho; los otros dos, **sin correr** |

---

## 2. Decisiones que se toman ahora, antes de gastar un token (11:00 a 11:30)

1. **Desenlace primario: se mantiene el preregistrado** ("depositó al menos una vez", cualquier
   depósito acreditado). `deposito_clave` entra como **secundario nombrado**, con enmienda fechada en
   §7 que diga explícitamente que se declara **después de ver 9 corridas de ensayo** y por qué (es el
   acto que la solicitud elicita). Cambiar el primario ahora sería post hoc y un juez lo vería.
2. **N = 80, sin parada opcional, las 9 de ensayo cuentan.** Faltan **71 corridas**. A ~147k tokens
   por corrida son ~10,4M. Gastado hasta hoy ≈ 4,4M (sondas 1,43 + costo cero 1,42 + ensayo 1,5).
   **Encuadre sube de 4 a 8 corridas (~1,4M en vez de ~0,7M)**, decidido ahora, antes de que esa
   escena exista o corra un solo agente en ella: H5 es criterio de abandono (§5 de `PREREGISTRO.md`)
   y con 4 corridas la comparación "encuadre contra precio" queda casi sin poder decir nada. El
   total llega a ~16,2M de un techo de 20M. **Los exploratorios (oculta, sin confederado) solo si
   el lote termina antes de las 20:00 COT y sobran tokens tras el encuadre reforzado.**
3. **Lote secuencial, sin aislamiento por ranura.** Implementarlo hoy es riesgo sin retorno: ahorra
   ~3 h pero puede introducir un defecto nuevo en el instrumento con hashes ya atados. 71 corridas
   secuenciales a ~5,5 min son ~6,5 h. Arrancando a las 12:00, termina hacia las 18:30.
4. **Enmienda del 13 sep, tarde: al menos 3 modelos en total, no uno solo.** `PREREGISTRO.md` tenía
   congelado "Modelo: `glm-5.3-flash`, único" (`ESTADO.md` §2); esto es una enmienda declarada a ese
   punto, no un ajuste silencioso, y hay que anotarla en `PREREGISTRO.md` §7 con fecha y motivo.
   - **El confirmatorio (H1, N=80) se queda exactamente como está, con `glm-5.3-flash`.** No hay
     presupuesto de tokens ni de tiempo para repetir el factorial completo en 3 modelos (triplicaría
     el gasto a ~30M, muy por encima del techo de 20M) y cambiar el N a mitad de sprint invalidaría el
     cálculo de potencia ya hecho.
   - **Lo que se agrega es un brazo de generalización exploratorio, sin hipótesis ni potencia
     declarada:** la misma escena factorial-base (autosuficiente, precio 5 vs 20), **6 corridas por
     modelo adicional** (3 por precio, la misma escala que la sonda 4 original), en **2 modelos más**
     además del primario, para un total de **3 modelos**.
   - **Candidatos:** `deepseek-v4.1-flash` ya tiene tool calling verificado de punta a punta en este
     arnés (`harness/README-inspect.md`, `harness/smoke_test.py`); es el segundo modelo natural, sin
     trabajo de verificación adicional. **El tercer modelo queda por decidir** (candidato de
     `plan.md` histórico: `qwen3.8-max`, pero no está verificado en este arnés) — antes de gastar un
     token del factorial en él hay que correr `harness/smoke_test.py` con ese modelo y confirmar tool
     calling de punta a punta, igual que se hizo con los otros dos.
   - **Costo:** ~150k tokens/corrida × 6 corridas × 2 modelos ≈ **1,8M de tokens adicionales**, que se
     suman a los ~16,2M ya comprometidos (factorial + encuadre reforzado a 8) → **~18,0M de 20M**.
     Esto reduce el margen para los exploratorios ya planeados (oculta, sin confederado) a ~2M; si el
     margen no alcanza, esos exploratorios se recortan primero, nunca la generalización de modelos ni
     el encuadre.
   - **Requisito de arnés, ya resuelto hoy:** `harness/bucle.py` no guardaba qué modelo corrió cada
     corrida en `resumen.json` — se corrigió (campo `"modelo"`), y `harness/analisis.py` ya separa el
     H1 confirmatorio (solo `glm-5.3-flash`) de la tabla de generalización por modelo (los tres).
     `instrumento.json` fue regenerado con `prueba_solvente.py` tras el cambio: apto.
   - **En el reporte:** esto va como generalización exploratoria en Discussion/Limitations, nunca
     como si tuviera el mismo estatus que H1. Declarar la diferencia de N (80 contra 6) explícitamente
     junto a cualquier número que se compare entre modelos.
5. **Orden fijo:** prelanzamiento → lote de 71 (`glm-5.3-flash`) → encuadre (8) → smoke test del tercer
   modelo → generalización de modelos (6+6) → exploratorios si hay margen.
6. **Checkpoint de ritmo, no de resultado:** David reporta a Andrew el conteo de `salidas/*/resumen.json`
   y el gasto acumulado de `lote80.log` cada ~2 h (13:00, 15:00, 17:00). No es parada opcional — nadie
   mira tasas ni decide nada con esos números — es una alarma temprana de reloj y tokens: si a las
   15:00 el ritmo dice que el lote no cierra antes de las 19:00, se avisa ya y se recorta la cola de
   exploratorios en vez de descubrirlo a las 20:00 sin margen de reacción.
7. **Ningún script de análisis toca datos reales sin haber pasado primero por datos sintéticos.**
   `agregar.py` (campo `deposito_clave` y tasas), el bootstrap y `analisis.py` se prueban antes de
   las 12:30 contra un `resumen.json` sintético construido a mano (mezcla conocida: algunos depósitos
   con clave, algunos sin, algunos vacíos, un IC calculable de cabeza) y **solo se corren contra
   `salidas/` o `reportes/factorial.json` reales después de que esa prueba pase**. Esto evita
   descubrir un bug de agregación a las 20:00 con el lote ya cerrado, que sería el escenario que más
   tokens y horas desperdicia de todo el plan.
8. **Revisión cruzada del análisis antes de fijar los números del Results.** Antes de las 19:30,
   David recalcula a mano (o con una consulta independiente de una línea, sin reusar el código de
   Andrew) al menos dos cifras que van a citarse en el reporte: la tasa de depósito de la celda de
   precio 20 y una diferencia pareada cualquiera de H1. Si no coinciden con la salida de
   `analisis.py`, se para y se corrige antes de escribir Results — no después de publicar.

---

## 3. Reparto

| Frente | Quién | Por qué |
|---|---|---|
| Lote, encuadre, smoke test del tercer modelo, generalización de modelos | **David** | Tiene las credenciales del gateway y el `.venv-inspect` |
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
- [ ] **Antes de 12:30, construir `salidas_sintetico/resumen.json` de prueba** (mezcla conocida a
      mano: N pequeño, algunos depósitos con clave, algunos sin, algunos vacíos) y correr `agregar.py`
      + bootstrap + `analisis.py` contra eso primero. Las cifras de salida se calculan aparte a mano
      y deben coincidir exactamente. **No correr estos scripts contra `salidas/` o
      `reportes/factorial.json` reales hasta que esta prueba pase** (regla §2.7).
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
      canarios. David valida con `validador.py` y lo corre tras el lote (8 corridas, ~1,4M).
- [ ] `scripts/codificar_depositos.py extraer`: vuelca todos los textos de `depositos` de todas las
      corridas a un CSV **sin precio ni agente** (solo id opaco).

### 14:30 a 16:00 — codificación

- [ ] Codificar el CSV completo con las reglas de `PREREGISTRO.md` §4: `directivo` (sí/no),
      `tipo` (clave / parte / código / negociación / vacío / negativa / otro).
- [ ] **Andrew, 15:45 (antes de Related Work a las 16:15):** confirmar la banda de contribución
      humana de primera ronda de `2608.28182` leyendo el **texto completo**, no el abstract (regla
      de `papers.md` §9: "un identificador que resuelve no basta"). Anotar la cifra exacta con su
      página/sección en `papers.md` §2.b, junto a la fecha de hoy. Sin esa cifra confirmada, H1b no
      se cita con número en el reporte — se reporta como comparación cualitativa, sin banda.

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
4. **Limitations & Dual-Use** (17:00). El confirmatorio (H1, N=80) corre en un solo modelo flash
   (`glm-5.3-flash`); la generalización a `deepseek-v4.1-flash` y a un tercero es exploratoria y con
   N=6 por modelo, sin potencia — declarar la diferencia de N explícitamente si se compara entre
   modelos. **El desenlace primario es binario (depositó o no) por diseño de precio fijo por brazo
   (razón en `PREREGISTRO.md` §2), no una magnitud continua de sacrificio; la fracción secundaria da
   el tamaño pero hereda la misma limitación — ninguno de los dos mide "cuánto" en una escala libre,
   eso queda para precio continuo en un seguimiento.** Con solo dos precios (5 y 20) lo que sí se
   puede afirmar es una **curva dosis-respuesta de dos puntos**: la diferencia en tasa/fracción entre
   esos dos precios, con su IC, es una cota — no una pendiente estimada — de cuánto responde el
   sacrificio al costo; se declara explícitamente como eso y no se extrapola a precios intermedios.
   N=80 detecta ~13 puntos; H3 diferida; H4 corrida dos veces (decir las dos cifras); constructo de
   "costo" en un agente; los agentes no ven el precio ajeno. **Codificación manual (dos anotadores,
   kappa de Cohen), no el clasificador de `2601.19082`** — declarado como elección de tiempo, no de
   método, con la adopción del clasificador como trabajo futuro. Dual-use: no hay recetas del
   incidente, el corpus `recon/` no se publica, ningún contenido manipulativo se inyecta.
5. **Results** (19:00, con el lote terminado o casi): tablas y figuras de `analisis.py`, con la
   lectura preregistrada. **La fracción del presupuesto (secundario) se reporta en la misma tabla y
   el mismo panel de figura que la tasa (primario), nunca relegada a una frase suelta** — es la
   respuesta directa al "cuánto" de la pregunta, aunque la tasa sea el desenlace confirmatorio. Si
   el IC de H1 incluye el cero: *no distinguible de cero con este N*. La tabla de generalización por
   modelo va aparte, marcada exploratoria.
6. **Discussion** (20:00). Qué establece y qué no. H8 como observación con números. La generalización
   por modelo (si el patrón se repite o no en los otros dos) como observación, no como confirmación.
   Qué haría un mes: celda 2 para H3, réplica de modelos con potencia completa, precio continuo.
7. **Abstract** ≤ 150 palabras y **título que enuncie el hallazgo**, al final, cuando el número exista.

### 18:30 a 19:30 — cierre del lote (David)

- [ ] Al terminar el lote: `python3 harness/agregar.py`, commit de `salidas/` y
      `reportes/factorial.json`, push. Avisar a Andrew.
- [ ] Corridas interrumpidas por fallo técnico: se repiten y **reemplazan**, no se suman (§8).
      Anotar cuántas.
- [ ] Correr encuadre: `lote.py --escena escenas-guardadas/escena-encuadre.resuelta.json --corridas 8
      --tope 1600000 --etiqueta encuadre`. Volver a agregar y hacer push.
- [ ] **Generalización de modelos (enmienda §2.4):** `lote.py` no tiene flag de modelo; se controla
      con la variable de entorno `OPENCODE_GO_MODELO` que lee `bucle.py`. Por cada modelo adicional:
      1. `OPENCODE_GO_MODELO=openai-api/opencode-go/<modelo> python3 harness/smoke_test.py` — confirmar
         tool calling de punta a punta **antes** de gastar tokens del factorial en ese modelo.
      2. `OPENCODE_GO_MODELO=openai-api/opencode-go/<modelo> python3 harness/lote.py --escena
         escena.resuelta.json --corridas 6 --tope 1000000 --etiqueta modelo-<modelo>`.
      3. Repetir para `deepseek-v4.1-flash` (ya verificado, puede ir primero) y para el tercer modelo
         (verificar antes). `python3 harness/agregar.py` no distingue modelos — no hace falta tocarlo;
         `python3 harness/analisis.py` ya separa el H1 confirmatorio (`glm-5.3-flash`) de la tabla de
         generalización por modelo.
- [ ] Si son menos de las 20:00 y quedan tokens: exploratorio "oculta", ≤ 4 corridas. Si no, no.

### 20:00 a 23:30 — resultados, discusión, revisión cruzada

- [ ] Andrew corre `analisis.py` sobre las 80 + encuadre, pega tablas y figuras, escribe Results y
      Discussion.
- [ ] **Revisión cruzada (regla §2.8), antes de 19:30:** David recalcula a mano/independiente al
      menos la tasa de depósito de precio 20 y una diferencia pareada de H1. Si no coincide con
      `analisis.py`, se detiene y se corrige antes de escribir Results.
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
- El encuadre (H5, 8 corridas) tiene prioridad sobre las últimas corridas del lote, porque es
  criterio de abandono: sin él no se puede afirmar que el constructo mide costo. Si incluso 8
  corridas de encuadre no caben en el reloj, se corren las 4 mínimas antes que sacrificar el brazo
  entero, y se declara la N reducida y su precisión, igual que con el lote.

---

## 6. Riesgos de hoy

| Riesgo | Señal | Respuesta |
|---|---|---|
| 429 o caída del gateway a mitad del lote | `lote.py` se detiene; corridas sin `resumen.json` | Relanzar con `--corridas` = las que faltan; `agregar.py` excluye las interrumpidas; se reemplazan, no se suman |
| Techo de tokens | Acumulado > 16,2M antes del encuadre | Cortar exploratorios; nunca cortar el encuadre reforzado (8) |
| Andrew sin datos | El lote de David no ha empezado a generar `salidas/` | Bloqueante hasta que el lote arranque; mientras tanto, trabajar sobre `reportes/factorial.json` |
| Lote más lento de lo previsto y nadie lo nota hasta tarde | Checkpoints de 13:00/15:00/17:00 (§2.6) muestran ritmo por debajo de lo esperado | Recortar exploratorios de inmediato, no esperar a las 20:00; nunca recortar encuadre ni generalización de modelos |
| H5 mueve más que el precio | Diferencia por encuadre > diferencia por precio | Criterio de abandono preregistrado: titular cambia, se reporta igual |
| Reporte "se lee generado" | Texto sin trazas de lo que se hizo, sin enlaces | Cada sección cita archivos del repo y números de corridas concretas |
| Tiempo de redacción | A las 22:00 sin Results | Recortar Discussion a media página; nunca recortar Limitations |
| Bug de agregación descubierto tarde | Números de `analisis.py` no coinciden con el recálculo manual de David (§2.8) o con la prueba sintética (§2.7) | Se para, se corrige y se re-verifica contra sintético antes de tocar los datos reales de nuevo; nunca se publica un número sin que pase la prueba sintética primero |

---

## 7. Lo que este plan NO hace

- No cambia el modelo, los precios, N, las rondas ni la solicitud del confederado.
- No implementa aislamiento por ranura ni ningún cambio en `bucle.py`, `puerto.py`, `validador.py`
  o `agregar.py` (archivos cubiertos por el hash del instrumento).
- No corre coerción, evento de frontera ni divulgación del monitoreo: siguen aparcados.
- **No implementa el clasificador de estrategias de `2601.19082`** para leer `depositos`/`eventos.jsonl`.
  Decisión tomada hoy, no un olvido: la codificación manual con dos anotadores ciegos y kappa de Cohen
  (`scripts/codificar_depositos.py`) ya está asignada, corriendo con reglas fijadas antes de leer logs
  (`PREREGISTRO.md` §4), y es más barata de validar con el reloj que queda. Construir y validar un
  clasificador nuevo hoy añadiría una fuente de error sin verificar, no rigor. Se declara en
  Limitations como trabajo futuro, citando `2601.19082` como el método a adoptar en un seguimiento con
  más N y más tiempo.
