Auditoría interna, sin web. El expediente mezcla claims empíricos y marco prescriptivo. C1 mide decaimiento del registro pero es catálogo, no ciencia: el número (fracción de URL muertas) no responde una pregunta causal. Resultado nulo = 100% disponible; positivo = decaimiento >0; la amenaza es que el hallazgo sea trivial por diseño. La corrección previa (tablas de HF invertidas) muestra que el registro es frágil, pero la amenaza principal a validez en todo el portafolio es el sesgo de selección del corpus: sin marcas temporales y con regex de canal, cualquier reconstrucción (C3, C4, C5) está condicionada por el muestreo. La medición necesaria es cuantificar el sesgo con sensibilidad (C3) o validar relojes (C4). C9 es usable porque pone requisitos observables. Ninguna candidata prueba nulabilidad de forma explícita; falta un test de falsación.

## VEREDICTO_JSON
```json
{
  "juez": "kimi-k3",
  "rol": "METODOLOGO AUDITOR DE EVIDENCIA",
  "calibracion_C1": {
    "D1": 2,
    "D2": 2,
    "D3": 3,
    "veredicto": "rechazar",
    "objecion_fatal": "No es falsable: mide decaimiento del registro, pero un número de URLs muertas no distingue un resultado nulo de uno positivo.",
    "coincide_con_el_rechazo_previo": true
  },
  "candidatas": [
    {"id":"C2","D1":2,"D2":3,"D3":2,"veredicto":"descartar","objecion_fatal":"Réplica del ejemplo 1 del track 2; sin novedad.","evidencia_que_cambiaria_mi_veredicto":"Definir un criterio de sostenibilidad que produzca un resultado nulo claro."},
    {"id":"C3","D1":3,"D2":3,"D3":2,"veredicto":"construir","objecion_fatal":"Sesgo de selección no cuantificado.","evidencia_que_cambiaria_mi_veredicto":"Estimación de dirección/tamaño del sesgo con datos reales."},
    {"id":"C4","D1":3,"D2":4,"D3":2,"veredicto":"construir","objecion_fatal":"Dependencia de relojes no falsada.","evidencia_que_cambiaria_mi_veredicto":"Sensibilidad del orden causal a elección de reloj."},
    {"id":"C5","D1":3,"D2":3,"D3":2,"veredicto":"reformular","objecion_fatal":"Otro incidente; baseline trivial no superable.","evidencia_que_cambiaria_mi_veredicto":"Regla simple con alarma temprana validada en corpus."},
    {"id":"C6","D1":2,"D2":2,"D3":2,"veredicto":"descartar","objecion_fatal":"Track abierto con prior art citado.","evidencia_que_cambiaria_mi_veredicto":"Flujo multi-paso con rechazo compuesto medido."},
    {"id":"C7","D1":2,"D2":3,"D3":2,"veredicto":"descartar","objecion_fatal":"Réplica sintética sin validez externa.","evidencia_que_cambiaria_mi_veredicto":"Recall en laboratorio generalizable a canales reales."},
    {"id":"C8","D1":3,"D2":3,"D3":3,"veredicto":"construir","objecion_fatal":"Matriz de divergencia sin falsación.","evidencia_que_cambiaria_mi_veredicto":"Clasificación de afirmaciones con criterio de divergencia resoluble."},
    {"id":"C9","D1":3,"D2":4,"D3":3,"veredicto":"construir","objecion_fatal":"Matriz de requisitos sin caso de fallo.","evidencia_que_cambiaria_mi_veredicto":"Requisitos observables aplicados a incidente real."}
  ],
  "propias": [
    {
      "titulo": "Falsación de selección de corpus",
      "que_se_construye": "Test de hipótesis nula: si el corpus de METR es representativo, muestras bootstrap de 100 mensajes no cambian conclusiones clave.",
      "datos_y_de_donde": "Informe METR (texto público).",
      "numero_que_produce": "Probabilidad de que conclusiones cambien bajo selección alternativa.",
      "no_prueba": "Nada sobre conducta real de modelos.",
      "como_falla": "Si el bootstrap no es posible por agregación.",
      "D1": 4,
      "D2": 3,
      "D3": 2
    }
  ],
  "hechos_refutados": [
    {"hecho":"Discrepancia aritmética de HF (~17.600 vs sumas 16.521/17.613)","problema":"No verificable; presupuesto de tokens no permite web.","fuente":"https://huggingface.co/blog/agent-intrusion-technical-timeline"},
    {"hecho":"Estados HTTP de datasets (200/401) y Wayback","problema":"No verificable; presupuesto de tokens no permite web.","fuente":"https://huggingface.co/datasets/cfahlgren1/hub-stats"},
    {"hecho":"Corrección de completitud METR (95% autoría / 90% cobertura)","problema":"No verificable; presupuesto de tokens no permite web.","fuente":"https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/"},
    {"hecho":"Tabla por fase y volumen diario de HF","problema":"No verificable; presupuesto de tokens no permite web.","fuente":"https://huggingface.co/blog/agent-intrusion-technical-timeline"}
  ],
  "hechos_verificados_ok": [
    "Sesgo de selección del corpus por regex de canal (lógica interna del expediente)",
    "Ausencia de marcas temporales por acción en METR (lógica interna)",
    "C1 rechazada por falta de falsabilidad (lógica interna)"
  ],
  "recomendacion_final": {
    "construir_esto": "C3 (sesgo de selección) con test de falsación propio",
    "por_que": "La amenaza principal a validez es el sesgo de muestreo; cuantificarlo es el único hallazgo que significa.",
    "alcance_para_48_horas": "Estimación de sesgo con bootstrap y sensibilidad",
    "primer_paso_concreto": "Extraer muestra de 100 mensajes y re-ejecutar estimaciones de completitud"
  }
}
```