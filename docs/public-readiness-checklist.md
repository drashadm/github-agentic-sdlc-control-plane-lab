# Public Readiness Checklist

Use this checklist for the final human review before the v1.0.0 release.

## Repository Hygiene

- [ ] README explains the thesis clearly.
- [ ] Lab index is complete.
- [ ] Roadmap is current.
- [ ] Validation harness passes.
- [ ] Local references resolve.
- [ ] No high-risk secrets are detected.
- [ ] No real exploit payloads are included.
- [ ] Educational examples are clearly labeled.

## Claims and Disclaimers

- [ ] Repo does not claim to be a production security product.
- [ ] Repo does not claim official certification coverage.
- [ ] Repo does not claim real signing, attestation, billing enforcement, eBPF, seccomp, or live token metering.
- [ ] Fake hashes and telemetry are labeled educational.
- [ ] Higher-assurance production controls are described as optional, not implemented.

## Reviewer Experience

- [ ] Reviewer quickstart exists.
- [ ] Vulnerability-to-defense matrix exists.
- [ ] Cram map exists.
- [ ] Hands-on drills exist.
- [ ] Oral defense prompts exist.
- [ ] v1.0 release notes exist or are planned.

## Final Release Gate

- [ ] Run `python scripts/validate_repo.py`.
- [ ] Run `git diff --check`.
- [ ] Review `README.md`.
- [ ] Review `docs/ROADMAP.md`.
- [ ] Tag v1.0.0 only after human approval.
