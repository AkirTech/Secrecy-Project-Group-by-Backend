# 安全 Group-by 后端

中文 | [English](README.md)

本工作区用于开发**安全多方联合分析项目中的 Group-by 部分**，负责在服务端 MPC 计算流程中完成分组与聚合。

整个项目的目标是基于现有 MPC 库复现论文中的协议，并通过前后端分离的应用进行演示。本工作区聚焦 Group-by；前端开发、JOIN 实现及完整查询系统的建设不属于本部分的职责范围。

## 研究背景

前期讨论见[《论文分段总结》](https://chatgpt.com/share/6ae87b2a-1d84-83e8-975a-54721fdc508f)。

讨论涉及两项相互补充的研究：

- *Secure Statistical Analysis on Multiple Datasets: Join and Group-By*（CCS 2023）：安全关系算子的协议设计。
- *SECRECY*（NSDI 2023）：安全查询执行及跨算子优化。

目前以 SPU 作为技术起点。[实施计划](docs/groupby-plan.zh.md)建议先完成 COUNT/SUM 基线，再逐步进行论文协议映射与后端集成。安全目标及待团队确认的接口约束也记录在计划中。

## 职责范围

本组件在服务端 MPC 执行流程中，对受保护的记录进行分组，并计算所需的聚合结果。后续需要与项目中的其他后端组件及经授权的结果交付流程衔接。

实现时需要明确区分“可完成聚合功能的基线方案”和“对特定论文协议的复现”。本地 MPC 实验也不足以证明整个应用的安全性或生产部署能力。

## 目录说明

| 位置 | 用途 |
| --- | --- |
| `src/backend/groupby/` | 为 Group-by 后端组件预留的目录。 |
| `requirements-py311-tested.txt` | 已有的 Python 依赖版本清单，初始化时原样保留。 |
| `.venv311/` | 已有的本地 Python 环境，已配置为不纳入版本控制。 |

## 当前状态

已实现 SPU 置换适配器、共同分组，以及采用前缀和、置换和差分的整数 SUM。
保留分段扫描基线用于对照。COUNT/MEAN/MIN/MAX/MEDIAN 仍为明确的未实现占位。
当前交付是记录差异的算法适配，不是恶意安全复现或已部署的后端服务；JOIN 由队友负责。

## 运行合成数据检查

```sh
python3.11 -m venv .venv311
.venv311/bin/python -m pip install -r requirements-py311-tested.txt
.venv311/bin/python src/backend/groupby/experiments/test_permutation.py
.venv311/bin/python src/backend/groupby/experiments/test_common.py
.venv311/bin/python src/backend/groupby/experiments/demo_sum.py
```

版本清单记录已测试的本地环境，本次尚未验证全新安装。
演示有意使用合成数据的参考 JOIN 交接文件，并重构模拟器结果，不实现安全 JOIN。
目前只运行了 demo 和算法检查，`test/` 中的完整场景验收程序尚未实现。

参见[实施计划](docs/groupby-plan.zh.md)、[调研记录](docs/research-notes.zh.md)
及[共同分组映射](docs/groupby-common.zh.md)。
