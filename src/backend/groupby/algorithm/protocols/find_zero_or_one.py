"""Protocol 4.16：选择 x=0 或 1 的行，再稳定压紧。

内部调用前提：每个有效组恰好一行满足谓词；不通过公开秘密进行检查。
EqZeroOrOne 用两次相等比较替代论文的位截断优化。
"""
import jax.numpy as jnp
from ..primitives.gen_perm import gen_perm
from ..primitives.apply_perm import apply_perm


def find_zero_or_one(c, x):
    selected = ((x == 0) | (x == 1)) & (c.valid_grouped != 0)
    permutation = gen_perm(1 - selected.astype(jnp.int32))
    return apply_perm(permutation, jnp.where(selected, c.values_grouped, 0))
