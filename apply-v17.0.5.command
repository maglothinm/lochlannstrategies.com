#!/bin/zsh
set -u
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "Lochlann Strategies v17.0.5 typography normalization"
echo

if command -v osascript >/dev/null 2>&1; then
  SITE_PATH="$(osascript -e 'POSIX path of (choose folder with prompt "Select the current lochlannstrategies.com repository folder")')" || exit 1
else
  printf "Enter the full path to the current website repository: "
  IFS= read -r SITE_PATH
fi

python3 "$SCRIPT_DIR/apply-v17.0.5.py" "$SITE_PATH"
STATUS=$?

echo
if [[ $STATUS -eq 0 ]]; then
  echo "Update complete. Review the files, then commit and push the repository."
else
  echo "The update was not applied. Review the error above."
fi

echo
printf "Press Return to close this window."
IFS= read -r _
exit $STATUS
