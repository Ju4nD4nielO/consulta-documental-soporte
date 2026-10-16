# ADR 0001: Start with a modular monolith

- Status: Accepted
- Date: 2026-10-15

## Context

The target system must demonstrate REST, GraphQL, background work, LLM workflows,
and distributed-system concerns. Splitting an empty project into microservices
would add network and deployment complexity before domain boundaries are known.

## Decision

Start with a modular Python application whose API boundaries are explicit. Run
the ingestion worker as a separate process once asynchronous work is introduced.
Extract another service only when measurements or ownership boundaries justify it.

## Consequences

- Local development and tests remain inexpensive.
- Domain boundaries can evolve without cross-service migrations.
- The queue and worker still demonstrate distributed failure modes.
- The project cannot claim independent microservice deployment at the start—and
  should not pretend that service count alone demonstrates distributed-systems
  experience.
