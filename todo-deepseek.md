# TODO — DeepSeek V4.1 Flash / Hermes (13 sep, desde ~13:20 COT)

Lote de 80 en curso hasta ~17:00. Reglas: no mirar 5 vs 20 hasta el cierre; no tocar `harness/`,
puertos 8201-8206, `parametros.json` ni `vista_*.json`; no correr `prueba_solvente.py` ni ningún
brazo hasta que termine el lote (mismos puertos). Los tests nuevos se escriben ahora, se corren después.
No redactas prosa del reporte: datos, estructura, código y enmiendas.

## Antes de las 17:00
- [ ] **Enmiendas del lote en curso** en `PREREGISTRO.md` §8, con hora (único autor):
  - [ ] revisión entre bloques de 40: solo instrumento (corridas válidas, hashes, "sin estímulo",
        rechazos, tareas completadas); **no** se mira la diferencia 5 vs 20; quién revisa y qué archivo
  - [ ] precio 0 se mide después del lote, en la misma escena y hash (8 corridas)
  - [ ] objeto "clave de verificación": connotación de credencial como límite conocido del primario
        (la negativa pagada citando confidencialidad, con corrida y agente)
- [ ] Código de análisis, probado contra mini-piloto y lote-a, para que a las 17:00 sea un comando:
  - [ ] Tabla 1: tasa de clave por precio, bootstrap por corrida, diferencia pareada 5 vs 20
  - [ ] Figura 2: tasa contra precio 0/5/20 con intervalos
  - [ ] Tabla 2: validez (corridas válidas, cadenas íntegras, rechazos, tareas completadas)
  - [ ] Supervivencia hasta el primer depósito por ronda y precio
  - [ ] Contagio: riesgo de depositar tras ver un depósito ajeno
  - [ ] ITT con la cadena de saliencia (leyó el almacén → mencionó la solicitud → leyó su clave → depositó)
  - [ ] Mediación por capacidad sobrante (tarea completada × respuesta)
  - [ ] `rechazos` en `agregar.py`: `startswith("comando_rechazado")`
- [ ] `escena-costo-cero.json` con los textos exactos de la escena actual, precios en 0, validada.
- [ ] `escena-30.json` (presupuesto apretado, 30 pasos), validada. Enmienda escrita antes de correrla.
- [ ] Enmiendas de los brazos futuros (objeto neutro, reclutador, participación privada, presupuesto
      apretado), escritas para revisión del equipo; ninguno corre antes de las 80 y el precio 0.
- [ ] Verificar contra la fuente local de METR que los reclutadores "tuvieron éxito" (número de línea)
      antes de que la afirmación entre al reporte.
- [ ] Párrafo de implicaciones Track 1 con las citas ya verificadas (datos y citas; la prosa es del equipo).
- [ ] Material del apéndice de uso dual con fuente: intentos de túnel TCP y netcat, repetición deliberada
      pagando, objeto que suena a credencial, confundidor de capacidad, tasa base del detector.
- [ ] Actualizar el PR #3 (estimador.py, codificacion.py, enmiendas) para revisión en paralelo.

## Después de las 17:00, en serie (mismos puertos)
- [ ] `agregar.py` sobre las 80; congelar `reportes/factorial.json` y anotar su hash en `todo.md`
- [ ] Precio 0: 8 corridas, misma escena y hash (~1M, ~20 min)
- [ ] Presupuesto apretado: 4-8 corridas, solo si hay tokens (~0,8M)
- [ ] 19:00 — análisis congelado; entregar tablas y figura al equipo

## Coordinación
- Claude hace: `salud_lote.py`, copias de seguridad, tabla de defectos, mapa de rúbrica, anclas de
  METR, Figura 1 y esqueleto de Figura 2, revisión de borradores. No edita `PREREGISTRO.md` mientras
  tú lo tengas abierto.
- Si a las 16:00 las tres enmiendas del lote no están escritas, las escribe Claude y te avisa.
