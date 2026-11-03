# Secure Group-by Backend

[中文](README.zh.md) | English

Workspace for the **Group-by portion of a secure multi-party analytics project**. This contribution covers the server-side backend component that performs grouping and aggregation as part of a larger MPC application.

The overall project aims to reproduce research protocols using an existing MPC library and demonstrate them through an application with separate frontend and backend services. This workspace focuses on Group-by; frontend development, JOIN implementation, and ownership of the complete query system are outside this contribution's scope.

## Research context

The background discussion is available in [论文分段总结](https://chatgpt.com/share/6ae87b2a-1d84-83e8-975a-54721fdc508f).

That discussion connects two research directions:

- *Secure Statistical Analysis on Multiple Datasets: Join and Group-By* (CCS 2023): secure relational operator protocols.
- *SECRECY* (NSDI 2023): secure query execution and optimization across operators.

SPU is the current technical starting point. The [implementation plan](docs/groupby-plan.md) proposes a COUNT/SUM baseline followed by explicit paper-protocol mapping and backend integration. Security and integration decisions awaiting team input are recorded there.

## Contribution scope

The intended component groups protected records and computes requested aggregates within the server-side MPC execution flow. It should eventually integrate with the project's other backend components and its authorized result delivery flow.

The implementation must distinguish between a functional aggregation baseline and reproduction of a specific paper protocol. Likewise, local MPC experiments do not establish the security or deployment readiness of the complete application.

## Workspace

| Location | Purpose |
| --- | --- |
| `src/backend/groupby/` | Reserved home for the Group-by backend contribution. |
| `requirements-py311-tested.txt` | Existing pinned Python dependency list, preserved as supplied. |
| `.venv311/` | Existing local Python environment; excluded from version control. |

## Current status

Implemented SPU permutation adapters, common grouping, and integer SUM using
prefix sums, permutation and differences. The segmented-scan baseline is retained
for comparison. COUNT/MEAN/MIN/MAX/MEDIAN remain explicit unimplemented stubs.
This is an algorithm adaptation with documented differences, not a malicious-security
reproduction or a deployed backend service. JOIN belongs to a teammate.

## Run the synthetic checks

```sh
python3.11 -m venv .venv311
.venv311/bin/python -m pip install -r requirements-py311-tested.txt
.venv311/bin/python src/backend/groupby/experiments/test_permutation.py
.venv311/bin/python src/backend/groupby/experiments/test_common.py
.venv311/bin/python src/backend/groupby/experiments/demo_sum.py
```

The version list describes the tested local environment; fresh installation has
not been verified here. The demo deliberately uses a synthetic reference JOIN
fixture and reconstructs simulator outputs. It does not implement secure JOIN.
Only the demo and algorithm checks have been exercised; the complete scenario
acceptance suite under `test/` is not yet implemented.

See [implementation plan](docs/groupby-plan.md), [research notes](docs/research-notes.md),
and [common grouping mapping (Chinese)](docs/groupby-common.zh.md).
