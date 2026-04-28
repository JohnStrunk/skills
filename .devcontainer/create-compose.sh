#!/usr/bin/env bash
# Generate docker-compose.yml from scratch.
# For each entry in mounts.txt, check whether the path exists on the host
# and, if so, add a volume mount.
#
# Usage: create-compose.sh <repo-name> <docker-image>

set -euo pipefail

if [[ $# -ne 1 ]]; then
    echo "Usage: $0 <docker-image>" >&2
    exit 1
fi

DOCKER_IMAGE="$1"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MOUNTS_FILE="${SCRIPT_DIR}/mounts.txt"
COMPOSE_FILE="${SCRIPT_DIR}/docker-compose.yml"

# Strip an inline comment from a line, respecting single/double quotes.
# A '#' is only treated as a comment start when it is outside quotes and
# either at position 0 or preceded by whitespace.
strip_comment() {
    local input="$1"
    local in_sq=0 in_dq=0
    local i ch
    for ((i = 0; i < ${#input}; i++)); do
        ch="${input:i:1}"
        case "$ch" in
            "'")  [[ $in_dq -eq 0 ]] && in_sq=$(( 1 - in_sq )) ;;
            '"')  [[ $in_sq -eq 0 ]] && in_dq=$(( 1 - in_dq )) ;;
            '#')
                if [[ $in_sq -eq 0 && $in_dq -eq 0 ]]; then
                    if [[ $i -eq 0 || "${input:i-1:1}" == [[:space:]] ]]; then
                        printf '%s' "${input:0:i}"
                        return
                    fi
                fi
                ;;
        esac
        done
    printf '%s' "$input"
}

# Remove one layer of surrounding single or double quotes.
strip_quotes() {
    local s="$1"
    if [[ ${#s} -ge 2 ]]; then
        local first="${s:0:1}" last="${s: -1}"
        if { [[ "$first" == '"' && "$last" == '"' ]] ||
             [[ "$first" == "'" && "$last" == "'" ]]; }; then
            s="${s:1:${#s}-2}"
        fi
    fi
    printf '%s' "$s"
}

# Collect extra volume mounts from mounts.txt
extra_volumes=()

if [[ -f "$MOUNTS_FILE" ]]; then
    echo "Processing volume mounts:"
    while IFS= read -r line || [[ -n "$line" ]]; do
        entry="$(strip_comment "$line")"
        entry="${entry#"${entry%%[![:space:]]*}"}"   # trim leading
        entry="${entry%"${entry##*[![:space:]]}"}"   # trim trailing
        [[ -z "$entry" ]] && continue

        if [[ "$entry" == *":ro" ]]; then
            rel_path="${entry%:ro}"
            mount_opts="ro"
        else
            rel_path="$entry"
            mount_opts="cached"
        fi

        rel_path="$(strip_quotes "$rel_path")"

        host_path="${HOME}/${rel_path}"

        if [[ -e "$host_path" ]]; then
            extra_volumes+=("      - \${HOME}/${rel_path}:/home/vscode/${rel_path}:${mount_opts}")
            echo "- ${host_path} ✅ ($mount_opts)"
        else
            echo "- ${host_path} ❌ (not found)"
        fi
    done < "$MOUNTS_FILE"
fi

# Write the complete docker-compose.yml
{
    echo "services:"
    echo "  devcontainer:"
    echo "    image: ${DOCKER_IMAGE}"
    echo "    volumes:"
    echo "      - ..:/workspace:cached"
    for v in "${extra_volumes[@]+"${extra_volumes[@]}"}"; do
        echo "$v"
    done
    echo "    command: sleep infinity"
} > "$COMPOSE_FILE"
