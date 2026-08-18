#!/bin/bash
set -u

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SOURCE_URL="https://github.com/maglothinm/lochlannstrategies.com/archive/refs/heads/main.zip"
OUTPUT_DIR="${1:-$HOME/Downloads}"
WORK_DIR="$(mktemp -d "${TMPDIR:-/tmp}/lochlann-v17.4.0.XXXXXX")"
SOURCE_ZIP="$WORK_DIR/current-main.zip"
EXTRACT_DIR="$WORK_DIR/source"
FINAL_NAME="lochlann-site-v17.4.0-executive-career-evidence.zip"
STATUS=0

cleanup() {
  rm -rf "$WORK_DIR"
}
trap cleanup EXIT

fail() {
  echo "ERROR: $1"
  STATUS=2
}

mkdir -p "$EXTRACT_DIR" "$OUTPUT_DIR"

if ! command -v python3 >/dev/null 2>&1; then
  fail "Python 3 is required to generate the updated ZIP."
elif ! command -v unzip >/dev/null 2>&1; then
  fail "The macOS unzip utility could not be found."
else
  echo "Preparing the current Lochlann repository..."
  if [ -n "${LOCHLANN_SOURCE_ZIP:-}" ] && [ -f "${LOCHLANN_SOURCE_ZIP}" ]; then
    cp "${LOCHLANN_SOURCE_ZIP}" "$SOURCE_ZIP" || fail "Could not copy LOCHLANN_SOURCE_ZIP."
  elif command -v curl >/dev/null 2>&1; then
    curl -L --fail --silent --show-error --retry 2 "$SOURCE_URL" -o "$SOURCE_ZIP" || fail "Could not download the current public GitHub repository."
  else
    fail "The macOS curl utility could not be found."
  fi
fi

if [ "$STATUS" -eq 0 ]; then
  unzip -q "$SOURCE_ZIP" -d "$EXTRACT_DIR" || fail "The downloaded repository ZIP could not be opened."
fi

if [ "$STATUS" -eq 0 ]; then
  REPO_DIR="$(find "$EXTRACT_DIR" -mindepth 1 -maxdepth 1 -type d -name 'lochlannstrategies.com-*' -print -quit)"
  if [ -z "$REPO_DIR" ] || [ ! -f "$REPO_DIR/index.html" ]; then
    fail "The current repository folder was not found inside the downloaded ZIP."
  fi
fi

if [ "$STATUS" -eq 0 ]; then
  echo "Applying and validating v17.4.0..."
  python3 "$SCRIPT_DIR/apply-v17.4.0.py" "$REPO_DIR" || fail "The v17.4.0 patch did not complete."
fi

if [ "$STATUS" -eq 0 ]; then
  GENERATED_ZIP="$(dirname "$REPO_DIR")/$FINAL_NAME"
  if [ ! -f "$GENERATED_ZIP" ]; then
    fail "The deployment ZIP was not generated."
  else
    FINAL_PATH="$OUTPUT_DIR/$FINAL_NAME"
    rm -f "$FINAL_PATH"
    cp "$GENERATED_ZIP" "$FINAL_PATH" || fail "Could not copy the deployment ZIP to $OUTPUT_DIR."
  fi
fi

if [ "$STATUS" -eq 0 ]; then
  echo
  echo "Ready-to-upload ZIP created:"
  echo "$FINAL_PATH"
  if command -v open >/dev/null 2>&1; then
    open -R "$FINAL_PATH" >/dev/null 2>&1 || true
  fi
else
  echo
  echo "No website files were changed."
fi

printf '\nPress Return to close...'
read -r _
exit "$STATUS"
