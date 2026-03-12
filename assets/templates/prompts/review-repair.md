Switch into review-and-repair mode.

Read and follow:

- `AGENTS.md`
- `docs/PLAN.md`
- `docs/STATUS.md`
- `docs/TEST_PLAN.md`
- relevant spec file or `spec/` files used by this project

Task:

Harden the current implementation against the plan and test plan before demo, handoff, or release.

Audit process:

1. Compare the implementation against the plan and spec.
2. Identify:
   - unfinished required behavior
   - weak reliability spots
   - missing tests or validations
   - UX or developer-flow regressions
   - startup, packaging, migration, or recovery risks
3. Triage findings by release risk.
4. Fix the highest-risk gaps first.
5. Run the relevant validation suite.
6. Update `docs/STATUS.md` with what was audited, what was fixed, what remains deferred, and final smoke commands.
7. Continue until the build is demo-ready or a real blocker remains.

Rules:

- No speculative rewrites.
- No new features unless they are required by the plan or spec.
- Prefer reliability, correctness, and recoverability over cleverness.
- Keep changes scoped and reviewable.
