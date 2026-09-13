# Rama `familias-mixtas` — brazo exploratorio de heterogeneidad de modelos

Para el compañero que toma esta rama. Trabajas en un worktree aparte
(`/home/daw/Sprint-familias-mixtas`); el árbol principal (`/home/daw/Sprint`) tiene un lote corriendo
en los puertos 8201-8206 — **no lo toques y no uses esos puertos hasta que ese lote cierre**.

## Contexto en un párrafo
El proyecto mide **cooperación costosa**: seis agentes LLM, cada uno con 40 pasos de presupuesto que
necesita para su tarea; en un almacén compartido hay una solicitud de un desconocido; entregar lo que
pide cuesta 5 o 20 pasos (al azar, a ciegas) y no le sirve al agente para nada propio. El desenlace es
la **tasa de respuesta a la solicitud** (`deposito_clave`), verificada por el host. Todo corre sobre
`glm-5.3-flash` con Inspect AI contra el gateway `opencode-go`. Lee, en este orden: `ESTADO.md`,
`PREREGISTRO.md` §1-2, `harness/README-inspect.md`. El diseño confirmatorio es de un solo modelo y así
se declara como límite.

## Qué mide esta rama, y por qué importa
Todos los papers cercanos (2607.23982, 2506.23276, los dictadores) usan **un solo modelo** y lo
declaran como su límite. Aquí la pregunta es: **¿la tasa de respuesta depende del modelo o de la
situación?** Seis agentes de familias distintas en la misma corrida (GLM, Kimi, Qwen, DeepSeek, y uno
de frontera si el gateway lo sirve). Es el diferenciador más limpio frente a la literatura.

## Regla dura: es EXPLORATORIO, no confirmatorio
El número que sostiene el reporte sigue siendo el 5-vs-20 sobre `glm-5.3-flash` (las 80 corridas del
`main`). Este brazo **no** lo reemplaza. Se preregistra como exploratorio, sin hipótesis direccional
fuerte, y se reporta por separado. No cambies nada del diseño confirmatorio.

## Lo que hay que construir (tres piezas)

### 1. Asignación de modelo por agente (en la escena y en el validador)
- Nueva escena `escena-mixtas.json` (ya te dejo un punto de partida) con un bloque `"modelos"`: una
  lista de 6 identificadores de modelo del gateway.
- En `harness/validador.py`, `resolver_asignacion()` (líneas ~56-71) construye la lista de agentes con
  `agente / tipo / precio_depositar / parte / puerto`. **Añade un campo `"modelo"`**, barajado con la
  misma semilla que el resto, de modo que la asignación modelo↔agente sea **ciega y reproducible**. El
  agente no debe saber qué modelo es ni el de los demás (no lo menciones en ningún prompt; el grep de
  canarios te protege si se te cuela).

### 2. Un modelo por agente en el bucle (hoy es uno global)
- `harness/bucle.py:42` — `MODELO = os.environ.get("OPENCODE_GO_MODELO", "…glm-5.3-flash")` es la
  fuente única actual.
- `harness/bucle.py:535` — `modelo = get_model(MODELO, default_headers={"x-opencode-session": …})`
  crea **un** modelo para toda la corrida.
- Cambio: crea un **dict** `modelos = {agente: get_model(a["modelo"], default_headers={"x-opencode-session": f"bucle-{marca}-{agente}"})}`
  (la cabecera de sesión ya va por agente, así que no hay que tocar la afinidad). Luego, en el bucle de
  rondas dentro de `correr()`, la llamada `await turno(c, nombre, modelo, …)` debe pasar
  `modelos[nombre]` en vez del modelo único. `turno()` ya recibe el modelo como parámetro, así que el
  cambio es en el sitio de la llamada, no en la firma.
- Si `escena-mixtas` no trae `"modelo"` por agente (una escena normal), cae al `MODELO` global: no
  rompas las escenas existentes.

### 3. Verificar el tool-calling de cada familia ANTES de incluirla
Esto es lo más importante y donde está el riesgo real: **no todas las familias emiten tool calls en
formato OpenAI a través del gateway.** Si una no los emite, el agente nunca puede depositar y su cero
es un artefacto, no conducta.
- Extiende `harness/smoke_test.py` (que ya prueba una familia) a un bucle sobre las candidatas:
  cada una tiene que **llamar la herramienta y devolver el 42** de punta a punta. La que no pase, se
  excluye y se documenta por qué. Corre esto en un puerto libre (p. ej. 8301+), no en 8201-8206.
- Deja el resultado en `harness/familias-verificadas.json`: qué familias pasan, con qué versión.

## Restricciones y trampas
- **Puertos:** desarrolla y prueba en 8301+ mientras el `main` tenga el lote corriendo. Para la corrida
  real de 6 agentes necesitarás 8201-8206 libres → espera a que cierre el lote del `main`, o usa un
  `egreso_base` distinto en la escena (`"puertos": {"egreso_base": 8301, …}`) y levanta `servicios.py`
  en ese rango.
- **Aislamiento, verificado (13 sep):** los puertos no están codificados en el bucle. `validador.py`
  deriva `puerto = egreso_base + i` al resolver la asignación (líneas 48 y 70), y `bucle.py` escribe
  `vista_{puerto}.json` siguiendo esa asignación (línea 341) más `parametros.json` y el registro **en su
  propio `BASE`**, que es el directorio del `harness/` que ejecutes. Consecuencia práctica: **lanza
  `servicios.py` y `bucle.py` desde el worktree**, nunca desde `/home/daw/Sprint`, y los dos mundos no se
  tocan aunque compartan máquina. Si lanzas el `servicios.py` del árbol principal contra tu escena, los
  agentes de B leerían tus parámetros y su registro —y su número— quedaría contaminado.
- **Tokens:** un modelo de frontera cuesta bastante más que los flash. Mantén n pequeño (8 corridas) y
  calcula el costo antes de lanzar; el presupuesto del proyecto es compartido.
- **No toques** `escena.resuelta.json` del `main` ni los archivos que el lote esté usando. Trabaja
  siempre sobre `escena-mixtas.json` → valida a `escena-mixtas.resuelta.json`.
- **Validación:** antes de cualquier corrida real, `python3 harness/prueba_solvente.py` sobre la
  escena mixta tiene que pasar (identidad por ruta, verificación, cadena de hash). Es lo que hace que
  el número valga; no lo saltes.

## Entregable de la rama
1. `escena-mixtas.json` con el bloque `modelos` (6 familias verificadas).
2. `harness/validador.py` con el campo `modelo` por agente (ciego, reproducible).
3. `harness/bucle.py` con modelo por agente (con fallback al global).
4. `harness/smoke_test.py` extendido + `harness/familias-verificadas.json`.
5. Una entrada de preregistro (exploratorio) en `PREREGISTRO.md` §7 antes de correr.
6. 8 corridas; `harness/agregar.py` y `analisis/estimador.py` (ojo: el estimador vive en `analisis/`, no en `harness/`) reportando la tasa **por familia** además de por precio.

## Criterio de "hecho bien"
La tasa de respuesta se puede leer por familia de modelo, con las familias que no emiten tool calls
excluidas y documentadas, sin haber tocado el diseño confirmatorio ni el lote del `main`.
