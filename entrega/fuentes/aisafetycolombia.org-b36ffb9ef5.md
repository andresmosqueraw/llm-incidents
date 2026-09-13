![](https://aisafetycolombia.org/aisc/patterns/aisc-hero-hackathon.svg)

[![AI Safety Colombia](https://aisafetycolombia.org/aisc/logo-lockup-crema.png)](https://aisafetycolombia.org/)

Idioma

[Español](https://aisafetycolombia.org/)
[English](https://aisafetycolombia.org/en)
[Português](https://aisafetycolombia.org/pt)

Guía para participar en línea
=============================

AI Incident Response Sprint, del viernes 11 al domingo 13 de septiembre, desde donde estés.

AI Safety Colombia · para quienes participan fuera del hub de Bogotá

**Qué bueno que te unas al sprint.** Esta guía es para quien participa en línea: qué hay que hacer antes del viernes, qué pasa cada día, cómo armar equipo, qué charlas y qué mentorías puedes seguir desde donde estés, y cómo enviar el proyecto.

El sprint es un evento en línea de Apart Research. Nosotros, el hub de Bogotá, somos una de las sedes presenciales, y además abrimos parte de nuestro programa para quien participa desde fuera: las charlas en español y varios bloques de mentoría.

Te recomendamos guardar esta página, porque la iremos actualizando durante la semana.

**Grupo de WhatsApp de la comunidad:** [entrar al grupo](https://chat.whatsapp.com/KwE8cciX48TAVhAOHnrLaZ)
. Es por donde se arma equipo con otra gente en Colombia y por donde mandamos los enlaces de las sesiones.

Información clave
-----------------

| Tema | Detalle |
| --- | --- |
| Fechas | Del viernes 11 al domingo 13 de septiembre de 2026 |
| Formato | Completamente en línea. Las charlas, la coordinación y la entrega pasan por la página del sprint, el Discord de Apart y Zoom |
| Costo | Participar es completamente gratuito |
| Registro | Te registras tú mismo en [la página del sprint de Apart](https://apartresearch.com/sprints/ai-incident-response-sprint-2026-09-11-to-2026-09-13?utm_source=aisafetycolombia)<br> y entras al [Discord](https://discord.gg/XswWBvugYs) |
| Antes del evento | Solo necesitas revisar [las dos lecturas de preparación](https://aisafetycolombia.org/sprint/guia-en-linea#estudio)<br>, que toman alrededor de una hora |
| Entrega del proyecto | domingo 13 de septiembre, 11:59 p. m. AoE, o sea las **6:59 a. m. del lunes 14** en Colombia |
| Equipos | Recomendamos equipos de 3 a 5 personas. Puedes armar el tuyo en el grupo de WhatsApp de la comunidad o en los canales de Discord de Apart |
| Ritmo | Trabajas a tu propio ritmo: no hay asistencia obligatoria y la única hora fija es la de la entrega |
| Idiomas | Las charlas del hub son en español y las de Apart, en inglés. El reporte final va en inglés |

Cómo participar en línea
------------------------

Son cuatro pasos y ninguno toma más de unos minutos.

*   ·**Regístrate en el sprint.** El botón _Sign Up_ de [la página de Apart](https://apartresearch.com/sprints/ai-incident-response-sprint-2026-09-11-to-2026-09-13?utm_source=aisafetycolombia)
    . Es gratis y es el registro que te habilita para entregar.
*   ·**Entra al [Discord del sprint](https://discord.gg/XswWBvugYs)
    .** Ahí pasan las charlas, la mesa de ayuda y los canales para formar equipo. Apart lo dice claro: todo el evento ocurre por Discord y Zoom.
*   ·**Entra al [grupo de WhatsApp de la comunidad](https://chat.whatsapp.com/KwE8cciX48TAVhAOHnrLaZ)
    .** Es el canal en español: por ahí se arma equipo con otra gente del país y por ahí mandamos los enlaces de las sesiones del hub.
*   ·**Revisa las dos lecturas de preparación.** Alrededor de una hora en total y están [aquí mismo](https://aisafetycolombia.org/sprint/guia-en-linea#estudio)
    .

Materiales de preparación
-------------------------

Para llegar preparado no necesitas hacer ningún curso. Solo te proponemos **dos lecturas, alrededor de una hora en total**, para que el viernes todos partamos de un contexto común sobre el incidente. Son las mismas para todo el mundo: la primera explica **qué pasó**, con fechas, fases y comandos, y la segunda, **qué nos dice el incidente sobre el comportamiento de los agentes**. Las dos están en inglés y son las que Apart pone primero en su lista de recursos.

Lectura 1~40 min

#### [Anatomy of a Frontier Lab Agent Intrusion](https://huggingface.co/blog/agent-intrusion-technical-timeline)

Hugging Face · publicado el 27 de julio

La reconstrucción forense del incidente, día por día, entre el 9 y el 13 de julio: las nueve fases del ataque, las vulnerabilidades involucradas, los comandos ejecutados y un visor interactivo de cerca de 17.600 acciones del agente. Es el punto de partida de prácticamente todos los frentes.

Lectura 2~20 min

#### [Core takeaways about this incident](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/#core-takeaways-about-this-incident)

METR · solo la sección _Core takeaways about this incident_

La investigación independiente que OpenAI encargó después del incidente. No hace falta leer las 91 páginas: esta sección reúne algunos de los hallazgos más importantes para entender el comportamiento de los agentes durante el incidente, entre ellos que casi nunca consideraron avisarle a una persona lo que estaban haciendo.

### Lecturas por frente

Las lecturas de esta sección son opcionales antes del viernes y están pensadas para cuando ya tengas una idea del frente en el que quieres trabajar. No necesitas revisarlas todas y **no reemplazan las dos lecturas de arriba**. Los equipos se arman en el grupo de WhatsApp y en los canales de Discord, y cada equipo escoge su frente. Cada frente está explicado [más abajo](https://aisafetycolombia.org/sprint/guia-en-linea#frentes)
, y cuando recomendamos una parte del informe de METR el enlace va directo a esa sección.

1\. Estándares de contención+

*   ·**METR, [Hacking the customer deployed Modal sandbox and Artifactory](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/#hacking-the-customer-deployed-modal-sandbox-and-artifactory)
    .** El segundo salto: el agente pasa de la infraestructura del laboratorio a la de un cliente. Útil para pensar dónde empiezan y terminan las responsabilidades de contención.
*   ·**METR, [Efforts to conceal actions and tamper with transcripts](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/#efforts-to-conceal-actions-and-tamper-with-transcripts)
    .** Análisis forense cuando el propio sistema puede alterar la evidencia.
*   ·**[Elastic Security Labs](https://www.elastic.co/security-labs/ai-agent-attack-detection-hugging-face-breach)
    .** La cadena de ataque vista desde la detección: varias señales llegaron a correlacionarse y ninguna escaló a una alerta.
*   ·**[AI Controls Matrix](https://cloudsecurityalliance.org/artifacts/ai-controls-matrix)
    , de Cloud Security Alliance.** El control **AIS-13**, sobre aislamiento de agentes. Se actualiza seguido, así que vale confirmar en esa página cuál es la versión vigente.

2\. Análisis del incidente+

*   ·**METR, [Investigation process and limitations](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/#investigation-process-and-limitations)
     y [Appendix: Methodology](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/#appendix-methodology)
    .** Qué chequeos podría repetir otra persona de forma independiente.
*   ·**METR, colaboración entre agentes:** [Collaboration on the message board](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/#collaboration-on-the-message-board)
    , [Coordination norms and technologies](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/#coordination-norms-and-technologies)
     y [Large collective projects](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/#large-collective-projects)
    . Cómo se coordinaron los agentes entre sí, con un detalle que no aparece en ningún otro recurso del sprint.
*   ·**UK AI Security Institute, [Cheating behaviour in frontier model evaluations](https://www.aisi.gov.uk/blog/cheating-behaviour-in-frontier-model-evaluations)
    .** Cinco modelos, 475 corridas cada uno, y todos hicieron trampa al menos una vez. Apart lo señala como el documento secundario más importante de todo el sprint.
*   ·**METR, [Investigating AI propensities after incidents](https://metr.org/blog/2026-07-28-investigating-ai-propensities-after-incidents/)
    ** (28 de julio). Es otro texto, no el informe: protocolos de investigación posteriores a un incidente.

3\. Respuesta regulatoria+

*   ·**METR, [Scope of this investigation](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/#scope-of-this-investigation)
     y [Appendix: Timeline of investigation](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/#appendix-timeline-of-investigation)
    .** Cuánto costó conseguir acceso independiente y qué quedó fuera del alcance.
*   ·**METR, [Agents did not attempt to notify humans](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/#agents-did-not-attempt-to-notify-humans-and-very-rarely-even-reasoned-about-doing-this)
    .** Insumo para pensar deberes de reporte y escalamiento.
*   ·**[Plantilla de la Comisión Europea para incidentes graves](https://digital-strategy.ec.europa.eu/en/library/ai-act-commission-publishes-reporting-template-serious-incidents-involving-general-purpose-ai)
     de IA de propósito general y [portal de reporte de Cal OES](https://www.caloes.ca.gov/office-of-the-director/operations/homeland-security/california-cybersecurity-integration-center/transparency-in-frontier-ai-act-reporting/)
    .** Dos instrumentos de reporte que ya existen y que nadie ha ejercido en público contra este incidente.

4\. Estrategia de comunicación+

Aquí el objeto de estudio es **cómo fue contado** el incidente. Toda afirmación va anclada al registro público: fechas, citas y fuentes identificables.

*   ·**[OpenAI, sobre el incidente](https://openai.com/index/hugging-face-model-evaluation-security-incident/)
    ** (21 de julio, ~15 min) y **[Anthropic, sobre tres incidentes reales](https://www.anthropic.com/news/investigating-incidents-cybersecurity-evals)
    ** (30 de julio, ~20 min). Dos laboratorios contaron episodios parecidos con once días de diferencia y los encuadraron de maneras muy distintas.
*   ·**METR, [We heavily delegated our analysis to often unreliable AI agents](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/#we-heavily-delegated-our-analysis-to-often-unreliable-ai-agents)
    .** Las limitaciones del propio proceso de investigación, que es justo lo que un periodista va a citar en contra.
*   ·**[Material preparado por CeSIA para prensa](https://cesia.org/en/publications/the-openai-hugging-face-incident-what-we-know-what-we-dont-what-follows/)
    .** Referencia de formato para decir qué se sabe, qué no y qué queda abierto.
*   ·Una advertencia de Apart: si tu proyecto implica hablar con periodistas, creadores o gente de política pública, la precisión va antes que cualquier titular atractivo.

5\. Track abierto+

No tiene una ruta dentro del informe de METR. Apart propone varias direcciones que parten de otros recursos.

*   ·**El dilema del defensor.** Durante la intrusión, varios modelos de frontera rechazaron peticiones forenses de los responders de Hugging Face, que terminaron usando un modelo abierto en su propia infraestructura. Está descrito en la primera lectura.
*   ·**[Defensive Refusal Bias](https://labs.scale.com/papers/defensive-refusal-bias)
    .** El vocabulario de seguridad se rechaza con más frecuencia, y explicitar que hay autorización no reduce el rechazo.
*   ·**Contaminación de benchmarks.** Los conjuntos de datos a los que llegó el agente apuntan a [ExploitGym](https://github.com/sunblaze-ucb/exploitgym)
     y [CyberGym](https://github.com/sunblaze-ucb/cybergym)
    . Si sus respuestas quedaron expuestas, ¿qué pasa con todo resultado posterior?

La lista completa de recursos está en la pestaña _Resources_ de [la página del sprint](https://apartresearch.com/sprints/ai-incident-response-sprint-2026-09-11-to-2026-09-13?utm_source=aisafetycolombia)
, pero **no hace falta revisarla toda**. Si puedes, llega el viernes sabiendo cuál de los cinco frentes te interesa más; no necesitas traer una propuesta definida.

Agenda del fin de semana
------------------------

No hay una hora a la que tengas que estar conectado. Apart lo dice así: trabajas a tu propio ritmo, las charlas son opcionales y el único plazo fijo es el de la entrega, el **lunes 14 de septiembre, 6:59 a. m. hora de Colombia**.

Aun así, el fin de semana rinde mucho más si te pones un horario y lo cumples con tu equipo. La forma más simple es tomar los bloques que ya están agendados, los de abajo, como puntos fijos del día y trabajar alrededor de ellos.

### Charlas de Apart

Apart organizó nueve charlas en línea, en inglés, abiertas para todo el mundo. Abajo encuentras los horarios en hora de Bogotá.

**Las charlas son opcionales y cada una tiene su propia inscripción.** Puedes inscribirte en las que más te interesen.

| Cuándo (Bogotá) | Ponente | Tema | Inscripción |
| --- | --- | --- | --- |
| Jueves, 9:15 a. m. | [Justin Shenk](https://www.justinshenk.com/)<br>Investigador independiente en seguridad de IA, Berlín | «HackTalk: Justin Shenk» | [Inscribirse](https://luma.com/ai-incident-response-sprint-justin-shenk) |
| Viernes, 8:15 a. m. | [Henry Papadatos](https://www.safer-ai.org/about/henry-papadatos)<br>Director ejecutivo de SaferAI | «An analysis of the Hugging Face breach, then what SaferAI proposes to do about the next one» | [Inscribirse](https://luma.com/ai-incident-response-sprint-henry-papadatos) |
| Viernes, 9:15 a. m. | [Boyd Kane](https://www.linkedin.com/in/boydrkane/)<br>Investigador en seguridad técnica de IA, MATS 9 Extension | «Uncovering public traces of the OpenAI Huggingface incident» | [Inscribirse](https://luma.com/ai-incident-response-sprint-boyd-kane) |
| Viernes, 12:00 m. | [Isaak Mengesha](https://www.isaakmengesha.com/)<br>Posdoctorado en la Oxford Martin School | «Incident Response Has a Measurement Problem» | [Inscribirse](https://luma.com/ai-incident-response-sprint-isaak-mengesha) |
| Viernes, 1:00 p. m. | [Stephen Casper](https://www.hks.harvard.edu/faculty/stephen-casper)<br>Profesor asistente de política pública, Harvard Kennedy School | «Predicting the first major AI-enabled terrorism incident: A pre-mortem and 9 predictions» | [Inscribirse](https://luma.com/ai-incident-response-sprint-stephen-casper) |
| Viernes, 2:00 p. m. | [David Krueger](https://davidscottkrueger.com/)<br>CEO de Evitable y profesor asistente en la Universidad de Montreal | «HackTalk: David Krueger» | [Inscribirse](https://luma.com/ai-incident-response-sprint-david-krueger) |
| Viernes, 4:15 p. m. | [Alex Mallen](https://www.linkedin.com/in/alex-mallen-815b01176/)<br>Equipo técnico de Redwood Research | «How near-term AI swarms could cause labs to lose control of AI development, absent improved defenses» | [Inscribirse](https://luma.com/ai-incident-response-sprint-alex-mallen) |
| Viernes, 7:15 p. m. | [Tim Hua](https://timhua.me/)<br>Equipo técnico de METR | «HackTalk: Tim Hua» | [Inscribirse](https://luma.com/ai-incident-response-sprint-tim-hua) |
| Domingo, 11:15 a. m. | [Marko Grobelnik](https://ailab.ijs.si/marko_grobelnik/)<br>Investigador del Instituto Jožef Stefan | «HackTalk: Marko Grobelnik» | [Inscribirse](https://luma.com/ai-incident-response-sprint-marko-grobelnik) |

### Charlas del hub

El hub de Bogotá organiza además sus propias charlas, **en español**, de unos 30 minutos cada una. Acá están las que se dan en línea, que son las que puedes seguir desde donde estés. Las que ese fin de semana ocurren solo en la sala no aparecen en esta tabla.

| Cuándo | Ponente | Charla | Enlace |
| --- | --- | --- | --- |
| Sábado, 10:00 a. m. | [Roberto García Alonso](https://www.linkedin.com/in/roberto-garcia-alonso/) | «Gobernar la inteligencia artificial: del principio ético a la responsabilidad jurídica» | [Inscribirse](https://luma.com/w6c6i9b4) |
| Sábado, 12:30 p. m. | [María Lorena Flórez](https://www.linkedin.com/in/maria-lorena-florez-rojas/) | «Del principio a la práctica: cómo operacionalizar la rendición de cuentas de la IA» | [Inscribirse](https://luma.com/8lqrcnmx) |
| Sábado, 2:00 p. m. | [Christian Urcuqui](https://www.linkedin.com/in/christianurcuqui/) | «Hackeando agentes de IA» | [Inscribirse](https://luma.com/60o0v4o1) |
| Sábado, 2:30 p. m. | [Luis Cosio](https://www.linkedin.com/in/luiscosio/) | «SL5: ¿Cómo proteger los modelos de inteligencia artificial contra los ataques más sofisticados?» | [Inscribirse](https://luma.com/8u5ymrfe) |
| Sábado, 3:00 p. m. | [Manuela Chacón](https://www.linkedin.com/in/manuela-viviana-chac%C3%B3n-chamorro-04b0621bb/) | «Resiliencia cooperativa para sistemas multiagente» | [Inscribirse](https://luma.com/vb88ho9c) |
| Domingo, 2:00 p. m. | [Luis Montoya](https://www.linkedin.com/in/luismmontoya/) | [«En camino a detectar y entender la Evaluation Awareness no verbalizada»](https://openreview.net/forum?id=zGmgeR0f4D) | [Inscribirse](https://luma.com/c36amemk) |

Cada charla tiene su enlace de inscripción en la última columna, y ahí está toda la información de la sesión. **Inscríbete en las que te interesen** y mantente pendiente de la hora: conectarte a tiempo corre por tu cuenta.

### Mentoría

Varios mentores del hub atienden en línea, así que puedes aprovecharlos aunque no estés en Bogotá. Estos son sus bloques.

| Cuándo | Mentor | Experiencia | Enlace |
| --- | --- | --- | --- |
| Sábado: de 8:00 a 11:00 a. m.Domingo: de 9:00 a 11:00 a. m. | [Luis Montoya](https://www.linkedin.com/in/luismmontoya/) | Interpretabilidad y evaluación de modelos: cómo detectar que un modelo se comporta distinto cuando sabe que lo observan | [Entrar al Meet](https://meet.google.com/rep-xvzi-ypi) |
| Sábado: 2:30 p. m. | [Christian Urcuqui](https://www.linkedin.com/in/christianurcuqui/) | Ciberseguridad ofensiva en sistemas con LLM: inyección indirecta de prompts y ataques a agentes | [Entrar al Meet](https://meet.google.com/oed-tkvj-rfx) |
| Sábado: 3:00 p. m. | [Luis Cosio](https://www.linkedin.com/in/luiscosio/) | Seguridad de infraestructura y centros de datos frente a adversarios con muchos recursos | [Entrar al Meet](https://meet.google.com/obt-kism-dwa) |
| Domingo: de 12:00 m. a 2:00 p. m. | [Diego Gómez](https://www.linkedin.com/in/diegoalejogm/) | Interpretabilidad y modelos multimodales para moderación de contenido: leer las activaciones de un modelo para detectar cuándo cambia de carácter | [Entrar al Meet](https://meet.google.com/jsv-kzvi-qnt) |

También puedes acudir a la red internacional de mentores del sprint en el [Discord de Apart](https://discord.gg/XswWBvugYs)
, sobre todo para preguntas que se salgan de las áreas de los mentores del hub.

Los cinco frentes
-----------------

El sprint parte de un incidente concreto: en julio, agentes de OpenAI terminaron interactuando con infraestructura de producción de Hugging Face.

A partir de ese caso puedes trabajar en cualquiera de los cinco frentes. **Todos tienen el mismo peso** y no hay una lista cerrada de retos: cada equipo formula su propia pregunta o proyecto.

| Frente | De qué trata | Se juzga por |
| --- | --- | --- |
| 1\. Estándares de contención | Reglas verificables para evitar que un agente llegue a tocar producción. | ¿Un tercero podría verificar el cumplimiento sin acceso a la red del laboratorio? ¿Un laboratorio realmente podría adoptarlo? |
| 2\. Análisis del incidente | Reconstruir qué ocurrió en julio y qué controles podrían haberlo detectado antes. | Preguntas que puedan resolverse, chequeos que alguien pueda ejecutar y explicaciones causales que permitan hacer predicciones. |
| 3\. Respuesta regulatoria | Diseñar un instrumento normativo que un regulador o legislador pueda utilizar. | Exactitud legal y especificidad: ¿podría una institución utilizarlo con modificaciones menores? |
| 4\. Estrategia de comunicación | Explicar un incidente de este tipo a públicos no técnicos sin exagerarlo ni minimizarlo. | Anclaje en evidencia concreta y alguna prueba de alcance, como un playtest, la lectura de un periodista o la respuesta de un creador. |
| 5\. Track abierto | Cualquier otro ángulo del incidente que tu equipo quiera explorar. | Un artefacto útil, claridad sobre sus límites y una explicación de qué permitiría hacer un mes adicional de trabajo. |

### Equipos

Recomendamos trabajar en equipos de **3 a 5 personas**, aunque también puedes entregar solo. El máximo que recomienda Apart es de cinco integrantes.

**¿No tienes equipo? No pasa nada.** Quien participa en línea arma equipo con otra gente que también está en línea, y para eso hay dos puertas: el [grupo de WhatsApp de la comunidad](https://chat.whatsapp.com/KwE8cciX48TAVhAOHnrLaZ)
, que es donde se junta la gente en Colombia, y los canales de formación de equipos del [Discord de Apart](https://discord.gg/XswWBvugYs)
, donde está todo el mundo.

Preséntate con dos líneas: qué sabes hacer y qué frente te llama. Es lo que más rápido hace que alguien te escriba.

Cómo enviar tu proyecto
-----------------------

La entrega final es un **reporte tipo mini-paper en PDF**, con la plantilla oficial de Apart y subido a la página del sprint. El registro de tu equipo en la plataforma lo hace tu propio equipo.

No necesitas programar para participar. Los proyectos de regulación, comunicación u otros frentes pueden entregar análisis, marcos, propuestas o herramientas sin código.

El reporte puede tener un máximo de **8 páginas**, sin contar referencias ni apéndices. Como referencia, muchos buenos proyectos quedan entre 4 y 8 páginas.

*   ·El artefacto del proyecto, por ejemplo un banco de pruebas, un detector, una matriz de control, un instrumento regulatorio o un kit de simulacro, puede ir en un repositorio enlazado o como apéndice.
*   ·Un repositorio público y un video de 3 a 5 minutos son opcionales.
*   ·Debes incluir una sección de **limitaciones y consideraciones de doble uso**: qué no demuestra tu trabajo, qué riesgos tiene y de qué maneras podría utilizarse indebidamente.
*   ·Antes del envío, ten a la mano los nombres, correos y usuarios de Discord de todo el equipo, además del título, el resumen y el PDF.

### El plazo

**El envío cierra el lunes 14 de septiembre, 6:59 a. m. hora de Colombia.**

Apart lo anuncia como «domingo 13 de septiembre, 11:59 p. m. AoE». AoE (_Anywhere on Earth_) es la zona horaria más permisiva, así que en Colombia el plazo termina el lunes temprano.

Aun así, te recomendamos subir una primera versión el domingo en la tarde, incluso si todavía estás haciendo ajustes. Puedes reemplazarla mientras el plazo siga abierto, y así reduces el riesgo de quedarte sin entregar por un problema de último minuto.

### Estructura sugerida del reporte

| Sección | Qué va ahí |
| --- | --- |
| Resumen | Qué construiste y qué encontraste, en un párrafo. |
| Problema | Qué parte del incidente estás abordando y por qué importa. |
| Qué construimos | Descripción del artefacto de forma que otra persona pueda entenderlo y utilizarlo. |
| Cómo lo probamos | Método, datos y qué mediste realmente. |
| Hallazgo principal | Una afirmación principal y la evidencia que la respalda. |
| Limitaciones y doble uso | Obligatorio. Qué no establece tu trabajo, cuáles son sus límites y cómo podría utilizarse mal. |
| Qué sigue | Qué harías si tuvieras un mes adicional para continuar. |
| Referencias y apéndices | No cuentan para el límite de páginas. |

### Cómo se evalúa

Todos los proyectos se califican con la misma rúbrica y compiten entre sí, sin importar el frente ni desde dónde se trabajó. El frente entra por su criterio propio, el de la tabla de los cinco frentes.

Los requisitos completos y la plantilla están en la pestaña _Guidelines_ de [la página del sprint](https://apartresearch.com/sprints/ai-incident-response-sprint-2026-09-11-to-2026-09-13?utm_source=aisafetycolombia)
.

**Todas las entregas reciben comentarios escritos**, no solo los proyectos ganadores.

Premios
-------

Apart reparte **USD 2.000** entre cinco puestos, mirando conjuntamente los proyectos de todos los frentes, hubs y participantes remotos. **Compites en igualdad de condiciones** con quienes están en una sede presencial.

El jurado evalúa los proyectos durante la semana siguiente al evento y los resultados se anuncian unas semanas después. Cada equipo nomina a una persona para recibir el premio, que después lo reparte internamente.

| Puesto | Premio |
| --- | --- |
| 1.er puesto | USD 1.000 |
| 2.º puesto | USD 500 |
| 3.er puesto | USD 300 |
| 4.º puesto | USD 100 |
| 5.º puesto | USD 100 |

### Oportunidades después del sprint

Algunos proyectos podrán seguir desarrollándose después del fin de semana:

*   ·Los equipos más fuertes reciben una invitación para postular a la beca de investigación de Apart, que dura entre tres y seis meses e incluye mentoría y apoyo para publicar.
*   ·CeSIA comparte el mejor trabajo del frente regulatorio con sus contactos en la Oficina de IA de la Unión Europea, dando crédito al equipo.
*   ·Los trabajos que puedan hacerse públicos se publican con licencia abierta y en un mismo lugar, para que puedan consultarse y citarse después del sprint.

Convivencia y código de conducta
--------------------------------

Queremos que el sprint sea un espacio respetuoso, colaborativo y agradable para todas las personas, también en los canales en línea. Al participar aceptas el [código de conducta de Apart Research](https://apartresearch.com/code-of-conduct)
 y algunos acuerdos básicos de convivencia:

*   ·Trata a todas las personas con respeto.
*   ·Respeta los límites de los demás. Si alguien te pide que pares algo, hazlo de inmediato.
*   ·Respeta la confidencialidad del trabajo de los otros equipos hasta que decidan hacerlo público.

No están permitidos:

*   ·Comentarios o acciones ofensivas o discriminatorias.
*   ·Conductas que interrumpan de manera persistente el trabajo de los demás.
*   ·Llegar o permanecer en el espacio en estado de embriaguez.
*   ·Intimidación o amenazas.
*   ·Acoso sexual de cualquier tipo, incluida la atención sexual no deseada o el contacto físico inapropiado.

Si alguna situación te incomoda, escríbenos por privado a [\[email protected\]](https://aisafetycolombia.org/cdn-cgi/l/email-protection#86e5e9e8f2e7e5f2e9c6e7eff5e7e0e3f2ffe5e9eae9ebe4efe7a8e9f4e1)
 o usa la mesa de ayuda del Discord de Apart. Revisamos cualquier situación con discreción y tomamos las medidas que sean necesarias para cuidar a las personas.

Y recuerda que **el sprint está pensado para combinar perfiles distintos**. Muchas de las personas que participan no vienen de machine learning, y justamente esa diversidad de perspectivas es parte del valor del evento.

Contactos y enlaces
-------------------

Para cualquier cosa del hub, el canal es [el grupo de WhatsApp de la comunidad](https://chat.whatsapp.com/KwE8cciX48TAVhAOHnrLaZ)
. Si prefieres tratar algo en privado, escribe a [\[email protected\]](https://aisafetycolombia.org/cdn-cgi/l/email-protection#a3c0cccdd7c2c0d7cce3c2cad0c2c5c6d7dac0cccfcccec1cac28dccd1c4)
.

Para preguntas sobre la entrega, la plantilla o la plataforma de Apart, puedes escribir a [\[email protected\]](https://aisafetycolombia.org/cdn-cgi/l/email-protection#20535052494e545360415041525452455345415243480e434f4d)
 o usar la mesa de ayuda de su [Discord](https://discord.gg/XswWBvugYs)
.

### Enlaces útiles

*   ·[Página del sprint de Apart Research](https://apartresearch.com/sprints/ai-incident-response-sprint-2026-09-11-to-2026-09-13?utm_source=aisafetycolombia)
    : registro, plantilla de entrega, _Guidelines_ y _Resources_
*   ·[Discord del sprint](https://discord.gg/XswWBvugYs)
    : charlas, formación de equipos, mentores y mesa de ayuda
*   ·[Grupo de WhatsApp de la comunidad](https://chat.whatsapp.com/KwE8cciX48TAVhAOHnrLaZ)
    : equipos en Colombia y enlaces de las sesiones del hub
*   ·[Página del hub en AI Safety Colombia](https://aisafetycolombia.org/sprint)
    : mentores y ponentes
*   ·[Código de conducta](https://apartresearch.com/code-of-conduct)
    

Preguntas frecuentes
--------------------

¿Tengo que estar conectado los tres días?

No. Trabajas al ritmo que te sirva y desde donde estés. Las charlas son opcionales, aunque las recomendamos, y el único plazo fijo es el de la entrega.

¿Qué pasa si no tengo equipo?

No pasa nada. Puedes buscar compañeros en el grupo de WhatsApp de la comunidad, que es por donde se arma equipo con otra gente en Colombia, o en los canales de formación de equipos del Discord de Apart. También puedes entregar solo.

¿Las charlas son obligatorias?

No, ninguna. Las de Apart son en línea y en inglés, y cada una tiene su propia inscripción. Las del hub son en español y las que se pueden seguir desde fuera están en la tabla de más arriba.

¿Hay créditos de cómputo?

No. Apart responde que **no entrega créditos de cómputo**, y el apoyo de hasta USD 50 por equipo que ofrece AI Safety Colombia es solo para los equipos que trabajan presencialmente en el hub de Bogotá.

¿Compito contra los hubs presenciales?

Sí, y en igualdad de condiciones. Apart evalúa conjuntamente las entregas de todos los hubs y de quienes participan de manera remota, con la misma rúbrica. Los cinco premios son globales.

¿En qué idioma escribo el reporte?

El reporte final va en **inglés**, porque la plantilla, la plataforma y el jurado de Apart trabajan en ese idioma y tu proyecto se evalúa junto con trabajos de otros países. Si escribir directamente en inglés te hace trabajar más lento, puedes desarrollar primero las ideas en español y traducirlas al final.

**¿Te quedó alguna pregunta que no aparece acá?** Escríbela en el grupo. Si vemos que también le sirve a otras personas, la añadimos a esta guía.

**Nos vemos el viernes. ¡Qué bueno contar contigo!**