# Handoff — AI Incident Response Sprint (Apart/CeSIA, 11–13 sep 2026)

Este paquete traslada dos cosas distintas: **(A)** el material de trabajo del sprint y **(B)** el estado de Hermes que lo produjo. Se migran por vías separadas.

---

## A. Material de trabajo (lo que un compañero necesita)

```
entrega/
├── README-MIGRACION.md          este archivo
├── jurado/                      panel adversarial completo
│   ├── EXPEDIENTE.md            hechos verificados del caso, con fuente y nº de línea
│   ├── PORTAFOLIO.md            las 9 candidatas descritas en neutro + encargo de propuestas propias
│   ├── BRIEF_JUEZ.md            reglas del panel, anti-eco, formato JSON de salida
│   ├── AGREGADO.md              agregación del panel (tabla, consensos, disensos, refutaciones)
│   ├── veredictos/              6 veredictos crudos, sin editar (uno por modelo y rol)
│   ├── run_jurado.sh            lanza 1 juez (proceso Hermes headless con modelo fijado)
│   ├── run_all.sh               despacha el panel en dos oleadas, con reintento
│   ├── aggregate.py             lee los veredictos y tabula; no reinterpreta
│   └── logs/                    stdout crudo de cada corrida
├── fuentes/                     textos completos en caché que el expediente cita por línea
│   ├── metr.org-*.md            informe independiente METR/Redwood (2.109 líneas)
│   ├── huggingface.co-*.md      timeline forense de HF (1.417 líneas)
│   ├── collusion.wiki-*.md      informe del incidente de la wiki alemana
│   ├── apartresearch.com-*.md   página del sprint, con el payload de las pestañas
│   ├── aisafetycolombia.org-*.md hub de Bogotá + guía de participación en línea
│   └── arxiv.org-*.md           Agent Flight Recorder (prior art de logs a prueba de manipulación)
└── sesion/                      export de la sesión de trabajo en Markdown (legible)
```

**Importante:** los números de línea del EXPEDIENTE solo significan algo junto a los archivos de `fuentes/`. Van juntos o no van.

**Advertencia de rutas:** `run_jurado.sh`, `run_all.sh` y el BRIEF llevan rutas absolutas `/home/daw/Sprint/jurado`. En otra máquina hay que conservar esa ruta o reemplazarla:
`sed -i 's|/home/daw/Sprint/jurado|/RUTA/NUEVA/jurado|g' run_jurado.sh run_all.sh BRIEF_JUEZ.md aggregate.py`

**Requisitos para correr el panel en otra máquina:**
1. Hermes instalado (`curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash`), mismo major/minor a ser posible.
2. Credenciales de proveedor propias: `hermes setup` y `hermes model`. El panel usa el gateway `opencode-go` con seis familias (glm-5.3, glm-5.3-flash, qwen3.8-max, kimi-k3, deepseek-v4-pro, deepseek-v4.1-flash). La suscripción con la que se corrió aquí es de una sola persona: sin su propia llave, el panel no corre. `hermes doctor` verifica.
3. Ajustar la lista de modelos en `run_all.sh` si el catálogo disponible difiere.

**Verificación del corpus de la wiki (opcional, no incluido por tamaño):** se re-descarga y se verifica contra las sumas publicadas.
```
curl -sL -O https://collusion.wiki/explorer/download/events.jsonl.gz
sha256sum events.jsonl.gz     # comparar con SHA256SUMS del mismo directorio del sitio
gunzip -c events.jsonl.gz | wc -l    # esperado: 19913
```

---

## B. Estado de Hermes (lo aprendido), por vía separada

Lo aprendido vive en tres sitios, con tamaños reales medidos:

| Qué | Ruta | Tamaño | Cómo se migra |
|---|---|---|---|
| Skills (procedimientos) | `~/.hermes/skills/` | 12 MB | `hermes sync push` / `hermes sync propose <skill>` (equipo) o copia directa |
| Memoria (quién es el usuario, notas) | `~/.hermes/memories/MEMORY.md`, `USER.md` | 8 KB | copia directa; revisar antes, tiene datos personales del dueño |
| Sesiones (incluida esta) | `~/.hermes/state.db` + `~/.hermes/sessions/` | 96 MB + 15 MB | `hermes backup` → `hermes import` |
| Configuración | `~/.hermes/config.yaml` | 6 KB | incluida en el backup; el destino puede preferir `hermes setup` |
| Cron, auth, kanban, MCP | `~/.hermes/{cron,auth.json,kanban.db,mcp-tokens}` | pequeño | incluidos en el backup |

```
# en la máquina origen
hermes backup -o ~/sprint-hermes-backup.zip        # todo: config, skills, sesiones, datos
hermes sessions export --format md --session-id <ID>   # transcripción legible de la sesión

# en la máquina destino
hermes import ~/sprint-hermes-backup.zip
hermes doctor
```

### El backup contiene secretos. Léelo antes de moverlo.

El zip incluye `.env` (llaves de API) y `auth.json` (tokens OAuth). Medidas:

- **No** subirlo a un repositorio, ni a la nube compartida, ni a un chat del equipo.
- Si el destino es **otra persona**: entregar solo `skills/`, `memories/` y el material de trabajo, y que esa persona corra su propia configuración con `hermes setup`. Para mostrar el estado sin filtrar credenciales existe `hermes dump` (redactado por defecto; `--show-keys` muestra solo prefijos).
- Si el destino es **tú en otro equipo**: borra del zip `.env` y `auth.json` y vuelve a ejecutar `hermes setup` allí, o al menos rota las llaves después de importar.
- La memoria (`USER.md`, `MEMORY.md`) describe a una persona concreta. Si el destino es un equipo, decide si eso es contexto útil o ruido.

### Para que esta sesión se pueda **retomar** (no solo leer)

Retomar requiere que la sesión exista en el almacén del destino. Eso lo resuelve `hermes backup` + `hermes import` (arrastra `state.db`). El export en Markdown sirve para **leerla**, no para continuarla:
```
hermes --resume 20260911_123046_32491f      # el ID de esta sesión
hermes --continue                            # la más reciente
```

### Nota sobre alcance

Esta sesión también dejó registradas las **7 sub-sesiones del panel** (una por juez, workspace `jurado`), visibles con `hermes sessions list`. Son parte del rastro de auditoría: muestran qué leyó cada juez y con qué modelo se produjo cada veredicto.
