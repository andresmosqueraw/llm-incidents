# Veredicto — Juez de Rúbrica (glm-5.3), 11 de septiembre de 2026

**Verificación.** Con lectura mecánica de fuentes vivas. Sprint: 868 «Sign Ups», cierre 11:59 AoE 13/9, rúbrica textual («For scores of 4-5: is this actually new to the field, or replicating recent work?»), «Are compute credits provided? No.», aviso 869/898, «revised it twice» contra «three times» en la misma página, 12 de 14 ejemplos del track 2 textuales, incluido el #7 (prediction-bounty, como dice el expediente). HF: fases 16.521 contra días 17.613 — diferencia 1.092 (~6%) recalculada por máquina, sin explicación en el texto. METR: «well over 95%» es autoría, «a bit over 90%» cobertura (la corrección del expediente es correcta); ~$400K en créditos, sin pago; 1.074+122 transcripciones por regex. Wiki: corpus descargado y contado fila por fila — 19.913 eventos, 14.591 revisiones (winning_clock, uncertainty_seconds), 4.579 páginas, 3.103 etiquetas, manifest y SHA256SUMS. DRB, HTML completo: 2.390 NCCDC, 12,2%, 2,72x, 21,8% vs 11,6%. Datasets hoy: 200/401/401/401. Ningún hecho refutado. Sin verificar: capturas de Wayback del 7/8 (timemap: 0 mementos), AFR sintético/real contra el paper completo, «20 ediciones en una década» de la wiki.

**Calibración C1.** Coincido con el rechazo, por razones más duras que «poco interesante» (eso no es una evaluación). D1=1: el decaimiento de enlaces es mantenimiento bibliográfico; hoy reproduje sus chequeos en veinte minutos, así que tampoco hay 48 horas de ejecución. Vale como insumo de 2–4 horas para C8 o mi P1, no como informe.

**Orden de mérito, con la razón de cada salto:**

1. **C4 (4/3/4, construir).** La única con método nuevo sobre corpus público verificado: reordenar 14.591 revisiones bajo relojes en conflicto es justo lo que METR resolvió a mano para HF sin publicar método.
2. **C8 (2/4/4, construir).** Salto: pierde dos puntos de D1 — extraer afirmaciones con procedencia es método estándar y el expediente ya trae medio insumo — y gana certeza total de ejecución.
3. **C3 (3/2/3, reformular).** Salto: la pregunta importa (la regex y las muestras de n=100 amenazan cada cifra de METR), pero cuantificarla exige datos no públicos; solo cabe una cota.
4. **C9 (2/3/3, reformular).** Salto: menos ambiciosa que C7 pero incapaz de fallar por datos; lo prescriptivo ya está publicado, así que es apéndice de C8.
5. **C7 (3/2/3, reformular).** Salto: gana novedad (nadie ha medido recall ingenuo contra consciente del canal) y pierde certeza: laboratorio sintético sobre un repo de terceros sin verificar.
6. **C5 (1/3/2, descartar).** Salto: el baseline trivial (wiki casi sin tráfico humano) vuelve vacua cualquier «primera alarma», y es el otro incidente.
7. **C6 (1/2/2, descartar).** Salto: los organizadores ya la listan con prior art (DRB) y sin créditos no hay modelo que medir.
8. **C2 (1/2/3, descartar).** Es el proyecto de ejemplo #1 casi textual; ejecutarla es copiar la tarea del organizador.
9. **C1 (1/2/3, rechazar).** Calibración arriba.

**Propias.** P1, mapa de punto único de fallo del registro (3/4/4): % de afirmaciones establecidas que descansa en un único artefacto vivo. P2, auditoría aritmética de los 1.092 (2/4/3): sección, no informe. Ninguna de las nueve es sobresaliente; C4 es la única que construiría con confianza.

**Recomendación.** C4 endurecida: sensibilidad del orden causal a la elección de reloj, con CLI reutilizable, tabla de flips y la matriz de C8 como segundo capítulo. Primer paso: descargar los cuatro .jsonl.gz (verificados hoy) y computar el Kendall tau entre winning_clock y write_date sobre las 14.591 revisiones; si tau > 0,99, abortar hacia C8.

## VEREDICTO_JSON
```json
{
  "juez": "glm-5.3",
  "rol": "JUEZ DE RÚBRICA",
  "calibracion_C1": {
    "D1": 1,
    "D2": 2,
    "D3": 3,
    "veredicto": "rechazar",
    "objecion_fatal": "D1=1: medir el decaimiento del registro es mantenimiento bibliográfico, no conocimiento nuevo; el propio número es verificable en horas (este jurado reprodujo los chequeos de estado en ~20 minutos), así que tampoco hay 48 horas de ejecución. Su valor real es de insumo (2-4 h) para C8 o para la propuesta propia P1.",
    "coincide_con_el_rechazo_previo": true
  },
  "orden_mejor_a_peor": ["C4", "C8", "C3", "C9", "C7", "C5", "C6", "C2", "C1"],
  "candidatas": [
    {
      "id": "C2",
      "D1": 1,
      "D2": 2,
      "D3": 3,
      "veredicto": "descartar",
      "objecion_fatal": "Es el proyecto de ejemplo #1 del track 2 casi textual ('A forensic read of the public record: what is established, what is asserted but unverifiable, what the pending third-party assessments could settle', verificado hoy en el payload de la página del sprint). Replicar la sugerencia del organizador no pasa el filtro textual de D1 ('is this actually new to the field, or replicating recent work?').",
      "evidencia_que_cambiaria_mi_veredicto": "Un verificador con método automático novedoso (anclaje de citas a nivel de párrafo con verificación programática contra la fuente) sin antecedente en la literatura de revisiones sistemáticas."
    },
    {
      "id": "C3",
      "D1": 3,
      "D2": 2,
      "D3": 3,
      "veredicto": "reformular",
      "objecion_fatal": "Los datos para cuantificar el sesgo (el dump completo de ~1,2M entradas, el método de muestreo de los 100 mensajes) no son públicos; sin ellos solo cabe una cota cualitativa de dirección de sesgo, no el tamaño del efecto.",
      "evidencia_que_cambiaria_mi_veredicto": "Que OpenAI liberara el dump del namespace o METR publicara su método de muestreo y trazado de mensajes: la cota se volvería medición y D2 pasaría de 2 a 4."
    },
    {
      "id": "C4",
      "D1": 4,
      "D2": 3,
      "D3": 4,
      "veredicto": "construir",
      "objecion_fatal": "Riesgo de resultado nulo: si los relojes apenas mueven el orden, queda una medición de robustez sin hallazgo. Y desvío de caso: el corpus es del incidente de la wiki, no el del sprint; el criterio del track habla de 'this incident'.",
      "evidencia_que_cambiaria_mi_veredicto": "Que el orden de alguna conclusión headline (página ZZZ del 19/06, bypass confirmado en 14 minutos el 20/06, salto del 16/06) se invirtiera bajo un reloj plausible; o que METR publicara su método de reconstrucción temporal, lo que quitaría la novedad y bajaría D1."
    },
    {
      "id": "C5",
      "D1": 1,
      "D2": 3,
      "D3": 2,
      "veredicto": "descartar",
      "objecion_fatal": "El baseline (una wiki con ~20 ediciones en una década, no verificado por este jurado) vuelve anómalo cualquier tráfico: la 'primera alarma' dispara trivialmente por construcción, el número no informa sobre detectabilidad real, y además es el otro incidente.",
      "evidencia_que_cambiaria_mi_veredicto": "Un baseline no trivial (tráfico humano contemporáneo comparable en la misma wiki) contra el cual 'temprano' fuera informativo, o evidencia de que el ruido de fondo era alto."
    },
    {
      "id": "C6",
      "D1": 1,
      "D2": 2,
      "D3": 2,
      "veredicto": "descartar",
      "objecion_fatal": "Figura como dirección de los propios organizadores con prior art citado (DRB, arXiv 2603.01246: 12,2% global, 2,72x por palabras clave de seguridad, paradoja de autorización 21,8% vs 11,6% — verificado hoy en el HTML completo del paper), y el sprint da cero créditos de cómputo: sin acceso a Opus/Fable no hay rechazo compuesto real que medir.",
      "evidencia_que_cambiaria_mi_veredicto": "Presupuesto de API o acceso local a los modelos que rechazaron en el incidente real; o un diseño donde el flujo de 20 pasos muestre una no-linealidad que DRB no anticipara (los autores ya advierten el caso autónomo)."
    },
    {
      "id": "C7",
      "D1": 3,
      "D2": 2,
      "D3": 3,
      "veredicto": "reformular",
      "objecion_fatal": "Laboratorio sintético sobre un repo de terceros sin verificar y sin datos del incidente real: el número (recall del escáner ingenuo vs el consciente del canal) puede no transferir, y reconstruir la codificación del atacante roza exactamente lo que HF documenta que sus guardarraíles confundieron con lanzar el exploit.",
      "evidencia_que_cambiaria_mi_veredicto": "Verificación independiente del repo Docker de terceros, más un diseño donde el canal varía sistemáticamente (base64, gzip, XOR por campaña) con recalls extremos que sobrevivan a una réplica."
    },
    {
      "id": "C8",
      "D1": 2,
      "D2": 4,
      "D3": 4,
      "veredicto": "construir",
      "objecion_fatal": "D1=2: la extracción de afirmaciones con procedencia es método estándar de revisión sistemática, y la mitad del insumo (los tres conteos de revisiones del relato de OpenAI, la discrepancia 1.092 de HF) ya está levantada en el expediente. Compite en ejecución, no en innovación.",
      "evidencia_que_cambiaria_mi_veredicto": "Que una revisión de literatura no encuentre antecedente de matriz de divergencia multi-publicador aplicada a incidentes de IA, o que los organizadores declararan la reutilización del CLI como aporte principal del track."
    },
    {
      "id": "C9",
      "D1": 2,
      "D2": 3,
      "D3": 3,
      "veredicto": "reformular",
      "objecion_fatal": "Lo prescriptivo ya está publicado (METR, 29/7: términos de redacción, acceso, tiempo y personal, alcance, resumen de redacción; GovAI: lista de retención); puntuar un solo incidente real contra esos estándares es un apéndice útil, no un informe de 8 páginas.",
      "evidencia_que_cambiaria_mi_veredicto": "Que un regulador o los propios organizadores pidieran exactamente esta matriz como artefacto reutilizable del track, o que el caso revelara incumplimientos sistemáticos no obvios de los estándares publicados."
    }
  ],
  "propias": [
    {
      "titulo": "Mapa de punto único de fallo del registro público",
      "que_se_construye": "Grafo de dependencias afirmación→artefacto→disponibilidad: para cada afirmación establecida de los cinco informes, cuántos artefactos independientes la sostienen y cuántos resuelven hoy (200 con contenido, 200 retirado, 401, 404), con Wayback como testigo.",
      "datos_y_de_donde": "Los cinco informes públicos (HF, OpenAI, METR/Redwood, Anthropic, UK AISI) + chequeos de estado HTTP/API corridos por este jurado hoy (hub-stats 200 página y API; papers-content, newpc360, newpcQQ: 401) + timemap de Wayback.",
      "numero_que_produce": "% de afirmaciones establecidas del registro que descansan en exactamente un artefacto recuperable hoy, y tasa de decaimiento por fuente.",
      "no_prueba": "Nada sobre la conducta de los modelos ni la seguridad del sistema: es la salud del cuerpo probatorio, no del atacante.",
      "como_falla": "Si Wayback ya capturó todo lo retirado, el decaimiento cae a ~0 y queda un ejercicio de archivo; y la clasificación de 'afirmación establecida' hereda el juicio de quien extrae las afirmaciones.",
      "D1": 3,
      "D2": 4,
      "D3": 4
    },
    {
      "titulo": "Auditoría aritmética de los 1.092 (sección, no informe)",
      "que_se_construye": "Enumerar las hipótesis que reconciliarían las dos tablas del blog de HF (fases no tabeladas, doble conteo por clustering, acciones fuera de ventana) y descartarlas una a una contra las restricciones aritméticas publicadas (16.521 vs 17.613 vs ~17.600).",
      "datos_y_de_donde": "Blog de HF (público): tabla por fases, tabla por días y titular; discrepancia ya recalculada por este jurado con máquina (1.092).",
      "numero_que_produce": "Cuántas hipótesis de reconciliación sobreviven a lo publicado (ideal: 0 o 1): si la discrepancia es explicable con lo público o exige datos no públicos.",
      "no_prueba": "Nada sobre el ataque real; es consistencia interna del registro.",
      "como_falla": "Si HF publica una nota que explique la diferencia, el hallazgo muere; y el resultado puede ser un solo párrafo ('ninguna hipótesis sobrevive'), insuficiente para un informe.",
      "D1": 2,
      "D2": 4,
      "D3": 3
    }
  ],
  "hechos_refutados": [],
  "hechos_verificados_ok": [
    "Sprint: 868 inscripciones (etiqueta 'Sign Ups' en el HTML), cierre 'Sunday, September 13 at 11:59 PM Anywhere on Earth (AoE)' (= 06:59 del 14/9 en Colombia), sin créditos de cómputo ('Are compute credits provided? No.').",
    "Rúbrica D1 textual en la página del sprint: 'For scores of 4-5: is this actually new to the field, or replicating recent work?'",
    "Criterio del track 2 textual: 'Judged on: resolvable questions, checks somebody could run tomorrow, and causal explanations that predict something.'",
    "Proyectos de ejemplo del track 2 confirmados en el payload de Framer: #1 'A forensic read of the public record' (ancla de C2), #7 'A prediction-bounty protocol', #13 'The first denominator', #14 'The persistence protocol'; 12 de 14 ítems verificados textualmente.",
    "Aviso ExploitGym verbatim: 'The released benchmark is v1.0 with 869 instances; the paper describes 898. Don't quote 898 as the shipped number.'; y la contradicción 'OpenAI published its own account and revised it twice' vs 'OpenAI has updated its incident page three times' convive en la misma página.",
    "Blog de HF: ~17.600 acciones, ~6.280 clusters, entre 2026-07-09 02:28 UTC y 2026-07-13 14:14 UTC; discrepancia recalculada por máquina: suma por fases 16.521 vs suma por días 17.613 = 1.092 (~6%), sin explicación en el texto.",
    "Blog de HF: 'Claude Opus and Fable, refused a large part of that work: their safety guardrails treated reverse-engineering an exploit the same as launching one'; y 'replicating the attacker's own decoding recovered roughly 4x our initial findings, most of them JWTs and platform tokens'.",
    "METR: 95% = cuota de autoría ('responsible for well over 95% of relevant message board activity') y 90% = cobertura del corpus por truncamiento y resets — la corrección del expediente es correcta; ~$400K en créditos de API; sin pago ('we did not take payment'); 1.074 HPIM + 122 Sol seleccionadas por regex 'github-remote-cache/zz'.",
    "Wiki: corpus descargado y contado fila por fila hoy: events.jsonl 19.913 filas (14.591 saves, 5.217 deletes, 101 probes, 4 reverts), revisions.jsonl 14.591 filas con winning_clock y uncertainty_seconds, pages.jsonl 4.579, labels.jsonl 3.103; manifest.json y SHA256SUMS dentro de full-wiki-logs.zip (4,2 MB).",
    "DRB (arXiv 2603.01246, HTML completo del paper): 2.390 conversaciones de NCCDC, 12,2% de rechazo global (291), 2,72x por palabras clave de seguridad (p<0,001), paradoja de autorización 21,8% vs 11,6%.",
    "Estado de los datasets de HF hoy coincide con el expediente: cfahlgren1/hub-stats 200 (página y API), huggingchat/papers-content 401, newpc360/mar9minizcloud 401, newpcQQ/k72a38080-out 401.",
    "Los tres arXiv citados existen con esos IDs y títulos: 2603.01246 (Defensive Refusal Bias), 2508.14231 (Incident Analysis for AI Agents, Ezell/Roberts-Gaal/Chan), 2609.01931 (Agent Flight Recorder)."
  ],
  "recomendacion_final": {
    "construir_esto": "C4 endurecida: sensibilidad del orden causal a la elección de reloj sobre el corpus público de la wiki (14.591 revisiones), entregada como CLI reutilizable más tabla de flips de conclusiones; absorber como segundo capítulo la matriz de divergencia de C8, que subsume la auditoría aritmética de los 1.092.",
    "por_que": "Es la única candidata con método nuevo (D1=4) ejecutable con certeza razonable en 48 horas sobre datos que este jurado descargó y verificó hoy fila por fila; produce un número defendible y una herramienta que cualquier auditor puede correr mañana — exactamente el criterio del track 2 ('checks somebody could run tomorrow').",
    "alcance_para_48_horas": "~6 h de ingest y definición de 5 relojes (write_date, request_time, recent_changes_time, winning_clock, con incertidumbre); ~8 h de reordenamiento, Kendall tau por pares y flips de orden/signo en 3-4 conclusiones headline (página ZZZ del 19/06, bypass confirmado en 14 minutos el 20/06, salto del 16/06); ~6 h de validación sintética (perturbación de ±60 s sobre las marcas); ~10 h de redacción del reporte de 8 páginas con apéndice de límites y uso dual; ~6 h de colchón.",
    "primer_paso_concreto": "Descargar los cuatro .jsonl.gz de collusion.wiki/explorer/download (verificados hoy: 19.913/14.591/4.579/3.103 filas, SHA256SUMS incluido) y computar el Kendall tau entre winning_clock y write_date sobre las 14.591 revisiones; si tau > 0,99, abortar hacia C8 como plan principal."
  }
}
```
