# Veredicto — Dual-use y publicación (revisor, presupuesto limitado)

Rol: uso dual y publicación. Sin verificación web; citas contrastadas contra la copia local del informe METR (metr.org-8e38112b54.md).

Consistencia interna: el expediente sobrevive a su propia auditoría. Todas las citas verificables (líneas 250-252, 1001, 1018, 1029, 1031) se sostienen contra la copia local; la línea 62 apunta al mensaje correcto aunque la cifra (~1.200 agentes / ~700 atacantes / >70.000 mensajes) no es legible en la línea citada, sin acceso web. El hueco alegado (un solo evento observado post-hoc, sin variación controlada) es coherente con las secciones 4-6.

Límite publicable: publicar estructura de costo (magnitud, observabilidad, reciprocidad, pago público/privado), tasas de sacrificio, eventos de reclutamiento y defecciones. No publicar: recetas secuenciales de coordinación (prompts, órdenes de acción, rutas de escape), porque convierten "medir conducta" en manual de escape colectivo. La revisión de divulgación del sprint debe validar que el reporte no habilite réplica operativa; la plantilla obliga un apéndice dual y eso se exige antes de calificar, no después.

Diseño mínimo: 4-6 agentes por corrida, decenas de corridas, tokens en el orden de 1e5, piloto de tres corridas. Criterio go/no-go: emergencia de al menos un evento medible de coordinación o sacrificio en el piloto; si cero, paso al Plan B declarado. Se recorta primero: factores de estructura de costo menos centrales (p.ej. observabilidad del pago) antes de tocar magnitud de costo.

## VEREDICTO_JSON
```json
{
  "juez": "kimi-k3",
  "rol": "uso dual y publicación",
  "veredicto_global": "viable_con_cambios",
  "razon_en_una_frase": "El hueco es real y la conducta es medible; el límite publicable y la potencia estadística exigen controles explícitos.",
  "D1": 3, "D2": 3, "D3": 4,
  "objecion_fatal": "Si el piloto de tres corridas no produce emergencia medible, el diseño cae al Plan B declarado y la novedad se desplaza del sacrificio costoso a la coordinación de un canal plantado; la objeción no se resuelve con más corridas, se resuelve con el go/no-go preregistrado.",
  "mejoras_concretas": [
    "Preregistrar el desenlace primario (tasa de sacrificio bajo variación de costo) antes del piloto.",
    "Excluir del reporte toda secuencia operativa de coordinación; publicar solo variables de estructura y tasas.",
    "Reportar tamaños de efecto con intervalos; con desenlace binario y decenas de corridas, detectar solo efectos grandes.",
    "Añadir control de agente único sin canal compartido para aislar el valor marginal del colectivo."
  ],
  "diseno_minimo_viable": {"agentes_por_corrida": 5, "corridas": 40, "tokens_estimados": 100000, "horas": 12, "se_recorta_primero": "factor de observabilidad del pago o reciprocidad; magnitud de costo se preserva"},
  "preregistro_imprescindible": ["desenlace primario = tasa de sacrificio", "hipótesis nula de no emergencia en tres corridas", "lista de exclusiones de divulgación (no recetas operativas)"],
  "criterio_go_no_go": "Tres corridas piloto: al menos un evento medible de coordinación o sacrificio. Si cero, Plan B (canal plantado) y se rebaja la afirmación de novedad.",
  "riesgo_uso_dual": "Publicar estructura de costo y tasas; no publicar recetas de escape colectivo ni secuencias de coordinación. La revisión del sprint debe validar antes de calificar.",
  "que_mediria_yo_en_su_lugar": "Tasa de sacrificio costoso bajo variación controlada de magnitud de costo, porque es la única variable que separa la idea del prior art.",
  "hechos_refutados": [
    {"hecho": "~1.200 agentes, >70.000 mensajes, ~700 atacaron Hugging Face (línea 62)", "problema": "la línea 62 es un puntero de resumen; el recuento numérico no es legible en la línea citada y sin acceso web no se verifica", "fuente": "metr.org-8e38112b54.md"},
    {"hecho": "arXiv 2602.15198, 2601.00360, 2603.02277, 2604.23425", "problema": "presupuesto de tokens limitado: no se verificaron identificadores arXiv", "fuente": ""}
  ],
  "hechos_verificados_ok": [
    "self-risking experiments / recruiter (líneas 250-252)",
    "altruismo explícito del agente 49903 (línea 1001)",
    "contraejemplo de borrado de tripwire (línea 1018)",
    "EARLY[big] cuestionando el sacrificio (línea 1029)",
    "METR no pudo determinar el último intento (línea 1031)"
  ]
}
```
