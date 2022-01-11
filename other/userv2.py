"""user v2."""

import json


def isInclude(data: dict, txt: str, isPrecise: bool = True) -> bool:
    """在列表中查询是否包含给定的文本.

    isPrecise: 是否精确匹配
    """
    if isPrecise:
        return True if txt == data['name'] else False
    return True if txt in data['name'] else False


def getID(data: dict) -> int:
    """在添加用户信息时指定ID."""
    if data == {}:
        return 1
    return int(list(data.keys())[-1]) + 1


def add(txt: str, data: dict) -> None:
    """添加用户信息."""
    nodes = txt.split(",")
    if len(nodes) != 3:
        print("输入信息错误")
    for user in data.values():
        if isInclude(user, nodes[0].strip()):
            print('名字已存在!')
            return
    id = getID(data)
    data[id] = {
        'name': nodes[0].strip(),
        'age': nodes[1].strip(),
        'tel': nodes[2].strip()
    }


def delete(name: str, data: dict) -> bool:
    """删除用户信息."""
    for id in data:
        if isInclude(data[id], name):
            data.pop(id)
            return True
    return False


def show(data: dict) -> None:
    """展示用户数据."""
    for id, user in data.items():
        print("{id} {name} {age} {tel}".format(
            id=id,
            name=user['name'],
            age=user['age'],
            tel=user['tel'],
        ))


def edit(id: str, data: dict) -> bool:
    """编辑已存在用户信息."""
    if id not in data:
        return False
    txt = input("请输入用户信息(name, age, tel): ")
    nodes = txt.split(",")
    if len(nodes) != 3:
        print("输入信息错误")
        return False
    data[id] = {
        'name': nodes[0].strip(),
        'age': nodes[1].strip(),
        'tel': nodes[2].strip()
    }
    return True


def find(txt: str, data: dict) -> None:
    """查找用户信息."""
    for id, user in data.items():
        if not isInclude(user, txt, False):
            print('未找到符合数据')
            return
    print("{id} {name} {age} {tel}".format(
        id=id,
        name=user['name'],
        age=user['age'],
        tel=user['tel'],
    ))


def read(fn: str) -> dict:
    """从文件中读取json数据."""
    try:
        with open(fn, 'r') as f:
            return json.load(f)
    except (FileNotFoundError):
        return {}


def save(data: dict, fn: str) -> bool:
    """保存json数据到文件."""
    try:
        with open(fn, 'w') as f:
            json.dump(data, f)
    except (json.JSONDecodeError) as err:
        print(err)
        return False
    return True


if __name__ == '__main__':
    filename = "./userinfo.json"
    users = read(filename)
    while True:
        op = input("请选择操作(add, del, edit, list, find, quit): ").strip()
        if op == "quit":
            if save(users, filename):
                exit(0)
            print('系统故障!')
            exit(0)
        elif op == "add":
            txt = input("请输入用户信息(name, age, tel): ")
            add(txt, users)
        elif op == "del":
            name = input("请输入名字: ")
            delete(name, users)
        elif op == "list":
            show(users)
        elif op == "edit":
            id = input("请输入ID: ")
            edit(id, users)
        elif op == "find":
            txt = input("请输入要查询的内容: ").strip()
            find(txt, users)
