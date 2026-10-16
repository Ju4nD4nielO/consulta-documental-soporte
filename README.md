# Document Support AI

[![CI](https://github.com/Ju4nD4nielO/consulta-documental-soporte/actions/workflows/ci.yml/badge.svg)](https://github.com/Ju4nD4nielO/consulta-documental-soporte/actions/workflows/ci.yml)

An educational, production-minded platform for asking questions about private
documents and receiving answers grounded in cited sources.

The project is built in public as a portfolio case study for AI Engineering. It
will cover Python application design, LLM orchestration, retrieval-augmented
generation (RAG), REST and GraphQL APIs, asynchronous processing, distributed
systems, evaluation, security, and observability.

> **Current status:** Milestone 0 — project foundation. The AI functionality is
> intentionally added in small, reviewable increments documented in the
> [roadmap](docs/ROADMAP.md).

## Why this project exists

Many LLM demos stop after a successful prompt. This project focuses on the
engineering work required to turn that prompt into a reliable service:

- traceable answers instead of unsupported claims;
- background document ingestion instead of blocking HTTP requests;
- explicit API contracts and typed boundaries;
- retries, idempotency, timeouts, and failure handling;
- repeatable evaluation, tests, metrics, and cost visibility.

## Planned architecture

```text
Web/API clients
      |
      +-- REST: documents, jobs and operational endpoints
      +-- GraphQL: conversations and flexible read models
                         |
                     API service
                         |
              +----------+----------+
              |                     |
        LLM workflow           task queue
      (LangChain/LangGraph)          |
              |                ingestion worker
              +----------+----------+
                         |
               PostgreSQL + pgvector
```

Each component is introduced only when its trade-offs can be demonstrated. See
the [architecture decisions](docs/architecture/README.md) for the reasoning.

## Local development

Requirements:

- Python 3.12–3.14
- Git
- Docker with Compose (introduced in a later milestone)

Create and activate a virtual environment:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Start the API:

```powershell
uvicorn document_support.main:app --reload
```

Then open `http://127.0.0.1:8000/docs` or request the health endpoint:

```powershell
Invoke-RestMethod http://127.0.0.1:8000/api/v1/health
```

## Quality checks

```powershell
ruff check .
ruff format --check .
mypy src
pytest
```

## Project workflow

- `main` contains completed, portfolio-ready releases.
- `develop` integrates completed milestones.
- `feat/<issue>-<description>` contains one reviewable change.
- Pull requests use squash merging and Conventional Commit titles.

Details are in [CONTRIBUTING.md](CONTRIBUTING.md). Estimates in the roadmap are
honest focused-work ranges; commit dates are never fabricated.

## Learning trail

Every milestone includes a Spanish learning note explaining the problem,
implementation, trade-offs, tests, and likely interview questions. Start with
[Fundamentos del proyecto](docs/learning/00-project-foundation.md).

## License

No license has been selected yet. Until one is added, the source is available
for review but all rights remain with the author.
