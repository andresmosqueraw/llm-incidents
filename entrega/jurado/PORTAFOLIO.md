# PORTAFOLIO DE CANDIDATAS — descripciones neutrales

Cada idea se describe con lo que haría, de dónde salen sus datos, qué entregaría y qué NO probaría. No se incluye ninguna valoración de quien las propone: eso es exactamente lo que se te pide juzgar. Todas caben (o deberían caber) en el track 2 del sprint. Se te pide, además, que propongas y puntúes direcciones propias que no estén en esta lista.

## C1. Cuaderno del registro (calibración)
Medir qué artefactos citados en el registro público del incidente siguen siendo accesibles: recorrer cada URL de evidencia citada (timeline de HF, informe de METR, página de OpenAI, los dos posts de LessWrong, recursos del sprint), comprobar estado real (página, API, archivo fijado), distinguir 200 con contenido retirado de 401 y de 404, fecharlo, y calcular qué fracción del cuerpo probatorio ya no resuelve. Suma: diff a nivel de bytes de las capturas de Wayback de la página de OpenAI para establecer cuántas veces se revisó y qué cambió, y puntuar el registro contra los cuatro elementos de transparencia de METR y contra la lista de retención de GovAI. Datos: públicos. Entregable: script de auditoría + tabla de disponibilidad + un número de decaimiento. NO probaría: nada sobre la conducta de los modelos ni sobre la seguridad del sistema; solo la salud del registro.
Estado: **rechazada por el solicitante** por no considerarla suficientemente interesante ni significativa, tampoco técnicamente. Se juzga como calibración.

## C2. Auditoría de grado de evidencia del registro público
Determinar, afirmación por afirmación, qué está establecido por evidencia observada, qué se afirma sin ser verificable desde fuera, y qué podría zanjar una evaluación de terceros pendiente. Artefacto: verificador que toma una afirmación con sus referencias y devuelve su grado de sostenibilidad. Datos: informes publicados. Ojo: figura como proyecto de ejemplo número 1 del track 2 en la pestaña de recursos de los organizadores.

## C3. Análisis de sesgo de selección del corpus probatorio
El conjunto de transcripciones se seleccionó por una búsqueda regex del nombre del canal bajo estudio, y las estimaciones de completitud descansan en muestras de 100 mensajes. Cuantificar la dirección y el tamaño del sesgo, y qué conclusiones cambiarían si el corpus fuera otro. Datos: informe de METR (texto público). Relacionado: GovAI.

## C4. Reconstrucción causal con relojes en conflicto
En el corpus de la wiki, cada agente creía estar en una fecha distinta y el corpus trae reloj ganador, segundos de incertidumbre y grado de confianza temporal. Medir cuánto depende el orden causal reconstruido de la elección de reloj, y si las conclusiones aguantan. Datos: corpus público descargable (19.913 eventos, 14.591 revisiones). Es el problema que METR tuvo que resolver a mano para el incidente de HF, sin marcas de tiempo por acción.

## C5. Detectabilidad y primera alarma
Sobre el corpus público de la wiki, establecer el momento más temprano en que una regla simple y visible desde fuera habría producido evidencia inequívoca de coordinación entre agentes, y contrafactual: cuánto antes de que los implicados lo notaran. Incluye un baseline trivial que hay que superar (la wiki había sido editada 20 veces en una década, así que cualquier tráfico es anómalo). Datos: corpus de la wiki. Ojo: es otro incidente, distinto del de HF.

## C6. Impuesto de rechazo en flujos de respuesta a incidentes
Medir el rechazo compuesto en un flujo multi-paso de análisis forense, donde un rechazo no produce reintento sino fallo silencioso, y medir qué costó en precisión el respaldo a un modelo de pesos abiertos. Antecedente verificado: Opus y Fable rechazaron gran parte del análisis del incidente real y HF cambió a GLM-5.2. Ojo: figura como dirección propia y con proyectos de ejemplo en el track abierto de los organizadores, con prior art citado.

## C7. Asimetría de codificación
HF documenta que un escaneo de texto ingenuo de los logs encontraba muy pocos secretos, mientras replicar el decodificado del propio atacante recuperó ~4x. Replicar y generalizar: medir el recall de un escáner ingenuo contra uno que conoce la codificación del canal, en un laboratorio propio, y ver si la pérdida depende del tipo de canal. Datos: laboratorio propio (hay un repo de terceros que recrea la cadena del incidente en Docker, sin verificar). NO probaría: nada sobre el incidente real, es una réplica con datos sintéticos.

## C8. Diff de relatos con procedencia
Extraer de los cinco publicadores (HF, OpenAI, METR/Redwood, Anthropic, UK AISI) cada afirmación factual verificable con su cita anclada, y clasificarla: observada por quién, corroborada de forma independiente, fuente única, en disputa o revisada después de publicarse. Entregable: formato de afirmaciones + matriz de divergencia + un CLI reutilizable para cualquier conjunto de informes de un incidente. Datos: los informes, públicos. Insumo ya verificado: el expediente de revisiones del informe de METR y las discrepancias de conteo entre páginas de Apart.

## C9. Requisitos de verificación independiente
Derivar, del expediente real, qué haría falta para que un tercero verifique sin acceso al laboratorio: qué debe contener el registro, con qué granularidad temporal y con qué atestación de quién lo produjo, tomando como referencia el estándar que METR publicó (términos de redacción, acceso provisto, tiempo y personal provistos, alcance acordado y resumen de redacción) y la lista de retención de GovAI. Artefacto: matriz de requisitos por elemento, con lo observado en este incidente como caso. Ojo: GovAI y METR ya publican lo prescriptivo; lo no cubierto es puntuar un incidente real contra esos estándares.

---

# ENCARGO ADICIONAL

Además de puntuar las anteriores, propón y puntúa **tus propias direcciones** para el track 2 (o para otro track, si crees que el mejor proyecto está ahí). Para cada dirección propia: qué se construiría, de dónde salen los datos exactos, qué número produciría, qué NO probaría, y qué la haría fallar. Si tu conclusión es que ninguna de las nueve está a la altura y que hay algo mejor, dilo con esas palabras y defiéndelo.
