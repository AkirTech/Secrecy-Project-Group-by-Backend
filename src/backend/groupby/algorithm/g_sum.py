"""论文 Protocol 4.4 的前缀和/置换/差分构造在 SPU 上的适配。

底层使用排序式置换，并增加 valid 处理；不继承论文的通信或恶意安全保证。
输入为 int32；有效位必须为 0/1，输入数值绝对值之和不得超过 int32 上限。
"""
from .g_common import groupby_common
from .sum_from_common import sum_from_common


def groupby_sum(keys, values, valid):
    common = groupby_common(keys, values, valid)
    return common.keys_out, sum_from_common(common), common.valid_out
