#!/usr/bin/env bash
# Panel de diseño completo: seis jueces, dos oleadas, un reintento cada uno.
#   qwen3.8-max        -> diseno     (metodología y potencia)
#   glm-5.3            -> sandbox    (plataforma y realismo)
#   deepseek-v4-pro    -> diablo     (acusación)
#   glm-5.3-flash      -> rubrica    (rúbrica del sprint)
#   kimi-k3            -> dual_breve (uso dual, con tope de tokens)
#   deepseek-v4.1-flash-> ejecucion  (plan y presupuesto)
set -u
DIR="/home/daw/Sprint/idea-sandbox"
cd "$DIR" || exit 1

run_one () {
  local model="$1" role="$2" out="$DIR/veredictos/$2__$1.md"
  if [ -s "$out" ]; then echo "== ya existe, se omite: $out"; return 0; fi
  ./run_juez.sh "$model" "$role" || ./run_juez.sh "$model" "$role"
}

echo "### oleada 1"
run_one qwen3.8-max diseno &
run_one glm-5.3 sandbox &
run_one deepseek-v4-pro diablo &
wait

echo "### oleada 2"
run_one glm-5.3-flash rubrica &
run_one kimi-k3 dual_breve &
run_one deepseek-v4.1-flash ejecucion &
wait

echo "### panel terminado"
ls -la "$DIR/veredictos"
