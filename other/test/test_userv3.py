"""user v3版本测试."""

from other.userv3 import User, Users


def test_users_getID():
    """测试获取新用户ID."""
    users = Users()
    assert (users.getID(), ) == (1, )
    user = User('Jack', 12, '876')
    users = Users([[1, user.name, user.age, user.tel]])
    assert (users.getID(), ) == (2, )


def test_users_add():
    """测试添加新用户."""
    user = User('Jack', 12, '876')
    users = Users()
    users.add(user)
    assert (users.users, ) == ([[1, 'Jack', 12, '876']], )
    user = User('Rose', 19, '623')
    users.add(user)
    assert (users.users, ) == ([[1, 'Jack', 12, '876'], [2, 'Rose', 19,
                                                         '623']], )


def test_users_find():
    """测试查询用户信息."""
    users = Users()
    assert (users.find(10), ) == ((), )
    users.users = [[1, 'Jack', 12, '876']]
    assert (users.find(10), ) == ((), )
    users.users = [[1, 'Jack', 12, '876'], [2, 'Rose', 19, '623']]
    assert (users.find(2), ) == ((2, 'Rose', 19, '623'), )


def test_users_delete():
    """测试删除用户信息."""
    users = Users()
    users.users = [[1, 'Jack', 12, '876']]
    user = User('Jack', 12, '876')
    users.delete([1, user.name, user.age, user.tel])
    assert (users.users, ) == ([], )
    users.users = [[1, 'Jack', 12, '876'], [2, 'Rose', 19, '623']]
    user = User('Rose', 19, '623')
    users.delete([2, user.name, user.age, user.tel])
    assert (users.users, ) == ([[1, 'Jack', 12, '876']], )
