#!/bin/sh -e
set -x
export PREFIX="uv run"

export SOURCE_FILES="."

${PREFIX} ruff check ${SOURCE_FILES} --fix --unsafe-fixes
${PREFIX} ruff format ${SOURCE_FILES}