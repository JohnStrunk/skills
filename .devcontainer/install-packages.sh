#! /bin/sh

set -e

cd "$(dirname "$0")"

# Switch to nftables to avoid iptables errors in Docker.
# This fixes "Table does not exist (do you need to insmod?)" errors when starting dockerd.
sudo update-alternatives --set iptables /usr/sbin/iptables-nft
sudo service docker stop || true
sudo pkill -x dockerd || true
sudo pkill -x containerd || true
sudo /usr/local/share/docker-init.sh

# Install Claude Code
curl -fsSL https://claude.ai/install.sh | bash

# Install coderabbit
curl -fsSL https://cli.coderabbit.ai/install.sh | sh

# Install python tools
for pkg in \
    "dvc[gdrive,s3]" \
    "harbor" \
    "ruff" \
    ; do
    uv tool install "$pkg"
done

# Install npm tools
npm install -g --no-fund \
    @google/gemini-cli \
    markdownlint-cli \
    @playwright/cli@latest \
    skills
npx -y playwright install --with-deps

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
        --agent claude-code \
        --agent gemini-cli \
        --agent opencode \
        --skill "$skillname"
    )
done
