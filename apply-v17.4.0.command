#!/bin/bash
set -u

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_DIR="${1:-}"

is_repo() {
  [ -n "$1" ] && [ -f "$1/index.html" ] && [ -f "$1/about.html" ] && [ -f "$1/experience.html" ] && [ -d "$1/assets" ]
}

if ! is_repo "$REPO_DIR"; then
  if is_repo "$SCRIPT_DIR"; then
    REPO_DIR="$SCRIPT_DIR"
  elif is_repo "$(dirname "$SCRIPT_DIR")"; then
    REPO_DIR="$(dirname "$SCRIPT_DIR")"
  elif command -v osascript >/dev/null 2>&1; then
    REPO_DIR="$(osascript -e 'POSIX path of (choose folder with prompt "Select the current Lochlann Strategies repository folder")' 2>/dev/null || true)"
  fi
fi

if ! is_repo "$REPO_DIR"; then
  echo "No valid Lochlann repository folder was selected."
  echo "You can also run: python3 apply-v17.4.0.py /path/to/lochlannstrategies.com"
  printf '\nPress Return to close...'
  read -r _
  exit 2
fi

printf 'Applying Lochlann Strategies v17.4.0 to:\n%s\n\n' "$REPO_DIR"
python3 "$SCRIPT_DIR/apply-v17.4.0.py" "$REPO_DIR"
STATUS=$?

if [ "$STATUS" -eq 0 ]; then
  ZIP_PATH="$(dirname "${REPO_DIR%/}")/lochlann-site-v17.4.0-executive-career-evidence.zip"
  if [ -f "$ZIP_PATH" ] && command -v open >/dev/null 2>&1; then
    open -R "$ZIP_PATH" >/dev/null 2>&1 || true
  fi
fi

printf '\nPress Return to close...'
read -r _
exit "$STATUS"
