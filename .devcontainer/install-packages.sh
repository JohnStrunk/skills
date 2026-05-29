#! /bin/bash

set -e -x -o pipefail

# Log output to a file for debugging
LOG_FILE="/tmp/install-packages.log"
exec > >(tee -a "$LOG_FILE") 2>&1

cd "$(dirname "$0")"

# Switch to nftables to avoid iptables errors in Docker.
# This fixes "Table does not exist (do you need to insmod?)" errors when starting dockerd.
sudo update-alternatives --set iptables /usr/sbin/iptables-nft
sudo service docker stop || true
sudo pkill -x dockerd || true
sudo pkill -x containerd || true
sudo /usr/local/share/docker-init.sh

# Install Antigravity CLI
curl -fsSL https://antigravity.google/cli/install.sh | bash

# Install Claude Code
curl -fsSL https://claude.ai/install.sh | bash

# Install python tools
# shellcheck disable=SC2043
for pkg in \
    "ruff" \
    ; do
    uv tool install "$pkg"
done

# Install npm tools
npm install -g --no-fund \
    markdownlint-cli2
    # @playwright/cli

# npx -y playwright install --with-deps

# Install skills
# https://skills.sh/
# https://github.com/vercel-labs/skills
for skill in \
    "anthropics/skills@skill-creator" \
    "upstash/context7@find-docs" \
; do
    source="$(echo "$skill" | cut -d '@' -f 1)"
    skillname="$(echo "$skill" | cut -d '@' -f 2)"
    ( cd .. && \
    npx -y skills install "$source" --yes \
        --agent antigravity \
        --agent claude-code \
        --agent opencode \
        --skill "$skillname"
    )
done
