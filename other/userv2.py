"""
Created on Mon Jan  3 15:17:43 2022.

@author: wangweiran
"""


users = {}

while True:
    op = input("请选择操作(add, del, edit, list, find, quit): ").strip()
    if op == "quit":
        break
    elif op == "add":
        txt = input("请输入用户信息(name, age, tel): ")
        nodes = txt.split(",")
        if len(nodes) != 3:
            print("输入信息错误")
            continue
        id = len(users) + 1
        users[id] = [nodes[0].strip(), nodes[1].strip(), nodes[2].strip()]
        # print(users)
    elif op == "del":
        name = input("请输入名字: ")
        for id in users:
            if name in users[id]:
                users.pop(id)
                break
        else:
            print("名字不存在!")
    elif op == "list":
        for user in users:
            print("{id} {name} {age} {tel}".format(
                id=user,
                name=users[user][0],
                age=users[user][1],
                tel=users[user][2]))
    elif op == "edit":
        id = int(input("请输入ID: "))
        if id in users:
            txt = input("请输入用户信息(name, age, tel): ")
            nodes = txt.split(",")
            if len(nodes) != 3:
                print("输入信息错误")
                continue
            users[id] = [nodes[0].strip(), nodes[1].strip(), nodes[2].strip()]
            continue
        print("ID不存在!")
    elif op == "find":
        txt = input("请输入要查询的内容: ")
        for id in users:
            for user in users[id]:
                if txt in user:
                    print("{id} {name} {age} {tel}".format(
                        id=id,
                        name=users[id][0],
                        age=users[id][1],
                        tel=users[id][2]))
