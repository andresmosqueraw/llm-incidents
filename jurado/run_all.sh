#!/usr/bin/env bash
# Despacha el panel completo en dos oleadas, con un reintento por juez.
# Asignación modelo -> rol pensada para diversidad de familias y para acotar costo:
#   glm-5.3            -> rubrica        (razonamiento fuerte, rúbrica)
#   qwen3.8-max        -> regulador      (contexto largo, política)
#   deepseek-v4-pro    -> diablo         (adversarial)
#   glm-5.3-flash      -> dfir           (barato, oficio)
#   deepseek-v4.1-flash-> ejecucion      (barato, viabilidad)
#   kimi-k3            -> metodologo_breve (caro: con tope de tokens)
set -u
DIR="/home/daw/Sprint/jurado"
cd "$DIR" || exit 1

run_one () {
  local model="$1" role="$2"
  local out="$DIR/veredictos/${role}__${model}.md"
  if [ -s "$out" ]; then
    echo "== ya existe, se omite: $out"
    return 0
  fi
  ./run_jurado.sh "$model" "$role" || ./run_jurado.sh "$model" "$role"
}

echo "### oleada 1: glm-5.3(ru), deepseek-v4-pro(diablo), deepseek-v4.1-flash(ejecucion)"
run_one glm-5.3 rubrica & 
run_one deepseek-v4-pro diablo &
run_one deepseek-v4.1-flash ejecucion &
wait

echo "### oleada 2: qwen3.8-max(re), glm-5.3-flash(dfir), kimi-k3(metodologo)"
run_one qwen3.8-max regulador &
run_one glm-5.3-flash dfir &
run_one kimi-k3 metodologo_breve &
wait

echo "### panel terminado. Veredictos:"
ls -la "$DIR/veredictos"
