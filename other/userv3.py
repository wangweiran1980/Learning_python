"""userv3版本 class版."""


class User(object):
    """用户类."""
    def __init__(self, name: str, age: int, tel: str) -> None:
        """初始化类."""
        self.name = name
        self.age = age
        self.tel = tel

    def edit(self, name: str, age: int, tel: str) -> None:
        """修改用户信息."""
        self.name = name
        self.age = age
        self.tel = tel

    def __repr__(self) -> str:
        """重写__repr__."""
        return str([self.name, self.age, self.tel])


class Users(object):
    """用户信息表."""
    users = []

    def __init__(self, users: list = []) -> None:
        """初始化."""
        if users:
            self.users = users

    def getID(self) -> int:
        """新增用户时，获取新用户ID."""
        return len(self.users) + 1 if self.users else 1

    def add(self, user: User) -> None:
        """添加新用户."""
        u = [self.getID(), user.name, user.age, user.tel]
        self.users.append(u)

    def find(self, id: int) -> tuple:
        """根据用户ID查找用户数据."""
        for user in self.users:
            if id == user[0]:
                return tuple(user)
        return tuple()

    def delete(self, user: list) -> None:
        """删除用户信息."""
        try:
            self.users.remove(user)
        except ValueError:
            pass

    def edit(self, id: int, user: User) -> None:
        """编辑用户数据."""
        for u in self.users:
            if id == u[0]:
                u[1] = user.name
                u[2] = user.age
                u[3] = user.tel

    def __repr__(self) -> str:
        """重写__repr__."""
        return str(self.users)


if __name__ == '__main__':
    users = Users()
    while True:
        op = input(
            '请先择操作(1: add, 2: edit, 3: delete, 4: find, 5: list: 6: quit): '
        ).strip()
        if op == 'quit':
            break
        elif op == 'add':
            u = input('请输入用户信息(name, age, tel): ').split(',')
            if len(u) != 3:
                print('用户信息输入错误!')
                continue
            u = [i.strip() for i in u]
            user = User(u[0], u[1], u[2])
            users.add(user)
        elif op == 'delete':
            try:
                id = int(input('请输入用户ID: ').strip())
                user = list(users.find(id))
                users.delete(user)
            except TypeError:
                print('ID号输入错误!')
                continue
        elif op == 'find':
            try:
                id = int(input('请输入用户ID: ').strip())
                print(users.find(id))
            except TypeError:
                print('ID号输入错误!')
                continue
        elif op == 'list':
            print(users.users)
        elif op == 'edit':
            try:
                id = int(input('请输入用户ID: ').strip())
            except TypeError:
                print('ID输入错误')
                continue
            u = input('请输入用户信息(name, age, tel): ').split(',')
            if len(u) != 3:
                print('用户信息输入错误!')
                continue
            u = [i.strip() for i in u]
            user = User(u[0], u[1], u[2])
            users.edit(id, user)
        else:
            print('输入错误!')
