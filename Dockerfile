FROM ghcr.io/astral-sh/uv:python3.14-trixie-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy

RUN apt-get update -yq && \
    apt-get install -yq --no-install-recommends \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev --extra lsp

#------------------------------------------------
# Runtime
#------------------------------------------------
FROM python:3.14-slim-trixie

RUN apt-get update -yq && \
    apt-get install -yq --no-install-recommends \
    chromium \
    && rm -rf /var/lib/apt/lists/*

ENV LNCRAWL_DATA_PATH=/data \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy

WORKDIR /app

COPY --from=builder /app/.venv /app/.venv

COPY pyproject.toml uv.lock ./
COPY lncrawl ./lncrawl
COPY sources ./sources
RUN /app/.venv/bin/python -c "import gzip, json, pathlib; p = pathlib.Path('sources/_index.json'); data = json.dumps(json.loads(p.read_text(encoding='utf-8')), ensure_ascii=False).encode(); p.with_name('_index.zip').write_bytes(gzip.compress(data, mtime=0))"

ENTRYPOINT ["/app/.venv/bin/python", "-m", "lncrawl"]
