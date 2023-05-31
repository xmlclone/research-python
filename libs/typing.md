```python
# 可选字符串
UserType = Literal['mg', 'inter']

# 可选类型
Union[Union[int, str], float] == Union[int, str, float]

# 待默认值可选参数
def foo(arg: Optional[int] = None) -> None:
    ...
```