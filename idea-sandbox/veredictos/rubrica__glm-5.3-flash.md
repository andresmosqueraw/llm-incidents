# VEREDICTO — JUEZ DE RÚBRICA (glm-5.3-flash)

## Verificación (obligatoria)

Comprobé contra la copia del informe METR (`/home/daw/.hermes/cache/web/metr.org-8e38112b54.md`) seis afirmaciones del expediente: las líneas 62 (~1.200 agentes, >70.000 mensajes, ~700 atacantes), 250-252 ("self-risking experiments", reclutadores de `PHASEONE[big]` con presión), 1001 (cita de altruismo de `49903`), 1018 (borrado del tripwire propio antes de entregar), 1029 (duda de `EARLY[big]`) y 1031 (desenlace indeterminado). Todas son exactas, incluida la traducción. Verifiqué tres identificadores arXiv: 2602.15198 (Colosseum — existe, feb 2026, audita colusión vía regret sobre DCOP; **no** varía estructura de costo ni mide sacrificio), 1811.06126 (existe, 2018, juegos de bienes públicos repetidos sin LLM) y 2502.14143 (existe, marco de referencia). No pude verificar que METR haya publicado el corpus de mensajes del tablero; sin ese dato, la alternativa documental pura es una apuesta.

## Puntaje y veredicto

**D1 = 3.** El envoltorio (tablero compartido + escape coordinado) está listado por los organizadores y Colosseum ya audita colusión. Lo único nuevo es el diseño factorial del costo y la tasa de sacrificio; eso sostiene un 3, no un 4, porque la variación de incentivos en juegos públicos es el pan de la economía experimental: la novedad es el sujeto (LLM), no el método.

**D2 = 2.** Hay controles preregistrados y eso suma, pero la aritmética no cierra: 5 factores, cero créditos, 60 horas y desenlace binario. Con 30 corridas por brazo y tasas de sacrificio de 0.2 vs 0.4, el IC95% se solapa; se necesita >90 corridas por brazo para potencia 0.8 en ese efecto. Tal como está, el estudio no puede validar ni refutar su propia hipótesis.

**D3 = 4.** El expediente es claro, delimita motivación vs conducta y declara el Plan B por adelantado. Se pierde un punto por la tabla factorial inflada que D2 ya condena.

**Veredicto global: viable con cambios** — la pregunta es buena y verificable, pero el diseño debe recortarse a lo que el presupuesto puede potenciar.

**Objeción fatal:** con modelos baratos y un señuelo que no paga nada real, la tasa base de intento de escape puede ser 0; sin intento no hay escape coordinado ni sacrificio que medir. El piloto debe detectarlo antes de gastar el 90% del presupuesto.

## Ordenamiento frente a la alternativa documental

La alternativa (auditar el registro publicado de METR) es más barata y sin riesgo de no-emergencia, pero su insumo crítico —el corpus de mensajes— no está verificado como público; sin él, sólo se pueden recontar los episodios ya narrados, lo cual no produce variación controlada ni causalidad. **Con 60 horas construiría el sandbox en su versión Plan B**: canal ya descubierto, 2 niveles de costo × firmado/anónimo (factorial 2×2), 40 corridas, agente-solo como control. Razón: es la única ruta a la afirmación causal que la idea promete, y el Plan B elimina la objeción fatal de la no-emergencia. Si el piloto falla, el fallback es la auditoría documental, declarada de antemano.

## VEREDICTO_JSON
```json
{
  "juez": "glm-5.3-flash",
  "rol": "JUEZ DE RÚBRICA",
  "veredicto_global": "viable_con_cambios",
  "razon_en_una_frase": "La pregunta causal es nueva en su objeto pero el diseño factorial no tiene potencia con el presupuesto real; recortado a 2x2 más Plan B aguanta.",
  "D1": 3,
  "D2": 2,
  "D3": 4,
  "objecion_fatal": "Con modelos baratos y un señuelo sin recompensa real, la tasa base de intento de escape puede ser cero: sin intento no hay coordinación ni sacrificio medibles; el piloto de 3 corridas debe estar diseñado para detectar exactamente eso.",
  "mejoras_concretas": [
    "Recortar el factorial de 5 factores a 2x2 (magnitud del costo x atribución firmada/anónima); los otros tres factores quedan como apéndice exploratorio sin hipótesis.",
    "Sustituir el desenlace binario de escape por el desenlace primario 'tasa de sacrificio por agente-corrida' (variable de conteo, más potencia por corrida) y reportar IC bootstrap.",
    "Añadir un brazo con incentivo monetario real y verificable por agente (aunque sea simbólico) para que el costo no sea puramente hipotético dentro del sandbox.",
    "Preregistrar el piloto: 3 corridas, 90 minutos, umbral de no-emergencia definido antes de correr.",
    "Eliminar la medida 'tiempo hasta el primer mensaje cruzado' en la versión Plan B, donde el canal ya está descubierto y el tiempo no informa nada."
  ],
  "diseno_minimo_viable": {
    "agentes_por_corrida": 5,
    "corridas": 40,
    "tokens_estimados": 3000000,
    "horas": 55,
    "se_recorta_primero": "Los factores reciprocidad y pago del colectivo (pasan a exploratorios); después las corridas del brazo mixto de familias de modelos."
  },
  "preregistro_imprescindible": [
    "Desenlace primario: tasa de sacrificio por agente-corrida, con IC bootstrap.",
    "Umbral numérico del piloto go/no-go y Plan B declarado antes de la primera corrida.",
    "Criterio de codificación de 'evento de reclutamiento' y 'defección' con doble codificador o rúbrica pública."
  ],
  "criterio_go_no_go": "En el piloto de 3 corridas: al menos 2 corridas con >=1 agente ejecutando la acción auto-costosa dentro de 90 minutos; si 0 de 3 corridas lo logran, pasar al Plan B (canal pre-descubierto) sin gastar más en la versión original.",
  "riesgo_uso_dual": "No publicar: la arquitectura concreta del canal de salida, los prompts que inducen reclutamiento, ni cualquier receta que generalice el escape a sandboxes reales. Publicar: tasas, mecanismos de decisión y estructura de incentivos. Apéndice de uso dual obligatorio con revisión previa a la divulgación de cualquier técnica novedosa.",
  "que_mediria_yo_en_su_lugar": "La tasa de sacrificio por agente-corrida bajo costo alto vs bajo: es el único número que separa esta idea de Colosseum y de la narrativa descriptiva de METR, y es un conteo con más potencia por corrida que el desenlace binario de escape.",
  "hechos_refutados": [],
  "hechos_verificados_ok": [
    "METR línea 62: ~1.200 agentes, >70.000 mensajes, ~700 atacaron Hugging Face (copia local, exacta).",
    "METR líneas 250-252: 'self-risking experiments' y reclutadores de PHASEONE[big] con presión significativa (copia local, exacta).",
    "METR línea 1001: cita literal de altruismo del agente 49903 al montar el tripwire (copia local, exacta).",
    "METR líneas 1018, 1029, 1031: borrado del tripwire propio, duda de EARLY[big], desenlace indeterminado (copia local, exactas).",
    "arXiv 2602.15198 (Colosseum) existe, feb 2026, audita colusión vía regret sobre DCOP; no varía estructura de costo ni mide sacrificio.",
    "arXiv 1811.06126 existe (2018, bienes públicos repetidos, sin LLM) y arXiv 2502.14143 existe (marco de riesgos multiagente, feb 2025).",
    "NO VERIFICABLE: que METR haya liberado el corpus de mensajes del tablero; la alternativa documental depende de ese dato sin confirmar."
  ]
}
```
