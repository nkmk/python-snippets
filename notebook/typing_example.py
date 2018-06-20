from typing import Union, List

def func_u(x: List[Union[int, float]]) -> float:
    return sum(x) ** 0.5

print(func_u([0.5, 9.5, 90]))
# 10.0
