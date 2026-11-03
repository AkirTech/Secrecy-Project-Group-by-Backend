# Group-by Backend Component

[中文](README.zh.md) | English

This directory is reserved for the server-side Group-by contribution to the MPC analytics project.

The component's responsibility is secure grouping and aggregation, integrated with the surrounding backend's data and execution flow. Aggregates discussed so far include COUNT, SUM, and possible later extensions such as MEDIAN; the final supported set has not been fixed.

The protocol to reproduce, MPC backend integration, input/output representation, API responsibilities, rules for revealing results, and deployment model are proposed in the design plan below and await team confirmation.

See the [workspace README](../../../README.md) for project context and contribution scope.

## Design and next steps

See the [implementation plan](../../../docs/groupby-plan.md) and [investigation record](../../../docs/research-notes.md). The proposed first increment is exact integer COUNT/SUM with secret keys and validity masks, fixed-capacity shared outputs, and an independent reference oracle. Integration and security requirements remain provisional.

Run the synthetic feasibility probe from the workspace root:

```sh
.venv311/bin/python src/backend/groupby/experiments/probe_spu.py
```

## Integer SUM baseline

`algorithm/g_sum.py` uses common grouping, global prefix sums, secret permutation
and adjacent differences. The former segmented-scan baseline is in `g_sum_baseline.py`. Inputs are equal-length int32 keys, values and
0/1 validity. Upstream must ensure the sum of absolute input values fits int32.
Invalid output payloads are zeroed; the kernel does not reconstruct results.
This adapts paper-level steps; sorting-based permutation and security assumptions differ.

Run `.venv311/bin/python src/backend/groupby/experiments/demo_sum.py`.
The synthetic simulator experiment uses `reference_only/expected_join.csv` as
an explicit JOIN handoff fixture padded to public right_capacity; JOIN is not
implemented. Simulator outputs are reconstructed for testing only. Independent
Python-integer reference, boundary/random checks and expected.json verify results.

## Secret permutation adapter

`algorithm/permutation.py` provides `gen_perm`, `apply_perm`, and `apply_inv`
using zero-based destination positions and reusable multi-column permutations.
Run `.venv311/bin/python src/backend/groupby/experiments/test_permutation.py`.
See the [Chinese interface and scope notes](../../../docs/permutation.zh.md).
This SPU-sort adapter does not reproduce the paper's specialized permutation
protocol or its communication guarantees. The original SUM baseline is preserved; aggregate stubs are now in separate files.

## Common grouping

See [field mapping and implementation differences (Chinese)](../../../docs/groupby-common.zh.md).
Run `.venv311/bin/python src/backend/groupby/experiments/test_common.py`.
