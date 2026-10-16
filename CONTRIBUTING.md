# Contributing

This repository uses a lightweight Git Flow so that its history demonstrates a
real review process without creating ceremony for its own sake.

## Branches

- `main`: stable, portfolio-ready milestones. Direct commits are avoided.
- `develop`: integration branch for work accepted during the current milestone.
- `feat/<issue>-<slug>`: new capability.
- `fix/<issue>-<slug>`: defect correction.
- `docs/<issue>-<slug>`: documentation-only change.

Branches start from `develop`. A feature is merged into `develop` through a pull
request. At the end of a milestone, `develop` is merged into `main` through a
release pull request.

## Commit and pull request conventions

Use imperative Conventional Commits:

```text
feat(api): add liveness endpoint
test(api): cover invalid document upload
docs(learning): explain vector similarity
```

Keep commits independently understandable. Pull request titles also follow this
format because PRs are squash-merged.

Every PR should state:

1. the problem being solved;
2. the relevant design decision;
3. how the behavior was verified;
4. what was learned or what trade-off was accepted.

## Definition of done

A change is done when it is typed, linted, tested, documented where necessary,
free of committed secrets, and reviewable as one coherent unit.

## Honest activity history

Estimates are expressed in focused working hours and session ranges. Git authors,
timestamps, commits, and pull requests reflect the actual work performed; they
are not backdated to create artificial activity.
