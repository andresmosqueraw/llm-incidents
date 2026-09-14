Corridas descartadas: colision de nombre de carpeta al paralelizar 4 lotes
de la escena "segunda-tarea" (14 sep, madrugada).

Causa: harness/bucle.py nombra la carpeta de salida como
  f"{marca}_{escena['escena']}"
donde 'marca' es un timestamp con resolucion de 1 segundo y escena['escena']
es el campo 'nombre' de la escena. Se crearon 4 variantes de la escena
(escena-segunda-tarea-p8601/8701/8801/8901.resuelta.json) que solo
cambiaban puertos.egreso_base -- el campo 'escena'/'nombre' seguia siendo
"segunda-tarea" en las 4. Dos pares de lotes arrancaron su corrida 1 en el
mismo segundo de reloj y escribieron eventos.jsonl/resumen.json/
presupuesto.json en la MISMA carpeta al mismo tiempo.

Resultado: eventos.jsonl con lineas entrelazadas de 2 corridas distintas
(362 y 380 eventos en vez de ~150-270 esperados), cadena de hash prev/hash
rota, resumen.json con el contenido de solo una de las 2 corridas (la que
escribio ultimo). Datos no reconstruibles, se descartan.

Las 4 corridas siguientes (corrida 2/2 de cada lote) NO colisionaron y son
validas: salidas/20260914T060150_segunda-tarea, 20260914T060210_segunda-tarea,
20260914T060431_segunda-tarea, 20260914T060505_segunda-tarea.

Leccion para relanzar en paralelo: dar a cada variante de escena un campo
'escena'/'nombre' unico (ej. "segunda-tarea-p8601"), no solo el puerto.
