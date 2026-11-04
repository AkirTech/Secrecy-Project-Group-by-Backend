"""COUNT(*)：只统计有效行，保留 values 参数以兼容统一入口。"""
from ..common import groupby_common
from .sum import sum_from_common


def count_from_common(common):
    return sum_from_common(common._replace(values_grouped=common.valid_grouped))


def groupby_count(keys, values, valid):
    c = groupby_common(keys, values, valid)
    return c.keys_out, count_from_common(c), c.valid_out
