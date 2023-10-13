from typing import Union, Any

def func_union(x: Union[int, float]) -> float:
    return x * 0.5

var: Any = 100

def func(x: int | float) -> float:
    return x * 0.5

i: int = 100
l: list[float] = [0.1, 0.2, 0.3]
d: dict[str, int] = {'a': 100, 'b': 200}
