FROM mcr.microsoft.com/devcontainers/python:3.12

ARG UV_VERSION=0.4.24

# set some user and workdir settings to work nicely with vscode
USER vscode
WORKDIR /home/vscode

RUN curl -LsSf "https://astral.sh/uv/${UV_VERSION}/install.sh" | sh \
    && . $HOME/.cargo/env \
    && uv version

RUN echo 'eval "$(uv generate-shell-completion bash)"' >> /home/vscode/.bashrc
