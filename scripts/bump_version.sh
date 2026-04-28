#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
VERSION_FILE="${REPO_ROOT}/VERSION"
REGISTRY_FILE="${REPO_ROOT}/registry.yaml"

if [ ! -f "$VERSION_FILE" ]; then
    echo "VERSION file not found at $VERSION_FILE" >&2
    exit 1
fi

if [ ! -f "$REGISTRY_FILE" ]; then
    echo "registry.yaml not found at $REGISTRY_FILE" >&2
    exit 1
fi

VERSION="$(tr -d '[:space:]' < "$VERSION_FILE")"

if [ -z "$VERSION" ]; then
    echo "VERSION file is empty" >&2
    exit 1
fi

if ! echo "$VERSION" | grep -qE '^[0-9]+\.[0-9]+\.[0-9]+$'; then
    echo "Invalid version format: '$VERSION' (expected X.Y.Z)" >&2
    exit 1
fi

if grep -q '    version:' "$REGISTRY_FILE"; then
    sed -i.bak "s/    version: .*/    version: ${VERSION}/" "$REGISTRY_FILE"
    rm -f "${REGISTRY_FILE}.bak"
    echo "Updated registry.yaml version to ${VERSION}"
else
    echo "No 'version:' field found in registry.yaml" >&2
    exit 1
fi
