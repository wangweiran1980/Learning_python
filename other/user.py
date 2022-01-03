"""
Created on Mon Jan  3 15:17:43 2022.

@author: wangweiran
"""


users = []

while True:
    op = input('请选择操作(add, del, edit, list, find, quit): ').strip()
    if op == 'quit':
        break
    elif op == 'add':
        txt = input('请输入用户信息(name, age, tel): ')
        nodes = txt.split(',')
        if len(nodes) != 3:
            print('输入信息错误')
            continue
        id = len(users)+1
        user = [id, nodes[0].strip(), nodes[1].strip(), nodes[2].strip()]
        users.append(user)
        print(users)
    elif op == 'del':
        id = int(input('请输入ID: '))
        for user in users:
            if id in user:
                users.remove(user)
        else:
            print('ID不存在!')
    elif op == 'list':
        for user in users:
            print(user)
    elif op == 'edit':
        id = int(input('请输入ID: '))
        for user in users:
            if id in user:
                txt = input('请输入用户信息(name, age, tel): ')
                nodes = txt.split(',')
                if len(nodes) != 3:
                    print('输入信息错误')
                    continue
                user[1] = nodes[0]
                user[2] = nodes[1]
                user[3] = nodes[2]
    elif op == 'find':
        name = input('请输入名字: ')
        for user in users:
            if name in user:
                print(user)
                break
        else:
            print('ID不存在!')
