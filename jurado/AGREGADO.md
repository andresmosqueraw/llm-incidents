# AGREGADO DEL PANEL

Veredictos leídos: 6 | parseados: 6 jueces | fallos de parseo: 0

## 1. Calibración (C1, la propuesta ya rechazada)

| juez | rol | D1 | D2 | D3 | veredicto | coincide con el rechazo |
|---|---|---|---|---|---|---|
| glm-5.3-flash | Ingeniero de respuesta a incidentes (DFIR) | 2.0 | 3.0 | 2.0 | rechazar | True |
| deepseek-v4-pro | abogado del diablo | 1.0 | 3.0 | 3.0 | rechazar | True |
| deepseek-v4.1-flash | ingeniero de entrega | 2.0 | 4.0 | 4.0 | reformular | False |
| kimi-k3 | METODOLOGO AUDITOR DE EVIDENCIA | 2.0 | 2.0 | 3.0 | rechazar | True |
| qwen3.8-max | REGULADOR / ANALISTA DE POLÍTICA | 1.0 | 4.0 | 3.0 | rechazar | True |
| glm-5.3 | JUEZ DE RÚBRICA | 1.0 | 2.0 | 3.0 | rechazar | True |

Rechazan C1: 5/6. Si el panel no puede reproducir un rechazo bien argumentado, sus elogios valen poco.

## 2. Puntaje por candidata (media del panel)

| id | n jueces | D1 | D2 | D3 | total medio | veredictos |
|---|---|---|---|---|---|---|
| C4 | 6 | 3.67 | 3.67 | 3.5 | 10.83 | {'construir': 6} |
| C8 | 6 | 2.83 | 3.5 | 3.83 | 10.17 | {'reformular': 2, 'construir': 4} |
| C1 | 1 | 2.0 | 4.0 | 4.0 | 10.0 | {'reformular': 1} |
| C9 | 6 | 2.33 | 3.0 | 3.33 | 8.67 | {'descartar': 3, 'construir': 1, 'reformular': 2} |
| C5 | 6 | 2.67 | 3.0 | 2.67 | 8.33 | {'reformular': 3, 'descartar': 2, 'construir': 1} |
| C7 | 6 | 2.5 | 2.83 | 2.83 | 8.17 | {'reformular': 2, 'descartar': 4} |
| C3 | 6 | 2.83 | 2.33 | 2.83 | 8.0 | {'reformular': 3, 'descartar': 2, 'construir': 1} |
| C2 | 6 | 1.5 | 2.67 | 2.67 | 6.83 | {'descartar': 5, 'reformular': 1} |
| C6 | 6 | 1.67 | 2.33 | 2.67 | 6.67 | {'descartar': 6} |

## 3. Objeciones fatales por candidata

### C4
- Riesgo de que la conclusión sea 'el orden casi no cambia' — resultado válido pero poco memorable para un jurado.
- Es análisis de sensibilidad sobre un corpus ya limpiado (trae reloj ganador e incertidumbre) y no verifica el incidente HF, sin marcas; impacto estrecho.
- El 'reloj ganador' del export ya resuelve buena parte del problema por nosotros: si el corpus trae `time_grade` y segundos de incertidumbre, la conclusión puede ser 'el orden aguanta' con independencia del método, y eso no sorprende a nadie.
- Dependencia de relojes no falsada.
- Es otro incidente (la wiki alemana, no HF): la transferibilidad metodológica al caso del sprint es un argumento, no una medición; y si las conclusiones resultan insensibles a la elección de reloj, el hallazgo es un negativo débil.
- Riesgo de resultado nulo: si los relojes apenas mueven el orden, queda una medición de robustez sin hallazgo. Y desvío de caso: el corpus es del incidente de la wiki, no el del sprint; el criterio del track habla de 'this incident'.

### C8
- Solapa fuerte con el ejemplo #1 del track 2 y con lo que el propio expediente ya hizo (comparaciones de conteo); el valor nuevo está solo en el CLI reutilizable, no en la tabla.
- Es un formato de anotación, no un hallazgo; las discrepancias de conteo y las revisiones ya están documentadas en el expediente.
- Es curación, y la calidad depende de que un humano lea cientos de páginas: la matriz de divergencia final puede tener 60 filas y 12 disputas, cifra que no decide nada por sí sola.
- Matriz de divergencia sin falsación.
- Extracción de afirmaciones a escala de cinco publicadores no cabe en 48 horas sin acotar; sin acotación la matriz será somera y el CLI quedará en demo. La clasificación 'en disputa' exige un criterio que, si es arbitrario, un abogado de la parte auditada lo demuele.
- D1=2: la extracción de afirmaciones con procedencia es método estándar de revisión sistemática, y la mitad del insumo (los tres conteos de revisiones del relato de OpenAI, la discrepancia 1.092 de HF) ya está levantada en el expediente. Compite en ejecución, no en innovación.

### C1
- Género ya trillado (link rot / citation decay) y sin relación con la conducta de los modelos, que es lo que el track 2 pide explicar.

### C9
- METR ya publicó lo prescriptivo (estándar del 29/07) y GovAI la lista de retención; derivar requisitos de lo publicado es un ensayo, no investigación.
- Lo prescriptivo ya lo publicaron METR y GovAI; puntuar un solo incidente contra un checklist es un caso de estudio subjetivo, no conocimiento nuevo ni falsable.
- GovAI y METR ya publican lo prescriptivo; puntuar un incidente contra sus listas es una tabla de cumplimiento, no un hallazgo, y el propio expediente reconoce que lo no cubierto es 'puntuar', que es justo lo que no produce novedad.
- Matriz de requisitos sin caso de fallo.
- Lo prescriptivo ya existe (estándar de METR del 29 de julio, lista de GovAI) y el formato checklist pisa el proyecto de ejemplo #6; el valor real —puntuar un incidente real contra el estándar— es la mitad de C8 y no aguanta un reporte entero solo.
- Lo prescriptivo ya está publicado (METR, 29/7: términos de redacción, acceso, tiempo y personal, alcance, resumen de redacción; GovAI: lista de retención); puntuar un solo incidente real contra esos estándares es un apéndice útil, no un informe de 8 páginas.

### C5
- El baseline trivial (20 edits en una década) hace que 'detectar cualquiera' sea inevitable y el hallazgo se vuelva un tautología de bajo valor a menos que se gradúe por falsa alarma.
- Baseline trivial y amañado (cualquier tráfico es anómalo) y contrafactual infalsificable (no se ve qué se notó internamente); además es otro incidente.
- Es otro incidente (la wiki alemana), no el de HF: responde al track 2 pero no al caso que el sprint pone en el centro, y el jurado puede leerlo como desvío.
- Otro incidente; baseline trivial no superable.
- El baseline trivial (20 ediciones en una década) hace que casi cualquier regla 'detecte temprano', así que el contrafactual arriesga ganar por construcción; y SecureLayer7 ya propuso el framing '¿en qué acción dispara tu control?' sobre el timeline de HF.
- El baseline (una wiki con ~20 ediciones en una década, no verificado por este jurado) vuelve anómalo cualquier tráfico: la 'primera alarma' dispara trivialmente por construcción, el número no informa sobre detectabilidad real, y además es el otro incidente.

### C7
- Es réplica con datos sintéticos y no dice nada sobre el incidente real; además el hallazgo del 4x ya es público — replicarlo agrega poco sin generalización por tipo de canal.
- Admite que NO prueba nada del incidente real y el resultado (recall 4x) ya lo publicó Hugging Face; es confirmación sobre datos sintéticos.
- Depende de un repo de terceros sin verificar que recrea la cadena en Docker; en el peor caso el 40% del tiempo se va depurando infraestructura ajena y no queda número.
- Réplica sintética sin validez externa.
- El 4x ya lo midió y publicó HF; replicarlo en laboratorio con datos sintéticos no prueba nada sobre el incidente y depende de un repo Docker de terceros sin verificar. Uso dual delicado: recrear la codificación del canal del atacante es una receta de evasión de DLP que el brief manda señalar, no recorrer.
- Laboratorio sintético sobre un repo de terceros sin verificar y sin datos del incidente real: el número (recall del escáner ingenuo vs el consciente del canal) puede no transferir, y reconstruir la codificación del atacante roza exactamente lo que HF documenta que sus guardarraíles confundieron con lanzar el exploit.

### C3
- El sesgo de selección ya está reconocido por METR en su texto; quedarse en 'medir la dirección' no produce un número defendible solo con el informe público como dato.
- Los datos para cuantificar el sesgo (transcripciones crudas) no son públicos: solo se relee lo que METR ya auto-declaró; sin corpus no sale un número.
- Es un argumento, no una medición: la estimación de sesgo depende de supuestos sobre la comunicación fuera del namespace que nadie puede observar; el número resultante es un intervalo de sensibilidad, no un dato.
- Sesgo de selección no cuantificado.
- Sin acceso al corpus crudo solo puede producir análisis cualitativo de sensibilidad sobre el texto de METR; la 'dirección y tamaño del sesgo' no es computable desde datos públicos, así que no produce el número que promete.
- Los datos para cuantificar el sesgo (el dump completo de ~1,2M entradas, el método de muestreo de los 100 mensajes) no son públicos; sin ellos solo cabe una cota cualitativa de dirección de sesgo, no el tamaño del efecto.

### C2
- Es literalmente el proyecto de ejemplo #1 del track 2 de los organizadores (pre-empt declarado); un grado-de-evidencia como verificador automático también era el ángulo ya propuesto por SecureLayer7.
- Es el proyecto de ejemplo nº1 del track 2 publicado por los organizadores: re-anotación del expediente, no investigación nueva.
- Es literalmente el proyecto de ejemplo nº1 de los organizadores: replicar un ejemplo publicado no puntúa en D1 con el filtro '¿es nuevo para el campo?'.
- Réplica del ejemplo 1 del track 2; sin novedad.
- Es literalmente el proyecto de ejemplo #1 del track 2 publicado por los organizadores; el criterio de 'establecido' sería disputado sin un estándar probatorio explícito.
- Es el proyecto de ejemplo #1 del track 2 casi textual ('A forensic read of the public record: what is established, what is asserted but unverifiable, what the pending third-party assessments could settle', verificado hoy en el payload de la página del sprint). Replicar la sugerencia del organizador no pasa el filtro textual de D1 ('is this actually new to the field, or replicating recent work?').

### C6
- Los organizadores ya lo listan como dirección propia con prior art (Defensive Refusal Bias, NCCDC 2.390 prompts, MITRE FRR); en 48h sin dataset propio solo se replica un efecto ya publicado.
- Dirección del track abierto con prior art citado (Defensive Refusal Bias, MITRE FRR) y sin créditos de cómputo para correr Opus/Fable/GLM.
- Los organizadores ya lo listaron como dirección propia con prior art citado (2603.01246, 2.390 prompts) y figura en proyectos de ejemplo: replicar lo listado no es nuevo; y medir el rechazo 'compuesto' exige un juez de rechazo que es a su vez un modelo, con error no medido.
- Track abierto con prior art citado.
- Replica dirección ya listada por los organizadores con prior art citado (Defensive Refusal Bias, arXiv 2603.01246, MITRE FRR); además sin créditos de cómputo para participantes en línea, correr flujos de 20 pasos contra modelos cerrados cuesta dinero propio del equipo.
- Figura como dirección de los propios organizadores con prior art citado (DRB, arXiv 2603.01246: 12,2% global, 2,72x por palabras clave de seguridad, paradoja de autorización 21,8% vs 11,6% — verificado hoy en el HTML completo del paper), y el sprint da cero créditos de cómputo: sin acceso a Opus/Fable no hay rechazo compuesto real que medir.

## 4. Propuestas propias de los jueces

### TTE (tiempo-a-evidencia) sobre el corpus de collusion.wiki  (glm-5.3-flash, D1=3.0 D2=4.0 D3=4.0)
- qué: Una batería de reglas de detección simple y visible desde fuera, corridas sobre events.jsonl (19.913 eventos etiquetados), con ground truth de cada fase (11/05 primer intento, 26/05 Artifactory, 16/06 salto, 21/06 IPs de empleados, 27/06 alerta de OpenAI) y con la detección real de OpenAI como horizonte de comparación.
- datos: collusion.wiki/explorer/download; el expediente verifica el corpus y su manifiesto; complementado con el timeline oficial del post para los hitos de respuesta real.
- número que produce: Horas/días antes de detección por regla (tiempo-a-evidencia), con curvas precision/recall sobre las 19.913 filas etiquetadas.
- no prueba: Nada sobre el incidente de Hugging Face ni sobre motivaciones o cadena de pensamiento; solo lo observado en la superficie de escritura pública.
- cómo falla: Si ninguna regla simple supera el baseline del tráfico anómalo de la wiki (20 edits en una década) con precision aceptable; caería en un hallazgo negativo — que seguiría siendo reportable con método d

### Anexo de uso dual: TTE también mide qué reglas del lado azul son ejecutables por un equipo pequeño  (glm-5.3-flash, D1=2.0 D2=3.0 D3=3.0)
- qué: Cada regla acompañada de su pseudocódigo reproducible y su costo de cómputo, de modo que otro respondedor o un laboratorio la verifique sin acceso.
- datos: Mismo corpus; el costo se estima del tamaño de los datos y del tiempo de correrlo en un laptop normal.
- número que produce: Costo por regla (ciclo o segundos en hardware de consumidor) versus horas ganadas — una tabla de trade-off falsa-alarma vs costo.
- no prueba: Nada fuera de este corpus; el archivo solo muestra hacia dónde va el margen.
- cómo falla: Si el costo de cómputo es dominado por el IO del dataset en vez de la regla misma, la tabla se vuelve trivial.

### Denominador de consistencia del registro público  (deepseek-v4-pro, D1=3.0 D2=4.0 D3=4.0)
- qué: Grafo de cifras cuantitativas extraído de los 5 informes (HF, OpenAI, METR, Anthropic, AISI), cada una re-derivada aritméticamente y con diff de revisiones vía Wayback; salida, tasa de consistencia y lista de cifras en disputa.
- datos: Los 5 informes públicos, tablas de fase/día del post de HF, capturas Wayback de la página de OpenAI, cifras de trampa de AISI.
- número que produce: Tasa de consistencia sobre 30-40 cifras, con dos hallazgos ya anclados: 1.092 acciones de discrepancia en HF y 3 conteos de 'revisó su relato'.
- no prueba: Nada sobre la conducta de los modelos ni sobre la seguridad de los sistemas.
- cómo falla: Si las cifras no están en tablas extraíbles o las revisiones no tienen capturas Wayback, el denominador colapsa a pocos números.

### P1 — Arnés de reproducibilidad del registro: disponibilidad + aritmética + redacción, con condición de aprobación preinscrita  (deepseek-v4.1-flash, D1=3.0 D2=4.0 D3=4.0)
- qué: Un script de auditoría que toma un incidente y devuelve tres enteros con regla de decisión escrita antes de correr: (a) fracción de URLs de evidencia citadas que aún resuelven, con distinción 200-con-contenido-retirado / 401 / 404 / 302 y fecha; (b) fracción de afirmaciones cuantitativas publicadas que reproducen aritméticamente al recomputarlas desde sus propias tablas; (c) fracción del cuerpo pr
- datos: Públicos y ya accesibles hoy: la tabla por fase y por día del blog de HF (verificada en /home/daw/.hermes/cache/web/huggingface.co-8088c1dfd6.md, líneas 189-207), el informe de METR (metr.org-8e38112b54.md), las capturas de Wayback del 07/08 21:30 UTC (CDX API), la API de datasets de HF (hub-stats 2
- número que produce: Tres porcentajes con intervalo de confianza por bootstrap sobre el conjunto de URLs y afirmaciones, más el conteo absoluto de afirmaciones que no reproducen (esperado: ≥1 confirmada, la brecha de 1.09
- no prueba: Nada sobre la conducta de los modelos, la seguridad del sistema ni la corrección de los informes: mide la salud y la fricción del registro, no la verdad de las afirmaciones sustantivas.
- cómo falla: Si todas las URLs resuelven y toda la aritmética cuadra, el resultado es un cero aburrido; y el diff de Wayback depende de que existan capturas del día de cada revisión, que es una lotería. Mitigación

### P2 — Localizar la brecha de 1.092 acciones en el replay público de Hugging Face  (deepseek-v4.1-flash, D1=4.0 D2=4.0 D3=3.0)
- qué: Comparar la tabla por fase publicada (16.521) con los datos que alimentan el replay interactivo y la serie diaria (17.613): por fase, por día y por tipo, para determinar dónde están las 1.092 acciones 'perdidas' y si el desfase es de ventana temporal, de clasificación o de cuadro. Entregable: diferencias por celda + una regla que explique cuál de los dos cuadros deriva.
- datos: El timeline interactivo del blog de HF (assets públicos, ya cacheado) y la tabla diaria del mismo post; todo público, ningún acceso privilegiado, ninguna cooperación requerida.
- número que produce: Un vector de diferencias por fase/día que suma 1.092, con la fracción de la brecha atribuida a cada causa candidata; si el replay no es machine-readable, el número es 'la brecha se localiza en N de 9 
- no prueba: No explica la intrusión ni el fallo de detección: mide consistencia interna de un cuadro publicado, y por tanto no puede atribuir intención ni capacidad.
- cómo falla: Si el replay es solo una imagen o video sin datos, el proyecto se queda sin denominador y hay que degradarlo a P1. Por eso P1 es la reserva y P2 se corre primero en un límite de 3 horas.

### Falsación de selección de corpus  (kimi-k3, D1=4.0 D2=3.0 D3=2.0)
- qué: Test de hipótesis nula: si el corpus de METR es representativo, muestras bootstrap de 100 mensajes no cambian conclusiones clave.
- datos: Informe METR (texto público).
- número que produce: Probabilidad de que conclusiones cambien bajo selección alternativa.
- no prueba: Nada sobre conducta real de modelos.
- cómo falla: Si el bootstrap no es posible por agregación.

### Prueba de admisibilidad regulatoria del registro público (AI Act Art. 73)  (qwen3.8-max, D1=4.0 D2=4.0 D3=4.0)
- qué: Un instrumento de admisión: se toma el registro público del incidente como si fuera la evidencia acompañante de un reporte de incidente serio ante una autoridad de vigilancia, y se puntúa cada hecho material contra un estándar probatorio declarado (observado por primera parte / corroborado independientemente / fuente única / unverificable / revisado post-publicación), emitiendo un veredicto de adm
- datos: Los cinco relatos públicos (HF, OpenAI, METR/Redwood, Anthropic, UK AISI) más Reuters vía CNA; todo en caché local y URLs del expediente; prueba de disponibilidad de artefactos ya corrida (hub-stats 200, tres datasets 401).
- número que produce: Porcentaje de hechos materiales admisibles sobre preponderancia de la evidencia vs. fuente única; conteo de hechos no falsables desde fuera; decaimiento de artefactos citados a fecha fija.
- no prueba: No prueba qué hizo el modelo ni qué omitió OpenAI en la redacción; solo mide si un tercero (regulador, juez, auditor) podría sostener cada afirmación sin acceso al laboratorio.
- cómo falla: Si el estándar probatorio se percibe como invención del equipo sin anclaje en práctica regulatoria real (guías de la AI Office, CoSAI v1.0), el memo jurídico se vuelve prosa; mitigación: anclar cada c

### Mapa de punto único de fallo del registro público  (glm-5.3, D1=3.0 D2=4.0 D3=4.0)
- qué: Grafo de dependencias afirmación→artefacto→disponibilidad: para cada afirmación establecida de los cinco informes, cuántos artefactos independientes la sostienen y cuántos resuelven hoy (200 con contenido, 200 retirado, 401, 404), con Wayback como testigo.
- datos: Los cinco informes públicos (HF, OpenAI, METR/Redwood, Anthropic, UK AISI) + chequeos de estado HTTP/API corridos por este jurado hoy (hub-stats 200 página y API; papers-content, newpc360, newpcQQ: 401) + timemap de Wayback.
- número que produce: % de afirmaciones establecidas del registro que descansan en exactamente un artefacto recuperable hoy, y tasa de decaimiento por fuente.
- no prueba: Nada sobre la conducta de los modelos ni la seguridad del sistema: es la salud del cuerpo probatorio, no del atacante.
- cómo falla: Si Wayback ya capturó todo lo retirado, el decaimiento cae a ~0 y queda un ejercicio de archivo; y la clasificación de 'afirmación establecida' hereda el juicio de quien extrae las afirmaciones.

### Auditoría aritmética de los 1.092 (sección, no informe)  (glm-5.3, D1=2.0 D2=4.0 D3=3.0)
- qué: Enumerar las hipótesis que reconciliarían las dos tablas del blog de HF (fases no tabeladas, doble conteo por clustering, acciones fuera de ventana) y descartarlas una a una contra las restricciones aritméticas publicadas (16.521 vs 17.613 vs ~17.600).
- datos: Blog de HF (público): tabla por fases, tabla por días y titular; discrepancia ya recalculada por este jurado con máquina (1.092).
- número que produce: Cuántas hipótesis de reconciliación sobreviven a lo publicado (ideal: 0 o 1): si la discrepancia es explicable con lo público o exige datos no públicos.
- no prueba: Nada sobre el ataque real; es consistencia interna del registro.
- cómo falla: Si HF publica una nota que explique la diferencia, el hallazgo muere; y el resultado puede ser un solo párrafo ('ninguna hipótesis sobrevive'), insuficiente para un informe.

## 5. Recomendaciones finales, textuales

### glm-5.3-flash (Ingeniero de respuesta a incidentes (DFIR))
- construir: C4 como núcleo con un anexo de C8 (matriz de afirmación-ancla para los cuestiones que dependen del orden temporal). Alternativa aceptada: TTE sobre collusion.wiki si el equipo prefiere detección sobre causalidad.
- por qué: C4 repite el mismo tipo de problema que METR resolvió a mano con 1.196 transcripciones sin marcas de tiempo por acción, pero sobre un corpus público con ground truth (reloj ganador, incertidumbre) — es el único ángulo del portafolio cuya contribución no está pre-empt por los organizadores, METR, GovAI ni Agent Flight Recorder, y es directamente reutilizable en la próxima investigación.
- alcance 48h: Día 1: cargar events.jsonl/revisions.jsonl, construir tres órdenes causales (reloj ganador, mediana con incertidumbre, orden conservador), identificar 5-10 inferencias causales sensibles al orden. Día 2: escribir el método, límites y uso dual; correr el C8-anexo mínimo sobre 20 afirmaciones del corp
- primer paso: Descargar el corpus con sumas SHA256 del manifiesto y, a partir de revisions.jsonl, extraer los tramos donde el reloj ganador difiere de los relojes percibidos por más del ancho de incertidumbre — ahí

### deepseek-v4-pro (abogado del diablo)
- construir: El denominador de consistencia del registro público (grafo de cifras + re-derivación aritmética + diff de revisiones), absorbiendo el diff de C1 y la matriz de C8.
- por qué: Es lo único falsable del panel que produce un número, con hallazgos ya anclados (1.092 acciones de discrepancia en HF; 3 conteos de revisiones) y que ninguna de las nueve entrega.
- alcance 48h: Extraer 30-40 cifras de los 5 informes, re-derivarlas, diffear 3-5 revisiones vía Wayback y entregar la tasa de consistencia con las cifras en disputa.
- primer paso: Volcar las tablas de fase y de día del post de Hugging Face y re-sumarlas (la discrepancia 16.521/17.613 ya está verificada) como primera fila del denominador.

### deepseek-v4.1-flash (ingeniero de entrega)
- construir: Titular C5+C4 sobre el corpus descargable de collusion.wiki (primera alarma inequívoca por regla simple visible desde fuera + estabilidad del orden causal ante el desambiguador de reloj), con P1 (arnés de reproducibilidad del registro) como andamiaje del apéndice de límites y como suelo garantizado. P2 (localización de la brecha de 1.092 acciones) se corre primero, con límite duro de 3 horas.
- por qué: Es lo único del portafolio que combina novedad real (el corpus tiene relojes en conflicto y coordenadas de incertidumbre publicadas; METR resolvió ese mismo problema a mano y sin marcas por acción), datos ya descargables sin cooperación de nadie, y un número que se mide offline y se reproduce con un comando. C5 responde literalmente al criterio del track ('chequeos que alguien pueda correr mañana'
- alcance 48h: 0-3 h: bajar el corpus, verificar sumas y SHA-256, cargar events/revisions/pages en SQLite o DuckDB. 3-10 h: C5 — definir 3 reglas simples y medir el primer instante de evidencia inequívoca de coordinación contra el baseline trivial (el wiki había sido editado 20 veces en una década) y contra el pri
- primer paso: Ya ejecutado y verificado en esta sesión: `curl -sL -o ev.jsonl.gz https://collusion.wiki/explorer/download/events.jsonl.gz` (200, 486.683 bytes) y `gunzip -c ev.jsonl.gz | wc -l` → 19.913. Siguiente 

### kimi-k3 (METODOLOGO AUDITOR DE EVIDENCIA)
- construir: C3 (sesgo de selección) con test de falsación propio
- por qué: La amenaza principal a validez es el sesgo de muestreo; cuantificarlo es el único hallazgo que significa.
- alcance 48h: Estimación de sesgo con bootstrap y sensibilidad
- primer paso: Extraer muestra de 100 mensajes y re-ejecutar estimaciones de completitud

### qwen3.8-max (REGULADOR / ANALISTA DE POLÍTICA)
- construir: C8 acotado + mi dirección propia como capa normativa: matriz de divergencia con procedencia de la disputa sobre la línea de tiempo de detección (Reuters/CNA vs OpenAI vs HF vs METR), CLI reutilizable, y anexo de admisibilidad regulatoria que puntúa el registro contra el estándar de transparencia de METR y revela el vacío legal (retención, granularidad temporal, redacciones).
- por qué: Es el único artefacto del portafolio que una autoridad real (AI Office, portal de Cal OES) usaría casi sin editar: convierte relatos en conflicto en hechos con código de procedencia y estándar probatorio explícito, todo con datos públicos, sin depender de que ninguna parte coopere, y produce tanto un número como un instrumento normativo. C4 es el segundo mejor por rigor de datos, pero es otro inci
- alcance 48h: Una disputa, cinco publicadores, ~120-180 afirmaciones con cita anclada; CLI en Python que ingiere el formato de afirmaciones y emite la matriz; 6 páginas de reporte + apéndice de limitaciones y uso dual; presupuesto ~20-30 horas de trabajo, costo computacional despreciable (solo lectura y parsing).
- primer paso: Extraer de la caché local de los cinco informes toda afirmación sobre cuándo y cómo se detectó la intrusión (incluida la tensión Reuters que ya documenta el expediente, sección H), asignar a cada una 

### glm-5.3 (JUEZ DE RÚBRICA)
- construir: C4 endurecida: sensibilidad del orden causal a la elección de reloj sobre el corpus público de la wiki (14.591 revisiones), entregada como CLI reutilizable más tabla de flips de conclusiones; absorber como segundo capítulo la matriz de divergencia de C8, que subsume la auditoría aritmética de los 1.092.
- por qué: Es la única candidata con método nuevo (D1=4) ejecutable con certeza razonable en 48 horas sobre datos que este jurado descargó y verificó hoy fila por fila; produce un número defendible y una herramienta que cualquier auditor puede correr mañana — exactamente el criterio del track 2 ('checks somebody could run tomorrow').
- alcance 48h: ~6 h de ingest y definición de 5 relojes (write_date, request_time, recent_changes_time, winning_clock, con incertidumbre); ~8 h de reordenamiento, Kendall tau por pares y flips de orden/signo en 3-4 conclusiones headline (página ZZZ del 19/06, bypass confirmado en 14 minutos el 20/06, salto del 16/
- primer paso: Descargar los cuatro .jsonl.gz de collusion.wiki/explorer/download (verificados hoy: 19.913/14.591/4.579/3.103 filas, SHA256SUMS incluido) y computar el Kendall tau entre winning_clock y write_date so

## 6. Hechos del expediente refutados por los jueces

- [deepseek-v4-pro] El expediente reporta '~18.000 posts' en el segundo incidente (sección I) :: Omite que la propia página del sprint dice 'about 15.000 edits' y que su corpus trae 14.591 revisiones: tres cifras para un mismo hecho, material para C8 :: https://apartresearch.com/sprints/ai-incident-response-sprint-2026-09-11-to-2026-09-13 (update 7 sept) vs https://collusion.wiki/
- [deepseek-v4-pro] METR: ~285 transcripciones iniciales y 1.196 adicionales (1.074 HPIM + 122 Sol) :: No verificado en el texto público: se corrobora ~1.300 y la proporción HPIM/Sol, pero el desglose 285/1.196 queda sin confirmar :: https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/
- [deepseek-v4.1-flash] Expediente §J: el Agent Flight Recorder 'evalúa en cargas sintéticas y trazas reales de SWE-agent, con detección del 100% para edición, borrado, reordenamiento y bifurcación'. :: Conflaciona dos experimentos distintos. El propio paper (arXiv 2609.01931) dice: 'The primary evaluation uses synthetic workloads. We validate RQ1 overhead on five real SWE-agent traces from SWE-bench (38 events)'. Las trazas reales son cinco, con 38 eventos, y se usan solo para el overhead (RQ1); e :: https://arxiv.org/html/2609.01931v1 (sección de evaluación y 'Threats to Validity: Internal')
- [deepseek-v4.1-flash] Expediente §H: 'el texto del track abierto dice "OpenAI ha actualizado su página del incidente tres veces"'; y §B/§A: los 14 proyectos de ejemplo del track 2, la nota de recursos '(21 de julio, actualizado el 28 y 29 de julio)' y la afirmación de que no hay créditos de cómputo para quien participa e :: Ninguna de esas cadenas aparece en la página del sprint: extraje 77.066 caracteres de texto de la página viva (200, 859 KB de HTML) y busqué en la copia local; 'three times', '898', '869', 'checklist', 'reward' y 'compute credit' dan cero coincidencias. Lo único publicado es 'OpenAI published its ow :: https://apartresearch.com/sprints/ai-incident-response-sprint-2026-09-11-to-2026-09-13 (texto servido, 11/09/2026) y copia local /home/daw/.hermes/cache/web/apartresearch.com-1ebd8ed64e2afa97.cache.md
- [deepseek-v4.1-flash] Expediente §D: METR concluyó que sus agentes eran responsables de 'bastante más del 95%' de la actividad del tablero 'y de un poco más del 90% de la actividad de los agentes'. :: Atribución invertida. METR escribe que los agentes de su conjunto de transcripciones son responsables de 'well over 95% of the activity on the message board', mientras que los datasets 'only capture a bit over 90% of the message board activity' (por truncamiento y resets de contenedor). Los dos porc :: https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/ (sección de completitud y limitaciones; copia local metr.org-8e38112b54.md, líneas 489 y 1461)
- [kimi-k3] Discrepancia aritmética de HF (~17.600 vs sumas 16.521/17.613) :: No verificable; presupuesto de tokens no permite web. :: https://huggingface.co/blog/agent-intrusion-technical-timeline
- [kimi-k3] Estados HTTP de datasets (200/401) y Wayback :: No verificable; presupuesto de tokens no permite web. :: https://huggingface.co/datasets/cfahlgren1/hub-stats
- [kimi-k3] Corrección de completitud METR (95% autoría / 90% cobertura) :: No verificable; presupuesto de tokens no permite web. :: https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/
- [kimi-k3] Tabla por fase y volumen diario de HF :: No verificable; presupuesto de tokens no permite web. :: https://huggingface.co/blog/agent-intrusion-technical-timeline
- [qwen3.8-max] Expediente D: '1.196 adicionales (1.074 de HPIM y 122 de Sol)' :: Imprecisión menor, no refutación de fondo: la fuente dice 'an overlapping dataset of 1196 transcripts', es decir solapante con el conjunto previo de ~285, no puramente aditivo; el total único (~1.300) es consistente con solapamiento, no con suma. :: https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/ (línea 442 del texto completo en caché)