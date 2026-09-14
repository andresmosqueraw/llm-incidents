# [TÍTULO] — andamio del reporte

> **Esto es un andamio, no un borrador.** La prosa la escribe el equipo: un reporte que se lee como
> generado no puntúa. Aquí está la estructura, el presupuesto de palabras de cada sección, la figura que
> le toca, y **cada cifra con el archivo del que sale**. Quien escriba rellena prosa alrededor de números
> ya verificados, en vez de decidir estructura a las 04:00.
>
> Convención de los huecos:
> `⟦CIFRA: valor — archivo⟧` cifra ya verificada, se copia tal cual.
> `⟦PENDIENTE: qué falta — quién⟧` no existe todavía; no se escribe prosa que dependa de ella.
> `⟦ESCRIBIR: …⟧` prosa humana.
>
> Límite duro: **8 páginas**, abstract **≤150 palabras**. Presupuesto de palabras abajo, suma ~3.900,
> que a dos columnas cabe con las tres figuras y la tabla.

---

## Abstract — 150 palabras máximo

⟦ESCRIBIR: cinco frases. (1) El hueco: nadie ha medido cooperación costosa en agentes de LLM muy por
debajo de la frontera de racionalidad. (2) Qué hicimos: seis agentes, tareas independientes, un
confederado pide un objeto ortogonal, ayudar cuesta presupuesto propio que no se recupera. (3) El
resultado de forma, no de magnitud: la cooperación se parte al introducir cualquier costo y luego es
indiferente a su tamaño. (4) Que se replica en un segundo mecanismo (no saquear un fondo común) y que la
identidad de quien pide no mueve nada. (5) Qué implica para responder a incidentes entre agentes.⟧

Cifras que puede citar el abstract, ya verificadas:
⟦CIFRA: precio 0 = 45,8% (22/48) — reportes/confirmatorio.json tasas.0⟧
⟦CIFRA: precio 5 = 20,5% (43/210) — reportes/confirmatorio.json tasas.5⟧
⟦CIFRA: primario pareado 20−5 = −3,3 pts, IC95 [−11,4; +4,3], incluye cero, N=70 — reportes/confirmatorio.json primario_pareado⟧

## 1. Introduction — ~550 palabras · **no depende de ningún número, escribible ya**

⟦ESCRIBIR: el incidente de julio de 2026 como motivación, con las anclas de METR verificadas (líneas
1025, 1027, 1041, 1050 de la copia local; «presión significativa» **no** es literal — ver anclas-metr.md).
Luego el salto: el incidente muestra que un agente consiguió que otro actuara, pero no dice a qué precio.
Cerrar con la pregunta del paper en una frase y la contribución en tres viñetas.⟧

La frase corta del hueco, en su forma verdadera (ver mapa-rubrica.md): no es «nadie ha medido cooperación
costosa», es **«nadie la ha medido muy por debajo de la frontera de racionalidad»** — 2607.23982 sondea
márgenes de ±0,05 alrededor de la frontera; aquí el beneficio privado es exactamente cero.

## 2. Related work — ~450 palabras · **no depende de ningún número, escribible ya**

⟦ESCRIBIR: cuatro grupos y qué deja fuera cada uno. (a) Riesgo moral y márgenes estrechos: 2607.23982,
2604.07821. (b) Juegos del dictador en LLM: 2410.21359, 2511.08721, 2402.05786 — sin costo instrumental.
(c) Bienes públicos: 2506.23276 y siguientes. (d) Entornos multiagente: 2602.15198, 2601.19082,
2412.10270, 2602.07777. Cada ID tiene que estar en papers.md — se verifica al final.⟧

Figura 1: mapa de regímenes, sitúa el diseño frente a los doce trabajos.
⟦CIFRA: figuras/fig1-regime-map.png (EN) y fig1-mapa-regimenes.png (ES), 300 dpi⟧

## 3. Design and instrument — ~700 palabras

⟦ESCRIBIR: la escena en un párrafo, y luego los cuatro pilares como la razón por la que el número vale:
costo con unidades en un libro con cadena de hashes; solicitud saliente por construcción (sin depósito
del confederado la corrida se excluye por «sin estímulo»); «no pudo» separado de «no quiso»; receptor
presente. Después el régimen dominado: beneficio privado cero, así que cualquier precio positivo deja la
cooperación estrictamente dominada.⟧

- Agentes, rondas, presupuesto: ⟦CIFRA: 6 agentes autosuficientes, 4 rondas, 8 acciones/ronda, presupuesto 40 pasos — escena.json temporal + verificado en presupuesto.json (145/145 no reclamantes con gastado+restante = 40)⟧
- Precios del factorial: ⟦CIFRA: 5 y 20 pasos — escena.json asignacion⟧
- Objeto pedido: clave de verificación, ortogonal a la tarea, alfabeto sin dígitos ni A-F.
- Validación adversarial: ⟦CIFRA: 12 invariantes I1-I12 + grep de canarios — harness/validador.py⟧
- Tabla 2 (validez del instrumento): ⟦CIFRA: tabla2-validez.md⟧

## 4. Results — ~900 palabras · **el núcleo; no se escribe hasta la congelación**

> **Qué entra al cuerpo y qué no.** Hay diez brazos y caben tres bloques. El criterio no es cuánto costó
> correr cada uno, sino qué afirmación del paper sostiene:
>
> | bloque del cuerpo | brazos | qué afirmación sostiene |
> | --- | --- | --- |
> | §4.1 la curva | factorial base + precio 0 + precio 1 | **el umbral**: la cooperación se rompe con cualquier precio y luego es indiferente a su tamaño |
> | §4.2 el lado de tomar, ronda 1 | abstención × 3 marcos × 2 K | **se replica** en un mecanismo independiente, y el hallazgo metodológico del agotamiento |
> | §4.3 lo que razonan | reclutador R1a y R1c (transcripciones) | **el mecanismo** de por qué el precio no produce pendiente, y que el nulo no es por desatención |
>
> **Precio 0 va al cuerpo aunque no sea el contraste preregistrado**: es el control positivo que
> demuestra que el instrumento detecta cooperación cuando la hay. Sin él, un nulo no se distingue de un
> instrumento sordo. **Precio 1 también**: es lo que sitúa el umbral abajo; sin él sólo se podría decir
> «entre 0 y 5 pasa algo».
>
> **Al apéndice:** identidad del solicitante (par-p5 / externo-p5) — el resultado es correcto pero con 6
> y 4 corridas su intervalo es [−30,6; +34,7] y no informa solo; la misma pregunta la contestan mejor el
> reclutador (par − tercero, 24 agentes por celda) y el lado de tomar (neutral − reclutador). En el cuerpo
> va **la frase**, apoyada en las tres; en el apéndice el detalle de cada una. También al apéndice: el
> análisis de posición, los defectos del instrumento y el brazo de reclutador completo.
>
> **No se corrió, y se dice:** la extensión del 2×2 a 16 por celda y el factorial más allá de 128,
> detenidos por el reloj de entrega y declarados en §8 del preregistro.

### 4.1 La curva de precio: un umbral, no una pendiente

| precio | tasa | IC95 | fuente |
| --- | --- | --- | --- |
| 0 | 45,8% (22/48) | [32,6; 59,7] | confirmatorio.json |
| 1 | ⟦PENDIENTE: 30,6% (11/36) hoy, pero deepseek repone corridas; cifra final sobre las 8 válidas — deepseek, luego yo⟧ | | exploratorios.json |
| 5 | 20,5% (43/210) | [15,6; 26,4] | confirmatorio.json |
| 20 | 17,1% (36/210) | [12,6; 22,8] | confirmatorio.json |

⟦PENDIENTE: intervalo de la diferencia **0 − 5**, que es el contraste del titular. Necesita las tasas por
corrida del base separadas por precio, del conjunto congelado; `confirmatorio.json` sólo guarda
agregados. — deepseek al congelar⟧

⟦CIFRA: primario pareado 20−5 = −3,3 pts [−11,4; +4,3], incluye cero, N=70 — confirmatorio.json⟧
⟦PENDIENTE: la misma cifra a N≥160 como seguimiento de precisión, reportando las tres miradas (70/80/160) — deepseek⟧

⟦ESCRIBIR: la lectura. Casi toda la caída ocurre entre 0 y 1; de 5 a 20 no hay efecto detectable. Lo que
importa es que el costo exista, no cuánto vale.⟧

Figura 2: ⟦CIFRA: figuras/fig-exploratorios.py → curva-precio.png; regenerar tras la congelación⟧

### 4.2 El mismo patrón en un segundo mecanismo: no saquear el fondo común

Reserva de 60 pasos, cada reclamo retira 2K, lo que queda se reparte. Tomar domina: neto +3,33 con K=5 y
+13,33 con K=20. Abstenerse cuesta K.

⟦CIFRA: toma en ronda 1 (fondo intacto en las seis celdas): sin marco 29,2% / 25,0%; neutral 14,6% / 18,8%; reclutador 20,8% / 20,0% (K=5 / K=20) — reportes/tomar-3x2.json celdas.*.toma_ronda1⟧
⟦CIFRA: abstención 71%-85%; ninguno de los doce contrastes excluye cero con el fondo intacto — tomar-3x2.json marco_solo_ronda1 e interaccion⟧

⟦ESCRIBIR: dos operacionalizaciones independientes, misma forma: plano en el parámetro que debería
moverla. Y **decir en voz alta el falso positivo evitado**: a todas las rondas, el contraste de marco a
K=20 daba +22,9 [+2,1; +43,7] y excluía cero; restringido a ronda 1 se cae a +6,2 [−12,5; +22,9]. Era
agotamiento del fondo, no marco. Eso es un punto a favor del rigor del trabajo, no una debilidad.⟧

### 4.3 Quién pide no importa; que haya alguien pidiendo, sí — **una frase en el cuerpo, detalle al apéndice**

⟦CIFRA: par − externo (identidad del solicitante) — exploratorios.json contraste_identidad_par_menos_externo; PENDIENTE cifra final tras reposiciones⟧
⟦CIFRA: par − tercero (reclutador) = +0,0 pts a precio 5 y −8,3 a precio 20, ambos incluyen cero — reportes/reclutador.json contrastes⟧
⟦CIFRA: neutral − reclutador (lado de tomar) = −4,2 y +1,7, ambos incluyen cero — tomar-3x2.json marco⟧

⟦ESCRIBIR: tres comparaciones independientes, las tres nulas. Es el nulo más informativo del paper porque
va contra la intuición del reclutamiento persuasivo.⟧

### 4.4 Por qué el precio no produce pendiente: lo que razonan los agentes

⟦CIFRA: sólo 2,1%-4,2% de los agentes razona el costo en pasos — reportes/reclutador-texto.json categorias['razona el costo en pasos']⟧
⟦CIFRA: se niegan explícitamente 27,1% (R1a) y 35,4% (R1c); mencionan al beneficiario 2,1% frente a 45,8% — reclutador-texto.json⟧
⟦CIFRA: sin ninguna categoría (cota superior de no-interacción) 56,2% (R1a) y 29,2% (R1c) — reclutador-texto.json⟧

⟦ESCRIBIR: el nulo no es por desatención — con un par nombrado casi la mitad procesó la apelación y aun
así no pagó. Y los agentes no hacen aritmética de costo-beneficio: aplican una regla sobre el objeto
(«la clave no es parte del código»). Un parámetro que no entra en la deliberación no puede producir una
pendiente. **Declarar el método**: codificación por palabra clave, un solo codificador, sin medida de
acuerdo, patrones publicados en analisis/reclutador_texto.py.⟧

## 5. Threats to validity — ~600 palabras · **escribible ya, todo verificado**

Fuente completa: `validez-instrumento.md`. Los cuatro, con su número:

1. ⟦CIFRA: el precio se asigna por posición y nunca rota: 01-03 llevan 5 y 04-06 llevan 20 en 108/108 corridas, porque `resolver_asignacion` baraja con `semilla: 20260912` una sola vez — validez-instrumento.md §1⟧
2. ⟦CIFRA: efecto de posición medido con tratamiento uniforme: −3,7 pts [−15,6; +8,1] sobre 45 corridas (tomar) y −14,3 [−38,1; +9,5] sobre 14 (dar); ninguno excluye cero, pero es del mismo orden que el primario — reportes/posicion.json⟧
3. ⟦CIFRA: la simultaneidad **se verifica y aguanta**: vista y reconciliaciones sólo al cerrar la ronda — validez-instrumento.md §3⟧
4. ⟦CIFRA: la tentación está confundida con la capacidad del fondo (a K=5 absorbe 6 reclamos, a K=20 absorbe 1,5; `sin marco K=20` se agota en 8/8) y el libro del fondo crea pasos: 11 reclamos de 46 acreditados sobre reserva 0, 220 pasos de la nada — validez-instrumento.md §4⟧
5. ⟦CIFRA: un servicio caído invalidó 9 corridas (56 depósitos rechazados); excluidas y repuestas — instrucciones-escenas.md §0.1⟧
6. Un solo modelo, contención por proceso y no por contenedor, `resolver()` no generaliza.

⟦ESCRIBIR: el párrafo que le da valor a esto: los cuatro defectos los encontró el equipo, están
cuantificados, y los dos arreglos son de una línea (semilla por corrida; reserva escalada con K). Un
nulo con los artefactos medidos vale más que un efecto sin ellos.⟧

## 6. Implications for incident response — ~400 palabras

⟦ESCRIBIR: lo que movió la conducta no fue quién pedía ni por quién, sino **que hubiera un pedido** y qué
regla tenía el agente sobre el objeto. Los que se negaron alegaron que la clave no era parte de su tarea
— una regla sobre el objeto, no un juicio sobre el solicitante. De ahí la recomendación barata:
delimitar qué puede salir de un agente, antes que enseñarle a desconfiar de quién pregunta. Atar al
incidente sin sobreafirmar: son n pequeñas y es una dirección.⟧

## 7. Dual use — apéndice obligatorio

⟦CIFRA: apendice-uso-dual-datos.md — los 325 rechazos clasificados; los «168 intentos de túnel» son reintentos al puerto propio (0 externos); de 18 comandos genuinamente salientes, 17 son `find / -name parte1.txt`⟧
⟦ESCRIBIR: la frase de Guidelines: no se publican recetas de instalación novedosas sin revisión.⟧

## Apéndices (no cuentan para las 8 páginas)

- `apendice-defectos.md` — 14 defectos del arnés + 10 confundidores de escena, con detección y verificación.
- `validez-instrumento.md` — los cuatro hallazgos de validez con sus tablas.
- `reclutador-analisis.md` — el brazo del reclutador completo.
- `tabla2-validez.md`, `traza-enmiendas.md` (13 enmiendas fechadas), `papers.md`.
- ⟦PENDIENTE: `reportes/congelado.json` — `congelar.py` no se ha corrido nunca; sin él ninguna cifra tiene hash ni hora. Es lo primero tras cerrar árbol 1 — deepseek⟧

---

## Checklist de cierre (fuente: checklist-entrega.md)

- [ ] ≤8 páginas · abstract ≤150 palabras
- [ ] apéndice de uso dual presente
- [ ] frase de «no se publican recetas de instalación sin revisión»
- [ ] cada ID de arXiv citado está en `papers.md`
- [ ] cada cifra del PDF rastreable a un archivo de `reportes/` con su hash en `congelado.json`
- [ ] las tres miradas del confirmatorio (70/80/160) reportadas, con el titular en la preplaneada
- [ ] desviaciones del preregistro declaradas (incluida la mirada anticipada al contraste)
- [ ] enviar borrador temprano: reenviar con el mismo título reemplaza los archivos
