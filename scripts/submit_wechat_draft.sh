#!/usr/bin/env bash
set -euo pipefail

RUN_DIR="${1:-}"
MODE="${2:-}"

if [[ -z "$RUN_DIR" ]]; then
  echo "usage: submit_wechat_draft.sh <run-dir> [--dry-run]" >&2
  exit 2
fi

PUBLISH_READY="$RUN_DIR/wechat/publish-ready.md"
if [[ ! -f "$PUBLISH_READY" ]]; then
  echo "missing $PUBLISH_READY; build it first with build_wechat_publish_ready.py" >&2
  exit 2
fi

ARTICLE_HTML="$RUN_DIR/wechat/article.html"

PUBLISHER_SCRIPT="${WECHAT_PUBLISHER_SCRIPT:-}"

if [[ -z "$PUBLISHER_SCRIPT" ]]; then
  if [[ "$MODE" == "--dry-run" ]]; then
    frontmatter_value() {
      local key="$1"
      awk -F '"' -v key="$key" '
        $0 ~ "^" key ":" {
          if (index($0, "\"") > 0) {
            print $2
          } else {
            sub("^" key ":[[:space:]]*", "")
            print
          }
          exit
        }
      ' "$PUBLISH_READY"
    }

    TITLE="$(frontmatter_value title)"
    AUTHOR="$(frontmatter_value author)"
    DIGEST="$(frontmatter_value digest)"
    if [[ -z "$DIGEST" ]]; then
      DIGEST="$(frontmatter_value summary)"
    fi
    COVER="$(frontmatter_value cover)"
    if [[ -z "$COVER" ]]; then
      COVER="$(frontmatter_value coverImage)"
    fi
    IMAGE_COUNT="$(grep -Ec '^!\[[^]]*\]\([^)]+\)' "$PUBLISH_READY" || true)"

    if [[ -f "$ARTICLE_HTML" ]]; then
      if python3 "$(dirname "$0")/validate_gzh_html.py" "$ARTICLE_HTML" >/dev/null 2>&1; then
        TYPESET_STATUS="present, 0 ERROR"
      else
        TYPESET_STATUS="present, HAS ERRORS (run scripts/validate_gzh_html.py)"
      fi
    else
      TYPESET_STATUS="missing (run the typeset stage first)"
    fi

    echo "local dry-run only: no WECHAT_PUBLISHER_SCRIPT configured"
    echo "publish-ready: $PUBLISH_READY"
    echo "title: ${TITLE:-unknown}"
    echo "author: ${AUTHOR:-unknown}"
    echo "digest: ${DIGEST:-unknown}"
    echo "cover: ${COVER:-unknown}"
    echo "inline images: $IMAGE_COUNT"
    echo "typeset html: $TYPESET_STATUS"
    exit 0
  fi

  echo "missing WeChat publisher adapter; set WECHAT_PUBLISHER_SCRIPT to a local script that accepts:" >&2
  echo "  <publish-ready.md> --theme default [--html <article.html>] [--dry-run]" >&2
  exit 2
fi

if [[ ! -f "$PUBLISHER_SCRIPT" ]]; then
  echo "missing WeChat publisher adapter script: $PUBLISHER_SCRIPT" >&2
  exit 2
fi

RUN_CMD=()
case "$PUBLISHER_SCRIPT" in
  *.ts)
    if command -v bun >/dev/null 2>&1; then
      RUN_CMD=(bun "$PUBLISHER_SCRIPT")
    elif [[ -x "$HOME/.npm/_npx/5c4f1b4a21be27f7/node_modules/.bin/bun" ]]; then
      RUN_CMD=("$HOME/.npm/_npx/5c4f1b4a21be27f7/node_modules/.bin/bun" "$PUBLISHER_SCRIPT")
    else
      RUN_CMD=(npx -y bun "$PUBLISHER_SCRIPT")
    fi
    ;;
  *.js|*.mjs)
    RUN_CMD=(node "$PUBLISHER_SCRIPT")
    ;;
  *.py)
    RUN_CMD=(python3 "$PUBLISHER_SCRIPT")
    ;;
  *)
    if [[ -x "$PUBLISHER_SCRIPT" ]]; then
      RUN_CMD=("$PUBLISHER_SCRIPT")
    else
      echo "publisher adapter is not executable and has no known extension: $PUBLISHER_SCRIPT" >&2
      exit 2
    fi
    ;;
esac

ARGS=("$PUBLISH_READY" --theme default)
if [[ -f "$ARTICLE_HTML" ]]; then
  ARGS+=(--html "$ARTICLE_HTML")
fi
if [[ "$MODE" == "--dry-run" ]]; then
  ARGS+=(--dry-run)
fi

"${RUN_CMD[@]}" "${ARGS[@]}"
