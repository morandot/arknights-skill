#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
VERSION_FILE="${REPO_ROOT}/VERSION"
DIST_DIR="${REPO_ROOT}/dist"
SKILL_NAME="arknights-skill"

if [ ! -f "${VERSION_FILE}" ]; then
    echo "VERSION file not found." >&2
    exit 1
fi

VERSION="$(cat "${VERSION_FILE}" | tr -d '[:space:]')"
ARCHIVE_NAME="${SKILL_NAME}-${VERSION}.zip"

mkdir -p "${DIST_DIR}"

TMP_DIR="$(mktemp -d)"
trap 'rm -rf "${TMP_DIR}"' EXIT

cp -R "${REPO_ROOT}/${SKILL_NAME}" "${TMP_DIR}/${SKILL_NAME}"

# Remove source metadata, caches, and OS artifacts
find "${TMP_DIR}/${SKILL_NAME}" -name ".DS_Store" -delete
find "${TMP_DIR}/${SKILL_NAME}" -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true
rm -f "${TMP_DIR}/${SKILL_NAME}/.source-commit" \
      "${TMP_DIR}/${SKILL_NAME}/.source-repo" \
      "${TMP_DIR}/${SKILL_NAME}/.source-ref" \
      "${TMP_DIR}/${SKILL_NAME}/.source-skill-path"

(cd "${TMP_DIR}" && zip -r "${DIST_DIR}/${ARCHIVE_NAME}" "${SKILL_NAME}/")

cd "${DIST_DIR}"
python3 -c "
import hashlib
fname = '${ARCHIVE_NAME}'
data = open(fname, 'rb').read()
h = hashlib.sha256(data).hexdigest()
with open(fname.replace('.zip', '.sha256'), 'w') as f:
    f.write(f'{h}  {fname}\n')
"

echo "Built: ${DIST_DIR}/${ARCHIVE_NAME}"
echo "SHA256: $(cat "${DIST_DIR}/${ARCHIVE_NAME%.zip}.sha256")"
