- [说明](#说明)
- [命令](#命令)
- [api](#api)
- [pytest.ini](#pytestini)
- [插件](#插件)
- [文档](#文档)

# 说明

1. 由于测试文件需要以`test_`开头或`_test`结尾，故其它文件都是依据此方式进行命名
2. 测试方法需要以`test_`开头或者`_test`结尾
3. 测试类应该以`Test`开头，测试类里面的每个`test`是一个独立的类的实例，即以`self.`设置属性，只对单个实例有效(类的实例仍然是共享的)
4. 测试文件不管放到那个包(目录)下，均会被pytest扫描到，只要符合上面第二条说的文件名以`test_`开头或`_test`结尾
   
> pytest will run all files of the form `test_*.py` or `*_test.py` in the current directory and its subdirectories Run multiple tests

# 命令

```shell
# 普通执行
pytest

# 查看执行详情
pytest -v

# 指定执行文件，此时文件名只要是符合python模块规则即可，即不是必须要使用test_开头或_test结尾，但是规范建议同一个项目的测试尽量以test_开头
pytest test_demo1.py
pytest demo1.py

# 当然也可以指定执行目录，默认执行pytest的情况下dirpkg下的测试用例会被自动扫描到
pytest dirpkg

# 可以一次性指定多个文件，还可以文件和目录混合使用
pytest test_demo1.py demo1.py dirpkg

# 几种日志模式
pytest # 默认的
pytest -v # 显示详细信息
pytest -q # 更简洁的信息

# 输出print内容
pytest -s

# 结合pytest-html生成报告
pytest --html report.html #注意不要和-s一起使用，否则看不见详细信息
# 上面方式会单独生成样式表(css)，不利于邮件发送，下面把所有元素集中到一个html文件内
pytest --html report.html --self-contained-html

# 根据标记执行用例，可以使用逻辑运算
pytest -m mark
pytest -m "not mark"
pytest -m "not mark1 and mark2"

# 当然也可以根据文件名，类名，函数名执行
pytest abc.py::TestClass::testfunc

# 当然还可以通过类名，函数名进行匹配，当然也支持自定义的mark
pytest -k "TestCls"

# 查看可用的fixture
pytest --fixtures

# 只允许已知的marker对测试函数进行标注，如果未定义的marker出现，则抛出错误
pytest --strict-markers

# 查看可用的marker，定义在ini文件的也会被识别
pytest --markers
```

# api

```python
import pytest


# 某个被测函数就是希望能抛出异常，即抛出异常才算是正常
# 建议pytest -q的方式执行
with pytest.raises(SystemExit):
    some_func()


# 使用marker，比如ini文件定义了P0的marker
# 可以使用多个
@pytest.marker.P0
@pytest.marker.slow
def test_xxx():
    ...
```

# pytest.ini

这里列举常用的配置，详细的配置参考[官方配置说明](https://docs.pytest.org/en/7.3.x/reference/reference.html#ini-options-ref)

```ini
[pytest]
; 指定运行测试所需的pytest最小版本
minversion = 3.7

; 指定命令行参数所携带的默认选项，可以指定多个
addopts = --maxfail=2 -rf

; 增加自定义marker
markers =
    slow: 可以加注释，比如这个标识执行慢的用例，如果执行时想排除此类用例，可以通过 -m "not slow"
    serial

log_level = INFO
log_format = %(asctime)s %(levelname)s %(message)s
log_date_format = %Y-%m-%d %H:%M:%S

; 开启命令行log显示
log_cli = True
log_cli_level = INFO
log_cli_format = %(asctime)s %(levelname)s %(message)s
log_cli_date_format = %Y-%m-%d %H:%M:%S

; 开启日志文件记录
log_file = logs/pytest-logs.log
log_file_level = INFO
log_file_format = %(asctime)s %(levelname)s %(message)s
log_file_date_format = %Y-%m-%d %H:%M:%S
```

# 插件

# 文档

1. [官方doc](https://docs.pytest.org/)
2. [配置文件](https://docs.pytest.org/en/7.3.x/reference/reference.html#ini-options-ref)
3. [命令行参数](https://docs.pytest.org/en/7.3.x/reference/reference.html#command-line-flags)