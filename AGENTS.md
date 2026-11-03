# Project guidance

This workspace owns the Group-by backend of an MPC analytics project. Read
`docs/groupby-plan.md` and `docs/research-notes.md` before implementation.
The frontend, JOIN implementation, and complete SQL engine are outside scope.
The user confirmed algorithm reproduction with documented differences on SPU;
malicious-security reproduction is not required. JOIN belongs to a teammate.
Three computing parties are provisional. Read `docs/join-groupby-contract.md`
before integration; its payload and release policy are still proposals.

## Implementation rules

- Keep plaintext reference code, MPC kernels, runtime adapters, and result release
  separate. Simulator inputs and outputs are plaintext in the test process;
  simulator success does not demonstrate distributed data isolation.
- Start with COUNT(*) and SUM over bounded integers. Do not silently convert
  exact integers to floating point. Ring size alone does not determine JAX dtype.
- Keep keys, values, validity bits, group boundaries, permutations, and intermediate
  cardinalities secret. Never use secret-dependent Python branching, array sizes,
  host indexing, `numpy.unique`, or plaintext grouping inside MPC execution.
- Carry a separate validity bit; zero is a valid key and aggregate value.
  JOIN padding must not contribute to counts or sums.
- Return shared, fixed-capacity results from the operator. Revealing results is a
  separate integration responsibility governed by an explicit recipient/policy.
- Distinguish functional baseline, paper-inspired adaptation, protocol reproduction,
  and security reproduction. Every reproduction claim needs a source-to-code map
  and a list of substituted primitives and changed assumptions.
- Do not infer malicious security from ABY3, or from tests. Do not infer a secure
  shuffle from a caller-provided random vector.
- Preserve `requirements-py311-tested.txt` and the existing virtual environment. Do not add the full
  SecretFlow stack or a web framework until an integration need is established.
- Use synthetic fixtures. Do not log private rows, secret masks, or shares in
  service code. Opening intermediates is allowed only in explicitly labeled
  synthetic experiments.

## Validation and project hygiene

- Use `.venv311/bin/python` for current experiments; record dependency versions.
- Validate integer results against an independent Python-integer oracle. Include
  empty/all-invalid inputs, duplicate keys, zero/negative keys, zero sums, invalid
  rows sharing valid keys, and numeric boundaries when implementing the operator.
- Benchmark compilation separately from execution; distinguish simulation from
  network runs. Report unmeasured communication/round counts as unavailable.
- Document unresolved decisions as proposals, not user-approved requirements.
- Keep both English and Chinese README entry points current when scope changes.
- Git has been initialized for this workspace. The target remote is
  `git@github.com:AkirTech/Secrecy-Project-Group-by-Backend.git`.
  Verify actual commit and remote status before claiming a successful push.
