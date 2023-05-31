# 模块和函数级别
def setup_module():
    print('setup module.')

def teardown_module():
    print('teardown module.')

def setup_function():
    print('setup function')

def teardown_function():
    print('teardown function')


def test_1():
    assert 1 == 1

def test_2():
    assert 1 == 1


class TestCls:
    # 类和方法级别
    def setup_class(cls):
        print('setup class')

    def teardown_class(cls):
        print('teardown class')

    def setup_method(self):
        print('setup method')

    def teardown_method(self):
        print('teardown method')

    def test_3(self):
        assert 1 == 1

    def test_4(self):
        assert 1 == 1