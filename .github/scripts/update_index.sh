#!/bin/bash
set -e

TASKS_FILE="$1"
TESTS_FILE="$2"
HTML_FILE="${HTML_FILE:-/app/index.html}"

OPEN_TASKS=$(awk '/^Open tasks:/ {grab=1; next} /^Closed tasks:/ {grab=0} grab && NF' "$TASKS_FILE")
CLOSED_TASKS=$(awk '/^Closed tasks:/ {grab=1; next} grab && NF' "$TASKS_FILE")
TEST_RESULTS=$(cat "$TESTS_FILE")
LAST_RUN="$(date '+%d/%m/%Y %H:%M %Z') by ${INVESTIGATOR:-unknown}"

# Swap the text inside <pre id="..."></pre> for new content.
# The content is passed in through an environment variable, so symbols
# like / or & in task names can't break the replacement.
fill_block() {
  BLOCK_ID="$1" BLOCK_TEXT="$2" perl -0777 -i -pe \
    's{(<pre id="\Q$ENV{BLOCK_ID}\E">).*?(</pre>)}{$1\n$ENV{BLOCK_TEXT}\n$2}s' "$HTML_FILE"
}

fill_block "open-tasks" "$OPEN_TASKS"
fill_block "closed-tasks" "$CLOSED_TASKS"
fill_block "test-results" "$TEST_RESULTS"
fill_block "last-run" "$LAST_RUN"

echo "Case board updated: $HTML_FILE"