#!/usr/bin/env bash
set -euo pipefail

TARGET_DIR="$(cd "$(dirname "$0")" && pwd)"
DEFAULT_REPO_URL="https://github.com/moranfong/arknights-skill.git"
DEFAULT_REPO_REF="main"
DEFAULT_SKILL_PATH="arknights-skill"
TMP_DIR="$(mktemp -d)"

cleanup() {
    rm -rf "${TMP_DIR}"
}

trap cleanup EXIT

if [ ! -f "${TARGET_DIR}/SKILL.md" ]; then
    echo "update.sh must run from an installed skill directory." >&2
    exit 1
fi

REPO_URL="${REPO_URL:-$(cat "${TARGET_DIR}/.source-repo" 2>/dev/null || echo "${DEFAULT_REPO_URL}")}"
REPO_REF="${REPO_REF:-$(cat "${TARGET_DIR}/.source-ref" 2>/dev/null || echo "${DEFAULT_REPO_REF}")}"
SKILL_PATH="${SKILL_PATH:-$(cat "${TARGET_DIR}/.source-skill-path" 2>/dev/null || echo "${DEFAULT_SKILL_PATH}")}"
CURRENT_COMMIT="$(cat "${TARGET_DIR}/.source-commit" 2>/dev/null || true)"

echo "Checking ${REPO_URL}@${REPO_REF}"
git clone --depth 1 --branch "${REPO_REF}" "${REPO_URL}" "${TMP_DIR}/repo"
LATEST_COMMIT="$(git -C "${TMP_DIR}/repo" rev-parse HEAD)"

if [ -n "${CURRENT_COMMIT}" ]; then
    git -C "${TMP_DIR}/repo" fetch --depth 1 origin "${CURRENT_COMMIT}" >/dev/null 2>&1 || true
    if git -C "${TMP_DIR}/repo" rev-parse --verify "${CURRENT_COMMIT}^{commit}" >/dev/null 2>&1; then
        mkdir -p "${TMP_DIR}/previous"
        git -C "${TMP_DIR}/repo" archive "${CURRENT_COMMIT}" "${SKILL_PATH}" | tar -x -C "${TMP_DIR}/previous"
        if ! diff -qr \
            --exclude ".source-commit" \
            --exclude ".source-ref" \
            --exclude ".source-repo" \
            --exclude ".source-skill-path" \
            --exclude "update.sh" \
            "${TMP_DIR}/previous/${SKILL_PATH}" "${TARGET_DIR}" >/dev/null; then
            echo "Local modifications detected in ${TARGET_DIR}. Reinstall or resolve them manually." >&2
            exit 1
        fi
    fi
fi

if [ "${CURRENT_COMMIT}" = "${LATEST_COMMIT}" ]; then
    echo "Already up to date (${LATEST_COMMIT})"
    exit 0
fi

rsync -a --delete \
    --exclude ".source-commit" \
    --exclude ".source-ref" \
    --exclude ".source-repo" \
    --exclude ".source-skill-path" \
    --exclude "update.sh" \
    "${TMP_DIR}/repo/${SKILL_PATH}/" "${TARGET_DIR}/"

cp "${TMP_DIR}/repo/update.sh" "${TARGET_DIR}/update.sh"
chmod +x "${TARGET_DIR}/update.sh"
printf '%s\n' "${LATEST_COMMIT}" > "${TARGET_DIR}/.source-commit"
printf '%s\n' "${REPO_URL}" > "${TARGET_DIR}/.source-repo"
printf '%s\n' "${REPO_REF}" > "${TARGET_DIR}/.source-ref"
printf '%s\n' "${SKILL_PATH}" > "${TARGET_DIR}/.source-skill-path"

echo "Updated ${TARGET_DIR} to ${LATEST_COMMIT}"
