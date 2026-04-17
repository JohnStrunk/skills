#! /bin/sh

set -e

# Switch to nftables to avoid iptables errors in Docker.
# This fixes "Table does not exist (do you need to insmod?)" errors when starting dockerd.
sudo update-alternatives --set iptables /usr/sbin/iptables-nft
sudo service docker stop || true
sudo pkill -x dockerd || true
sudo pkill -x containerd || true
sudo /usr/local/share/docker-init.sh

# Install Claude Code
curl -fsSL https://claude.ai/install.sh | bash

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
