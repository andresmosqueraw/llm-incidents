#!/usr/bin/env bash
# Un juez del panel de diseño para la idea del sandbox altruista.
# Uso: ./run_juez.sh <modelo> <rol>
# Roles: diseno | sandbox | diablo | rubrica | dual | ejecucion | dual_breve
set -u
MODEL="$1"; ROL="$2"
DIR="/home/daw/Sprint/idea-sandbox"
OUT="$DIR/veredictos/$ROL"__"$MODEL.md"
mkdir -p "$DIR/veredictos" "$DIR/logs"

case "$ROL" in
  diseno)
    ROLTXT="Rol: METODÓLOGO EXPERIMENTAL. Tu pregunta es si el diseño mide lo que dice medir. Exige: tamaño de efecto detectable con el número de corridas propuesto, preregistro del desenlace primario, controles que aíslen la reciprocidad de la conducta orientada al otro, definición operacional de 'sacrificio' que no se pueda cumplir por accidente, y cómo se distingue cooperación costosa de simple imitación o de una política aprendida. Di cuánta potencia falta y cuántas corridas harían falta para el efecto más pequeño que le importaría a un jurado."
    VERIF="Verifica al menos tres afirmaciones del expediente contra las fuentes originales y al menos un identificador arXiv del prior art."
    PROSA="máximo 700 palabras"; MAXMIN=45 ;;
  sandbox)
    ROLTXT="Rol: INGENIERO DE PLATAFORMA Y DFIR. Evalúa el realismo y la construibilidad. Qué partes del sandbox son verificables y cuáles son teatro; dónde el diseño pierde validez externa (por ejemplo, si el canal es un directorio que los agentes ya saben compartido); qué instrumentación hace falta para capturar cada medida sin que el instrumento sea el canal; qué se rompe con modelos baratos; y si el 'servicio señuelo' basta para que el evento de escape sea creíble para un lector."
    VERIF="Verifica al menos tres afirmaciones del expediente contra las fuentes originales y al menos un identificador arXiv del prior art."
    PROSA="máximo 700 palabras"; MAXMIN=45 ;;
  diablo)
    ROLTXT="Rol: ABOGADO DEL DIABLO. Construye la mejor acusación: que el envoltorio ya está listado por los organizadores, que 'altruismo' es interpretación y no medición, que con modelos baratos y un sandbox de mentira no emergerá nada, que la colusión multiagente ya está publicada, y que el uso dual puede costarle la sanción al equipo. Nombra la objeción fatal y sostenla con evidencia. Si tras el esfuerzo concluyes que la idea sobrevive a tu ataque, dilo explícitamente."
    VERIF="Verifica al menos tres afirmaciones del expediente contra las fuentes originales y al menos un identificador arXiv del prior art."
    PROSA="máximo 700 palabras"; MAXMIN=45 ;;
  rubrica)
    ROLTXT="Rol: JUEZ DE RÚBRICA. Aplica la rúbrica publicada del sprint al pie de la letra y puntúa las tres dimensiones sin generosidad. Además: ordena esta idea frente a una alternativa de análisis documental (auditar el registro publicado), y di cuál construirías con 60 horas, con la razón."
    VERIF="Verifica al menos dos afirmaciones del expediente contra las fuentes originales."
    PROSA="máximo 500 palabras"; MAXMIN=35 ;;
  dual)
    ROLTXT="Rol: REVISOR DE USO DUAL Y PUBLICACIÓN. Decide qué del proyecto puede publicarse y qué no: mecanismos, tasas, instrumentación, harness, transcripciones. Marca el límite entre 'medición de conducta' y 'receta de escape colectivo'. Di cómo se maneja la revisión de divulgación del sprint y qué parte del reporte debería quedar bajo retención. Añade qué valor tendría esto para un regulador, si alguno."
    VERIF="Verifica al menos dos afirmaciones del expediente contra las fuentes originales."
    PROSA="máximo 500 palabras"; MAXMIN=35 ;;
  dual_breve)
    ROLTXT="Rol: REVISOR DE USO DUAL Y PUBLICACIÓN, CON PRESUPUESTO DE TOKENS LIMITADO. Decide qué puede publicarse y qué no, dónde está el límite entre medir conducta y publicar una receta de escape colectivo, y cómo se maneja la revisión de divulgación del sprint."
    VERIF="NO hagas verificación web (ahorro de tokens). Audita la consistencia interna del expediente y marca en hechos_refutados lo que no puedas verificar por presupuesto."
    PROSA="máximo 250 palabras"; MAXMIN=20 ;;
  ejecucion)
    ROLTXT="Rol: JEFE DE PROYECTO. Convierte esto en un plan de 60 horas con dos personas apoyadas en agentes: cronograma por bloques, presupuesto de tokens con números, qué se corre en paralelo, qué se recorta primero, el piloto go/no-go con su condición numérica, y el plan B declarado de antemano. Di si el plan cabe y qué parte del reporte se escribe cuándo."
    VERIF="Verifica al menos dos afirmaciones del expediente contra las fuentes originales."
    PROSA="máximo 500 palabras"; MAXMIN=35 ;;
  *) echo "rol desconocido: $ROL" >&2; exit 2 ;;
esac

PROMPT="Lee y obedece el brief completo en $DIR/BRIEF-JUECES.md y después el único documento que referencia, $DIR/EXPEDIENTE-IDEA.md. $VERIF $ROLTXT Mantén la prosa en $PROSA. No dediques más de $MAXMIN minutos. Escribe tu veredicto en la ruta exacta $OUT y termina con el bloque JSON tal como lo define el brief. Es obligatorio dejar el archivo escrito: si te queda poco presupuesto, escribe el JSON primero y la prosa después."

echo "== juez: modelo=$MODEL rol=$ROL"
timeout 1800 hermes -z "$PROMPT" -m "$MODEL" --provider opencode-go --yolo --in "$DIR" > "$DIR/logs/${ROL}__${MODEL}.stdout" 2>&1
RC=$?
echo "== hermes rc=$RC"
if [ ! -s "$OUT" ]; then
  echo "!! sin archivo de veredicto; revisar $DIR/logs/${ROL}__${MODEL}.stdout"
  tail -20 "$DIR/logs/${ROL}__${MODEL}.stdout"
  exit 1
fi
echo "== ok: $(wc -c < "$OUT") bytes"
