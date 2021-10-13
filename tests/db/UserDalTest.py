from unittest import TestCase

from tests.db.UserDal import UserDal


class UserDalTest(TestCase):

    # 生成数据库与数据表
    def testIdIn(self):
        dal = UserDal()
        users = dal.getIdIn([3,5])
        for user in users:
            print("Id:", user.id, "用户名:", user.username, "密码：", user.password)
