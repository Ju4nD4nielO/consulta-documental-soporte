# Delivery and learning roadmap

The estimates below describe focused work, including explanation, implementation,
tests, and review. They are planning ranges—not fabricated calendar history.
Depending on study pace, one 4–8 hour milestone may span several days.

| Milestone | Outcome | Estimated focus |
| --- | --- | ---: |
| 0. Foundation | Typed API skeleton, tests, CI, workflow and architecture record | 4–6 h |
| 1. API contracts | Document REST API, GraphQL query model, validation and error design | 6–9 h |
| 2. Persistence | PostgreSQL, migrations, repositories and integration tests | 7–10 h |
| 3. Async ingestion | Queue, worker, job states, retries and idempotency | 8–12 h |
| 4. RAG pipeline | Parsing, chunking, embeddings, pgvector search and citations | 10–14 h |
| 5. LLM workflow | Provider abstraction, LangChain/LangGraph tools and guardrails | 9–13 h |
| 6. Evaluation | Golden dataset, retrieval/answer metrics and regression gates | 7–10 h |
| 7. Production readiness | Auth, observability, rate limits, deployment and threat review | 10–14 h |

Expected total: **61–88 focused hours**. A sustainable learning pace of 6–10
hours per week makes this roughly an 8–12 week portfolio project.

## Milestone rules

Each milestone should produce:

- one issue or clearly written scope;
- one or more focused feature branches;
- passing local and CI verification;
- a pull request into `develop`;
- a Spanish learning note;
- a release pull request from `develop` to `main` when the milestone is complete.

The roadmap may change when experiments provide evidence. Changes should be
recorded, not hidden, because revising a design is part of engineering.
