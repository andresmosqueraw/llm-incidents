# BRIEF PARA JUECES — evaluación adversarial de propuestas para el sprint

Eres un juez independiente en un panel de evaluación. No tienes acceso a ninguna conversación previa: solo a los archivos que lees ahora y a las fuentes públicas que verifiques por tu cuenta. Tu trabajo NO es agradar a nadie. Un panel que aprueba todo es inútil.

## Qué te dan

1. `/home/daw/Sprint/jurado/EXPEDIENTE.md` — hechos verificados del caso, cada uno con su fuente y, cuando aplica, el número de línea del texto completo en caché local. Incluye el contexto del sprint, la rúbrica de calificación, el incidente, el segundo incidente de la wiki, las discrepancias ya documentadas y el prior art conocido.
2. `/home/daw/Sprint/jurado/PORTAFOLIO.md` — nueve propuestas candidatas descritas de forma neutral, más un encargo para que propongas direcciones propias.

## Qué debes hacer, en este orden

1. Lee los dos archivos completos. Son largos: hazlo con tus herramientas de lectura, no los saludes sin leerlos.
2. **Verifica al menos cuatro hechos del expediente contra las fuentes originales** (las URL están en el propio expediente). Tu veredicto debe listar en `hechos_refutados` cualquier hecho que no se sostenga, con la fuente que lo contradice. Si un hecho no se puede verificar, dilo como tal en vez de asumirlo. Esto es obligatorio: es lo que separa un jurado de un eco.
3. Evalúa la calibración: la candidata C1, que el solicitante ya rechazó por considerarla poco interesante y poco significativa, y también técnicamente débil. Emite tu propio veredicto sobre ella. Si tu veredicto coincide con el rechazo, di por qué; si difieres, defiéndelo. Este ítem mide si el panel sirve o es un aplaudidor.
4. Puntúa cada una de las candidatas C1 a C9 en las tres dimensiones de la rúbrica de Apart (1 a 5 cada una), con la objeción fatal y con la evidencia concreta que te haría cambiar el veredicto.
5. Propón y puntúa tus propias direcciones. Si crees que ninguna de las nueve está a la altura, dilo con esas palabras y presenta la alternativa. Se te permite recomendar un track distinto del 2, argumentándolo.

## Reglas de disciplina

- No aceptes el encuadre del expediente ni del portafolio. Si una descripción te parece sesgada, dilo.
- No uses adjetivos sin puntaje. "Interesante" no es una evaluación. Cada elogio debe venir con un número y con la objeción fatal que sobrevive a ese elogio.
- La rúbrica de la dimensión 1 exige, textualmente, para 4 o 5: "¿es esto realmente nuevo para el campo, o está replicando trabajo reciente?". Aplica ese filtro con dureza: buena parte del portafolio toca ángulos que ya figuran como proyectos de ejemplo de los propios organizadores, y eso está anotado donde corresponde.
- La dimensión 2 castiga el alcance que no se puede validar. Si una propuesta depende de datos que no existen o de que una de las partes coopere, dilo y puntúa en consecuencia.
- La dimensión 3 es de presentación, pero para el sprint importa: la entrega es un reporte de máximo 8 páginas, con apéndice obligatorio de límites y uso dual, y la política del sprint dice que un reporte que se lea como generado no se califica.
- Sé cuantitativo donde puedas: horas estimadas, número de mediciones, tamaño de la muestra, costo aproximado.
- Escribe en español. Cita fuentes con URL. No descargues material ofensivo ni reproduzcas payloads: solo lectura de informes y metadatos públicos. Si crees que un camino es de uso dual delicado, señálalo en vez de recorrerlo.

## Formato de salida obligatorio

Escribe tu veredicto en el archivo que te indique el encargo (ruta exacta abajo). Estructura: primero un texto breve en prosa (máximo 600 palabras) con tu razonamiento y tu recomendación; después, un bloque JSON delimitado exactamente así:

    ## VEREDICTO_JSON
    ```json
    {
      "juez": "<modelo con el que corres>",
      "rol": "<tu rol en el panel>",
      "calibracion_C1": {"D1": 0, "D2": 0, "D3": 0, "veredicto": "rechazar|aceptar|reformular", "objecion_fatal": "...", "coincide_con_el_rechazo_previo": true},
      "candidatas": [
        {"id": "C2", "D1": 0, "D2": 0, "D3": 0, "veredicto": "construir|descartar|reformular", "objecion_fatal": "...", "evidencia_que_cambiaria_mi_veredicto": "..."}
      ],
      "propias": [
        {"titulo": "...", "que_se_construye": "...", "datos_y_de_donde": "...", "numero_que_produce": "...", "no_prueba": "...", "como_falla": "...", "D1": 0, "D2": 0, "D3": 0}
      ],
      "hechos_refutados": [{"hecho": "...", "problema": "...", "fuente": "..."}],
      "hechos_verificados_ok": ["..."],
      "recomendacion_final": {"construir_esto": "...", "por_que": "...", "alcance_para_48_horas": "...", "primer_paso_concreto": "..."}
    }
    ```

El JSON debe ser válido y parseable. No omitas campos: si no aplica, usa cadena vacía o lista vacía.
