FROM mcr.microsoft.com/devcontainers/base:bookworm

ARG BUILDARCH
ARG HUGO_VERSION=0.131.0

# Install Hugo for Github Releases Page
RUN mkdir -p /tmp/hugo && \
    cd /tmp/hugo && \
    curl -LO  https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_${HUGO_VERSION}_linux-${BUILDARCH}.deb && \
    sudo apt install ./hugo_${HUGO_VERSION}_linux-${BUILDARCH}.deb && \
    cd / && \
    rm -rf /tmp/hugo

RUN sudo apt-get update && \
    sudo apt-get install -y python3 && \
    sudo apt-get clean && \
    sudo rm -rf /var/lib/apt/lists/*


