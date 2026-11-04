"""精确均值返回 (keys, numerator, denominator, valid)，无效分母为 1。"""
import jax.numpy as jnp
from ..common import groupby_common
from .sum import sum_from_common
from .count import count_from_common


def mean_from_common(common):
    return (common.keys_out, sum_from_common(common),
            jnp.where(common.valid_out != 0, count_from_common(common), 1), common.valid_out)


def groupby_mean(keys, values, valid):
    return mean_from_common(groupby_common(keys, values, valid))
