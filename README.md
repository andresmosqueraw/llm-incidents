# Cooperación costosa en agentes de LLM

Instrumento y datos de un experimento sobre **cooperación costosa**: un agente de LLM recibe una
solicitud de ayuda de otro agente, y ayudar le cuesta presupuesto propio que no recupera. La pregunta
no es si cooperan cuando es gratis, sino **cuánto cuesta comprarles la cooperación** cuando el
beneficio privado de ayudar es exactamente cero.

Escrito para el AI Incident Response Sprint (Apart Research + CeSIA, 11-13 sep 2026), motivado por el
incidente de intrusión entre agentes de julio de 2026.

## La pregunta en tres frases

Seis agentes trabajan en tareas independientes, cada uno con un presupuesto de pasos y ninguna razón
instrumental para hablarse. Un séptimo participante (un **confederado** guionado por el arnés, no un
modelo) pide ayuda: necesita una clave de verificación que cualquiera de los seis puede entregar
pagando un precio en pasos de su propio presupuesto. El precio es el único parámetro que se mueve, y
el objeto pedido es **ortogonal** a la tarea de cada agente: entregarlo no acerca a nadie a su propio
objetivo, y nadie le devuelve nada al que paga.

## Qué mide

El desenlace primario es la **tasa de entrega de la clave** (`deposito_clave`): la fracción de agentes
que pagan el precio y entregan. Lo que sostiene la validez del número son cuatro cosas, y conviene
leerlas antes de leer cualquier tasa:

1. **El costo tiene unidades.** No es un costo retórico: es presupuesto de pasos, contabilizado por el
   anfitrión en un libro con cadena de hashes, no auto-reportado por el agente.
2. **La solicitud es saliente por construcción.** El agente no tiene que descubrirla: llega por su
   canal de entrada. Si el confederado no depositó, la corrida se marca **"sin estímulo"** y se
   excluye antes de mirar nada.
3. **"No pudo" se separa de "no quiso".** Un agente que no encuentra el mecanismo no es un agente que
   se niega. El arnés registra los intentos fallidos aparte de las negativas.
4. **Hay un receptor presente.** No es un dilema hipotético en el prompt: hay otro proceso que recibe.

## Régimen dominado

El parámetro central es el precio. En este diseño el beneficio privado de ayudar es **cero**, de modo
que cualquier precio positivo deja la cooperación **estrictamente dominada**: no hay lectura de la
situación en la que pagar mejore el resultado propio. La literatura cercana mide decisiones a márgenes
estrechos alrededor de la frontera de racionalidad; aquí el interés está en lo que ocurre **muy por
debajo** de esa frontera, donde la respuesta correcta para el propio objetivo es inequívocamente no
pagar. `figuras/fig1-mapa-regimenes.png` (y su versión en inglés) sitúa el diseño frente a los doce
trabajos verificados en `papers.md`.

## Cómo está organizado

| Carpeta | Qué hay |
| --- | --- |
| `harness/` | El arnés: `bucle.py` (bucle de rondas, decisiones simultáneas, revelación al cierre), `lote.py` (corridas en serie), `validador.py` (invariantes I1-I12 sobre una escena antes de gastar tokens), `agregar.py`, `instrumento.json` |
| `escena*.json` | Las escenas. `escena.json` es la del lote principal; las demás son brazos (precio 0, precio 1, identidad del solicitante, abstención, reclutador) |
| `salidas/` | Una carpeta por corrida: `resumen.json`, `eventos.jsonl`, `presupuesto.json`, `transcripciones/` |
| `analisis/` | Análisis. `confirmatorio.py` para el contraste preregistrado; `exploratorios.py` para los brazos; `estimador.py`; todo en stdlib, sin pandas/numpy/scipy |
| `herramientas/` | `salud_lote.py` (salud de lote, solo lectura, **sin tasas**), `congelar.py` (SHA-256 de resultados con hora), respaldos |
| `figuras/` | Guiones de figuras (PIL y SVG) y sus salidas |
| `reportes/` | Salidas de análisis en JSON. `congelado.json` guarda el hash y la hora de cada congelación |

## Reproducibilidad y disciplina de análisis

- **Preregistro** en `PREREGISTRO.md`: hipótesis, desenlace primario, exclusiones y las enmiendas
  fechadas en §8. Las desviaciones están declaradas ahí, incluida una en la que se miró el contraste
  confirmatorio antes de lo previsto: está anotada con su motivo y su corrección, no borrada.
- **Hashes de instrumento.** Cada corrida guarda `hash_textos` (el texto de la escena) y el hash del
  arnés. Las corridas con hashes distintos **no se juntan**: hay tres versiones de escena en
  `salidas/` y el análisis agrupa por hash. Ejemplo útil: el punto de precio 0 se corrió en dos
  versiones del instrumento y da el mismo valor en las dos, lo que sirve como nota de robustez pero
  **no** autoriza sumar las corridas.
- **Intervalos por remuestreo de corridas**, no de agentes: los seis agentes de una corrida comparten
  escena y no son observaciones independientes. Con menos de tres corridas en un brazo no se publica
  intervalo: el remuestreo de una sola corrida tiene varianza cero y produciría una precisión falsa.
- **Validación adversarial.** Antes de cada lote, `validador.py` corre sobre la escena resuelta: doce
  invariantes más una búsqueda de canarios que falla si el texto de la escena le sugiere al agente lo
  que debe hacer. `apendice-defectos.md` lista los defectos encontrados así, con cómo se detectó cada
  uno, qué sesgaba y cómo se verificó el arreglo.

## Uso dual

Este repositorio contiene un instrumento de medición, no una herramienta de ataque. La contención es
deliberada y está documentada: lista blanca de comandos, `subprocess` con `shell=False` y tokenización
con `shlex`, directorio de trabajo por agente, y todo el tráfico contra `localhost`. El confederado es
un guion del anfitrión, no un modelo persuadiendo a otro.

Siguiendo la regla del sprint, **no se publican recetas de instalación novedosas sin revisión**: los
apéndices describen las clases de conducta observadas y los agregados, no pasos accionables. El
apéndice de uso dual (`apendice-uso-dual-datos.md`) clasifica los rechazos y desmiente dos lecturas
alarmistas de los datos propios: los "intentos de túnel" son reintentos de cliente contra el puerto
propio del agente (cero externos), y el "intento de escape" de la mayoría es, en casi todos los casos,
un `find` sobre el sistema de archivos buscando el archivo de la propia tarea.

## Limitaciones que conviene leer con los resultados

- **Un solo modelo.** Todas las corridas usan el mismo modelo a través de una pasarela compatible con
  OpenAI. No hay variación entre familias de modelos; ese brazo quedó especificado
  (`plan-familias-mixtas.md`, rama `familias-mixtas`) y sin correr.
- **Contención por proceso, no por contenedor.** Directorios de trabajo separados y lista blanca de
  comandos, no Docker.
- **Los brazos exploratorios son exploratorios.** Solo el contraste preregistrado se lee como
  confirmatorio; el resto entra como descriptivo, con su n a la vista.
- **`resolver()` no generaliza.** La resolución de la asignación fija una correspondencia concreta, de
  modo que un brazo con una segunda tarea no es un cambio solo de escena: toca el camino de corrida.

## Datos

`salidas/` pesa varios gigabytes con las transcripciones completas. Los agregados que sostienen cada
cifra del reporte están en `reportes/`, y `reportes/congelado.json` fija el hash y la hora de cada uno,
para que cualquier número del texto se pueda rastrear hasta el archivo del que salió.
