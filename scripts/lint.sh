#!/bin/sh -e
set -x

export PREFIX="uv run"

export SOURCE_FILES="."

${PREFIX} mypy ${SOURCE_FILES}
${PREFIX} pyright ${SOURCE_FILES}
${PREFIX} ruff check ${SOURCE_FILES}
${PREFIX} ruff format --check ${SOURCE_FILES}