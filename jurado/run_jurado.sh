#!/usr/bin/env bash
# Lanza un juez del panel: proceso Hermes independiente y headless, con modelo fijado.
# Uso: ./run_jurado.sh <modelo> <rol>
# Roles: rubrica | diablo | dfir | regulador | metodologo | ejecucion | metodologo_breve
set -u
MODEL="$1"; ROL="$2"
DIR="/home/daw/Sprint/jurado"
OUT="$DIR/veredictos/${ROL}__${MODEL}.md"
mkdir -p "$DIR/veredictos" "$DIR/logs"

case "$ROL" in
  rubrica)
    ROLTXT="Rol: JUEZ DE RÚBRICA. Aplica la rúbrica publicada al pie de la letra y ordena las candidatas de mejor a peor. No la interpretes con generosidad: si una propuesta merece 2, pon 2. Tu entregable más útil es el orden, con la razón de cada salto de puesto."
    VERIF="Verifica al menos cuatro hechos del expediente contra las fuentes originales, como pide el brief."
    PROSA="máximo 600 palabras"
    MAXMIN=45 ;;
  diablo)
    ROLTXT="Rol: ABOGADO DEL DIABLO. Tu única tarea es construir la mejor acusación posible contra cada candidata: no es nuevo, no importa, no cabe en el plazo, ya está cubierto, o no produce un número. Estás obligado a nombrar la objeción fatal de cada una y a sostenerla con evidencia. Si tras el esfuerzo concluyes que alguna sobrevive a tu ataque, dilo explícitamente: eso la vuelve creíble."
    VERIF="Verifica al menos cuatro hechos del expediente contra las fuentes originales, como pide el brief."
    PROSA="máximo 600 palabras"
    MAXMIN=45 ;;
  dfir)
    ROLTXT="Rol: INGENIERO DE RESPUESTA A INCIDENTES (DFIR). Evalúa con el criterio de tu oficio: ¿usarías esto en un incidente real? ¿Qué le falta para ser útil el día de un incidente? ¿Qué existe ya en la práctica profesional que lo vuelva redundante? Hablas desde la operación, no desde la academia."
    VERIF="Verifica al menos cuatro hechos del expediente contra las fuentes originales, como pide el brief."
    PROSA="máximo 600 palabras"
    MAXMIN=45 ;;
  regulador)
    ROLTXT="Rol: REGULADOR / ANALISTA DE POLÍTICA. Evalúa si el artefacto serviría a un regulador real (por ejemplo la AI Office europea o el portal de Cal OES): especificidad, accionabilidad, si resistiría un uso casi sin editar, y qué vacío legal revela. Aplica ojo de abogado: qué se puede probar, qué no, y con qué estándar."
    VERIF="Verifica al menos cuatro hechos del expediente contra las fuentes originales, como pide el brief."
    PROSA="máximo 600 palabras"
    MAXMIN=45 ;;
  metodologo)
    ROLTXT="Rol: METODÓLOGO AUDITOR DE EVIDENCIA. Tu pregunta central no es si la idea suena bien, sino si sus afirmaciones se sostienen: qué sería un resultado nulo, cómo se distinguiría de uno positivo, cuál es la amenaza principal a la validez, y qué medición haría falta para que el hallazgo signifique algo. Audita el expediente con dureza, incluidos los hechos que se presentan como ya verificados."
    VERIF="Verifica al menos cuatro hechos del expediente contra las fuentes originales, como pide el brief."
    PROSA="máximo 600 palabras"
    MAXMIN=45 ;;
  metodologo_breve)
    ROLTXT="Rol: METODÓLOGO AUDITOR DE EVIDENCIA, CON PRESUPUESTO DE TOKENS LIMITADO. Tu pregunta central no es si la idea suena bien, sino si sus afirmaciones se sostienen: qué sería un resultado nulo, cómo se distinguiría de uno positivo, cuál es la amenaza principal a la validez, y qué medición haría falta para que el hallazgo signifique algo."
    VERIF="NO hagas verificación web (para ahorrar tokens). Limítate a auditar la consistencia interna del expediente y del portafolio, y marca explícitamente en hechos_refutados cualquier punto que no puedas verificar por falta de presupuesto."
    PROSA="máximo 250 palabras"
    MAXMIN=20 ;;
  ejecucion)
    ROLTXT="Rol: INGENIERO DE ENTREGA. Evalúa viabilidad: qué se construye y se mide en las horas que quedan (el cierre es el lunes 14 de septiembre a las 06:59 hora de Colombia), con una o dos personas apoyadas en agentes de IA. Di qué se recorta, qué se entrega si todo lo demás falla, y cuál candidata garantiza un resultado numérico incluso en el peor escenario."
    VERIF="Verifica al menos tres hechos del expediente contra las fuentes originales."
    PROSA="máximo 500 palabras"
    MAXMIN=35 ;;
  *) echo "rol desconocido: $ROL" >&2; exit 2 ;;
esac

PROMPT="Lee y obedece el brief completo en $DIR/BRIEF_JUEZ.md, y después los dos archivos que referencia ($DIR/EXPEDIENTE.md y $DIR/PORTAFOLIO.md). $VERIF $ROLTXT Mantén la prosa en $PROSA. No dediques más de $MAXMIN minutos al trabajo. Escribe tu veredicto en la ruta exacta $OUT y termina con el bloque JSON tal como lo define el brief. Es obligatorio que el archivo quede escrito antes de terminar: si te queda poco presupuesto, escribe el JSON primero y la prosa después."

echo "== juez: modelo=$MODEL rol=$ROL"
echo "== salida: $OUT"
timeout 1800 hermes -z "$PROMPT" -m "$MODEL" --provider opencode-go --yolo --in "$DIR" > "$DIR/logs/${ROL}__${MODEL}.stdout" 2>&1
RC=$?
echo "== hermes rc=$RC"
if [ ! -s "$OUT" ]; then
  echo "!! el juez no escribió su archivo; revisar $DIR/logs/${ROL}__${MODEL}.stdout"
  tail -25 "$DIR/logs/${ROL}__${MODEL}.stdout"
  exit 1
fi
echo "== ok: $(wc -c < "$OUT") bytes"
