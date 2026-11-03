# Group-by 后端组件

中文 | [English](README.md)

本目录为 MPC 联合分析项目中的服务端 Group-by 组件预留。

本组件负责安全分组与聚合，并与其他后端组件的数据流和执行流程衔接。目前讨论过的聚合功能包括 COUNT、SUM，以及可能后续扩展的 MEDIAN；最终支持范围尚未确定。

待复现的协议、MPC 后端集成方式、输入输出表示、API 职责边界、结果公开规则及部署方式，已在下方设计计划中提出初步方案，仍待团队确认。

项目背景与职责范围见[工作区中文 README](../../../README.zh.md)。

## 设计与下一步

参见[实施计划](../../../docs/groupby-plan.md)和[调研记录](../../../docs/research-notes.md)。建议首先实现精确整数 COUNT/SUM、秘密分组键和有效位、固定容量的秘密共享输出，以及独立明文参考实现。集成接口与安全目标仍待确认。

在工作区根目录运行合成数据可行性检查：

```sh
.venv311/bin/python src/backend/groupby/experiments/probe_spu.py
```

## 整数 SUM 基线

`algorithm/g_sum.py` 使用共同分组、全局前缀和、秘密置换和差分求和。
原分段扫描实现保留在 `algorithm/g_sum_baseline.py` 用于对照。
输入为等长 int32 的键、金额、有效位；有效位必须为 0/1，所有输入金额
绝对值之和须不超过 int32 上限，由上游保证。输出容量不变，无效载荷清零。
内核不重构结果。当前是论文高层步骤的 SPU 适配，底层置换和安全假设有差异。

运行：`.venv311/bin/python src/backend/groupby/experiments/demo_sum.py`。
演示读取 `reference_only/expected_join.csv` 作为合成 JOIN 交接数据，并按
公开 right_capacity 填充；不实现 JOIN。模拟器会公开最终返回值，仅用于测试。
包含独立 Python 整数参考实现、边界与固定种子随机检查，并核对 expected.json。

## 秘密置换适配层

`algorithm/permutation.py` 提供 `gen_perm`、`apply_perm`、`apply_inv`，
使用零基目标位置表示，支持复用置换重排多列。详见
[接口说明与聚合方法评估](../../../docs/permutation.zh.md)。
运行 `.venv311/bin/python src/backend/groupby/experiments/test_permutation.py` 验证。
这是基于 SPU 排序的功能适配，不是论文专用置换协议；原 SUM 基线另存，各聚合占位方法已拆分。

## 共同分组与文件分工

参见[返回字段、步骤映射和实现差异](../../../docs/groupby-common.zh.md)。
运行 `.venv311/bin/python src/backend/groupby/experiments/test_common.py` 验证共同分组及 SUM 组合。
