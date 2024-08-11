FROM mcr.microsoft.com/devcontainers/base:bookworm

ARG HUGO_VERSION=0.131.0

# Install Hugo for Github Releases Page
RUN mkdir -p /tmp/hugo && \
    cd /tmp/hugo && \
    curl -LO  https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_${HUGO_VERSION}_linux-amd64.deb && \
    sudo apt install ./hugo_${HUGO_VERSION}_linux-amd64.deb && \
    cd / && \
    rm -rf /tmp/hugo


