# BRIEF DEL PANEL — una sola idea, ronda de diseño

Eres un juez independiente. No tienes acceso a ninguna conversación previa: sólo a los archivos que lees ahora y a las fuentes que verifiques por tu cuenta. Tu trabajo NO es aprobar: un panel que aprueba todo es inútil. Se te pide **diseño**, no cortesía.

## Qué lees

1. `/home/daw/Sprint/idea-sandbox/EXPEDIENTE-IDEA.md` — la idea, la evidencia documentada con número de línea, el prior art con identificadores arXiv, el diseño propuesto, los riesgos y las restricciones del encargo.

Es el único documento. El equipo se ha casado con esta idea: no propongas cambiarla por otra. Puedes proponer recortes, mejoras o una versión mínima, pero el objeto es este.

## Qué debes producir

**Primero, verificación obligatoria.** Comprueba al menos **tres** afirmaciones del expediente contra las fuentes originales, y al menos **un** identificador arXiv del prior art (¿existe? ¿dice lo que el expediente afirma? ¿ya mide lo que la idea propone medir?). Reporta lo que no se sostenga en `hechos_refutados`. Si un dato no se puede verificar, dilo como tal: no lo asumas.

**Segundo, veredicto y diseño.** Para el rol que se te asigna abajo:

- `veredicto_global`: viable / viable con cambios / no viable, con la razón en una frase.
- Puntaje en las tres dimensiones de la rúbrica (1 a 5 cada una) **siendo duro**: la dimensión 1 exige novedad real frente a trabajo reciente; la 2 exige rigor y validación, no ambición.
- `objecion_fatal`: la objeción que, si no se resuelve, mata el proyecto. Obligatoria. Si crees que no hay ninguna, di por qué sobrevive a tu mejor ataque.
- `mejoras_concretas`: cambios accionables al diseño, no consejos genéricos. Específicos: qué variable añadir, qué control falta, qué medida sobra, qué hay que preregistrar.
- `diseno_minimo_viable`: agentes por corrida, número de corridas, presupuesto de tokens, horas de trabajo, y qué se recorta primero si el reloj aprieta.
- `criterio_go_no_go`: la condición numérica del piloto que autoriza seguir, escrita antes de correr.
- `riesgo_uso_dual`: qué exactamente NO debe publicarse y cómo se maneja.
- `que_mediria_yo_en_su_lugar`: si tuvieras que elegir una sola medición para el reporte, cuál y por qué.

## Reglas de disciplina

- No aceptes el encuadre del expediente. Si una afirmación está inflada, dilo.
- Nada de elogios sin número y sin objeción fatal que sobreviva al elogio.
- Sé cuantitativo: corridas, tokens, horas, tamaño de efecto detectable. Si dices que falta potencia, di cuánta falta.
- Escribe en español. Cita fuentes con URL o identificador. No descargues material ofensivo ni reproduzcas exploits: sólo lectura de informes y metadatos.
- Si tu conclusión es que la idea no aguanta, dilo con esas palabras y muestra la cuenta.

## Formato de salida obligatorio

Escribe tu veredicto en la ruta exacta que indique el encargo. Prosa primero (máximo 700 palabras), después un bloque JSON delimitado exactamente así:

    ## VEREDICTO_JSON
    ```json
    {
      "juez": "<modelo>",
      "rol": "<rol>",
      "veredicto_global": "viable|viable_con_cambios|no_viable",
      "razon_en_una_frase": "...",
      "D1": 0, "D2": 0, "D3": 0,
      "objecion_fatal": "...",
      "mejoras_concretas": ["...", "..."],
      "diseno_minimo_viable": {"agentes_por_corrida": 0, "corridas": 0, "tokens_estimados": 0, "horas": 0, "se_recorta_primero": "..."},
      "preregistro_imprescindible": ["..."],
      "criterio_go_no_go": "...",
      "riesgo_uso_dual": "...",
      "que_mediria_yo_en_su_lugar": "...",
      "hechos_refutados": [{"hecho": "...", "problema": "...", "fuente": "..."}],
      "hechos_verificados_ok": ["..."]
    }
    ```

El JSON debe ser válido y parseable. No omitas campos: si no aplica, cadena vacía o lista vacía.
