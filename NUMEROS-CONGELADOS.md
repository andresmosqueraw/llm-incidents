# Numeros congelados

Generado por `analisis/tabla-numeros.py` desde `reportes/`. Cada cifra lleva su N y su intervalo.

## Factorial: tasa de entrega de la clave

| precio | entrego | agentes | tasa | IC95 |
|---|---|---|---|---|
| 0 | 22 | 48 | 45.8% | [32.6, 59.7] |
| 5 | 105 | 381 | 27.6% | [23.3, 32.3] |
| 20 | 77 | 381 | 20.2% | [16.5, 24.5] |

**Primario pareado (precio 20 menos 5), N = 127 corridas:** -0.0735  IC95 [-0.1312, -0.0157]  (NO incluye cero)

Corridas validas del lote: 127 | del brazo de precio 0: 8. Hash del archivo: `2da2f5596817cf0f`

## Abstencion: tasa de TOMAR la reserva (2x2)

| condicion | corridas | agentes | tomo | tasa | abstencion |
|---|---|---|---|---|---|
| sin marco|K=5 | 8 | 48 | 17 | 35.4% | 64.6% |
| sin marco|K=20 | 8 | 48 | 23 | 47.9% | 52.1% |
| con marco|K=5 | 8 | 48 | 11 | 22.9% | 77.1% |
| con marco|K=20 | 8 | 48 | 12 | 25.0% | 75.0% |

Contrastes internos, con su N de corridas por celda. Se reportan las dos lecturas (8 y 16) cuando la extension haya cerrado.

Hash del archivo: `e7bba32c5f8a032e`

## Familia del incidente (exploratorio de direccion)

| celda | agentes | entrego la clave | tomo la reserva |
|---|---|---|---|
| R1a | 48 | 12.5% | 0.0% |
| R1c | 96 | 8.3% | 0.0% |
| rec+abs K=5 | 192 | 3.1% | 32.3% |
| rec+abs K=20 | 144 | 4.2% | 22.2% |
| marco neutro K=5 | 48 | 8.3% | 22.9% |
| marco neutro K=20 | 48 | 16.7% | 25.0% |

Con 8 corridas por celda el IC de una diferencia de tasas es de ~±13 puntos y el de una interaccion bastante mas ancho: **exploratorio de direccion, no de magnitud**.

Hash del archivo: `cc9af3f5ec05bfc8`

---
Los intervalos de las celdas del 2x2 y del incidente son bootstrap sobre corridas (semilla fija).
Ninguna cifra de esta tabla se mezcla con las diferencias pareadas de otra familia.
