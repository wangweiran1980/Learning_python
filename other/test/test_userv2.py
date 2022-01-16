"""userv2测试代码."""

from other.userv2 import add, delete, getID, isInclude, read


def test_user():
    """测试isInclude."""
    data = {'name': 'Jack', 'age': '12', 'tel': '9347'}
    assert (True, ) == (isInclude(data, 'Ja', False), )
    assert (True, ) == (isInclude(data, 'Jack', True), )
    assert (False, ) == (isInclude(data, 'Ja', True), )
    assert (False, ) == (isInclude(data, 'DB', True), )


def test_getID():
    """测试获取ID."""
    users = {}
    assert (1, ) == (getID(users), )
    users = {1: {1, 2, 3}}
    assert (2, ) == (getID(users), )


def test_add():
    """测试添加用户信息."""
    users = {}
    txt = 'Jack , 12 ,   3947 '
    add(txt, users)
    assert ({1: {'name': 'Jack', 'age': '12', 'tel': '3947'}}, ) == (users, )


def test_del():
    """测试删除用户信息."""
    users = {1: {'name': 'Jack', 'age': '12', 'tel': '238947'}}
    assert (True, ) == (delete('Jack', users), )
    assert ({}, ) == (users, )
    users = {1: {'name': 'Jack', 'age': '12', 'tel': '238947'}}
    assert (False, ) == (delete('Ja', users), )
    assert ({1: {'name': 'Jack', 'age': '12', 'tel': '238947'}}, ) == (users, )


def test_read():
    """测试从json文件读取数据."""
    filename = "./userinfo.json"
    assert ({
        '1': {
            'name': 'Jack',
            'age': '12',
            'tel': '3947'
        }
    }, ) == (read(filename), )
    filename = './aa.json'
    assert ({}, ) == (read(filename), )
