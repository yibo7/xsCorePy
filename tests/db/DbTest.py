from unittest import TestCase

from sqlalchemy import select, or_

from XsCore.db import db_provider, DbDal

# class UserBll(BllBase(UserEntity)):
#     def __init__(self):
#         pass
from tests.db.UserEntity import UserEntity



dal = DbDal(UserEntity)

'''
默认的DbDal提供了大量常用数据库操作方法
如果只想使用基本的数据操作方法，可以直接这样创建即可：DbDal(UserEntity)
一般来说DbDal已经可以满80%的数据操作
，当然你也可以参考扩展某个表的测试样例
'''
class DbTest(TestCase):

    # 生成数据库与数据表
    def testInit(self):

        db_provider.create_all_table()

    # 添加一条数据
    def testAddModel(self):
        user = UserEntity()
        user.username = "安安"
        user.password = "56986545"

        dal.add(user)

    # 添加多条数据
    def testAddModelList(self):

        # 创建5个用户，并一次性添加到数据库
        users = [UserEntity(username=f"用户{count}", password=f"密码{count}") for count in range(1, 5)]
        dal.addList(users)

    # 指定id获取一条数据
    def testGetEntity(self):
        user = dal.getOne(1)
        print("用户名:", user.username, "密码：", user.password)

    # 指定条件获取一条数据
    def testGetEntityByWhere(self):
        # 多个条件中是and关系

        user = dal.getOneWhere(username="小明", id=2)
        if user:
            print("Id:", user.id, "用户名:", user.username, "密码：", user.password)
        else:
            print("找不到相关的数据")

    # 获取某个表的所有数据
    def testAll(self):
        # 默认为升序，采用id降序
        users = dal.getAll(UserEntity.id.desc())
        for user in users:
            print("Id:", user.id, "用户名:", user.username, "密码：", user.password)

    # 获取某个表指定条件的数据
    def testgetList(self):
        # 默认升序查询
        # users = dal.getList(UserEntity.username.like("%用户%", ))
        # 获取列表-or查询-降序
        users = dal.getList(or_(UserEntity.username.like("%用户%", ), UserEntity.id == 1), UserEntity.id.desc())
        for user in users:
            print("Id:", user.id, "用户名:", user.username, "密码：", user.password)

    # 获取最新的3条数据
    def testGetTop(self):
        users = dal.getTop(3)
        for user in users:
            print("Id:", user.id, "用户名:", user.username, "密码：", user.password)

    # 查看分页，不带条件
    def testgetPagesAll(self):
        # 查询UserEntity第一页，每页显示3条数据
        # 默认升序调用
        users = dal.getPageAll(1, 3)
        # 降序调用
        # users = dal.getPageAll(1, 3, UserEntity.id.desc())
        for user in users:
            print("Id:", user.id, "用户名:", user.username, "密码：", user.password)

    # 查看分页，带条件
    def testgetPagesWhere(self):

        # 查询UserEntity第一页，每页显示3条数据
        # 默认升序调用
        # users = dal.getPageWhere(UserEntity, 1, 3, or_(UserEntity.username.like("%用户%", ), UserEntity.id == 1))

        # 降序调用
        users = dal.getPageWhere(1, 3, or_(UserEntity.username.like("%用户%", ), UserEntity.id == 1),
                                 UserEntity.id.desc())
        for user in users:
            print("Id:", user.id, "用户名:", user.username, "密码：", user.password)

    # 是否存在记录-条件id
    def testIsHaveId(self):
        ishave = dal.existsId(1)
        print("是否存在记录：", ishave)

    # 是否存在记录-自定义条件
    def testIsHave(self):
        ishave = dal.exists(UserEntity.username == '小明3')
        print("是否存在记录：", ishave)

    def testGetMaxId(self):
        maxId = dal.getMaxId()
        print("当前表的最大id是：",maxId)

    def testGetCountAll(self):
        count = dal.getCountAll()
        print("记录的总条数为：", count)

    def testGetCountWhere(self):
        count = dal.getCountWhere(UserEntity.username.like("%用户%"))
        print("记录的总条数为：", count)

    def testDelId(self):
        dal.delId(4)

    def testDelWhere(self):
        dal.delWhere(username='用户4')

    def testDelAll(self):
        dal.delAll()