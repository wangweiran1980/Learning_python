"""
Created on Mon Jan  3 15:17:43 2022.

@author: wangweiran
"""

users = {}


def isInclude(data: list, txt: str, precise: bool = True) -> bool:
    """在列表中查询是否包含给定的文本."""
    if precise:
        if txt in data:
            return True
    else:
        for item in data:
            if txt in item:
                return True
    return False


def getID() -> int:
    """在添加用户信息时指定ID."""
    if users == {}:
        return 1
    return list(users.keys())[-1] + 1


def add():
    """添加用户信息."""
    txt = input("请输入用户信息(name, age, tel): ")
    nodes = txt.split(",")
    if len(nodes) != 3:
        print("输入信息错误")
    for user in users.values():
        if isInclude(user, nodes[0].strip()):
            print('名字已存在!')
            return
    id = getID()
    users[id] = [nodes[0].strip(), nodes[1].strip(), nodes[2].strip()]


def delete():
    """删除用户信息."""
    name = input("请输入名字: ")
    for id in users:
        if isInclude(users[id], name):
            users.pop(id)
            return
    print("名字不存在!")


def show():
    """展示用户数据."""
    for user in users:
        print("{id} {name} {age} {tel}".format(
            id=user,
            name=users[user][0],
            age=users[user][1],
            tel=users[user][2],
        ))


def edit():
    """编辑已存在用户信息."""
    id = int(input("请输入ID: "))
    if id not in users:
        print('ID不存在!')
        return
    txt = input("请输入用户信息(name, age, tel): ")
    nodes = txt.split(",")
    if len(nodes) != 3:
        print("输入信息错误")
        return
    users[id] = [nodes[0].strip(), nodes[1].strip(), nodes[2].strip()]


def find():
    """查找用户信息."""
    txt = input("请输入要查询的内容: ").strip()
    for user in users.values():
        if isInclude(user, txt, False):
            print("{name} {age} {tel}".format(name=user[0],
                                              age=user[1],
                                              tel=user[2]))
            return
    print('未找到符合数据')


while True:
    op = input("请选择操作(add, del, edit, list, find, quit): ").strip()
    if op == "quit":
        break
    elif op == "add":
        add()
    elif op == "del":
        delete()
    elif op == "list":
        show()
    elif op == "edit":
        edit()
    elif op == "find":
        find()
