#!/bin/bash
set -eo pipefail

SCRIPTS="/app/.github/scripts"

banner() {
  echo "=============================="
  echo "$1"
  echo "=============================="
}

banner "Building the case task list (todo.py)"
python3 "$SCRIPTS/todo.py" | tee /tmp/todo_output.txt

banner "Running unit tests (todo-test.py)"
python3 "$SCRIPTS/todo-test.py" | tee /tmp/test_output.txt

banner "Updating the case board (update_index.sh)"
bash "$SCRIPTS/update_index.sh" /tmp/todo_output.txt /tmp/test_output.txt

banner "Pipeline finished"