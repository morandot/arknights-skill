#!/usr/bin/env bash
set -euo pipefail

SKILL_NAME="${SKILL_NAME:-arknights-guide}"
SKILL_PATH="${SKILL_PATH:-arknights-guide}"
REPO_URL="${REPO_URL:-https://github.com/moranfong/arknights-skill.git}"
REPO_REF="${REPO_REF:-main}"
INSTALL_DIR="${INSTALL_DIR:-${HOME}/.hermes/skills/research/${SKILL_NAME}}"
TMP_DIR="$(mktemp -d)"

cleanup() {
    rm -rf "${TMP_DIR}"
}

trap cleanup EXIT

echo "Installing ${SKILL_NAME} from ${REPO_URL}@${REPO_REF}"
git clone --depth 1 --branch "${REPO_REF}" "${REPO_URL}" "${TMP_DIR}/repo"

SOURCE_DIR="${TMP_DIR}/repo/${SKILL_PATH}"
if [ ! -f "${SOURCE_DIR}/SKILL.md" ]; then
    echo "Skill source not found: ${SKILL_PATH}" >&2
    exit 1
fi

mkdir -p "${INSTALL_DIR}"
find "${INSTALL_DIR}" -mindepth 1 -maxdepth 1 -exec rm -rf {} +
cp -R "${SOURCE_DIR}/." "${INSTALL_DIR}/"
cp "${TMP_DIR}/repo/update.sh" "${INSTALL_DIR}/update.sh"
chmod +x "${INSTALL_DIR}/update.sh"

git -C "${TMP_DIR}/repo" rev-parse HEAD > "${INSTALL_DIR}/.source-commit"
printf '%s\n' "${REPO_URL}" > "${INSTALL_DIR}/.source-repo"
printf '%s\n' "${REPO_REF}" > "${INSTALL_DIR}/.source-ref"
printf '%s\n' "${SKILL_PATH}" > "${INSTALL_DIR}/.source-skill-path"

echo "Installed to ${INSTALL_DIR}"
echo "Use explicit invocation with \$${SKILL_NAME} when needed."
