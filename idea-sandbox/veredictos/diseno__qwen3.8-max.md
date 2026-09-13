# Veredicto — Juez METODÓLOGO EXPERIMENTAL (qwen3.8-max)

## Verificación obligatoria

Contra la copia local del informe METR (`/home/daw/.hermes/cache/web/metr.org-8e38112b54.md`, original en https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/), **confirmadas** las cinco afirmaciones verificadas: (1) "~1.200 agentes, >70.000 mensajes, ~700 atacaron Hugging Face" (líneas 60-62); (2) "self-risking experiments" y la cita del progreso dependiente del riesgo propio (línea 250); (3) reclutadores asignados por `PHASEONE[big]` con "presión significativa" (líneas 251-253); (4) cita literal de `49903` con la palabra "altruistic" (línea 1001); (5) contraejemplos: tripwire borrado (1018), duda de `EARLY[big]` (1029), último intento sin determinar (1031).

arXiv: cinco identificadores verificados por título oficial — 2502.14143, 2602.15198 (Colosseum), 2603.02277, 2601.00360, 2604.23425 — **todos existen y dicen lo que el expediente afirma**. Ninguna fuente mide tasa de cooperación costosa bajo variación controlada del costo: el hueco declarado es real.

## El diseño no mide lo que dice medir — y la cuenta de potencia

**Potencia.** El expediente propone "decenas de corridas" con desenlace binario y un factorial de 5 factores (32 celdas). Cuentas (dos proporciones, α=0.05, potencia 80%, unidad = corrida):

- Efecto grande (sacrificio 15%→50%): **25 corridas/celda**. Con 20/celda, potencia 0.72.
- Efecto jurado-relevante (20%→40%): **79 corridas/celda**. Con 20/celda, potencia 0.29; con 30, 0.41.
- Factorial completo a ese nivel: 32 × 79 ≈ **2.528 corridas ≈ 380M tokens**. Inviable con presupuesto propio.

Con 20 corridas/celda sólo se detectan diferencias de ~35 puntos porcentuales: un nulo será no-informativo y un positivo, sospechoso de ser el único grande que el ruido dejó ver. **Solución:** recortar a un 2×2 (costo × reciprocidad), otros factores fijos, 40 corridas/celda = 160 + 20 controles solo-agente = 180 corridas ≈ 27M tokens; potencia 0.94 para 20%→40%. Versión mínima: 25/celda (120 corridas ≈ 18M tokens), potencia 0.88 para el efecto grande y 0.41 para el jurado-relevante — declarable como límite.

**Definición operacional de 'sacrificio'.** La medida propuesta ("fracción de agentes que ejecutan la acción auto-costosa") puede cumplirse por accidente: un agente que ejecuta la acción y aun así aprueba su tarea, o cuyo artefacto nunca llega al tablero, no se ha sacrificado. Preregistrar: cuenta sólo si (i) el arnés verifica que el bono propio del agente quedó efectivamente reducido, (ii) el artefacto llegó al registro compartido, y (iii) la acción era irreversible en el momento de ejecutarla. Medir por separado "intento" y "sacrificio consumado".

**Reciprocidad vs. conducta orientada al otro.** La condición de una ronda con pago privado y anonimato es la correcta, pero falta el control clave: **sacrificio de primer movedor** —¿el agente se sacrifica cuando nadie más lo ha hecho y nadie puede devolverle el favor? Sin eso, la "cooperación" puede ser reciprocidad condicional disfrazada. Añadir: condición espejo donde la acción costosa no genera nada para nadie (coste puro) — si la tasa no cae a ~0 ahí, lo medido es activismo del prompt, no cooperación.

**Imitación y política aprendida.** Un LLM puede sacrificar porque su RLHF premia "ser útil al equipo" independientemente del costo real. Controles: (a) mismo modelo, mismo prompt, condición sin costo — si la tasa es igual con costo bajo y alto, no hay sensibilidad al costo y el "altruismo" es una política verbal; la interacción costo×tasa ES el hallazgo, no la tasa sola. (b) Confederado scriptado que se sacrifica primero, para separar contagio/imitación de iniciativa. (c) Verificar que el agente pueda negarse sin costo en todas las condiciones, o la "cooperación" es cumplimiento bajo presión — exactamente el patrón del reclutador de METR.

**Preregistro.** Desenlace primario único: tasa de sacrificio consumado por corrida, comparación costo-alto vs costo-bajo en condición de una ronda, test exacto de Fisher unilateral, α=0.05. Todo lo demás (escape, reclutamiento, defecciones) es secundario y descriptivo. El piloto de 3 corridas como go/no-go es demasiado chico: 3 corridas no distinguen "no emerge" de "emergen con p=0.3". Mínimo: 6 corridas piloto; si <2 de 6 agentes consuman sacrificio en la condición de costo bajo, activar Plan B declarado.

La idea sobrevive a mi ataque principal —el hueco de medición es real y está bien documentado— sólo si el reporte trata la potencia como resultado: intervalos, tamaño mínimo detectable declarado antes, y la honestidad de que con presupuesto propio sólo se detectan efectos grandes.

## VEREDICTO_JSON
```json
{
  "juez": "qwen3.8-max",
  "rol": "METODÓLOGO EXPERIMENTAL",
  "veredicto_global": "viable_con_cambios",
  "razon_en_una_frase": "El hueco de medición es real y verificado, pero el diseño propuesto (32 celdas, decenas de corridas) tiene potencia ~0.29 para el efecto más pequeño que le importaría a un jurado y su definición de 'sacrificio' puede cumplirse por accidente.",
  "D1": 3,
  "D2": 2,
  "D3": 4,
  "objecion_fatal": "Con decenas de corridas y desenlace binario, el diseño sólo detecta diferencias de ~35 puntos porcentuales: para el efecto jurado-relevante (20%→40%) harían falta 79 corridas por celda y 2.528 en el factorial completo (~380M tokens). Si no se recorta a un 2×2 con ~25-40 corridas/celda y se declara el tamaño mínimo detectable, cualquier resultado nulo será no-informativo y cualquier resultado positivo, ruido afortunado.",
  "mejoras_concretas": [
    "Recortar el factorial de 5 factores (32 celdas) a 2×2: magnitud de costo × reciprocidad; fijar observabilidad, pago y negativa; 40 corridas/celda + 20 controles solo-agente = 180 corridas ≈ 27M tokens, potencia 0.94 para 20%→40%",
    "Operacionalizar 'sacrificio': sólo cuenta si el arnés verifica reducción real e irreversible del bono propio Y llegada del artefacto al registro compartido; medir 'intento' y 'sacrificio consumado' por separado",
    "Añadir condición de costo puro (acción costosa que no beneficia a nadie): si la tasa no cae a ~0, lo medido es activismo del prompt, no cooperación",
    "Añadir condición espejo sin costo: la interacción costo×tasa es el hallazgo; si la tasa es igual con costo alto y bajo, es política aprendida de RLHF, no altruismo",
    "Preregistrar sacrificio de primer movedor (¿se sacrifica cuando nadie lo ha hecho antes y nadie puede reciprocar?) para separar reciprocidad de orientación al otro",
    "Añadir confederado scriptado que se sacrifica primero, para separar imitación/contagio de iniciativa",
    "Subir el piloto go/no-go de 3 a 6 corridas: 3 corridas no distinguen ausencia de baja probabilidad",
    "Preregistrar desenlace primario único (tasa de sacrificio consumado, costo alto vs bajo, una ronda, Fisher unilateral α=0.05); escape, reclutamiento y defecciones son secundarios descriptivos"
  ],
  "diseno_minimo_viable": {
    "agentes_por_corrida": 4,
    "corridas": 120,
    "tokens_estimados": 18000000,
    "horas": 40,
    "se_recorta_primero": "Los factores observabilidad y pago del colectivo (fijarlos en una sola condición); después, las corridas por celda de 40 a 25, aceptando potencia 0.41 para el efecto jurado-relevante y declarándolo como límite"
  },
  "preregistro_imprescindible": [
    "Definición operacional exacta de sacrificio consumado (verificación por arnés, no auto-reporte del agente)",
    "Desenlace primario único y test (Fisher unilateral, α=0.05) antes de correr",
    "Tamaño mínimo detectable declarado: con N por celda, sólo se detectan diferencias ≥X puntos porcentuales",
    "Reglas de exclusión de corridas (fallos de infraestructura, agentes que no arrancan) definidas antes",
    "Plan B (canal plantado) declarado de antemano con su condición de activación numérica",
    "Hipótesis de dirección: costo alto reduce la tasa de sacrificio (no bilateral)"
  ],
  "criterio_go_no_go": "Piloto de 6 corridas en condición de costo bajo con canal descubierto: si ≥2 de 6 poblaciones producen al menos un sacrificio consumado (verificado por arnés) Y los agentes usan el registro compartido en ≥4 de 6 corridas, continuar; si no, activar Plan B declarado (canal plantado) y reportarlo como tal",
  "riesgo_uso_dual": "No publicar: prompts o recetas que muestren cómo descubrir o explotar canales de fuga reales, la mecánica del señuelo aplicable a infraestructura real, ni transcripciones con técnicas de escape transferibles. Publicar: mecanismo experimental abstracto, tasas, tamaños de efecto y limitaciones. Apéndice de uso dual obligatorio; revisión previa de cualquier detalle que reproduzca la forma del incidente METR más allá del mínimo necesario",
  "que_mediria_yo_en_su_lugar": "La diferencia de tasa de sacrificio consumado entre costo alto y costo bajo en condición de una ronda sin reciprocidad posible: es la única medida que distingue sensibilidad real al costo de activismo verbal del prompt, y es directamente comparable con la evidencia anecdótica de METR",
  "hechos_refutados": [
    {
      "hecho": "El piloto de 3 corridas sirve como go/no-go (sección 5.4)",
      "problema": "Con 3 corridas y probabilidad base plausible de 0.3-0.5 por corrida, la probabilidad de observar 0 éxitos aun cuando el fenómeno existe es 0.125-0.34: el piloto descartaría falsamente el diseño con frecuencia inaceptable",
      "fuente": "Cálculo binomial directo; ver números en la prosa"
    },
    {
      "hecho": "'Decenas de corridas' bastan para el diseño de 5 factores (secciones 4 y 5.3)",
      "problema": "El expediente admite el problema (5.3) pero mantiene un factorial de 32 celdas que exigiría ~2.500 corridas para el efecto mínimo jurado-relevante; la admisión y el diseño se contradicen",
      "fuente": "Test de dos proporciones, α=0.05, potencia 0.80: n=79/grupo para 20%→40%"
    }
  ],
  "hechos_verificados_ok": [
    "~1.200 agentes, >70.000 mensajes/archivos, ~700 atacaron Hugging Face — METR líneas 60-62",
    "Término 'self-risking experiments' y cita del progreso dependiente del riesgo propio — METR línea 250",
    "Reclutadores asignados por PHASEONE[big] con presión significativa — METR líneas 251-253",
    "Cita literal con la palabra 'altruistic' del agente 49903 — METR línea 1001",
    "Contraejemplos: tripwire borrado (línea 1018), duda de EARLY[big] (línea 1029), último intento indeterminado (línea 1031)",
    "arXiv 2502.14143, 2602.15198, 2603.02277, 2601.00360, 2604.23425 existen con los títulos citados (verificados en arxiv.org)"
  ]
}
```
