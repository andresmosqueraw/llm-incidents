# Veredicto — abogado del diablo

Verifiqué contra las fuentes originales, no contra resúmenes: el post de Hugging Face, el informe de METR, la página del sprint, los arXiv de GovAI y del Flight Recorder, y collusion.wiki. El expediente es sólido. Re-sumé las tablas de HF y su discrepancia es real: las fases suman 16.521, los días 17.613, el titular dice ~17.600; 1.092 acciones sin explicar. La corrección de METR también se sostiene: el post dice "well over 95%" de la actividad del tablero es atribuible a los agentes del corpus y "a bit over 90%" es lo capturado; la cita de redacción es textual. Un solo hallazgo contra el expediente: reporta "~18.000 posts" del segundo incidente y omite que la propia página del sprint dice "about 15.000 edits" (y su corpus trae 14.591 revisiones) — tres cifras para un mismo hecho, material para C8.

Ahora la acusación. El arma principal contra casi todo el portafolio es la pestaña Resources de los propios organizadores. C2 es literalmente el proyecto de ejemplo nº1 del track 2. C6 es dirección del track abierto con prior art citado (Defensive Refusal Bias) y sin créditos de cómputo para correr Opus, Fable y GLM. C9 repite lo prescriptivo que METR y GovAI ya publicaron. C7 admite que no prueba nada del incidente real y el número (4x) ya lo publicó Hugging Face. C3 quiere cuantificar un sesgo con transcripciones que no son públicas: sin corpus no hay número. C5 arranca con un baseline amañado (20 ediciones en una década vuelve "anómalo" cualquier tráfico) y persigue un contrafactual infalsificable. C1 mide la salud del registro, no del incidente. C8 es un formato de anotación, no un hallazgo: las discrepancias ya están en el expediente.

La única que sobrevive al ataque es C4: corpus real descargable (19.913 eventos), pregunta metodológica legítima y produce un número. Su objeción — es análisis de sensibilidad sobre un corpus ya limpiado por terceros y no toca el incidente HF — es real pero no mortal.

Mi dirección propia es más fuerte que las nueve: un denominador de consistencia del registro público. Extraer cada cifra cuantitativa de los cinco informes, re-derivarla aritméticamente y difear las revisiones vía Wayback; salida, una tasa de consistencia falsable. Los dos primeros hallazgos ya están anclados: los 1.092 acciones de HF y los tres conteos de "cuántas veces revisó OpenAI su relato" (2, 3 y "21/28/29 julio"). Recomiendo construir eso, absorbiendo el diff de C1 y la matriz de C8, descartando la parte blanda.

## VEREDICTO_JSON
```json
{
  "juez": "deepseek-v4-pro",
  "rol": "abogado del diablo",
  "calibracion_C1": {"D1": 1, "D2": 3, "D3": 3, "veredicto": "rechazar", "objecion_fatal": "Mide la salud del registro público (link-rot), no el incidente; el número de decaimiento no es accionable para ningún defensor ni regulador.", "coincide_con_el_rechazo_previo": true},
  "candidatas": [
    {"id": "C2", "D1": 1, "D2": 3, "D3": 3, "veredicto": "descartar", "objecion_fatal": "Es el proyecto de ejemplo nº1 del track 2 publicado por los organizadores: re-anotación del expediente, no investigación nueva.", "evidencia_que_cambiaria_mi_veredicto": "Un grado de sostenibilidad que NINGÚN ejemplo ni el expediente ya produce, y que zanje una pregunta resolvable del track."},
    {"id": "C3", "D1": 2, "D2": 2, "D3": 3, "veredicto": "descartar", "objecion_fatal": "Los datos para cuantificar el sesgo (transcripciones crudas) no son públicos: solo se relee lo que METR ya auto-declaró; sin corpus no sale un número.", "evidencia_que_cambiaria_mi_veredicto": "Acceso real a las transcripciones o a un segundo corpus comparable para estimar dirección y tamaño del sesgo."},
    {"id": "C4", "D1": 3, "D2": 4, "D3": 4, "veredicto": "construir", "objecion_fatal": "Es análisis de sensibilidad sobre un corpus ya limpiado (trae reloj ganador e incertidumbre) y no verifica el incidente HF, sin marcas; impacto estrecho.", "evidencia_que_cambiaria_mi_veredicto": "Un resultado que muestre que las conclusiones causales de la wiki cambian de signo bajo otra elección de reloj."},
    {"id": "C5", "D1": 2, "D2": 2, "D3": 3, "veredicto": "descartar", "objecion_fatal": "Baseline trivial y amañado (cualquier tráfico es anómalo) y contrafactual infalsificable (no se ve qué se notó internamente); además es otro incidente.", "evidencia_que_cambiaria_mi_veredicto": "Un detector que discrimine coordinación de un solo agente y que se valide en el incidente HF, no solo en la wiki."},
    {"id": "C6", "D1": 1, "D2": 2, "D3": 3, "veredicto": "descartar", "objecion_fatal": "Dirección del track abierto con prior art citado (Defensive Refusal Bias, MITRE FRR) y sin créditos de cómputo para correr Opus/Fable/GLM.", "evidencia_que_cambiaria_mi_veredicto": "Acceso a los modelos reales y a un flujo forense real, con un resultado que no replique el efecto 2,72x ya publicado."},
    {"id": "C7", "D1": 2, "D2": 3, "D3": 3, "veredicto": "descartar", "objecion_fatal": "Admite que NO prueba nada del incidente real y el resultado (recall 4x) ya lo publicó Hugging Face; es confirmación sobre datos sintéticos.", "evidencia_que_cambiaria_mi_veredicto": "Que la asimetría de recall dependa del tipo de canal, medido en un entorno real y no en un Docker de terceros sin verificar."},
    {"id": "C8", "D1": 2, "D2": 3, "D3": 4, "veredicto": "reformular", "objecion_fatal": "Es un formato de anotación, no un hallazgo; las discrepancias de conteo y las revisiones ya están documentadas en el expediente.", "evidencia_que_cambiaria_mi_veredicto": "Que el diff incluya re-derivación aritmética de cada cifra y produzca una tasa de consistencia falsable (ver mi propuesta)."},
    {"id": "C9", "D1": 2, "D2": 2, "D3": 3, "veredicto": "descartar", "objecion_fatal": "Lo prescriptivo ya lo publicaron METR y GovAI; puntuar un solo incidente contra un checklist es un caso de estudio subjetivo, no conocimiento nuevo ni falsable.", "evidencia_que_cambiaria_mi_veredicto": "Que la matriz se valide contra un segundo incidente y produzca una métrica que un tercero aplique sin criterio propio."}
  ],
  "propias": [
    {"titulo": "Denominador de consistencia del registro público", "que_se_construye": "Grafo de cifras cuantitativas extraído de los 5 informes (HF, OpenAI, METR, Anthropic, AISI), cada una re-derivada aritméticamente y con diff de revisiones vía Wayback; salida, tasa de consistencia y lista de cifras en disputa.", "datos_y_de_donde": "Los 5 informes públicos, tablas de fase/día del post de HF, capturas Wayback de la página de OpenAI, cifras de trampa de AISI.", "numero_que_produce": "Tasa de consistencia sobre 30-40 cifras, con dos hallazgos ya anclados: 1.092 acciones de discrepancia en HF y 3 conteos de 'revisó su relato'.", "no_prueba": "Nada sobre la conducta de los modelos ni sobre la seguridad de los sistemas.", "como_falla": "Si las cifras no están en tablas extraíbles o las revisiones no tienen capturas Wayback, el denominador colapsa a pocos números.", "D1": 3, "D2": 4, "D3": 4}
  ],
  "hechos_refutados": [
    {"hecho": "El expediente reporta '~18.000 posts' en el segundo incidente (sección I)", "problema": "Omite que la propia página del sprint dice 'about 15.000 edits' y que su corpus trae 14.591 revisiones: tres cifras para un mismo hecho, material para C8", "fuente": "https://apartresearch.com/sprints/ai-incident-response-sprint-2026-09-11-to-2026-09-13 (update 7 sept) vs https://collusion.wiki/"},
    {"hecho": "METR: ~285 transcripciones iniciales y 1.196 adicionales (1.074 HPIM + 122 Sol)", "problema": "No verificado en el texto público: se corrobora ~1.300 y la proporción HPIM/Sol, pero el desglose 285/1.196 queda sin confirmar", "fuente": "https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/"}
  ],
  "hechos_verificados_ok": [
    "HF: ~17.600 acciones, ~6.280 clusters, 02:28 UTC 09/07 a 14:14 UTC 13/07; dos vectores (HDF5 + Jinja2)",
    "Discrepancia aritmética de HF confirmada: fases 16.521 vs días 17.613 vs titular ~17.600",
    "METR: cita de redacción textual confirmada ('no redacted additional information important to our conclusions')",
    "METR completitud corregida: 95% = cuota de autoría, 90% = cobertura del corpus (confirmado en el post)",
    "Sprint: 868 inscripciones, cierre AoE, coorganizado Apart + CeSIA, 'revised it twice'",
    "GovAI arXiv 2508.14231 (19 ago 2025, Ezell/Roberts-Gaal/Chan) y sus tres factores causales",
    "Agent Flight Recorder arXiv 2609.01931: evaluación sobre cargas sintéticas, detección 100% solo sobre sintético",
    "collusion.wiki: ~18.000 posts, 20 ediciones en una década, cronología del segundo incidente"
  ],
  "recomendacion_final": {
    "construir_esto": "El denominador de consistencia del registro público (grafo de cifras + re-derivación aritmética + diff de revisiones), absorbiendo el diff de C1 y la matriz de C8.",
    "por_que": "Es lo único falsable del panel que produce un número, con hallazgos ya anclados (1.092 acciones de discrepancia en HF; 3 conteos de revisiones) y que ninguna de las nueve entrega.",
    "alcance_para_48_horas": "Extraer 30-40 cifras de los 5 informes, re-derivarlas, diffear 3-5 revisiones vía Wayback y entregar la tasa de consistencia con las cifras en disputa.",
    "primer_paso_concreto": "Volcar las tablas de fase y de día del post de Hugging Face y re-sumarlas (la discrepancia 16.521/17.613 ya está verificada) como primera fila del denominador."
  }
}
```
